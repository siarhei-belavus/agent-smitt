# Contributing

Agent Smitty maintains a curated engineering workflow. A new skill should solve a distinct recurring problem and explain when to invoke it. Changes to existing skills should name the behavior they change and the failure they prevent.

## Layout

```text
skills/
  engineering/          Stable software delivery skills
    federated-workflow/ Shared contract sources, not an invokable skill
  productivity/         Stable thinking and communication skills
docs/                   Installation, workflow, catalog, and credits
bin/                    Local installer and reference packager
tests/                  Distribution checks
.github/                CI and issue templates
```

Keep each skill in a directory named after its unique frontmatter `name`. Supporting scripts, templates, and references belong in that directory. Keep engineering and productivity skills in their existing categories. Avoid adding personal experiments and one-off migrations to the public catalog.

## Package linked references

The Skills CLI copies individual skill directories. References outside a skill's directory need bundled copies to survive installation.

Canonical sources live in their owning skill or in `skills/engineering/federated-workflow/`. Edit those files. `references/bundled/` inside a skill is generated distribution content and is checked into Git so installation needs no build step.

After editing a source or adding a relative Markdown link:

```sh
python3 bin/sync-skill-references
```

The packager follows linked Markdown files transitively and includes only the references each skill needs. It rewrites link destinations for their installed locations and includes the root license in each skill. Copied skill instructions use `SKILL.reference.md` so they do not become duplicate skill entries. A bundled copy supplies reference text, not another skill's invocation.

For a new cross-skill reference, write the ordinary relative Markdown link to its canonical source, then run the packager. It converts that link to the bundled destination. Links in fenced examples remain example content.

Do not edit generated copies directly. The check mode detects drift and stale files:

```sh
python3 bin/sync-skill-references --check
```

## Validate

Use Python 3.10 or later. The standard-library checks need no package installation.

```sh
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 -m unittest discover -s skills/engineering/setup-federated-workflow/tests -p 'test_*.py' -v
python3 bin/sync-skill-references --check
git diff --check
```

For a distribution smoke test, create a temporary project outside this checkout and run the CLI there, pointing it at this repository's absolute path:

```sh
npx skills add /absolute/path/to/agent-smitty --skill '*' --agent codex --yes
```

Check discovery with `--list` and repeat with `--copy` when changing packaging. Never add generated agent installation links to this repository.

## Documentation and attribution

Keep the [workflow guide](docs/workflow.md) consistent with the skill rules. Update the [catalog](docs/skills.md) when adding or removing a skill. Use English for repository documentation and sentence case for headings.

Preserve upstream copyright and skill-specific credits. Include the source and license for substantial third-party contributions. Remove credentials and private project data from examples and issue reports.

Describe validation and behavioral consequences in pull requests. Leave unrelated skill instructions unchanged when changing distribution or documentation.
