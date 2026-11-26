# Public portal setup

The original repository address is retained. The curated checkout contains the public portal, research metadata, notebooks and documentation. The historical catalog points to its immutable source snapshot.

## Option A — static portal (smallest footprint)

1. Open Settings → Pages → Build and deployment.
2. Choose Deploy from a branch, main, /docs.
3. Save. This publishes the ring explorer and historical catalog.

## Option B — portal plus executable Python laboratory

1. Open Settings → Pages and choose GitHub Actions as the publishing source.
2. In Actions select **Publish public portal and Python laboratory** → Run workflow on main.
3. Once the deployment succeeds, visit the published Pages URL. The main portal links to JupyterLite.
4. Repeat the workflow after changes that should be published. This workflow is deliberately manual to avoid rebuilding the browser runtime on every documentation edit.

The build uses a standard public GitHub runner and a temporary Pages artifact. Python executes on the visitor's computer. Only the small, standalone laboratory notebook is included; the archived notebooks, local model gateways, and bulk research corpus are not copied to the site. No paid runner or AI service is configured. Pages deployment and the JupyterLite build still require a successful first workflow run.

## Research verification

The **Verify public research** workflow runs on main updates and pull requests, and can also be dispatched manually. It uses historical Git trees instead of downloading all historical blobs. The **Attest verification report** workflow is a manual main-branch run; its short-lived report artifact and signature identify the execution provenance and scoped checks, not a proof of all research.

GitHub Actions, Pages, public Issues/Discussions, and repository security settings may require administrator enablement. Historical Git storage is separate from published-site size; no history rewrite is performed here.
