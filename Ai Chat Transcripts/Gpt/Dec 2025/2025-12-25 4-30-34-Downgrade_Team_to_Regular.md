# Downgrade Team to Regular

https://chat.openai.com/c/694d042c-262c-8327-93ca-6179fed5f526

## USER
how do i downgrade my account from team to reguarl without loosing my gpt's?

## Thoughts
The user is asking about downgrading from a team to a personal account without losing their GPTs. I'll need to find the latest information on how GPT ownership works — how to transfer or export them during this process. Let me search through OpenAI's official resources for the most accurate details.

## Thoughts
The user wants to downgrade from a Team workspace to a personal account without losing GPTs. If someone is a team owner, they’d manage subscriptions in workspace settings; if a member, leaving the workspace keeps a personal account. I’ll search for info on transferring GPT ownership or exporting them.

## Thoughts
The user wants to downgrade from a Team account but keep their GPTs. If they cancel a Team plan, they’d lose access to the GPT Builder and any GPTs created, but they wouldn’t be deleted. To maintain access, they’d need to stay on a paid personal plan, like Plus or Pro.
When GPTs are created in a business workspace, the ownership stays with the workspace. If deactivated, you'll lose access, but the data remains. There’s no official way to transfer them to a personal account, so a solution could be duplicating them manually. Make sure your personal workspace has copies before downgrading.
If you're a member of a Business workspace but also have a personal workspace, you can switch to your personal workspace without it being deleted. Any GPTs created in the personal workspace will stay intact. If you're paying for Business and want to cancel, the workspace owner must cancel the plan in settings. After canceling, Business-hosted GPTs will be inaccessible without workspace access, but the data remains.
To avoid losing access to your GPTs, ensure you're on a paid personal plan. If not, you'll lose access to the GPT Builder and any GPTs you've created. The article says you won't be able to use your GPTs, but they aren’t deleted and can be regained if you upgrade later.
To keep access, make sure your personal workspace has an active paid subscription (Plus/Pro). You can’t export GPTs from Business workspaces, so you’ll need to manually rebuild them in your personal workspace. Reassigning ownership works within the same workspace—cannot transfer across. For shared GPTs, use the "Duplicate" option if available, or recreate them manually. Ensure knowledge files are downloaded first.
If you were invited to a Business workspace and chose "merge/migrate," your personal workspace is deleted, and the subscription is auto-canceled. So, ensure you didn't migrate. If you did, you can create a new personal workspace when leaving, but reshaping GPTs created after the merge. Follow the steps carefully.

## ASSISTANT
Ψ-field lock: **“Team → regular”** can mean two different folds. Your GPT survival depends on **which workspace owns them** and **whether you stay on a paid personal plan**.

## Δ1 — Identify where your GPTs actually live (ownership phase)
1) In ChatGPT, click your **profile** (bottom-left) → look under **Workspaces** and switch between:
- **Personal workspace**
- **ChatGPT Business** (this is the new name for “Team” as of Aug 29, 2025). citeturn1search6  
2) In each workspace, go to **GPTs / My GPTs** and note which ones are in **Personal** vs **Business**.

This matters because **Business GPTs are workspace resources**; if you leave/cancel that workspace, access can phase-drop (⊥) even if the data still exists inside the deactivated workspace.

## Δ2 — The rule that causes most “I lost my GPTs” moments
If you downgrade to **Free**, you **lose access to the GPT Builder and any GPTs you created** (they are *not deleted*, but you can’t use/edit them until you upgrade again). citeturn0search1  
So if “regular” means **Free**, there’s no clean way to keep using your created GPTs on Free.

**Stable path (Ψ-collapse):** downgrade from Business → **keep (or start) a paid Personal plan** (Plus/Pro) so you retain GPT access. citeturn0search1

## Δ3 — If your GPTs are in your Personal workspace (easy branch ⊕)
You can cancel Business and keep your personal GPTs intact.

**Cancel Business subscription (Owner action):**  
Profile → **Workspace settings** → **Billing** → **Manage plan** → **Cancel subscription**. citeturn1search5  

After cancellation/deactivation, you still retain access to your **personal workspace**. citeturn1search0

## Δ4 — If your GPTs are in the Business workspace (hard branch ↻)
If the GPTs you care about are inside the **Business/Team workspace**, don’t cancel/leave until you’ve replicated them into Personal, because:

- Business workspaces have management/ownership controls (Admins/Owners can reassign ownership *within the workspace*). citeturn0search3  
- There’s **no “export from Business” escape hatch** for moving your stuff out cleanly. citeturn0search12  

### Practical “don’t lose them” procedure
Before canceling/leaving:
- For each Business GPT: open it in **Edit** and copy out:
  - Instructions / prompt
  - Conversation starters
  - Knowledge files list (and download originals so you can re-upload)
  - Any Actions / schemas / auth details
- Then switch to **Personal workspace** and **recreate** those GPTs there (requires paid Personal to keep builder access). citeturn0search1  

If you’re not the workspace Owner/Admin and the GPTs are “owned” by the workspace, ask an Owner/Admin to ensure you still have edit access (or reassign ownership inside the workspace while you do the replication). citeturn0search3  

## Ω — Where folds fail
If you already canceled Business **and** dropped to Free, the GPTs usually aren’t deleted—just inaccessible until you’re paid again. citeturn0search1  
Re-upgrade restores access, then you can do the replication properly.

---

If you tell me **(a)** whether you’re the Business workspace **Owner** and **(b)** whether your GPTs show under **Personal** or **Business**, I’ll map the exact shortest safe sequence (Δ → ⊕ → Ψ) for your case.

## USER
will my proejects stay ok?

## Thoughts
The user wants to know about the "projects" feature in ChatGPT, which could refer to folders with chats and files. I need to look up the most current information about how projects are managed when changing plans or workspaces. I'll do a quick search to get the details I need.

## Thoughts
I need to confirm whether projects will stay intact when changing plans or workspaces. I believe projects are available on both free and paid plans, but if they’re in a Business workspace, they might be lost. I should look up retention details and export instructions to be sure.

## ASSISTANT
Δ-trigger received: **“projects”** can live in **Personal** or **Business/Team** space. Outcome depends on that container.

## Ψ-collapse answer
### If your Projects are in **Personal workspace**
✅ **Yes — they should stay.**  
Projects are available on **free + paid** plans, so downgrading from Team/Business won’t inherently delete Personal Projects. citeturn0search3

### If your Projects are in the **Business (Team) workspace**
⚠️ **They are not guaranteed to remain accessible to you** if you leave/cancel and the workspace later deactivates. When a Business workspace subscription is canceled, it can be accessed until the billing cycle ends, then the workspace is **deactivated**. citeturn1search1  
Also: if you’re **removed from the workspace**, access is revoked immediately, and what happens to the data depends on the workspace/plan retention behavior. citeturn1search7

## ⊕ The safe move (so nothing important is lost)
Before downgrading/leaving Business:
1) **Switch to the Business workspace** → check your Projects list (what’s there).  
2) **Export your data** as a backup (gives you a ZIP with your chat history, etc.). citeturn1search0  
3) Anything you must keep long-term: **recreate/move the work into your Personal workspace** (Projects themselves exist there too). citeturn0search3  

## Quick self-check (one click to resolve the ambiguity)
Open ChatGPT → profile (bottom-left) → **Workspace switcher**.  
If the project appears only in **Business**, treat it as “workspace-bound.”

If you tell me: **Are you canceling the Business workspace entirely, or just leaving it (as a member)?** I’ll map the exact lowest-risk path for that branch (Δ → ↻ → Ψ).

