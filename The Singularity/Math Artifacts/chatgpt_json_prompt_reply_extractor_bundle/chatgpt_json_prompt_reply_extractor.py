# ============================================================
# CHATGPT JSON EXPORT -> PROMPT/REPLY TRAINING EXTRACTOR
#
# Put this in a notebook cell or run as a .py script.
#
# Default input folder:
#   D:\Nexus\Nexus10\AI\Training\transscripts\gpt
#
# Outputs:
#   _extracted_prompt_reply\extracted_turns.jsonl
#   _extracted_prompt_reply\prompt_reply_pairs.jsonl
#   _extracted_prompt_reply\chatml_training.jsonl
#   _extracted_prompt_reply\prompt_reply_pairs.csv
#
# Notes:
# - Filters hidden/system/tool/internal messages.
# - Extracts visible user + assistant text.
# - Uses the active current_node branch when available.
# - Strips injected "## Instructions ... ## End Instructions" blocks by default.
# ============================================================

from pathlib import Path
import json
import csv
import re
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


# -----------------------------
# CONFIG
# -----------------------------

INPUT_DIR = Path(r"D:\Nexus\Nexus10\AI\Training\transscripts\gpt")
OUTPUT_DIR = INPUT_DIR / "_extracted_prompt_reply"

USE_CURRENT_NODE_PATH_ONLY = True

STRIP_CHATGPT_INSTRUCTION_BLOCKS = True

# Removes common embedded promo blocks from assistant text.
# Useful for old exports that contain "Try SciSpace..." ad text.
STRIP_COMMON_PROMO_BLOCKS = True

INCLUDE_USER_ROLES = {"user"}
INCLUDE_ASSISTANT_ROLES = {"assistant"}

VISIBLE_CONTENT_TYPES = {"text", "multimodal_text"}

MIN_PROMPT_CHARS = 1
MIN_REPLY_CHARS = 1

SKIP_AGENT_MODE_UNAVAILABLE = False


# -----------------------------
# TEXT CLEANING
# -----------------------------

