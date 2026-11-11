# handy-skills

面向办公、开发提效与英文单词学习的 Agent Skills 仓库，英文版使用基础名，简体中文版增加 `-cn`。

English: [README.md](README.md)。

## 技能

| English | 中文 | 能力 |
| -------------------- | -------------------------------------------------------------------- | ------------------------------------- |
| [`debloat`](skills/en/debloat/SKILL.md) | [`debloat-cn`](skills/zh-CN/debloat-cn/SKILL.md) | 重述最后一条信息，只做清理，不要润色，更有逻辑、更简洁，去掉口头禅和废话 |
| [`source-brief`](skills/en/source-brief/SKILL.md) | [`source-brief-cn`](skills/zh-CN/source-brief-cn/SKILL.md) | 整理文章与论文，区分陈述性质和证据状态 |
| [`word-aha`](skills/en/word-aha/SKILL.md) | [`word-aha-cn`](skills/zh-CN/word-aha-cn/SKILL.md) | 以句子为起点，从 1～5 句有来源例句中对照猜义，再换句检验英文单词用法 |
| [`arb`](skills/en/arb/SKILL.md) | [`arb-cn`](skills/zh-CN/arb-cn/SKILL.md) | 架构评审委员会评审；准则待定 |

机器可读目录见 [catalog.yml](catalog.yml)，本地化规则见 [CLAUDE.md](CLAUDE.md)。

## 安装

需要 Node.js 22.20+ 与 Git。在目标项目目录运行下列命令，直接复制即可；默认安装到当前项目的 Codex，不修改全局技能。

`--agent codex` 可换为 `--agent claude-code` 或 `--agent cursor`；增加 `--global` 可供所有项目使用。技能安装器的[参数说明](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)。

### 中文版

```bash
npx --yes skills add ontology-of-everything/handy-skills --skill debloat-cn arb-cn source-brief-cn word-aha-cn --agent codex --copy --yes
```

### 英文版

```bash
npx --yes skills add ontology-of-everything/handy-skills --skill debloat arb source-brief word-aha --agent codex --copy --yes
```

### 按需安装单个技能

**`debloat-cn`**

```bash
npx --yes skills add ontology-of-everything/handy-skills --skill debloat-cn --agent codex --copy --yes
```

**`arb-cn`**

```bash
npx --yes skills add ontology-of-everything/handy-skills --skill arb-cn --agent codex --copy --yes
```

**`source-brief-cn`**

```bash
npx --yes skills add ontology-of-everything/handy-skills --skill source-brief-cn --agent codex --copy --yes
```

**`word-aha-cn`**

```bash
npx --yes skills add ontology-of-everything/handy-skills --skill word-aha-cn --agent codex --copy --yes
```

### 查看可安装技能

```bash
npx --yes skills add ontology-of-everything/handy-skills --list
```

英文载荷位于 `skills/en/`，简体中文载荷位于 `skills/zh-CN/`。ClawHub 仅发布英文版。

## 用法

阅读整理和英文单词学习支持自动选用，也可显式调用；其余技能仅显式调用：

```text
$debloat-cn 重述你最后一条信息，只做清理，不要润色
$source-brief-cn 整理这篇论文，区分事实、观点、经验与未证实信息
$word-aha-cn 用交互卡片带我学习点咖啡时常用的英文单词
$arb-cn 以架构评审委员会身份评审这份架构方案
```

## 英文单词学习

本技能把“先背单词→再拼句子”换成**先读熟句→对照猜义→换句验证**，以句子为理解英文单词的起点。
搜索目标词当前用法的 1～5 句有来源日常例句，保留目标词，让熟悉语境同时提供词义线索、搭配和场景。
线索不足就补充、不懂就简化，答后用“啊哈！”提示框串联理解，再通过多选或单个词作答检验新情境，并记录独立表现与所需帮助供复盘。

```bash
npx skills add ontology-of-everything/handy-skills --skill word-aha-cn --agent codex --copy -y
```

```text
$word-aha-cn 带我学点咖啡时常用的英文单词，用多选或单个词回答
```

## 贡献

`qa/` 仅供本机使用，不提交、不发布；公开校验不依赖它。需要运行本机用例时，使用 `./tools/validate-all.sh --local-qa`。

项目职责与目录规范见 [CLAUDE.md](CLAUDE.md)。

```bash
git config core.hooksPath .githooks
./tools/validate-all.sh
```

## 许可

[Apache-2.0](LICENSE) © handy-skills contributors。
