# 学习科学的证据基础

本文件是 `SKILL.md` 里每条规则的依据。用户质疑“为什么要这样教”时，引用这里。

**诚实声明**：以下是定向检索的结果，不是系统性综述。核心结论（提取练习、间隔重复）是元分析级别、高度可复制；部分结论来自单篇研究，方向可信但强度较低，已逐条标注。

---

## 一、最高效的两个方法（元分析级别，未被动摇）

### 1. 提取练习 / 自测（practice testing）

- **Rowland 2014**, *Psychological Bulletin*（1100+ 引用）——《The effect of testing versus restudy on retention》元分析：测试显著优于重读；**初始为回忆式测试（recall）比再认式测试（recognition）收益更大**。
- **Adesope et al. 2017**, *Review of Educational Research*（550+ 引用）——实践测试优于重读及所有其他对照条件。
- 机制：提取本身是学习事件（"effortful processing"），不只是测量。

**→ SKILL.md 规则**：每步都要求用户先输出；会话必须以自测结束。

### 2. 间隔练习（distributed practice）

- **Cepeda et al. 2006**（元分析）；**2020**, *Educational Psychology Review*（《A Meta-Analytic Review of the Benefit of Spacing out Retrieval Practice Episodes on Retention》）——重复确认间隔优于集中。
- 最优间隔随**目标保留时长**变化：保留越久，间隔越长（大致为保留期的 10–20%）。

**→ SKILL.md 规则**：卡片间隔阶梯 + 上限 180 天。

### Dunlosky 2013 的效用分级（最常被引用的总表）

**Dunlosky et al. 2013**, *Psychological Science in the Public Interest*，3100+ 引用，评了 10 种方法：

| 分级 | 方法 |
|---|---|
| **高效** | ① 实践测试（practice testing）② 间隔练习（distributed practice） |
| 中等 | ③ 精细提问（elaborative interrogation）④ 自我解释（self-explanation）⑤ 交错练习（interleaved practice） |
| **低效** | 总结、划线/高亮、关键词记忆法、文本想象、**重读** |

关键点：**重读和划线是学生最常用的，恰好是最没用的**——它们制造“感觉在学”的错觉。

**→ SKILL.md 规则**：“明确禁止的学习方式”一节。

---

## 二、教师侧：Rosenshine 的 10 条原则

**Rosenshine 2012**, *American Educator*，《Principles of Instruction》。三个独立来源交叉验证（认知科学 + 名师课堂观察 + 认知支架研究），是当前最权威的教学框架：

1. 复习旧知开场（每日复习）
2. **小步呈现新内容，每步后立即练习**
3. **大量提问，检查所有学生**
4. 提供示范范例（worked examples）
5. 引导练习（guided practice）
6. **检查理解**（不是问“有问题吗”）
7. **保持高成功率**（观察值约 80–82%）
8. 为难点提供脚手架，并逐步撤除
9. 要求并监督独立练习（练到自动化）
10. 周 / 月复习

**关键实证细节**：
- 有效教师 82% 学生回答正确；低效教师仅 73%。
- 低效教师常问“还有问题吗？”，没人举手就以为学会了——研究明确认定这招无效。
- 有效教师花在**引导练习**上的时间远多于低效教师；低效教师讲得短、直接发卷子，结果学生错一堆还得重讲。

**→ SKILL.md 规则**：铁律 2/3、第 4/6/7 步、85% 判定。

---

## 三、认知负荷理论（CLT）

**Sweller et al. 2019**, *Educational Psychology Review*，《Cognitive Architecture and Instructional Design: 20 Years Later》（2200+ 引用）：

- 工作记忆容量与时长有限，长时记忆无限。
- 三类负荷：内在（任务本身）、外在（呈现方式，应降低）、相关（用于构建图式，应促进）。
- **worked example effect**：给完整范例比让新手自己摸索更有效（对新手）。

