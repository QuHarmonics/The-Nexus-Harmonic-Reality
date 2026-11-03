# Repository architecture and consolidation plan

**Goal:** turn an existing, openly shared research dump into a navigable, reproducible, versioned research repository **without destroying its history**.

## Recommended destination tree

```text
The-Nexus-Harmonic-Reality/
├── README.md                         Public front door
├── docs/
│   ├── START_HERE.md                 Reading paths
│   ├── REPOSITORY_MAP.md             This migration guide
│   ├── GLOSSARY.md                   Terms, operators, ledger words
│   └── STATUS_LEDGER.md              Results, scope, dependencies
├── core/                             Canonical domain definitions
│   ├── ring/                         Partner, address, sphere, seam
│   ├── clock/                        One Inverter and loop laws
│   ├── retained-continuation/        State, step, inverse, closures
│   └── collision/                    Joint step and conserved charges
├── projects/                         Reproducible independent projects
│   ├── nexus-ai/                     BIND, local LM gateway, certificates
│   ├── sha256-glasskey/              SHA-256 experiments and tests
│   ├── bbp-pi/                       BBP / digit and integral machinery
│   ├── spectral-rh/                  Operator and Riemann work
│   ├── atomic-nuclear/               Period and magic-number programs
│   └── ...                           New domain-specific projects
├── papers/
│   ├── index.md                      Title → version → DOI → code
│   ├── published/                    Immutable copies of published files
│   └── sources/                      Editable manuscript sources
├── lab/
│   ├── active/                       Current experiments by topic
│   ├── drafts/                       Unpublished writing
│   └── incubator/                    Open ideas / incomplete links
├── records/
│   ├── seals/                        Prediction hashes and readout routes
│   ├── runs/                         Execution logs and correction logs
│   └── dialogue/                     Select transcripts and indexes
├── archive/
│   ├── notebooks/                    Superseded notebook generations
│   ├── scripts/                      Earlier unpromoted code
│   └── original-dump/                Manifest of original folder layout
└── assets/                           Diagrams and README media
```

Folders are **destination categories, not a claim that the structure already exists**. Do not move material until a manifest and mapping are recorded.

## The two classification axes

Every artifact receives two labels:

| Axis | Values | Why |
|:--|:--|:--|
| **Lifecycle** | `published`, `reproducible`, `active`, `draft`, `legacy`, `superseded` | Says how to treat the artifact, independent of age |
| **Domain** | `ring`, `clock`, `retained`, `compiler`, `sha256`, `bbp`, `spectral`, `matter`, `other` | Tells a reader what question it addresses |

For example, a 2025 notebook can be `reproducible / sha256` while a 2026 notebook can be `active / sha256`. **Age does not imply quality or obsolescence.** A published paper remains in the publication record even when its reasoning is superseded.

## Where existing folders go

| Existing root | Treatment |
|:--|:--|
| `Published Papers PDF` | Build DOI/version index; retain publication copies and source attributions |
| `Published Papers - MD` | Pair matching source manuscripts with published PDFs; preserve version history |
| `Newest MD Files` | Separate active drafts from published outputs and historical notes |
| `Jupyter-Notebooks-Newest` | Classify each notebook by project and lifecycle; promote runnable tests |
| `Jupyter-Notebooks-Sorted` | Retain earlier generation as legacy and promote any still-current code |
| `Jupyter-Notebook-Dump` | Freeze manifest and checksums; remove duplicates *only from curated views*, not the historical record |
| `Python Code` | Move tested code into projects with dependencies and commands; retain prototypes in lab/archive |
| `Mini Thesis` | Build subject index; link manuscript versions to DOI records |
| `Transcripts` | Keep provenance; move only chosen excerpts/indexes into Git, and store large raw archives externally |

## Project directory contract

A project is promoted into `projects/` when it can explain and reproduce its own work:

```text
projects/nexus-ai/
├── README.md           Goal, domain contract, status, usage
├── src/                Source code
├── notebooks/          Curated notebooks
├── tests/              Assertions and independent checks
├── runs/               Small example outputs and trace manifests
├── requirements.txt    Only if actually needed
└── CHANGELOG.md        Corrections, revisions, deprecated routes
```

Each project should state **WHAT**, **WHERE**, **ROUTE**, **INVERSE**, **STATUS**, **HOW TO RUN**, and **READOUT**. This keeps the compiler convention visible in the directory structure.

## Publication index contract

Create one row per *version* of a paper, not merely one row per title:

| Field | Required |
|:--|:--|
| `title`, `author`, `date`, `version` | Yes |
| `status`: published / draft / superseded | Yes |
| `DOI / Zenodo URL` | If published and available |
| `paper path` | Yes, if mirrored here |
| `source path` | When available |
| `code / notebook / run paths` | When available |
| `supersedes` / `superseded by` | When applicable |
| `correction log` | When applicable |

**Never overwrite a published artifact to make its contents look newer.** Publish a new version and record the relationship.

## Safe migration sequence

1. **Inventory first.** Export file paths, byte sizes, SHA-256 hashes, MIME/extensions and Git commit IDs. Record which are duplicated by content rather than filename.
2. **Publish navigation first.** README and reader's guide can be added without moving one historical file.
3. **Index publications.** Pair `.pdf`, `.md`, source versions and DOI. Resolve duplicate copies through indexes, not deletion.
4. **Promote reproducible code.** Move *selected* canonical scripts/notebooks into topic projects and add tests. Preserve originals or Git history.
5. **Move active work.** Put current unpublished experiments in `lab/active/` and drafts in `lab/drafts/`.
6. **Archive the remaining dump.** Keep a stable manifest and record old-to-new path mappings; redirect or document changed links.
7. **Separate large data.** Source code and small traces stay in Git. Bulk media, datasets, million-line dialogue and large notebook outputs can live in Drive / archival releases, with checksums and exact external links in the repo.
8. **Set licensing deliberately.** Existing paper CC BY-NC notices do not define a blanket software license. Decide separately how code, datasets and prose may be reused.

## House rules

- No guessed DOI, no reconstructed publication dates, no invented test counts.
- No manual rewriting of historical transcripts or older published papers.
- Status labels describe **the specific theorem or run**, not a whole directory.
- An execution log must identify its source revision, seed, command, scope and failure count.
- Research corrections are first-class artifacts, not embarrassing files to erase.
- A missing result is recorded as `OPEN`; no placeholder value is counted as evidence.

## Why not move everything today?

GitHub already has a substantial public directory tree. Changing hundreds of links and duplicate copies before making an inventory would sacrifice the very traceability the project is built around. **A navigable front door and an indexed, incremental migration get the benefit without that loss.**