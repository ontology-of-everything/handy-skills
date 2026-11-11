# handy-skills

Agent skills for office work, reading notes, and English vocabulary. English names are the base; Simplified Chinese adds `-cn`.

中文：[README-CN.md](README-CN.md)

## Skills

| English | 中文 | What it does |
| --- | --- | --- |
| [`debloat`](skills/en/debloat/SKILL.md) | [`debloat-cn`](skills/zh-CN/debloat-cn/SKILL.md) | Restate the last message. Clean it up only: clearer logic, fewer words, filler removed, wording left unpolished. |
| [`source-brief`](skills/en/source-brief/SKILL.md) | [`source-brief-cn`](skills/zh-CN/source-brief-cn/SKILL.md) | Organize reading notes. Separate statements from evidence. |
| [`word-aha`](skills/en/word-aha/SKILL.md) | [`word-aha-cn`](skills/zh-CN/word-aha-cn/SKILL.md) | Learn an English word from 1–5 sourced sentences, then check it in a new sentence. |
| [`arb`](skills/en/arb/SKILL.md) | [`arb-cn`](skills/zh-CN/arb-cn/SKILL.md) | Architecture Review Board review. Criteria pending. |

`source-brief` and `word-aha` can be selected automatically. The others run only when named.

```text
$debloat Restate the last message. Clean it up only
$source-brief Organize this paper and distinguish claims, opinions, experience, and unverified information
$word-aha Help me learn everyday English words for ordering coffee through context cards
$arb Review this architecture proposal as the Architecture Review Board
```

Word Aha starts from sentences, not from a word list. It keeps the target word visible in 1–5 sourced examples, compares context, then checks a new situation with a multi-select or a single word.

Index: [catalog.yml](catalog.yml). Rules: [CLAUDE.md](CLAUDE.md).

## Install

Node.js 22.20+ and Git. Run from the project directory. This installs into Codex for that project. Use `--agent claude-code` or `--agent cursor` for another agent, and `--global` for every project. [Installer options](https://github.com/vercel-labs/skills/blob/main/docs/commands.md).

English:

```bash
npx --yes skills add ontology-of-everything/handy-skills --skill debloat arb source-brief word-aha --agent codex --copy --yes
```

Simplified Chinese: the same command with `debloat-cn arb-cn source-brief-cn word-aha-cn`.

One skill: replace that list with one name. List the skills: `npx --yes skills add ontology-of-everything/handy-skills --list`.

Payloads: `skills/en/`, `skills/zh-CN/`. ClawHub publishes English only.

## Contributing

`qa/` is private and untracked. Public checks do not use it. Run `./tools/validate-all.sh --local-qa` only when local QA is present.

```bash
git config core.hooksPath .githooks
./tools/validate-all.sh
```

## License

[Apache-2.0](LICENSE) © handy-skills contributors.
