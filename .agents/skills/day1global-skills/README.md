# Day1Global-Skills

[English](#english) | [中文](#中文)

---

<a id="english"></a>

## English

Investment Analysis Skills for AI Agents — covering tech earnings, value investing, market sentiment, macro liquidity, and Bitcoin cycle analysis.

Author: [Ruby](https://x.com/Rubywang), [Star](https://x.com/starzq)

### Skills Overview

| Skill | Description |
|-------|-------------|
| `tech-earnings-deepdive` | Institutional-grade tech stock earnings deep dive with 16 analysis modules, 6 investment philosophy perspectives, and actionable decision framework |
| `us-value-investing` | Buffett-style 4-dimension value investing analysis (ROE, debt safety, FCF quality, economic moat) |
| `us-market-sentiment` | US stock market sentiment monitoring via 5 core indicators (NAAIM, institutional allocation, retail flows, forward P/E, hedge fund leverage) |
| `macro-liquidity` | Global liquidity monitoring and risk early-warning system (Fed net liquidity, SOFR, MOVE index, yen carry trade) |
| `btc-bottom-model` | Bitcoin cycle timing model with 13-indicator weighted scoring system (0-100 Market Heat Score) covering ETF flows, funding rate, on-chain metrics (MVRV, NUPL, SOPR), and cycle indicators — provides both buy and sell recommendations |

### Installation

**Method 1: Skills.sh (auto-discovery)**

```bash
npx skills add https://github.com/star23/Day1Global-Skills --all
```

Skills are installed to `.agents/skills/` and activate automatically when matching topics are detected in conversation.

**Method 2: Claude Code native slash commands**

If you want to invoke skills via `/skill-name` (e.g., `/btc-bottom-model`) inside Claude Code, copy them to `.claude/skills/`:

```bash
# Clone the repo
git clone https://github.com/star23/Day1Global-Skills.git

# Copy all skills to your project's .claude/skills/ directory
mkdir -p your-project/.claude/skills
cp -r Day1Global-Skills/btc-bottom-model your-project/.claude/skills/
cp -r Day1Global-Skills/us-value-investing your-project/.claude/skills/
cp -r Day1Global-Skills/us-market-sentiment your-project/.claude/skills/
cp -r Day1Global-Skills/macro-liquidity your-project/.claude/skills/
cp -r Day1Global-Skills/tech-earnings-deepdive your-project/.claude/skills/
```

Or copy to `~/.claude/skills/` for global access across all projects.

After copying, restart Claude Code — you can then use `/btc-bottom-model`, `/us-value-investing`, etc. as slash commands.

### Usage

No additional configuration needed after installation. Simply ask your AI agent questions in natural language — the relevant skill activates automatically when it detects matching topics.

#### tech-earnings-deepdive

A comprehensive tech stock earnings analysis and multi-perspective investment memo system (v3.0).

**What it does:**

- **Key Forces Identification** — Pinpoint 1-3 decisive forces that determine the company's future value
- **16 Analysis Modules (A-P)** — Revenue quality, profitability, cash flow, forward guidance, competitive landscape, core KPIs, products & new businesses, partner ecosystem, executive team, macro & policy impact, valuation models, ownership distribution, long-term monitoring variables, R&D efficiency, accounting quality, ESG screening
- **6 Investment Philosophy Perspectives** — Quality Compounder (Buffett/Munger), Imaginative Growth (Baillie Gifford/ARK), Fundamental Long-Short (Tiger Cubs), Deep Value (Klarman/Marks), Catalyst-Driven (Tepper/Ackman), Macro Tactical (Druckenmiller)
- **Multi-Method Valuation Matrix** — Owner Earnings, PEG, Reverse DCF, Magic Formula, EV/EBITDA, EV/Revenue + Rule of 40
- **Variant View** — Identify blind spots in market consensus
- **Anti-Bias Framework** — 6 cognitive trap self-checks, 7 financial red flags, 5 tech-specific blind spots, Pre-Mortem analysis
- **Actionable Decisions** — Action Price, position sizing cadence, add/trim/exit triggers, long-term monitoring checklist

**Example prompts:**

```
Analyze NVDA's latest earnings report
```
```
How did META perform this quarter?
```
```
Analyze MSFT from multiple legendary investors' perspectives. Is it a buy right now?
```

**Evidence Standards:**

| Tier | Type | Examples |
|------|------|---------|
| Tier 1 | Primary Sources | CEO quotes, employee reviews, customer feedback, GitHub activity, patents, hiring trends |
| Tier 2 | Factual Sources | SEC filings (10-K/10-Q/8-K), financial data, court documents |
| Tier 3 | Opinion Sources | Sell-side research, news analysis, price target consensus |

---

#### us-value-investing

Systematically evaluates listed companies through 4 core dimensions using Buffett-style value investing methods.

**4 Dimensions:**

1. **ROE Sustainability** — 3+ years of consistent returns on equity
2. **Debt Safety** — Debt-to-asset ratio and leverage assessment
3. **Free Cash Flow Quality** — FCF vs. net income ratio
4. **Economic Moat** — Brand, network effects, cost advantage, switching costs

**Scoring:** Each dimension scores 0-3 points (max 12). Ratings: A (10-12), B (7-9), C (4-6), D (0-3).

**Example prompts:**

```
Is AAPL worth holding long-term from a value investing perspective?
```
```
Help me analyze COST's fundamentals
```

---

#### us-market-sentiment

Monitors US stock market sentiment through 5 core indicators to determine greed/fear levels and provide position recommendations.

**5 Indicators:**

1. **NAAIM Exposure Index** — Active fund manager equity exposure
2. **Institutional Equity Allocation** — Global institutional portfolio allocation
3. **Retail Net Buying** — Daily retail investor fund flows
4. **S&P 500 Forward P/E** — Valuation metric vs. historical range
5. **Hedge Fund Leverage** — Borrowing multiples from prime brokerage data

**Example prompts:**

```
Is the US stock market overheating right now?
```
```
Should I reduce my positions?
```

---

#### macro-liquidity

Tracks the most critical "water level" in the global financial system — liquidity — through 4 core indicators.

**4 Indicators:**

1. **Fed Net Liquidity** — Fed Total Assets - TGA - ON RRP
2. **SOFR Rate** — Overnight funding stress in the banking system
3. **MOVE Index** — Treasury market volatility (bond market VIX)
4. **Yen Carry Trade Signals** — USDJPY and US-Japan yield spread

**Example prompts:**

```
How is liquidity right now?
```
```
Is the Fed injecting or draining liquidity?
```

---

#### btc-bottom-model

Bitcoin cycle timing model with a weighted 0-100 Market Heat Score. Tracks 13 indicators across Daily Pulse (32 pts) and Weekly Structure (68 pts) to provide both buy and sell recommendations across the full market cycle.

**Daily Pulse Indicators (32 pts):**

1. **ETF Daily Net Flow** (12) — Institutional demand via spot BTC ETFs
2. **Funding Rate** (8) — Derivatives market leverage sentiment
3. **Fear & Greed Index** (7) — Composite market sentiment
4. **Long/Short Ratio** (5) — Trader positioning balance

**Weekly Structure Indicators (68 pts):**

1. **LTH-MVRV** (12) — Long-term holder profit/loss ratio
2. **NUPL** (11) — Network-wide unrealized profit/loss
3. **LTH-SOPR** (9) — Long-term holder spending profitability
4. **STH-SOPR** (8) — Short-term holder spending profitability
5. **LTH Supply %** (7) — Accumulation vs. distribution phase
6. **365d MA Ratio** (6) — Price vs. annual moving average
7. **200w MA Multiplier** (6) — Price vs. cycle floor
8. **Weekly RSI** (5) — Medium-term momentum
9. **Volume Change** (4) — Selling exhaustion / blow-off detection

**Rating Scale:** 0-15 Extreme Fear (buy) → 46-55 Neutral → 86-100 Extreme Greed (sell)

**Example prompts:**

```
Has Bitcoin bottomed out? Can I buy the dip?
```
```
Is BTC overheated? Should I take profits?
```
```
What do on-chain indicators say about BTC right now?
```

---

### Skill Synergy

| Combination | Use Case |
|-------------|----------|
| `tech-earnings-deepdive` + `us-value-investing` | Cross-validate earnings analysis with 4-dimension value scoring |
| `tech-earnings-deepdive` + `us-market-sentiment` | Factor macro sentiment into earnings analysis |
| `tech-earnings-deepdive` + `macro-liquidity` | Integrate liquidity conditions when it's a Key Force |

### Disclaimer

All analyses generated by these skills are based on publicly available information and model estimates. They are for research purposes only and do not constitute investment advice. Investing involves risk — please exercise caution in your decisions.

---

<a id="中文"></a>

## 中文

AI Agent 投资分析 Skills 共享仓库 — 覆盖科技股财报、价值投资、市场情绪、宏观流动性和比特币周期分析。

作者：[Ruby](https://x.com/Rubywang)、[Star](https://x.com/starzq)

### Skills 一览

| Skill | 描述 |
|-------|------|
| `tech-earnings-deepdive` | 机构级科技股财报深度分析，覆盖 16 大分析模块、6 大投资哲学视角和可执行决策体系 |
| `us-value-investing` | 巴菲特式四维价值投资分析（ROE、债务安全、自由现金流质量、经济护城河） |
| `us-market-sentiment` | 美股市场情绪监控，追踪 5 大核心指标（NAAIM、机构配置、散户资金流、远期 P/E、对冲基金杠杆） |
| `macro-liquidity` | 全球流动性监控与风险预警系统（美联储净流动性、SOFR、MOVE 指数、日元套息交易） |
| `btc-bottom-model` | 比特币周期择时模型，13 指标加权评分系统（0-100 市场热度评分），覆盖 ETF 资金流、资金费率、链上指标（MVRV、NUPL、SOPR）和周期指标 — 同时提供买入和卖出建议 |

### 安装方法

**方式一：Skills.sh（自动发现）**

```bash
npx skills add https://github.com/star23/Day1Global-Skills --all
```

Skills 安装到 `.agents/skills/`，对话中识别到相关话题时自动激活。

**方式二：Claude Code 原生斜杠命令**

如果你想在 Claude Code 中通过 `/skill-name`（如 `/btc-bottom-model`）直接调用，需要将 skills 复制到 `.claude/skills/` 目录：

```bash
# 克隆仓库
git clone https://github.com/star23/Day1Global-Skills.git

# 复制所有 skills 到你项目的 .claude/skills/ 目录
mkdir -p your-project/.claude/skills
cp -r Day1Global-Skills/btc-bottom-model your-project/.claude/skills/
cp -r Day1Global-Skills/us-value-investing your-project/.claude/skills/
cp -r Day1Global-Skills/us-market-sentiment your-project/.claude/skills/
cp -r Day1Global-Skills/macro-liquidity your-project/.claude/skills/
cp -r Day1Global-Skills/tech-earnings-deepdive your-project/.claude/skills/
```

也可以复制到 `~/.claude/skills/` 实现全局可用（所有项目都能调用）。

复制完成后重启 Claude Code，即可使用 `/btc-bottom-model`、`/us-value-investing` 等斜杠命令。

### 使用方法

安装后无需额外配置。直接用自然语言向 AI Agent 提问即可，Skill 会在识别到相关话题时自动激活。

#### tech-earnings-deepdive：科技股财报深度分析

一个为 AI Agent 打造的科技股财报深度分析与多视角投资备忘录系统（v3.0）。

**核心能力：**

- **Key Forces 识别** — 锚定 1-3 个决定公司未来价值的决定性力量
- **16 大分析模块（A-P）** — 收入质量、盈利能力、现金流、前瞻指引、竞争格局、核心 KPI、产品与新业务、合作伙伴生态、高管团队、宏观政策、估值模型、筹码分布、长期监控变量、研发效率、会计质量、ESG 筛查
- **6 大投资哲学视角** — 质量复利（巴菲特/芒格）、想象力成长（Baillie Gifford/ARK）、基本面多空（Tiger Cubs）、深度价值（Klarman/Marks）、催化剂驱动（Tepper/Ackman）、宏观战术（Druckenmiller）
- **多方法估值矩阵** — Owner Earnings、PEG、反向 DCF、魔法公式、EV/EBITDA、EV/Revenue + Rule of 40
- **Variant View（变异视角）** — 找出市场共识的盲点
- **反偏见框架** — 6 大认知陷阱自检、7 大财务红旗、5 大科技股盲区、Pre-Mortem 事前尸检
- **可执行决策** — Action Price、建仓节奏、加仓/减仓/清仓触发条件、长期监控清单

**示例提问：**

```
帮我深度分析一下 NVDA 最新一季的财报
```
```
META 这季度表现如何？
```
```
从多个投资大师的视角帮我看看 MSFT，现在值得买入吗？
```

**证据标准：**

| 层级 | 类型 | 举例 |
|------|------|------|
| 第一层 | 一手来源 | CEO 原话、员工评价、客户评价、GitHub 活跃度、专利、招聘动向 |
| 第二层 | 事实来源 | SEC 文件（10-K/10-Q/8-K）、财报数据、法庭文件 |
| 第三层 | 观点来源 | 卖方研报、新闻分析、价格目标汇总 |

---

#### us-value-investing：美股价值投资分析

基于巴菲特方法论，通过 4 个核心维度系统评估上市公司。

**四大维度：**

1. **ROE 持续性** — 3 年以上稳定的净资产收益率
2. **债务安全性** — 资产负债率和杠杆评估
3. **自由现金流质量** — FCF 与净利润的比值
4. **经济护城河** — 品牌、网络效应、成本优势、转换成本

**评分：** 每个维度 0-3 分（满分 12 分）。评级：A（10-12）、B（7-9）、C（4-6）、D（0-3）。

**示例提问：**

```
从价值投资角度看，AAPL 值得长期持有吗？
```
```
帮我分析一下 COST 的基本面
```

---

#### us-market-sentiment：美股市场情绪监控

通过 5 大核心指标监控美股市场情绪，判断贪婪/恐惧程度并提供仓位建议。

**5 大指标：**

1. **NAAIM 敞口指数** — 主动基金经理权益敞口
2. **机构权益配置比例** — 全球机构投资者组合配置
3. **散户净买入** — 每日散户资金流向
4. **标普 500 远期 P/E** — 估值水平与历史区间对比
5. **对冲基金杠杆** — 主经纪商披露的借贷倍数

**示例提问：**

```
美股现在是不是过热了？
```
```
我该不该减仓？
```

---

#### macro-liquidity：宏观流动性监控

追踪全球金融体系中最关键的"水位"——流动性，通过 4 大核心指标。

**4 大指标：**

1. **美联储净流动性** — 美联储总资产 - TGA - ON RRP
2. **SOFR 利率** — 银行体系隔夜资金压力
3. **MOVE 指数** — 国债市场波动率（债市 VIX）
4. **日元套息交易信号** — USDJPY 汇率与美日利差

**示例提问：**

```
现在流动性怎么样？
```
```
美联储是在放水还是收水？
```

---

#### btc-bottom-model：比特币周期择时模型

基于 13 大指标加权评分（0-100 市场热度评分），覆盖完整市场周期，同时提供买入和卖出建议。

**日线脉搏指标（32 分）：**

1. **ETF 每日净流入**（12 分）— 机构通过现货 ETF 的需求信号
2. **资金费率**（8 分）— 衍生品市场杠杆情绪
3. **恐惧与贪婪指数**（7 分）— 综合市场情绪
4. **多空比**（5 分）— 交易者持仓方向

**周线结构指标（68 分）：**

1. **LTH-MVRV**（12 分）— 长期持有者盈亏比
2. **NUPL**（11 分）— 全网未实现盈亏
3. **LTH-SOPR**（9 分）— 长期持有者消费盈利率
4. **STH-SOPR**（8 分）— 短期持有者消费盈利率
5. **LTH 供应占比**（7 分）— 积累 vs 分配阶段
6. **365 日均线比率**（6 分）— 价格 vs 年均线
7. **200 周均线倍数**（6 分）— 价格 vs 周期底线
8. **周线 RSI**（5 分）— 中期动量
9. **成交量变化**（4 分）— 卖压衰竭 / 放量见顶检测

**评级范围：** 0-15 极度恐慌（买入）→ 46-55 中性 → 86-100 极度贪婪（卖出）

**示例提问：**

```
比特币见底了吗？可以抄底吗？
```
```
BTC 是不是过热了？该止盈吗？
```
```
链上数据怎么看当前的 BTC？
```

---

### Skill 协同

| 组合 | 使用场景 |
|------|----------|
| `tech-earnings-deepdive` + `us-value-investing` | 财报分析完成后，运行四维价值评分做交叉验证 |
| `tech-earnings-deepdive` + `us-market-sentiment` | 模块 J 涉及宏观情绪时联动 |
| `tech-earnings-deepdive` + `macro-liquidity` | 流动性环境是 Key Force 时联动 |

### 免责声明

此仓库中所有 Skill 生成的分析均基于公开信息和模型推算，仅供研究参考，不构成投资建议。投资有风险，决策需谨慎。
