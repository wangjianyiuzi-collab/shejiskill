# shejiskill

面向中文直播电商与小红书3:4视觉的 Agent Skill。它将海报制作拆成“信息母版选择”和“审美方向推导”两个独立步骤，支持分析、改版、生成、参考图蒸馏和移动端质检。

## 核心能力

- 七类直播海报信息结构：主活动、周排期、时间胶囊、单品故事、多商品清单、主题长图、福利互动。
- 五种工作模式：只分析、改版、生成、设计蒸馏、仅输出提示词。
- 参考图角色隔离：内容、风格、人物、商品和版式来源不会隐式混用。
- 审美系统：品牌极简、生活编辑、大字视觉、节庆促销、清洁排品、文化材质。
- 反AI套路：限制无意义渐变、玻璃卡片、装饰贴纸、随机英文和多重标题特效。
- 无字底图与确定性排字分离，减少中文、Logo、日期和价格乱码。
- 100分交付量表、关键失败条件和14个维护评测案例。

## 安装

```bash
npx skills add wangjianyiuzi-collab/shejiskill
```

安装后可以这样使用：

```text
使用 optimize-live-poster-layouts 分析这张直播海报。
只诊断问题，不修改图片。
```

```text
使用 optimize-live-poster-layouts，把这张图改成小红书3:4。
图一只提供内容，图二只提供风格，人物和商品不能替换。
```

## Skill结构

```text
skills/optimize-live-poster-layouts/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── design-system.json
│   ├── template-library.json
│   ├── aesthetic-system.md
│   ├── prompt-templates.md
│   ├── quality-rubric.md
│   ├── dataset-manifest.json
│   └── evaluation-cases.json
└── scripts/
    └── validate_skill_data.py
```

## 数据边界

当前公开运行时只保留9篇来源文章、171张图片、117张有效海报的聚合统计，不包含原文章标题、来源链接、图片链接、完整OCR、品牌名或商品名。该样本适合形成信息架构假设，不代表所有平台、品牌和品类的通用审美结论。

## 验证

```bash
python3 skills/optimize-live-poster-layouts/scripts/validate_skill_data.py
```