**2024 年重要整合**——*QJEP*，《Does difficulty moderate learning? A comparative analysis of the desirable difficulties framework and cognitive load theory》：

“合意困难”（越难越好）与 CLT（越省越好）长期冲突，该综述提出统一模型：

> **按「元素交互性」和「专业水平」调节难度**：
> - 低元素交互性任务（简单、孤立）→ **加大难度**有益（增强专注与保持）
> - 高元素交互性任务（复杂、多因素）→ **降低难度**防止认知过载

**→ SKILL.md 规则**：第 4 步的“复杂→降负荷 / 简单→加难度”。

---

## 四、85% 最优正确率

**Wilson et al. 2019**, *Nature Communications*，《The Eighty Five Percent Rule for optimal learning》：

- 对一大类基于随机梯度下降的学习算法（含人工神经网络与生物神经网络模型），**训练最优错误率约 15.87%，即正确率约 85%**。
- 这为 Rosenshine 的经验值 80% 提供了理论依据，并给出了更精确的数字。

**→ SKILL.md 规则**：第 8 步判定表。

---

## 五、掌握学习与“2 sigma”

**Bloom 1984**, *Educational Researcher*：一对一辅导 + 掌握学习的学生，平均成绩比普通课堂高约 **2 个标准差**；约 90% 的受辅导学生达到普通课堂前 10% 的水平。

核心机制是**闸门**：未掌握不前进。这解释了为什么本 skill 的第 8 步是硬闸门。

AI 导师的效应量（0.73–1.3 SD，见第七节）已接近这一区间。

---

## 六、反馈

**Hattie & Timperley 2007**, *Review of Educational Research*（《The Power of Feedback》，被引数万）：

- 反馈是影响学习最强的因素之一，但**可以正向也可以负向**。
- 有效的反馈回答三个问题：
  1. **Where am I going?**（目标）
  2. **How am I going?**（现状）
  3. **Where to next?**（下一步）
- 针对**任务/过程**的反馈有效；针对**人**（“你真聪明”）的表扬无效甚至有害。
- 分数/等级单独呈现时效果差，需配合具体说明。

**→ SKILL.md 规则**：第 7 步的反馈三问格式；禁止表扬式反馈。

---

## 七、AI 导师：2023–2025 的新证据（老框架里没有）

### 1. 无护栏的 AI 会损害学习（最重要的发现）

**Bastani et al. 2025**, *PNAS*，《Generative AI without guardrails can harm learning: Evidence from high school mathematics》（被引 200+）：

- 近千名高中生，随机分配到两种 AI 导师：
  - **GPT Base**：标准 ChatGPT 界面
  - **GPT Tutor**：prompt 中内置学习保护（苏格拉底式引导，不直接给答案）
- 使用期间：GPT Base 成绩 +48%，GPT Tutor +127%
- **撤走 AI 后：GPT Base 组比从未用过 AI 的对照组低 17%**
- GPT Tutor 组**没有**这一负面效应

原文结论：无护栏时，学生把 AI 当“拐杖”（crutch）用，之后独立作答更差。

**→ SKILL.md 规则**：铁律 1（绝不先给答案）、铁律 6（先问“你怎么想的”）。这不是教学偏好，是有实证的护栏。

### 2. 正确设计的 AI 导师可超越课堂主动学习

**Kestin et al. 2025**, *Scientific Reports*（DOI 10.1038/s41598-025-97652-6），RCT：

- AI 导师（用与课堂相同的教学法最佳实践设计）vs. 课堂主动学习
- 学生**用更少时间学到两倍以上**，投入度和动机更高
- 效应量：线性回归 0.63（因天花板效应低估），**分位回归 0.73–1.3 SD**
- 已接近 Bloom 的 2 sigma

### 3. AI 增强人类导师，比替代更稳

**Wang et al. 2024**, Tutor CoPilot（900 导师 / 1800 名 K-12 学生 RCT）：

