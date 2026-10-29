# Installation

## Install with the Skills CLI

The [Skills CLI](https://github.com/vercel-labs/skills) installs the `SKILL.md` format used by this repository. Use a Node.js version supported by the current CLI.

```sh
npx skills add siarhei-belavus/agent-smitty
```

The interactive installer selects skills and agents. Project installation is the default. For all skills in a specific agent:

```sh
npx skills add siarhei-belavus/agent-smitty --skill '*' --agent codex
```

For a global installation:

```sh
npx skills add siarhei-belavus/agent-smitty --skill '*' --agent codex --global
```

For a single standalone tool:

```sh
npx skills add siarhei-belavus/agent-smitty --skill diagnosing-bugs
```

List the available skills without installing:

```sh
npx skills add siarhei-belavus/agent-smitty --list
```

Each skill includes the Markdown references it links to. A reference copy does not install another skill's invocation entry. Install the complete pack when using the planning and delivery workflow, because its skills invoke each other by name.

To inspect or update installations, use `npx skills list`, `npx skills check`, and `npx skills update`. Refer to the [CLI documentation](https://github.com/vercel-labs/skills) for agent identifiers and current options.

## Develop from a checkout

```sh
git clone https://github.com/siarhei-belavus/agent-smitty.git
cd agent-smitty
npx skills add . --skill '*' --agent codex
```

The repository also keeps a dependency-free Python installer for Codex contributors who want live links to the checkout:

```sh
./bin/install-codex-skills
```

It links skills into `~/.agents/skills`, along with the shared workflow contract directory. Edits in the checkout are immediately visible through these links. It is idempotent and refuses to replace an unrelated existing path. Use `--target /path/to/skills` for an isolated installation. Inspect existing entries before switching installation methods over the same destination.

## Prepare your agent

Installing instructions does not configure a project or grant provider access. Planning and delivery need:

- An agent that can read repository files and run Git and repository validation commands.
- Subagent support for skills that delegate research, implementation, or review, especially `coordinate-delivery`.
- Authenticated access to the selected Code Host and Work Tracker. The setup skill records how to use those providers in the repository's bindings.
- The project's normal build, test, and development tools.

The pack uses portable skill files, but tool names and delegation capabilities vary between agents. The CLI's ability to install a skill does not prove that an agent supports every workflow operation.

Start with [repository setup](workflow.md#configure-the-repositories). Simple interviews, design advice, and standalone diagnosis do not require federation setup.

## Reproducible use

For CI or a shared team setup, check out a reviewed commit and install that local source. Record the chosen revision in your own configuration. The main branch changes as the skills evolve.

```sh
git clone https://github.com/siarhei-belavus/agent-smitty.git
git -C agent-smitty checkout "$SKILLS_REF"
agent-smitty/bin/install-codex-skills --target "$HOME/.agents/skills"
```

Set `SKILLS_REF` to the revision you reviewed. Python 3.10 or later is required for the local installer and repository checks.
