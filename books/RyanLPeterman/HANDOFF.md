# RyanLPeterman transcript-to-book handoff

## User request

Turn every transcript in `/Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/transcripts/RyanLPeterman` into a detailed English book. Preserve useful discussion, remove repetition, keep interview questions and ordered follow-ups together, add editorial diagrams when they clarify a mechanism, and render an offline interactive HTML book plus editable JSON.

The user explicitly authorized parallel agents for the complete book.

## Skills

- Active task skill: [`transcript-to-book`](file:///Users/yongjiexue/.codex/skills/transcript-to-book/SKILL.md)
- Local saved reusable skill folder: `/Users/yongjiexue/.codex/skills/transcript-to-book/`
- Skill creation instructions used: [`skill-creator`](file:///Users/yongjiexue/.codex/skills/.system/skill-creator/SKILL.md)

Read the active `SKILL.md` before changing the workflow. Its important rules are: use the authoritative prepared manifest, read every source chunk, preserve source evidence, distinguish speaker claims from editorial synthesis, keep all sources in the ledger, and validate before rendering.

## Current outputs

- Final HTML: [`book.html`](file:///Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/books/RyanLPeterman/book.html)
- Editable book JSON: [`book.json`](file:///Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/books/RyanLPeterman/book.json)
- Authoritative manifest: [`prepared-v2/manifest.json`](file:///Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/books/RyanLPeterman/prepared-v2/manifest.json)
- Authored source wrappers: `books/RyanLPeterman/sections/source-*.json`
- Progress ledger: [`editorial/progress.json`](file:///Users/yongjiexue/Documents/GitHub/youtube-transcript-pipeline/books/RyanLPeterman/editorial/progress.json)
- Lossless compact reading files: `books/RyanLPeterman/editorial/compact-reading/<source-id>/chunk-###.md`

The current edition is marked `complete`: 107 manifest sources, 106 included sections, 1 intentionally excluded non-substantive celebration clip, 0 pending sources, 1,423 initiating question blocks, and 829 nested follow-ups. All 106 sections are hand-authored; the former 35 fallback sections were rewritten in the latest pass. The excluded source is `source-25fc71be2283fe84` (“100,000 🙏”); it contains only a brief celebration, laughter, and thanks.

## How to validate or rebuild

From the repository root:

```bash
python3 books/RyanLPeterman/editorial/assemble_book.py --complete
python3 /Users/yongjiexue/.codex/skills/transcript-to-book/scripts/render_book.py \
  books/RyanLPeterman/book.json \
  --manifest books/RyanLPeterman/prepared-v2/manifest.json \
  --output /tmp/ryan-final.html --overwrite
```

The second command completed successfully during this run. In the latest pass it rebuilt `book.html` with 106 chapters and no external scripts or stylesheets. Playwright was not installed, so the desktop and 390px mobile overflow check was not re-run on this edition. Rerun it before publishing. The earlier check (on the previous edition) passed and produced these screenshots:

- `editorial/final-desktop-check.png`
- `editorial/final-mobile-check.png`

The renderer is strict about table blocks: use `headers`, not `columns`. Evidence ranges must fall within the source’s parsed timestamp bounds. Source hashes must come from `prepared-v2/manifest.json`.

## Important implementation details

- The parser was corrected for long videos with timestamps such as `[100:00.44]`; the authoritative data is `prepared-v2`, not the older `prepared` directory.
- `editorial/author_helpers.py` provides the validated authoring DSL (`p`, `qa`, `follow`, `flow`, `table`, `callout`, `write`).
- `editorial/assemble_book.py` groups chapters into thematic parts and adds related-section links. It must be run with `--complete` for the final edition.
- `editorial/fallback_sections.py` was added during the quota outage to create timestamp-linked structural maps. The latest pass replaced all 35 of those wrappers with hand-authored sections (each written with `author_helpers.write`, validated, and reviewed chunk-by-chunk). The script remains only as a fallback tool and is no longer used for the current edition.
- Original transcripts are preserved. Do not delete `transcripts/`, `prepared-v2/`, compact-reading files, or existing authored wrappers.

## Ownership and resume guidance

All source IDs are listed in `editorial/assignments.json`. Existing wrappers in `sections/` are authoritative and should not be overwritten casually. To improve a fallback section, read its compact chunks fully, replace its wrapper using `author_helpers.write(...)`, then run the renderer command above.

The reusable skill itself is saved outside the repository at `/Users/yongjiexue/.codex/skills/transcript-to-book/`; keep that path in any future handoff or agent message. A copy for Claude Code is at `/Users/yongjiexue/.claude/skills/transcript-to-book/` (SKILL.md, references/, scripts/, assets/, agents/; `__pycache__` excluded). Both copies are identical as of this pass, and the scripts still import `render_book.py` from the `.codex` path, so keep that path in place.
