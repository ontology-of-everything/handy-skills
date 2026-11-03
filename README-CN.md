# myoffice-skills

面向办公、开发提效与英文单词学习的 Agent Skills 仓库，英文版使用基础名，简体中文版增加 `-cn`，部分技能仅提供中文版；`trimme` 保留指定名称。

English: [README.md](README.md)。

## 技能

| English | 中文 | 能力 |
| -------------------- | -------------------------------------------------------------------- | ------------------------------------- |
| — | [`trimme`](skills/zh-CN/trimme/SKILL.md) | 保留原意，去掉口头禅、重复和废话，适当理顺逻辑，不做润色 |
| [`claude-md`](skills/en/claude-md/SKILL.md) | [`claude-md-cn`](skills/zh-CN/claude-md-cn/SKILL.md) | 根据仓库事实生成或精简 CLAUDE.md |
| [`source-brief`](skills/en/source-brief/SKILL.md) | [`source-brief-cn`](skills/zh-CN/source-brief-cn/SKILL.md) | 整理文章与论文，区分陈述性质和证据状态 |
| [`word-aha`](skills/en/word-aha/SKILL.md) | [`word-aha-cn`](skills/zh-CN/word-aha-cn/SKILL.md) | 以句子为起点，从 1～5 句有来源例句中对照猜义，再换句检验英文单词用法 |
| [`agent-dx-cli`](skills/en/agent-dx-cli/SKILL.md) | [`agent-dx-cli-cn`](skills/zh-CN/agent-dx-cli-cn/SKILL.md) | 以十维检查、GWS 实践和证据评分指导 CLI 工程，按需编写配套技能 |
| [`arb`](skills/en/arb/SKILL.md) | [`arb-cn`](skills/zh-CN/arb-cn/SKILL.md) | 架构评审委员会评审；准则待定 |
| — | [`presentation-making-cn`](skills/zh-CN/presentation-making-cn/SKILL.md) | 从材料理解到可记忆的 HTML／Markdown 文稿，含对齐与检视重构 |
| — | [`brand-ui-design-cn`](skills/zh-CN/brand-ui-design-cn/SKILL.md) | 运用六条界面设计原则，强化品牌记忆与界面体验 |

机器可读目录见 [catalog.yml](catalog.yml)，本地化规则见 [CLAUDE.md](CLAUDE.md)。

## 安装

需要 Node.js 22.20+ 与 Git。在目标项目目录运行下列命令，直接复制即可；默认安装到当前项目的 Codex，不修改全局技能。

`--agent codex` 可换为 `--agent claude-code` 或 `--agent cursor`；增加 `--global` 可供所有项目使用。技能安装器的[参数说明](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)。

### 中文版

```bash
npx --yes skills add ontology-of-everything/myoffice-skills --skill trimme brand-ui-design-cn presentation-making-cn claude-md-cn arb-cn source-brief-cn agent-dx-cli-cn word-aha-cn --agent codex --copy --yes
```

### 英文版

```bash
npx --yes skills add ontology-of-everything/myoffice-skills --skill claude-md arb source-brief agent-dx-cli word-aha --agent codex --copy --yes
```

### 按需安装单个技能

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

**`claude-md-cn`**

```bash
npx --yes skills add ontology-of-everything/myoffice-skills --skill claude-md-cn --agent codex --copy --yes
```

**`arb-cn`**

```bash
npx --yes skills add ontology-of-everything/myoffice-skills --skill arb-cn --agent codex --copy --yes
```

**`source-brief-cn`**

```bash
npx --yes skills add ontology-of-everything/myoffice-skills --skill source-brief-cn --agent codex --copy --yes
```

**`agent-dx-cli-cn`**

```bash
npx --yes skills add ontology-of-everything/myoffice-skills --skill agent-dx-cli-cn --agent codex --copy --yes
```

**`word-aha-cn`**

```bash
npx --yes skills add ontology-of-everything/myoffice-skills --skill word-aha-cn --agent codex --copy --yes
```

### 查看可安装技能

```bash
npx --yes skills add ontology-of-everything/myoffice-skills --list
```

英文载荷位于 `skills/en/`，简体中文载荷位于 `skills/zh-CN/`；中文独立技能 `trimme` 保留指定名称。ClawHub 仅发布英文版。

## 用法

阅读整理、英文单词学习、品牌记忆与界面设计支持自动选用，也可显式调用；其余技能仅显式调用：

```text
$trimme 清理以下内容，保留原意，不做润色
$agent-dx-cli-cn 审查此 CLI，以证据评分并实施已授权的改进
$source-brief-cn 整理这篇论文，区分事实、观点、经验与未证实信息
$word-aha-cn 用交互卡片带我学习点咖啡时常用的英文单词
$claude-md-cn 根据当前仓库事实生成精简的 CLAUDE.md
$arb-cn 以架构评审委员会身份评审这份架构方案
$presentation-making-cn 将这些材料制作成清晰、可记忆的演示文稿
$brand-ui-design-cn 根据六条原则优化这个产品界面
```

## 英文单词学习

本技能把“先背单词→再拼句子”换成**先读熟句→对照猜义→换句验证**，以句子为理解英文单词的起点。
搜索目标词当前用法的 1～5 句有来源日常例句，保留目标词，让熟悉语境同时提供词义线索、搭配和场景。
线索不足就补充、不懂就简化，答后用“啊哈！”提示框串联理解，再通过多选或单个词作答检验新情境，并记录独立表现与所需帮助供复盘。

```bash
npx skills add ontology-of-everything/myoffice-skills --skill word-aha-cn --agent codex --copy -y
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

[Apache-2.0](LICENSE) © myoffice-skills contributors。
