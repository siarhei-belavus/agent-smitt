# Repository instructions

This repository is the source of truth for the skills under `skills/`.

- Keep each skill and all of its relative references in one complete directory
  tree.
- Give every skill a unique `name` in its `SKILL.md` front matter.
- Put stable engineering skills under `skills/engineering` and stable personal
  workflow skills under `skills/productivity`. Keep experiments and private
  maintenance tools outside the public catalog.
- Run the installer tests after changing skill layout or installation behavior.
- Do not add generated Codex symlinks to this repository.
- Keep linked reference sources in their owning directories. Regenerate
  `references/bundled/` with `python3 bin/sync-skill-references`; do not edit
  generated copies directly. Run its `--check` mode before delivery.
- Keep the public catalog in `docs/skills.md` and workflow guide in
  `docs/workflow.md` consistent with the retained skills.
