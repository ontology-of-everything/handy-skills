# handy-skills

面向办公、阅读笔记和英文单词学习的 Agent Skills。英文版用基础名，简体中文版加 `-cn`。

English: [README.md](README.md)

## 技能

| English | 中文 | 能力 |
| --- | --- | --- |
| [`debloat`](skills/en/debloat/SKILL.md) | [`debloat-cn`](skills/zh-CN/debloat-cn/SKILL.md) | 重述最后一条信息，只做清理，不润色：理顺逻辑，减少字数，去掉口头禅和废话 |
| [`source-brief`](skills/en/source-brief/SKILL.md) | [`source-brief-cn`](skills/zh-CN/source-brief-cn/SKILL.md) | 整理文章与论文，区分陈述和证据 |
| [`word-aha`](skills/en/word-aha/SKILL.md) | [`word-aha-cn`](skills/zh-CN/word-aha-cn/SKILL.md) | 从 1～5 句有来源例句对照猜义，再换句检验英文单词 |
| [`arb`](skills/en/arb/SKILL.md) | [`arb-cn`](skills/zh-CN/arb-cn/SKILL.md) | 架构评审委员会评审。准则待定 |
| [`fit`](skills/en/fit/SKILL.md) | [`fit-cn`](skills/zh-CN/fit-cn/SKILL.md) | 以人为中心指导前端修改、设计和排查。 |
| [`security-and-hardening`](skills/en/security-and-hardening/SKILL.md) | — | 安全审查与加固。原样引自 [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/tree/main/skills/security-and-hardening)，采用 MIT 许可证。 |
| — | [`principle-thin-wrapper-cn`](skills/zh-CN/principle-thin-wrapper-cn/SKILL.md) | 薄封装原则：优先复用成熟组件，按需薄封装。 |

`source-brief-cn`、`word-aha-cn`、`principle-thin-wrapper-cn`、`fit` 和 `fit-cn` 可以自动选用。其余技能只在点名时运行。

```text
$debloat-cn 重述你最后一条信息，只做清理，不要润色
$source-brief-cn 整理这篇论文，区分事实、观点、经验与未证实信息
$word-aha-cn 用交互卡片带我学习点咖啡时常用的英文单词
$arb-cn 以架构评审委员会身份评审这份架构方案
```

单词啊哈从句子开始，不从词表开始。它在 1～5 句有来源例句里保留目标词，对照语境，再用多选或一个词检验新句子。

目录：[catalog.yml](catalog.yml)。规则：[CLAUDE.md](CLAUDE.md)。

## 安装

需要 Node.js 22.20+ 和 Git。在项目目录运行。默认装到该项目的 Codex。`--agent` 可换成 `claude-code` 或 `cursor`；加 `--global` 则所有项目可用。[安装参数](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)。

中文：

```bash
npx --yes skills add ontology-of-everything/handy-skills --skill debloat-cn arb-cn source-brief-cn word-aha-cn principle-thin-wrapper-cn --agent codex --copy --yes
```

英文：同一命令，技能名换成 `debloat arb source-brief word-aha`。

只装一个：把列表换成一个名字。查看可装技能：`npx --yes skills add ontology-of-everything/handy-skills --list`。

载荷在 `skills/en/` 和 `skills/zh-CN/`。ClawHub 只发布英文版。

引入的 `security-and-hardening` 还依赖共享的[安全清单](skills/references/security-checklist.md)。使用时请保持其仓库相对路径；单技能安装工具可能不会复制该文件。

## 贡献

`qa/` 只在本机，不提交、不发布。公开校验不使用它。本机有用例时再运行 `./tools/validate-all.sh --local-qa`。

```bash
git config core.hooksPath .githooks
./tools/validate-all.sh
```

## 许可

[Apache-2.0](LICENSE) © handy-skills contributors。
引入的 security-and-hardening 技能及其共享清单采用上游 [MIT 许可证](skills/en/security-and-hardening/LICENSE)。
