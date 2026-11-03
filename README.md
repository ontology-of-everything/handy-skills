# myoffice-skills

Practical Agent Skills for office workflows, developer productivity, and English vocabulary learning.
English editions use the base name and Simplified Chinese editions add `-cn`; some skills are Chinese-only. `trimme` keeps its chosen name.

中文说明见 [README-CN.md](README-CN.md).

## Skills

| English | 中文 | What it does |
| -------------------- | -------------------------------------------------------------------- | -------------------------------------------------------- |
| — | [`trimme`](skills/zh-CN/trimme/SKILL.md) | Removes filler and repetition, preserves meaning, and lightly clarifies logic without polishing. |
| [`claude-md`](skills/en/claude-md/SKILL.md) | [`claude-md-cn`](skills/zh-CN/claude-md-cn/SKILL.md) | Creates or prunes CLAUDE.md from repository evidence. |
| [`source-brief`](skills/en/source-brief/SKILL.md) | [`source-brief-cn`](skills/zh-CN/source-brief-cn/SKILL.md) | Organizes reading notes and distinguishes statements from evidence. |
| [`word-aha`](skills/en/word-aha/SKILL.md) | [`word-aha-cn`](skills/zh-CN/word-aha-cn/SKILL.md) | Starts with sentences to learn English words through 1–5 sourced examples, context comparison, and transfer checks. |
| [`agent-dx-cli`](skills/en/agent-dx-cli/SKILL.md) | [`agent-dx-cli-cn`](skills/zh-CN/agent-dx-cli-cn/SKILL.md) | Designs, reviews, and refactors CLIs with evidence scoring and GWS practice. Supports companion skill authoring when requested. |
| [`arb`](skills/en/arb/SKILL.md) | [`arb-cn`](skills/zh-CN/arb-cn/SKILL.md) | Architecture Review Board reviews; criteria pending. |
| — | [`presentation-making-cn`](skills/zh-CN/presentation-making-cn/SKILL.md) | Turns sources into memorable HTML or Markdown decks through alignment and review. |
| — | [`brand-ui-design-cn`](skills/zh-CN/brand-ui-design-cn/SKILL.md) | Applies six UI design principles to strengthen brand memory and interface experience. |

Machine-readable metadata lives in [catalog.yml](catalog.yml). Localization rules live in [CLAUDE.md](CLAUDE.md).

## Install

Requires Node.js 22.20+ and Git. Copy a command below and run it from your project directory. These commands install to Codex in the current project.

Use `--agent claude-code` or `--agent cursor` for another agent; add `--global` to install across projects. See the [installer options](https://github.com/vercel-labs/skills/blob/main/docs/commands.md).

### English editions

```bash
npx --yes skills add ontology-of-everything/myoffice-skills --skill claude-md arb source-brief agent-dx-cli word-aha --agent codex --copy --yes
```

### Simplified Chinese editions

```bash
npx --yes skills add ontology-of-everything/myoffice-skills --skill trimme brand-ui-design-cn presentation-making-cn claude-md-cn arb-cn source-brief-cn agent-dx-cli-cn word-aha-cn --agent codex --copy --yes
```

### Install one skill

**`trimme`**

```bash
npx --yes skills add ontology-of-everything/myoffice-skills --skill trimme --agent codex --copy --yes
```

**`brand-ui-design-cn`**

```bash
npx --yes skills add ontology-of-everything/myoffice-skills --skill brand-ui-design-cn --agent codex --copy --yes
```

**`presentation-making-cn`**

```bash
npx --yes skills add ontology-of-everything/myoffice-skills --skill presentation-making-cn --agent codex --copy --yes
```

**`claude-md`**

```bash
npx --yes skills add ontology-of-everything/myoffice-skills --skill claude-md --agent codex --copy --yes
```

**`arb`**

```bash
npx --yes skills add ontology-of-everything/myoffice-skills --skill arb --agent codex --copy --yes
```

**`source-brief`**

```bash
npx --yes skills add ontology-of-everything/myoffice-skills --skill source-brief --agent codex --copy --yes
```

**`agent-dx-cli`**

```bash
npx --yes skills add ontology-of-everything/myoffice-skills --skill agent-dx-cli --agent codex --copy --yes
```

**`word-aha`**

```bash
npx --yes skills add ontology-of-everything/myoffice-skills --skill word-aha --agent codex --copy --yes
```

### List available skills

```bash
npx --yes skills add ontology-of-everything/myoffice-skills --list
```

English payloads live in `skills/en/`; Simplified Chinese payloads live in `skills/zh-CN/` and use their declared names; Chinese-only `trimme` keeps its chosen name. ClawHub publishes English editions only.

## Usage

Reading notes, English vocabulary practice, and brand UI design support automatic selection and explicit invocation; other skills require explicit invocation:

```text
$trimme Clean up this text while preserving meaning, without polishing
$agent-dx-cli Review this CLI and implement the authorized improvements
$source-brief Organize this paper and distinguish claims, opinions, experience, and unverified information
$word-aha Help me learn everyday English words for ordering coffee through context cards
$claude-md Create concise CLAUDE.md guidance from this repository
$arb Review this architecture proposal as the Architecture Review Board
$presentation-making-cn Turn these materials into a memorable presentation
$brand-ui-design-cn Improve this product interface using the six design principles
```

## English vocabulary learning with Word Aha

Word Aha reverses "memorize words → assemble sentences": **sentences are the starting point for
understanding English words**. Search for 1–5 sourced everyday examples of the current use, keep the
target word visible, and compare familiar context clues to connect meaning, collocations, and
situations. Add context or simplify unclear language, use a post-answer "aha!" callout, then check a
new situation through multi-select or single-word answers, recording independent performance and
assistance for review.

```bash
npx skills add ontology-of-everything/myoffice-skills --skill word-aha --agent codex --copy -y
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

[Apache-2.0](LICENSE) © myoffice-skills contributors.
