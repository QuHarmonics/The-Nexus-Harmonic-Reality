#!/usr/bin/env python3
"""
NEXUS DATA SURVEY
See what you're working with
"""

import os
from pathlib import Path
from collections import Counter, defaultdict
import json

DATA_DIR = Path(os.environ.get('NEXUS_DATA', '/media/dean/Nvme/nexus/training'))

def survey(data_dir):
    data_path = Path(data_dir)
    
    print("="*60)
    print("NEXUS DATA SURVEY")
    print("="*60)
    print(f"Directory: {data_path}")
    print()
    
    # Count by extension
    extensions = Counter()
    sizes = defaultdict(int)
    samples = defaultdict(list)
    
    all_files = list(data_path.rglob("*"))
    files_only = [f for f in all_files if f.is_file()]
    
    print(f"Total items: {len(all_files)}")
    print(f"Files: {len(files_only)}")
    print(f"Directories: {len(all_files) - len(files_only)}")
    print()
    
    for f in files_only:
        ext = f.suffix.lower() or '(no ext)'
        extensions[ext] += 1
        try:
            sizes[ext] += f.stat().st_size
            if len(samples[ext]) < 3:
                samples[ext].append(str(f))
        except:
            pass
    
    print("BY EXTENSION:")
    print("-"*60)
    for ext, count in extensions.most_common(20):
        size_mb = sizes[ext] / 1e6
        print(f"  {ext:12} {count:6} files  {size_mb:8.1f} MB")
    
    print()
    print("SAMPLES:")
    print("-"*60)
    for ext in ['.md', '.txt', '.py', '.json']:
        if ext in samples:
            print(f"\n{ext}:")
            for s in samples[ext][:2]:
                print(f"  {s}")
    
    # Total size
    total_size = sum(sizes.values()) / 1e9
    print()
    print(f"TOTAL SIZE: {total_size:.2f} GB")
    
    # Estimate tokens (rough: 4 chars per token)
    text_extensions = ['.md', '.txt', '.py', '.json', '.markdown', '.rst', '.html']
    text_size = sum(sizes[ext] for ext in text_extensions if ext in sizes)
    est_tokens = text_size / 4
    print(f"TEXT SIZE:  {text_size/1e9:.2f} GB")
    print(f"EST TOKENS: {est_tokens/1e6:.1f}M")
    
    # Subdirectory breakdown
    print()
    print("TOP-LEVEL DIRECTORIES:")
    print("-"*60)
    subdirs = defaultdict(lambda: {"count": 0, "size": 0})
    
    for f in files_only:
        try:
            rel = f.relative_to(data_path)
            top = rel.parts[0] if len(rel.parts) > 1 else "(root)"
            subdirs[top]["count"] += 1
            subdirs[top]["size"] += f.stat().st_size
        except:
            pass
    
    for name, info in sorted(subdirs.items(), key=lambda x: -x[1]["count"])[:15]:
        print(f"  {name:30} {info['count']:6} files  {info['size']/1e6:8.1f} MB")
    
    # Save report
    report = {
        "directory": str(data_path),
        "total_files": len(files_only),
        "extensions": dict(extensions),
        "sizes_mb": {k: v/1e6 for k, v in sizes.items()},
        "total_gb": total_size,
        "est_tokens_millions": est_tokens/1e6,
        "subdirs": {k: v for k, v in subdirs.items()}
    }
    
    report_file = data_path.parent / "data_survey.json"
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2, default=str)
    
    print()
    print(f"Report saved: {report_file}")
    
    return report

if __name__ == "__main__":
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else DATA_DIR
    survey(path)