- 导师随机获得 AI 实时教学建议，学生掌握率 **+4 个百分点**
- **原本评分较低的导师组 +9 个百分点**——补的是弱项
- 成本约每导师每年 $20
- 分析 55 万条消息发现：有 AI 的导师更多使用专家式教学策略

**→ 对 skill 设计的含义**：AI 的价值在于**约束和引导学习者的努力**，而不是替他把答案说出来。

---

## 八、被推翻 / 大幅降级的流行说法

### 1. 学习风格（视觉型 / 听觉型）——证伪

**2023**, *Medical Science Educator*；**2026**, *Journal of Educational Psychology*（《Debunking the learning styles neuromyth》）等持续确认：没有证据支持按学习风格匹配教学能提升效果。**不要按学习风格设计教学。**

### 2. 成长型思维（growth mindset）——效应远小于宣传

- **Sisk et al. 2018**, *Psychological Science*，两篇元分析（k=273, **N=365,915**；k=43, N=57,155）：**整体效应很弱**，仅低社经地位或学业风险学生可能受益。
- **Yeager et al. 2019**, *Nature*（1500+ 引用）：短干预提升了低成就学生成绩并增加高阶数学选课，但**效果依赖学校同伴规范**是否与干预信息一致。

《Mindset》畅销书的印象与实证差距很大。可以鼓励努力，但不要把它当学习策略。

### 3. 重读 / 划线——一直低效（见第一节）

---

## 九、预考效应

**Pan & Sana 2021**, *JEP: Applied*，《Pretesting versus posttesting》，5 个实验 n=1573：

- 学习前先测（errorful generation，即使全错）**优于**学习后测
- 优势在多种测试格式、有无反馈、不同保留间隔下均成立
- 机制：预考增强了后续对文本内容的加工

**→ SKILL.md 规则**：第 2 步预考，不可跳过。

---

## 十、交错练习的边界条件

**Brunmair & Richter 2019**, *Psychological Bulletin*，《Similarity matters: A meta-analysis of interleaved learning and its moderators》：

- 交错**对归纳学习有效**（分类学习、数学题型识别）
- 效果在以下条件最强：**类别间相似、类别内不相似、材料更复杂**
- **对说明文（expository texts）和单词表效果不佳，应谨慎使用**

**→ SKILL.md 规则**：交错规则 + 单词表/说明文例外。

---

## 文献速查

| 结论 | 文献 |
|---|---|
| 10 种学习法效用分级 | Dunlosky et al. 2013, *Psych. Science in the Public Interest* |
| 教学 10 原则 | Rosenshine 2012, *American Educator* |
| 认知负荷理论 20 年 | Sweller et al. 2019, *Educational Psychology Review* |
| 难度按元素交互性调节 | 2024, *QJEP*, 10.1177/17470218241308143 |
| 85% 最优正确率 | Wilson et al. 2019, *Nature Communications* |
| 2 sigma | Bloom 1984, *Educational Researcher* |
| 反馈三问 | Hattie & Timperley 2007, *Review of Educational Research* |
| 测试效应元分析 | Rowland 2014, *Psychological Bulletin*；Adesope et al. 2017, *RER* |
| 间隔效应元分析 | Cepeda et al. 2006；2020, *Educational Psychology Review* |
| 预考 > 后测 | Pan & Sana 2021, *JEP: Applied* |
| 交错练习边界 | Brunmair & Richter 2019, *Psychological Bulletin* |
| AI 无护栏有害 | Bastani et al. 2025, *PNAS*, 10.1073/pnas.2422633122 |
| AI 导师超越课堂 | Kestin et al. 2025, *Scientific Reports*, 10.1038/s41598-025-97652-6 |
| AI 增强人类导师 | Wang et al. 2024, Tutor CoPilot |
| 成长型思维效应弱 | Sisk et al. 2018, *Psychological Science*；Yeager et al. 2019, *Nature* |
| 学习风格证伪 | 2026, *Journal of Educational Psychology*, 10.1037/edu0001056 |