def clean_whitespace(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text.strip()


def strip_instruction_blocks(text: str) -> str:
    if not STRIP_CHATGPT_INSTRUCTION_BLOCKS:
        return text
    pattern = re.compile(
        r"^\s*## Instructions\s*.*?## End Instructions\s*",
        flags=re.IGNORECASE | re.DOTALL,
    )
    return pattern.sub("", text).strip()


def strip_common_promo_blocks(text: str) -> str:
    if not STRIP_COMMON_PROMO_BLOCKS:
        return text

    # Removes common old embedded promo tails.
    patterns = [
        r"\n\s*---\s*\n\s*\*\*?🔍\s*Looking to explore deeper\?.*?$",
        r"\n\s*🔍\s*Looking to explore deeper\?.*?$",
        r"\n\s*```markdown\s*#### Users also ask these questions:.*?```\s*$",
    ]
    out = text
    for pat in patterns:
        out = re.sub(pat, "", out, flags=re.IGNORECASE | re.DOTALL)
    return out.strip()


def extract_text_from_content(content: Dict[str, Any]) -> str:
    if not isinstance(content, dict):
        return ""

    ctype = content.get("content_type")

    if ctype == "text":
        parts = content.get("parts", [])
        if not isinstance(parts, list):
            return ""
        out = []
        for p in parts:
            if isinstance(p, str):
                out.append(p)
            elif isinstance(p, dict):
                if isinstance(p.get("text"), str):
                    out.append(p["text"])
                else:
                    # Avoid putting binary/file structures into training.
                    label = p.get("content_type") or p.get("type")
                    if label:
                        out.append(f"[{label}]")
        return clean_whitespace("\n".join(out))

    if ctype == "multimodal_text":
        parts = content.get("parts", [])
        if not isinstance(parts, list):
            return ""
        out = []
        for p in parts:
            if isinstance(p, str):
                out.append(p)
            elif isinstance(p, dict):
                if isinstance(p.get("text"), str):
                    out.append(p["text"])
                elif p.get("content_type") == "text" and isinstance(p.get("text"), str):
                    out.append(p["text"])
                else:
                    label = p.get("content_type") or p.get("type")
                    if label:
                        out.append(f"[{label}]")
        return clean_whitespace("\n".join(out))

    return ""


# -----------------------------
# CHATGPT EXPORT GRAPH HANDLING
# -----------------------------

def load_json_file(path: Path) -> Optional[Dict[str, Any]]:
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except UnicodeDecodeError:
        try:
            with path.open("r", encoding="utf-8-sig") as f:
                return json.load(f)
        except Exception as e:
            print(f"[ERROR] Could not load {path.name}: {e}")
            return None
    except Exception as e:
        print(f"[ERROR] Could not load {path.name}: {e}")
        return None


def timestamp_to_iso(ts: Any) -> Optional[str]:
    if ts is None:
        return None
    try:
        return datetime.fromtimestamp(float(ts), tz=timezone.utc).isoformat()
    except Exception:
        return None


def get_main_path_nodes(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    mapping = data.get("mapping", {})
    if not isinstance(mapping, dict) or not mapping:
        return []

    if USE_CURRENT_NODE_PATH_ONLY:
        current = data.get("current_node")
        chain_ids = []
        seen = set()

        while current and current in mapping and current not in seen:
            seen.add(current)
            chain_ids.append(current)
            current = mapping[current].get("parent")

        if chain_ids:
            chain_ids.reverse()
            return [mapping[i] for i in chain_ids if i in mapping]

    nodes = list(mapping.values())

    def sort_key(node: Dict[str, Any]):
        msg = node.get("message") or {}
        ct = msg.get("create_time")
        return (ct is None, ct or 0)

    return sorted(nodes, key=sort_key)


def is_visible_message(msg: Dict[str, Any]) -> bool:
    if not isinstance(msg, dict):
        return False

    metadata = msg.get("metadata") or {}

    if metadata.get("is_visually_hidden_from_conversation"):
        return False

    role = (msg.get("author") or {}).get("role")
    if role not in INCLUDE_USER_ROLES and role not in INCLUDE_ASSISTANT_ROLES:
        return False

    content = msg.get("content") or {}
    ctype = content.get("content_type")
    if ctype not in VISIBLE_CONTENT_TYPES:
        return False

    text = extract_text_from_content(content)
    if not text:
        return False

    return True


def extract_visible_turns(data: Dict[str, Any], source_file: str) -> List[Dict[str, Any]]:
    title = data.get("title") or ""
    conversation_id = data.get("conversation_id") or data.get("id") or ""
    create_time = timestamp_to_iso(data.get("create_time"))
    update_time = timestamp_to_iso(data.get("update_time"))

    turns = []

    for node in get_main_path_nodes(data):
        msg = node.get("message")
        if not is_visible_message(msg):
            continue

        role = (msg.get("author") or {}).get("role")
        content = msg.get("content") or {}
        text = extract_text_from_content(content)

        if role == "user":
            text = strip_instruction_blocks(text)

        if role == "assistant":
            text = strip_common_promo_blocks(text)

        text = clean_whitespace(text)
        if not text:
            continue

        if role == "assistant" and SKIP_AGENT_MODE_UNAVAILABLE:
            if text.strip().lower() == "agent mode is not available for this conversation. please start a new conversation.":
                continue

        turns.append({
            "source_file": source_file,
            "conversation_id": conversation_id,
            "conversation_title": title,
            "conversation_create_time_utc": create_time,
            "conversation_update_time_utc": update_time,
            "message_id": msg.get("id"),
            "parent_id": node.get("parent"),
            "create_time_utc": timestamp_to_iso(msg.get("create_time")),
            "role": role,
            "content": text,
        })

    return turns


def pair_user_assistant(turns: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    pairs = []
    pending_user = []
    pending_user_ids = []
    pending_user_times = []

    i = 0
    while i < len(turns):
        t = turns[i]
        role = t["role"]

        if role == "user":
            pending_user.append(t["content"])
            pending_user_ids.append(t.get("message_id"))
            pending_user_times.append(t.get("create_time_utc"))
            i += 1
            continue

        if role == "assistant":
            if not pending_user:
                i += 1
                continue

            assistant_parts = []
            assistant_ids = []
            assistant_times = []

            while i < len(turns) and turns[i]["role"] == "assistant":
                assistant_parts.append(turns[i]["content"])
                assistant_ids.append(turns[i].get("message_id"))
                assistant_times.append(turns[i].get("create_time_utc"))
                i += 1

            prompt = clean_whitespace("\n\n".join(pending_user))
            reply = clean_whitespace("\n\n".join(assistant_parts))

            if len(prompt) >= MIN_PROMPT_CHARS and len(reply) >= MIN_REPLY_CHARS:
                first = t
                pairs.append({
                    "source_file": first["source_file"],
                    "conversation_id": first["conversation_id"],
                    "conversation_title": first["conversation_title"],
                    "conversation_create_time_utc": first["conversation_create_time_utc"],
                    "user_message_ids": pending_user_ids,
                    "assistant_message_ids": assistant_ids,
                    "user_create_times_utc": pending_user_times,
                    "assistant_create_times_utc": assistant_times,
                    "prompt": prompt,
                    "reply": reply,
                })

            pending_user = []
            pending_user_ids = []
            pending_user_times = []
            continue

        i += 1

    return pairs


# -----------------------------
# MAIN RUN
# -----------------------------

def run_extraction(input_dir: Path, output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)

    json_files = sorted(input_dir.glob("*.json"))

    all_turns = []
    all_pairs = []
    failures = []

    print(f"[INPUT]  {input_dir}")
    print(f"[OUTPUT] {output_dir}")
    print(f"[SCAN]   Found {len(json_files):,} JSON files\n")

    for idx, path in enumerate(json_files, 1):
        data = load_json_file(path)
        if data is None:
            failures.append(str(path))
            continue

        turns = extract_visible_turns(data, path.name)
        pairs = pair_user_assistant(turns)

        all_turns.extend(turns)
        all_pairs.extend(pairs)

        print(f"[{idx:>5}/{len(json_files):<5}] {path.name}")
        print(f"    turns={len(turns):,}  pairs={len(pairs):,}  title={data.get('title')!r}")

    turns_path = output_dir / "extracted_turns.jsonl"
    with turns_path.open("w", encoding="utf-8") as f:
        for row in all_turns:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    pairs_path = output_dir / "prompt_reply_pairs.jsonl"
    with pairs_path.open("w", encoding="utf-8") as f:
        for row in all_pairs:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    chatml_path = output_dir / "chatml_training.jsonl"
    with chatml_path.open("w", encoding="utf-8") as f:
        for row in all_pairs:
            record = {
                "messages": [
                    {"role": "user", "content": row["prompt"]},
                    {"role": "assistant", "content": row["reply"]},
                ],
                "metadata": {
                    "source_file": row["source_file"],
                    "conversation_title": row["conversation_title"],
                    "conversation_id": row["conversation_id"],
                }
            }
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    csv_path = output_dir / "prompt_reply_pairs.csv"
    with csv_path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "source_file",
                "conversation_title",
                "conversation_create_time_utc",
                "prompt",
                "reply",
            ],
            extrasaction="ignore",
        )
        writer.writeheader()
        for row in all_pairs:
            writer.writerow(row)

    print("\n[DONE]")
    print(f"  visible turns: {len(all_turns):,}")
    print(f"  prompt/reply pairs: {len(all_pairs):,}")
    print(f"  failures: {len(failures):,}")
    print("\n[FILES WRITTEN]")
    print(f"  {turns_path}")
    print(f"  {pairs_path}")
    print(f"  {chatml_path}")
    print(f"  {csv_path}")

    if failures:
        print("\n[FAILED FILES]")
        for x in failures[:25]:
            print(" ", x)
        if len(failures) > 25:
            print(f"  ... {len(failures) - 25} more")

    print("\n[PREVIEW]")
    for n, row in enumerate(all_pairs[:3], 1):
        print(f"\n--- PAIR {n} ---")
        print("SOURCE:", row["source_file"])
        print("TITLE :", row["conversation_title"])
        print("PROMPT:", row["prompt"][:500].replace("\n", "\\n"))
        print("REPLY :", row["reply"][:500].replace("\n", "\\n"))

    return all_turns, all_pairs


if __name__ == "__main__":
    all_turns, all_pairs = run_extraction(INPUT_DIR, OUTPUT_DIR)
