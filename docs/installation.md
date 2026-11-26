# Installation

## Install with the Skills CLI

The [Skills CLI](https://github.com/vercel-labs/skills) installs the `SKILL.md` format used by this repository. Use a Node.js version supported by the current CLI.

```sh
npx skills add siarhei-belavus/agent-smitt
```

The interactive installer selects skills and agents. Project installation is the default. For all skills in a specific agent, such as Codex or Claude Code:

```sh
npx skills add siarhei-belavus/agent-smitt --skill '*' --agent codex
npx skills add siarhei-belavus/agent-smitt --skill '*' --agent claude-code
```

For a global installation:

```sh
npx skills add siarhei-belavus/agent-smitt --skill '*' --agent codex --global
```

For a single standalone tool:

```sh
npx skills add siarhei-belavus/agent-smitt --skill diagnosing-bugs
```

List the available skills without installing:

```sh
npx skills add siarhei-belavus/agent-smitt --list
```

Each skill includes the Markdown references it links to. A reference copy does not install another skill's invocation entry. Install the complete pack when using the planning and delivery workflow, because its skills invoke each other by name.

A project-owned skill copy can be adapted as part of the project's documentation. For symlink installations, resolve the maintained source before proposing edits; a link inside the project does not grant ownership of an external checkout. Generated reference bundles follow their owning source's packaging procedure.

To inspect or update installations, use `npx skills list`, `npx skills check`, and `npx skills update`. Refer to the [CLI documentation](https://github.com/vercel-labs/skills) for agent identifiers and current options.

## Develop from a checkout

```sh
git clone https://github.com/siarhei-belavus/agent-smitt.git
cd agent-smitt
npx skills add . --skill '*' --agent codex
```

The repository also keeps a dependency-free Python installer for contributors who want live links to the checkout:

```sh
./bin/install-codex-skills
```

It links skills into `~/.agents/skills`, the Codex default, along with the shared workflow contract directory. For Claude Code, pass `--target "$HOME/.claude/skills"`. Edits in the checkout are immediately visible through these links. It is idempotent and refuses to replace an unrelated existing path. Use `--target /path/to/skills` for an isolated installation. Inspect existing entries before switching installation methods over the same destination.

## Prepare your agent

Installing instructions does not configure a project or grant provider access. Planning and delivery need:

- An agent that can read repository files and run Git and repository validation commands.
- Subagent support for skills that delegate research, implementation, or review. `deliver-spec` also needs separate ticket-coordinator contexts capable of their own delegation, with a mechanism to observe, continue, and recover them. Coordinators start as ordinary subagents; one that cannot delegate reports that before claiming its ticket and is relaunched as a separate top-level session. The [execution host contract](../skills/engineering/federated-workflow/EXECUTION-HOST.md) defines the required capabilities.
- Authenticated access to the selected Code Host and Work Tracker. The setup skill records how to use those providers in the repository's bindings.
- The project's normal build, test, and development tools.

The pack uses portable skill files, but tool names and delegation capabilities vary between agents. The CLI's ability to install a skill does not prove that an agent supports every workflow operation.

Start with [repository setup](workflow.md#configure-the-repositories). Simple interviews, design advice, and standalone diagnosis do not require federation setup.

## Reproducible use

For CI or a shared team setup, check out a reviewed commit and install that local source. Record the chosen revision in your own configuration. The main branch changes as the skills evolve.

```sh
git clone https://github.com/siarhei-belavus/agent-smitt.git
git -C agent-smitt checkout "$SKILLS_REF"
agent-smitt/bin/install-codex-skills --target "$HOME/.agents/skills"
```

Set `SKILLS_REF` to the revision you reviewed. Python 3.10 or later is required for the local installer and repository checks.
