# handy-skills

Practical Agent Skills for office workflows, developer productivity, and English vocabulary learning.
English editions use the base name and Simplified Chinese editions add `-cn`.

中文说明见 [README-CN.md](README-CN.md).

## Skills

| English | 中文 | What it does |
| -------------------- | -------------------------------------------------------------------- | -------------------------------------------------------- |
| [`debloat`](skills/en/debloat/SKILL.md) | [`debloat-cn`](skills/zh-CN/debloat-cn/SKILL.md) | Restates the last message by cleaning it up only: clearer logic, fewer words, filler removed, wording left unpolished. |
| [`source-brief`](skills/en/source-brief/SKILL.md) | [`source-brief-cn`](skills/zh-CN/source-brief-cn/SKILL.md) | Organizes reading notes and distinguishes statements from evidence. |
| [`word-aha`](skills/en/word-aha/SKILL.md) | [`word-aha-cn`](skills/zh-CN/word-aha-cn/SKILL.md) | Starts with sentences to learn English words through 1–5 sourced examples, context comparison, and transfer checks. |
| [`arb`](skills/en/arb/SKILL.md) | [`arb-cn`](skills/zh-CN/arb-cn/SKILL.md) | Architecture Review Board reviews; criteria pending. |

Machine-readable metadata lives in [catalog.yml](catalog.yml). Localization rules live in [CLAUDE.md](CLAUDE.md).

## Install

Requires Node.js 22.20+ and Git. Copy a command below and run it from your project directory. These commands install to Codex in the current project.

Use `--agent claude-code` or `--agent cursor` for another agent; add `--global` to install across projects. See the [installer options](https://github.com/vercel-labs/skills/blob/main/docs/commands.md).

### English editions

```bash
npx --yes skills add ontology-of-everything/handy-skills --skill debloat arb source-brief word-aha --agent codex --copy --yes
```

### Simplified Chinese editions

```bash
npx --yes skills add ontology-of-everything/handy-skills --skill debloat-cn arb-cn source-brief-cn word-aha-cn --agent codex --copy --yes
```

### Install one skill

**`debloat`**

```bash
npx --yes skills add ontology-of-everything/handy-skills --skill debloat --agent codex --copy --yes
```

**`arb`**

```bash
npx --yes skills add ontology-of-everything/handy-skills --skill arb --agent codex --copy --yes
```

**`source-brief`**

```bash
npx --yes skills add ontology-of-everything/handy-skills --skill source-brief --agent codex --copy --yes
```

**`word-aha`**

```bash
npx --yes skills add ontology-of-everything/handy-skills --skill word-aha --agent codex --copy --yes
```

### List available skills

```bash
npx --yes skills add ontology-of-everything/handy-skills --list
```

English payloads live in `skills/en/`; Simplified Chinese payloads live in `skills/zh-CN/`. ClawHub publishes English editions only.

## Usage

Reading notes and English vocabulary practice support automatic selection and explicit invocation; other skills require explicit invocation:

```text
$debloat Restate the last message. Clean it up only
$source-brief Organize this paper and distinguish claims, opinions, experience, and unverified information
$word-aha Help me learn everyday English words for ordering coffee through context cards
$arb Review this architecture proposal as the Architecture Review Board
```

## English vocabulary learning with Word Aha

Word Aha reverses "memorize words → assemble sentences": **sentences are the starting point for
understanding English words**. Search for 1–5 sourced everyday examples of the current use, keep the
target word visible, and compare familiar context clues to connect meaning, collocations, and
situations. Add context or simplify unclear language, use a post-answer "aha!" callout, then check a
new situation through multi-select or single-word answers, recording independent performance and
assistance for review.

```bash
npx skills add ontology-of-everything/handy-skills --skill word-aha --agent codex --copy -y
```

```text
$word-aha Help me learn English words for ordering coffee; let me answer with selections or a single word
```

## Contributing

`qa/` is private and untracked; public checks do not depend on it. Run `./tools/validate-all.sh --local-qa` only when local QA is available.

Project rules and repository ownership: [CLAUDE.md](CLAUDE.md).

```bash
git config core.hooksPath .githooks
./tools/validate-all.sh
```

## License

[Apache-2.0](LICENSE) © handy-skills contributors.
