# 分类人工复核清单

迁移预演中**确信度较低**的卡片，共 718 张。

判断依据：规则会优先在「旧标签划定的候选范围」内选条目；
下列卡片在该范围内**没有关键词证据**，因此由关键词单独定夺或回落人工首选——最可能误判。

> ⚠️ 另有 0 张卡由人工旧标签直接认定——算法并没有真正"验证"过它们。
> 旧标签已被证明是**粗而非错**的先验，它不会自我纠错，所以这批卡不能算「无需复核」，
> 改由 `docs/classification-audit.md` 的**盲审抽样**抽查：隐藏旧标签与算法答案后独立判定。

| 卡片 | 类型 | 旧标签 | 建议条目 | 判断依据 | 关键词命中的其他条目 |
|---|---|---|---|---|---|
| sk-0001 | quote | learning-difficulties | A6 了解儿童 | 全无关键词证据，按旧标签先验定夺 | 学习困难学生（11.6） |
| sk-0002 | method | learning-difficulties | A16 评价与分数 | 文本证据推翻旧标签（关键词 4.80，压过旧标签项 4.14） | 学习困难学生（15.1） · 家庭与母亲（4.1） |
| sk-0003 | principle | learning-difficulties | A20 检查知识与考查 | 文本证据推翻旧标签（关键词 5.10，压过旧标签项 2.50） | 学习困难学生（6.2） · 教师（2.4） |
| sk-0005 | principle | learning-difficulties | A7 健康与作息 | 旧标签先验 + 文本证据（关键词 10.07 + 先验 1.0 = 11.07） | 学习困难学生（4.9） · 家庭与母亲（4.1） |
| sk-0007 | quote | learning-difficulties | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 7.83 + 先验 1.0 = 8.83） | （除建议条目外无其他关键词命中） |
| sk-0008 | practice | learning-difficulties | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 3.69 + 先验 1.0 = 4.69） | （除建议条目外无其他关键词命中） |
| sk-0009 | quote | family-school | A8 家庭与母亲 | 旧标签先验 + 文本证据（关键词 3.50 + 先验 2.5 = 6.00） | 尊严、爱与信任（4.2） · 了解儿童（3.4） |
| sk-0010 | principle | family-school | A8 家庭与母亲 | 旧标签先验 + 文本证据（关键词 7.64 + 先验 2.5 = 10.14） | 幸福与精神生活（3.4） · 道德判断与品德培养（3.0） |
| sk-0011 | practice | family-school | A13 阅读与书籍 | 文本证据推翻旧标签（关键词 7.10，压过旧标签项 6.67） | 思维与智力（6.7） · 检查知识与考查（5.6） |
| sk-0012 | principle | family-school, learning-difficulties | A7 健康与作息 | 旧标签先验 + 文本证据（关键词 14.36 + 先验 1.0 = 15.36） | 学习困难学生（10.5） · 评价与分数（4.2） |
| sk-0013 | quote | family-school | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 4.98 + 先验 1.0 = 5.98） | 教师（2.4） |
| sk-0014 | principle | labor-education | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 2.33 + 先验 2.5 = 4.83） | （除建议条目外无其他关键词命中） |
| sk-0016 | practice | labor-education | A3 幸福与精神生活 | 文本证据推翻旧标签（关键词 7.96，压过旧标签项 7.81） | 劳动与创造（5.3） · 思维与智力（4.1） |
| sk-0017 | quote | labor-education | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 5.31 + 先验 2.5 = 7.81） | 幸福与精神生活（7.1） · 道德判断与品德培养（3.0） |
| sk-0018 | method | labor-education, learning-difficulties | A13 阅读与书籍 | 文本证据推翻旧标签（关键词 7.10，压过旧标签项 4.83） | 家庭与母亲（4.1） · 思维与智力（3.4） |
| sk-0019 | quote | health-first | A7 健康与作息 | 旧标签先验 + 文本证据（关键词 8.94 + 先验 2.5 = 11.44） | 检查知识与考查（5.1） · 全面发展与个性（5.1） |
| sk-0020 | practice | health-first, family-school | A7 健康与作息 | 旧标签先验 + 文本证据（关键词 14.78 + 先验 2.5 = 17.28） | 阅读与书籍（11.1） · 家庭与母亲（4.1） |
| sk-0021 | method | health-first | A7 健康与作息 | 旧标签先验 + 文本证据（关键词 14.78 + 先验 2.5 = 17.28） | 自然与思维课（4.2） · 家庭与母亲（4.1） |
| sk-0023 | method | health-first, learning-difficulties | A7 健康与作息 | 旧标签先验 + 文本证据（关键词 10.63 + 先验 2.5 = 13.13） | 学习困难学生（4.9） |
| sk-0024 | quote | aesthetic-nature-education | A13 阅读与书籍 | 文本证据推翻旧标签（关键词 7.44，压过旧标签项 6.71） | 美与艺术（4.2） · 道德判断与品德培养（3.0） |
| sk-0025 | principle | aesthetic-nature-education | A11 劳动与创造 | 文本证据推翻旧标签（关键词 2.98，压过旧标签项 2.50） | 教师（2.4） |
| sk-0026 | practice | aesthetic-nature-education | A14 美与艺术 | 旧标签先验 + 文本证据（关键词 6.85 + 先验 2.5 = 9.35） | 健康与作息（5.3） · 幸福与精神生活（3.8） |
| sk-0027 | quote | aesthetic-nature-education | A14 美与艺术 | 旧标签先验 + 文本证据（关键词 11.06 + 先验 2.5 = 13.56） | 思维与智力（12.4） · 全面发展与个性（5.1） |
| sk-0028 | principle | aesthetic-nature-education | A14 美与艺术 | 旧标签先验 + 文本证据（关键词 4.74 + 先验 2.5 = 7.24） | 尊严、爱与信任（4.2） · 了解儿童（3.4） |
| sk-0029 | quote | collective-education | A9 集体与同伴 | 旧标签先验 + 文本证据（关键词 3.16 + 先验 2.5 = 5.66） | 评价与分数（4.8） · 全面发展与个性（4.4） |
| sk-0030 | quote | collective-education | A9 集体与同伴 | 旧标签先验 + 文本证据（关键词 3.16 + 先验 2.5 = 5.66） | 尊严、爱与信任（4.8） |
| sk-0031 | practice | collective-education | A9 集体与同伴 | 旧标签先验 + 文本证据（关键词 3.16 + 先验 2.5 = 5.66） | 尊严、爱与信任（5.0） · 幸福与精神生活（4.0） · 家庭与母亲（3.5） |
| sk-0032 | method | collective-education, learning-difficulties | A9 集体与同伴 | 旧标签先验 + 文本证据（关键词 5.46 + 先验 2.5 = 7.96） | 了解儿童（3.8） · 教师（2.4） |
| sk-0033 | principle | collective-education | A9 集体与同伴 | 旧标签先验 + 文本证据（关键词 3.16 + 先验 2.5 = 5.66） | 尊严、爱与信任（4.8） · 劳动与创造（3.0） |
| sk-0034 | quote | teacher-growth | A10 教师 | 旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88） | 自我教育（3.8） |
| sk-0035 | principle | teacher-growth | A10 教师 | 旧标签先验 + 文本证据（关键词 9.23 + 先验 2.5 = 11.73） | 劳动与创造（3.0） · 阅读与书籍（2.9） |
| sk-0036 | quote | teacher-growth | A10 教师 | 旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88） | 尊严、爱与信任（4.6） |
| sk-0037 | principle | teacher-growth | A9 集体与同伴 | 文本证据推翻旧标签（关键词 8.62，压过旧标签项 8.10） | 阅读与书籍（7.1） · 幸福与精神生活（7.0） |
| sk-0038 | principle | teacher-growth | A10 教师 | 旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88） | 评价与分数（4.8） · 自我教育（3.8） |
| sk-0039 | quote | love-education | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 4.90 + 先验 2.5 = 7.40） | （除建议条目外无其他关键词命中） |
| sk-0040 | principle | love-education | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 7.39 + 先验 1.0 = 8.39） | （除建议条目外无其他关键词命中） |
| sk-0041 | quote | love-education, teacher-growth | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 15.08 + 先验 2.5 = 17.58） | 家庭与母亲（3.5） |
| sk-0042 | method | love-education, teacher-growth | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 4.90 + 先验 2.5 = 7.40） | 思维与智力（4.2） · 教师（2.4） |
| sk-0043 | quote | love-education | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 9.20 + 先验 2.5 = 11.70） | 教师（2.4） |
| sk-0044 | principle | assessment-grading | A16 评价与分数 | 旧标签先验 + 文本证据（关键词 14.42 + 先验 2.5 = 16.92） | 学习困难学生（5.6） · 习惯与纪律（4.9） |
| sk-0045 | principle | assessment-grading | A16 评价与分数 | 旧标签先验 + 文本证据（关键词 13.70 + 先验 2.5 = 16.20） | 学习困难学生（5.6） · 尊严、爱与信任（4.6） |
| sk-0046 | quote | assessment-grading, family-school | A16 评价与分数 | 旧标签先验 + 文本证据（关键词 4.74 + 先验 2.5 = 7.24） | 尊严、爱与信任（4.6） · 家庭与母亲（4.1） |
| sk-0047 | principle | assessment-grading | A16 评价与分数 | 旧标签先验 + 文本证据（关键词 4.16 + 先验 2.5 = 6.66） | 道德判断与品德培养（6.4） · 尊严、爱与信任（4.6） |
| sk-0048 | method | assessment-grading, learning-difficulties | A16 评价与分数 | 旧标签先验 + 文本证据（关键词 4.77 + 先验 2.5 = 7.27） | 尊严、爱与信任（4.8） |
| sk-0049 | quote | child-study | A6 了解儿童 | 旧标签先验 + 文本证据（关键词 7.14 + 先验 2.5 = 9.64） | 家庭与母亲（3.5） · 教师（2.4） |
| sk-0050 | practice | child-study, family-school | A8 家庭与母亲 | 旧标签先验 + 文本证据（关键词 15.18 + 先验 2.5 = 17.68） | 幸福与精神生活（7.4） · 尊严、爱与信任（4.3） |
| sk-0051 | quote | child-study, learning-difficulties | A1 全面发展与个性 | 文本证据推翻旧标签（关键词 5.06，压过旧标签项 4.69） | 学习困难学生（12.0） · 思维与智力（3.7） |
| sk-0052 | principle | child-study | A6 了解儿童 | 旧标签先验 + 文本证据（关键词 3.80 + 先验 2.5 = 6.30） | 幸福与精神生活（3.3） · 教师（2.4） |
| sk-0053 | principle | child-study | A6 了解儿童 | 旧标签先验 + 文本证据（关键词 9.99 + 先验 2.5 = 12.49） | 思维与智力（5.7） |
| sk-0054 | quote | reading-and-books | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 9.80 + 先验 2.5 = 12.30） | 美与艺术（5.9） · 幸福与精神生活（3.3） |
| sk-0055 | method | reading-and-books | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 21.47 + 先验 2.5 = 23.97） | 幸福与精神生活（7.7） · 美与艺术（4.2） |
| sk-0056 | practice | reading-and-books | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 6.83 + 先验 2.5 = 9.33） | 集体与同伴（5.2） · 幸福与精神生活（4.0） |
| sk-0057 | quote | reading-and-books | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 11.06 + 先验 2.5 = 13.56） | 自我教育（4.3） · 幸福与精神生活（3.8） |
| sk-0058 | quote | reading-and-books | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 8.71 + 先验 2.5 = 11.21） | 思维与智力（3.3） |
| sk-0059 | quote | thinking-and-nature | A12 自然与思维课 | 旧标签先验 + 文本证据（关键词 15.89 + 先验 1.0 = 16.89） | 思维与智力（7.0） · 了解儿童（3.4） |
| sk-0060 | principle | thinking-and-nature, learning-difficulties | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 7.46 + 先验 2.5 = 9.96） | 了解儿童（7.2） |
| sk-0061 | principle | thinking-and-nature | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 6.67 + 先验 2.5 = 9.17） | 自我教育（4.4） · 自然与思维课（4.1） |
| sk-0062 | practice | thinking-and-nature | A12 自然与思维课 | 旧标签先验 + 文本证据（关键词 9.60 + 先验 1.0 = 10.60） | 思维与智力（7.0） · 了解儿童（3.4） |
| sk-0063 | quote | thinking-and-nature | A12 自然与思维课 | 旧标签先验 + 文本证据（关键词 4.14 + 先验 1.0 = 5.14） | （除建议条目外无其他关键词命中） |
| sk-0064 | quote | teacher-growth, reading-and-books | A10 教师 | 旧标签先验 + 文本证据（关键词 8.42 + 先验 2.5 = 10.92） | 阅读与书籍（7.1） · 思维与智力（4.2） |
| sk-0065 | principle | assessment-grading, child-study | A16 评价与分数 | 旧标签先验 + 文本证据（关键词 10.20 + 先验 2.5 = 12.70） | 阅读与书籍（6.8） · 学习困难学生（5.6） |
| sk-0066 | quote | labor-education, learning-difficulties | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 10.14 + 先验 2.5 = 12.64） | 思维与智力（11.1） · 学习困难学生（5.7） |
| sk-0067 | method | thinking-and-nature, child-study, aesthetic-nature-education | A12 自然与思维课 | 旧标签先验 + 文本证据（关键词 11.13 + 先验 1.0 = 12.13） | 思维与智力（7.0） · 健康与作息（5.3） |
| sk-0069 | principle | health-first, family-school | A7 健康与作息 | 旧标签先验 + 文本证据（关键词 19.06 + 先验 2.5 = 21.56） | 幸福与精神生活（7.1） · 检查知识与考查（5.1） |
| sk-0070 | quote | love-education, teacher-growth | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 9.53 + 先验 2.5 = 12.03） | 幸福与精神生活（10.8） · 公民与祖国（8.0） |
| sk-0071 | method | family-school, child-study | A10 教师 | 文本证据推翻旧标签（关键词 7.21，压过旧标签项 6.64） | 全面发展与个性（4.4） · 家庭与母亲（4.1） |
| sk-0072 | principle | reading-and-books | A4 自我教育 | 旧标签先验 + 文本证据（关键词 10.18 + 先验 1.0 = 11.18） | 阅读与书籍（6.8） · 思维与智力（3.3） |
| sk-0073 | quote | aesthetic-nature-education, thinking-and-nature | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 4.05 + 先验 2.5 = 6.55） | 自然与思维课（4.1） · 了解儿童（3.4） |
| sk-0075 | method | assessment-grading, child-study, learning-difficulties | A16 评价与分数 | 旧标签先验 + 文本证据（关键词 10.20 + 先验 2.5 = 12.70） | 学习困难学生（6.4） · 自我教育（5.9） |
| sk-0077 | quote | reading-and-books, learning-difficulties | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 6.83 + 先验 2.5 = 9.33） | 健康与作息（6.4） · 学习困难学生（4.9） |
| sk-0078 | method | teacher-growth, child-study | A10 教师 | 旧标签先验 + 文本证据（关键词 8.42 + 先验 2.5 = 10.92） | 思维与智力（7.0） · 检查知识与考查（5.6） |
| sk-0079 | principle | labor-education, child-study | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 13.40 + 先验 2.5 = 15.90） | 评价与分数（4.8） · 思维与智力（3.3） |
| sk-0080 | quote | teacher-growth, child-study | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 8.85 + 先验 1.0 = 9.85） | 教师（7.2） · 幸福与精神生活（3.0） |
| sk-0082 | quote | thinking-and-nature, aesthetic-nature-education | A11 劳动与创造 | 文本证据推翻旧标签（关键词 8.38，压过旧标签项 6.19） | 自然与思维课（4.1） · 思维与智力（3.7） |
| sk-0083 | principle | learning-difficulties, health-first | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 5.31 + 先验 1.0 = 6.31） | 思维与智力（4.1） · 阅读与书籍（2.9） |
| sk-0084 | quote | teacher-growth, child-study | A4 自我教育 | 旧标签先验 + 文本证据（关键词 9.75 + 先验 1.0 = 10.75） | 幸福与精神生活（7.3） · 道德判断与品德培养（3.0） |
| sk-0085 | quote | labor-education | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 2.33 + 先验 2.5 = 4.83） | 自我教育（4.4） · 思维与智力（4.2） · 幸福与精神生活（3.3） |
| sk-0086 | principle | labor-education, collective-education | A9 集体与同伴 | 旧标签先验 + 文本证据（关键词 3.16 + 先验 2.5 = 5.66） | 自我教育（4.4） · 幸福与精神生活（4.0） |
| sk-0088 | quote | love-education, collective-education | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 9.13 + 先验 2.5 = 11.63） | 评价与分数（11.3） · 道德判断与品德培养（5.4） |
| sk-0089 | practice | family-school | A4 自我教育 | 文本证据推翻旧标签（关键词 10.95，压过旧标签项 9.44） | 道德判断与品德培养（9.4） · 尊严、爱与信任（4.3） |
| sk-0091 | practice | reading-and-books, collective-education | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 12.67 + 先验 2.5 = 15.17） | 家庭与母亲（3.5） |
| sk-0092 | method | aesthetic-nature-education, family-school | A14 美与艺术 | 旧标签先验 + 文本证据（关键词 9.19 + 先验 2.5 = 11.69） | 劳动与创造（10.0） · 自然与思维课（4.2） |
| sk-0093 | quote | teacher-growth, reading-and-books | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 11.06 + 先验 2.5 = 13.56） | 幸福与精神生活（3.7） · 思维与智力（3.4） |
| sk-0094 | quote | health-first | A7 健康与作息 | 旧标签先验 + 文本证据（关键词 8.42 + 先验 2.5 = 10.92） | 思维与智力（6.7） · 全面发展与个性（5.2） |
| sk-0095 | principle | labor-education | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 5.31 + 先验 2.5 = 7.81） | 公民与祖国（5.7） · 尊严、爱与信任（4.9） |
| sk-0096 | quote | aesthetic-nature-education, labor-education | A14 美与艺术 | 旧标签先验 + 文本证据（关键词 8.95 + 先验 2.5 = 11.45） | 劳动与创造（5.3） · 幸福与精神生活（3.3） |
| sk-0097 | principle | teacher-growth | A10 教师 | 旧标签先验 + 文本证据（关键词 7.21 + 先验 2.5 = 9.71） | 尊严、爱与信任（4.3） · 自我教育（3.8） |
| sk-0098 | quote | teacher-growth | A10 教师 | 旧标签先验 + 文本证据（关键词 7.21 + 先验 2.5 = 9.71） | 尊严、爱与信任（4.7） · 美与艺术（4.2） |
| sk-0100 | practice | teacher-growth | A10 教师 | 旧标签先验 + 文本证据（关键词 13.25 + 先验 2.5 = 15.75） | 阅读与书籍（7.1） · 集体与同伴（5.2） |
| sk-0101 | method | assessment-grading | A20 检查知识与考查 | 文本证据推翻旧标签（关键词 12.44，压过旧标签项 3.31） | 思维与智力（3.3） · 教师（2.4） |
| sk-0103 | principle | reading-and-books, learning-difficulties | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 6.83 + 先验 2.5 = 9.33） | 学习困难学生（5.6） · 了解儿童（3.4） |
| sk-0104 | quote | teacher-growth, collective-education | A14 美与艺术 | 文本证据推翻旧标签（关键词 5.93，压过旧标签项 4.88） | 习惯与纪律（4.9） · 自我教育（3.8） |
| sk-0105 | quote | health-first, child-study | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 2.33 + 先验 1.0 = 3.33） | （除建议条目外无其他关键词命中） |
| sk-0106 | quote | labor-education, teacher-growth | A10 教师 | 旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88） | 幸福与精神生活（3.0） · 劳动与创造（2.3） |
| sk-0107 | quote | love-education, family-school | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 6.77 + 先验 1.0 = 7.77） | 家庭与母亲（3.5） · 劳动与创造（3.0） |
| sk-0108 | principle | thinking-and-nature, child-study | A3 幸福与精神生活 | 文本证据推翻旧标签（关键词 11.09，压过旧标签项 6.19） | 思维与智力（3.7） · 了解儿童（3.4） |
| sk-0109 | method | child-study, teacher-growth | A11 劳动与创造 | 文本证据推翻旧标签（关键词 7.93，压过旧标签项 6.30） | 全面发展与个性（5.0） · 幸福与精神生活（4.0） |
| sk-0110 | principle | learning-difficulties, child-study | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 10.36 + 先验 1.0 = 11.36） | 教师（2.4） · 劳动与创造（2.3） |
| sk-0112 | practice | collective-education, teacher-growth | A5 尊严、爱与信任 | 文本证据推翻旧标签（关键词 8.89，压过旧标签项 7.63） | 自我教育（6.6） · 思维与智力（4.0） |
| sk-0113 | quote | aesthetic-nature-education, reading-and-books | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 5.84 + 先验 2.5 = 8.34） | 幸福与精神生活（6.4） · 了解儿童（3.4） |
| sk-0115 | principle | child-study, teacher-growth | A3 幸福与精神生活 | 文本证据推翻旧标签（关键词 6.98，压过旧标签项 5.62） | 尊严、爱与信任（4.6） · 教师（2.4） |
| sk-0116 | method | teacher-growth, collective-education | A15 思维与智力 | 文本证据推翻旧标签（关键词 7.40，压过旧标签项 4.88） | 全面发展与个性（4.4） · 尊严、爱与信任（4.3） |
| sk-0117 | practice | aesthetic-nature-education, thinking-and-nature | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 6.98 + 先验 1.0 = 7.98） | 自然与思维课（4.2） · 了解儿童（3.4） |
| sk-0118 | principle | reading-and-books, assessment-grading | A14 美与艺术 | 文本证据推翻旧标签（关键词 9.19，压过旧标签项 6.97） | 幸福与精神生活（7.0） · 自我教育（5.9） |
| sk-0119 | quote | labor-education | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 7.01 + 先验 2.5 = 9.51） | 幸福与精神生活（7.7） · 尊严、爱与信任（4.8） |
| sk-0120 | quote | love-education, family-school | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 4.90 + 先验 2.5 = 7.40） | 自我教育（4.4） · 幸福与精神生活（3.4） |
| sk-0122 | method | reading-and-books, teacher-growth | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 11.06 + 先验 2.5 = 13.56） | 劳动与创造（5.3） · 习惯与纪律（4.9） |
| sk-0123 | quote | aesthetic-nature-education | A7 健康与作息 | 文本证据推翻旧标签（关键词 8.42，压过旧标签项 7.24） | 劳动与创造（5.3） · 尊严、爱与信任（4.9） |
| sk-0124 | quote | assessment-grading, child-study | A16 评价与分数 | 旧标签先验 + 文本证据（关键词 18.47 + 先验 2.5 = 20.97） | 全面发展与个性（4.4） · 公民与祖国（4.0） |
| sk-0126 | method | health-first, child-study | A4 自我教育 | 文本证据推翻旧标签（关键词 21.33，压过旧标签项 15.73） | 健康与作息（13.2） · 评价与分数（10.6） |
| sk-0127 | quote | family-school, child-study | A8 家庭与母亲 | 旧标签先验 + 文本证据（关键词 3.50 + 先验 2.5 = 6.00） | （除建议条目外无其他关键词命中） |
| sk-0128 | principle | family-school, labor-education | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 9.90 + 先验 2.5 = 12.40） | 幸福与精神生活（11.1） · 健康与作息（5.9） |
| sk-0129 | principle | collective-education, labor-education | A17 习惯与纪律 | 旧标签先验 + 文本证据（关键词 9.88 + 先验 1.0 = 10.88） | 家庭与母亲（7.6） · 幸福与精神生活（7.0） |
| sk-0130 | quote | aesthetic-nature-education, teacher-growth | A14 美与艺术 | 旧标签先验 + 文本证据（关键词 4.45 + 先验 2.5 = 6.95） | 幸福与精神生活（3.7） · 道德判断与品德培养（3.0） |
| sk-0131 | quote | health-first, child-study | A7 健康与作息 | 旧标签先验 + 文本证据（关键词 14.36 + 先验 2.5 = 16.86） | 了解儿童（3.4） · 教师（2.4） |
| sk-0133 | principle | reading-and-books, child-study | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 6.83 + 先验 2.5 = 9.33） | 评价与分数（5.8） · 幸福与精神生活（3.3） |
| sk-0134 | method | collective-education, love-education, teacher-growth | A9 集体与同伴 | 旧标签先验 + 文本证据（关键词 6.84 + 先验 2.5 = 9.34） | 道德判断与品德培养（6.8） · 思维与智力（4.7） |
| sk-0136 | quote | teacher-growth, love-education | A10 教师 | 旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88） | 幸福与精神生活（3.4） · 了解儿童（3.4） |
| sk-0137 | quote | thinking-and-nature, aesthetic-nature-education | A12 自然与思维课 | 旧标签先验 + 文本证据（关键词 13.76 + 先验 1.0 = 14.76） | 思维与智力（7.0） · 美与艺术（4.7） |
| sk-0138 | quote | teacher-growth, love-education | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 8.85 + 先验 2.5 = 11.35） | 评价与分数（4.8） · 健康与作息（4.1） |
| sk-0139 | principle | collective-education, teacher-growth, labor-education | A5 尊严、爱与信任 | 文本证据推翻旧标签（关键词 13.23，压过旧标签项 10.85） | 集体与同伴（8.4） · 阅读与书籍（7.4） |
| sk-0141 | quote | teacher-growth | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 7.44 + 先验 1.0 = 8.44） | 习惯与纪律（4.9） · 全面发展与个性（4.4） |
| sk-0142 | method | teacher-growth, family-school, child-study | A3 幸福与精神生活 | 文本证据推翻旧标签（关键词 6.29，压过旧标签项 5.38） | 尊严、爱与信任（4.4） · 自我教育（4.3） |
| sk-0143 | quote | teacher-growth, child-study, love-education | A4 自我教育 | 旧标签先验 + 文本证据（关键词 10.97 + 先验 1.0 = 11.97） | 自然与思维课（5.2） · 评价与分数（4.8） |
| sk-0144 | quote | teacher-growth | A10 教师 | 旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88） | 劳动与创造（3.0） |
| sk-0145 | quote | child-study, teacher-growth | A10 教师 | 旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88） | 幸福与精神生活（3.0） |
| sk-0146 | principle | health-first | A7 健康与作息 | 旧标签先验 + 文本证据（关键词 13.71 + 先验 2.5 = 16.21） | 尊严、爱与信任（5.0） · 自然与思维课（4.2） |
| sk-0147 | quote | aesthetic-nature-education | A11 劳动与创造 | 文本证据推翻旧标签（关键词 10.14，压过旧标签项 2.50） | （除建议条目外无其他关键词命中） |
| sk-0148 | method | reading-and-books, aesthetic-nature-education | A11 劳动与创造 | 文本证据推翻旧标签（关键词 2.98，压过旧标签项 2.50） | 教师（2.4） |
| sk-0149 | practice | aesthetic-nature-education | A12 自然与思维课 | 旧标签先验 + 文本证据（关键词 8.30 + 先验 1.0 = 9.30） | 幸福与精神生活（7.0） · 美与艺术（4.5） |
| sk-0151 | principle | labor-education | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 2.33 + 先验 2.5 = 4.83） | 幸福与精神生活（4.0） · 了解儿童（3.8） |
| sk-0152 | quote | collective-education, child-study | A4 自我教育 | 文本证据推翻旧标签（关键词 14.78，压过旧标签项 5.66） | 习惯与纪律（5.0） · 尊严、爱与信任（4.4） |
| sk-0153 | principle | child-study, teacher-growth | A10 教师 | 旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88） | （除建议条目外无其他关键词命中） |
| sk-0154 | principle | labor-education, collective-education | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 5.31 + 先验 2.5 = 7.81） | 尊严、爱与信任（4.8） · 全面发展与个性（4.4） |
| sk-0155 | quote | aesthetic-nature-education, child-study | A14 美与艺术 | 旧标签先验 + 文本证据（关键词 10.38 + 先验 2.5 = 12.88） | 自然与思维课（4.1） · 幸福与精神生活（4.0） |
| sk-0156 | method | love-education, child-study | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 11.65 + 先验 1.0 = 12.65） | 尊严、爱与信任（9.6） · 健康与作息（4.3） |
| sk-0157 | quote | family-school, love-education | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 11.11 + 先验 2.5 = 13.61） | 家庭与母亲（3.5） |
| sk-0158 | quote | collective-education, aesthetic-nature-education | A15 思维与智力 | 文本证据推翻旧标签（关键词 7.01，压过旧标签项 6.18） | 幸福与精神生活（3.8） · 集体与同伴（3.7） |
| sk-0159 | practice | teacher-growth | A10 教师 | 旧标签先验 + 文本证据（关键词 7.21 + 先验 2.5 = 9.71） | 习惯与纪律（4.9） · 劳动与创造（3.0） |
| sk-0160 | method | health-first | A7 健康与作息 | 旧标签先验 + 文本证据（关键词 10.63 + 先验 2.5 = 13.13） | 习惯与纪律（10.8） · 了解儿童（7.2） |
| sk-0161 | method | teacher-growth, collective-education | A9 集体与同伴 | 旧标签先验 + 文本证据（关键词 9.09 + 先验 2.5 = 11.59） | 道德判断与品德培养（6.4） · 思维与智力（3.7） |
| sk-0162 | quote | teacher-growth | A15 思维与智力 | 文本证据推翻旧标签（关键词 14.03，压过旧标签项 9.71） | 教师（7.2） · 健康与作息（5.9） |
| sk-0163 | practice | collective-education | A9 集体与同伴 | 旧标签先验 + 文本证据（关键词 12.24 + 先验 2.5 = 14.74） | 阅读与书籍（2.9） · 教师（2.4） |
| sk-0164 | quote | collective-education, teacher-growth | A5 尊严、爱与信任 | 文本证据推翻旧标签（关键词 9.42，压过旧标签项 9.34） | 集体与同伴（6.8） · 了解儿童（3.4） |
| sk-0165 | quote | teacher-growth, child-study, collective-education | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 9.03 + 先验 1.0 = 10.03） | 评价与分数（4.8） · 自我教育（4.4） |
| sk-0166 | method | love-education, collective-education, child-study | A9 集体与同伴 | 旧标签先验 + 文本证据（关键词 8.56 + 先验 2.5 = 11.06） | 幸福与精神生活（6.8） · 习惯与纪律（5.0） |
| sk-0167 | practice | health-first, learning-difficulties | A7 健康与作息 | 旧标签先验 + 文本证据（关键词 16.57 + 先验 2.5 = 19.07） | 习惯与纪律（10.8） · 幸福与精神生活（7.8） |
| sk-0169 | quote | labor-education, collective-education | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 7.79 + 先验 2.5 = 10.29） | 尊严、爱与信任（4.3） · 健康与作息（4.1） |
| sk-0170 | principle | love-education, collective-education | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 3.31 + 先验 1.0 = 4.31） | 道德判断与品德培养（3.0） · 教师（2.4） |
| sk-0171 | quote | teacher-growth, collective-education | A1 全面发展与个性 | 文本证据推翻旧标签（关键词 6.63，压过旧标签项 4.88） | 评价与分数（4.2） · 了解儿童（3.8） |
| sk-0173 | quote | aesthetic-nature-education | A14 美与艺术 | 旧标签先验 + 文本证据（关键词 4.45 + 先验 2.5 = 6.95） | 自我教育（4.3） · 道德判断与品德培养（3.0） |
| sk-0174 | quote | thinking-and-nature, learning-difficulties | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 3.69 + 先验 2.5 = 6.19） | 自然与思维课（4.1） · 教师（2.4） |
| sk-0175 | quote | reading-and-books, aesthetic-nature-education | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 6.98 + 先验 1.0 = 7.98） | 劳动与创造（4.7） |
| sk-0176 | quote | family-school, reading-and-books, child-study | A6 了解儿童 | 旧标签先验 + 文本证据（关键词 3.80 + 先验 2.5 = 6.30） | 美与艺术（4.7） · 道德判断与品德培养（3.0） |
| sk-0177 | method | collective-education, child-study, teacher-growth | A9 集体与同伴 | 旧标签先验 + 文本证据（关键词 3.16 + 先验 2.5 = 5.66） | 美与艺术（4.2） · 幸福与精神生活（3.0） |
| sk-0178 | quote | assessment-grading, learning-difficulties | A16 评价与分数 | 旧标签先验 + 文本证据（关键词 10.20 + 先验 2.5 = 12.70） | 思维与智力（11.2） · 尊严、爱与信任（4.8） |
| sk-0179 | method | assessment-grading, learning-difficulties | A16 评价与分数 | 旧标签先验 + 文本证据（关键词 23.93 + 先验 2.5 = 26.43） | 教师（2.4） · 劳动与创造（2.3） |
| sk-0180 | principle | assessment-grading, family-school | A16 评价与分数 | 旧标签先验 + 文本证据（关键词 14.36 + 先验 2.5 = 16.86） | 家庭与母亲（7.6） · 幸福与精神生活（4.0） |
| sk-0181 | quote | assessment-grading | A16 评价与分数 | 旧标签先验 + 文本证据（关键词 10.26 + 先验 2.5 = 12.76） | 阅读与书籍（7.1） · 检查知识与考查（5.6） |
| sk-0182 | principle | assessment-grading, family-school | A16 评价与分数 | 旧标签先验 + 文本证据（关键词 4.16 + 先验 2.5 = 6.66） | 劳动与创造（4.7） · 家庭与母亲（4.1） |
| sk-0184 | quote | health-first | A7 健康与作息 | 旧标签先验 + 文本证据（关键词 13.77 + 先验 2.5 = 16.27） | 了解儿童（3.4） · 劳动与创造（2.3） |
| sk-0186 | quote | health-first, learning-difficulties | A7 健康与作息 | 旧标签先验 + 文本证据（关键词 25.01 + 先验 2.5 = 27.51） | 思维与智力（11.2） · 自然与思维课（4.1） |
| sk-0187 | method | health-first, child-study | A7 健康与作息 | 旧标签先验 + 文本证据（关键词 26.09 + 先验 2.5 = 28.59） | 习惯与纪律（4.9） · 自我教育（4.3） |
| sk-0188 | practice | health-first, labor-education | A7 健康与作息 | 旧标签先验 + 文本证据（关键词 18.57 + 先验 2.5 = 21.07） | 自然与思维课（5.7） · 劳动与创造（2.3） |
| sk-0189 | principle | health-first | A7 健康与作息 | 旧标签先验 + 文本证据（关键词 30.30 + 先验 2.5 = 32.80） | 习惯与纪律（10.8） · 了解儿童（3.4） |
| sk-0190 | quote | thinking-and-nature, learning-difficulties | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 6.67 + 先验 2.5 = 9.17） | 检查知识与考查（6.2） · 学习困难学生（4.9） |
| sk-0191 | principle | thinking-and-nature | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 7.01 + 先验 2.5 = 9.51） | 自然与思维课（4.1） · 劳动与创造（2.3） |
| sk-0192 | method | thinking-and-nature, child-study | A12 自然与思维课 | 旧标签先验 + 文本证据（关键词 9.60 + 先验 1.0 = 10.60） | 思维与智力（3.7） · 幸福与精神生活（3.7） |
| sk-0193 | quote | thinking-and-nature, reading-and-books | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 17.51 + 先验 2.5 = 20.01） | 自然与思维课（16.1） · 思维与智力（6.7） |
| sk-0194 | quote | thinking-and-nature | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 7.04 + 先验 2.5 = 9.54） | 幸福与精神生活（7.3） · 自然与思维课（5.5） |
| sk-0196 | quote | teacher-growth, child-study | A10 教师 | 旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88） | 家庭与母亲（3.5） |
| sk-0197 | quote | teacher-growth, child-study | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 8.85 + 先验 1.0 = 9.85） | 思维与智力（4.0） · 道德判断与品德培养（3.0） |
| sk-0198 | quote | love-education, child-study | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 14.61 + 先验 1.0 = 15.61） | 家庭与母亲（3.5） · 道德判断与品德培养（3.0） |
| sk-0199 | practice | love-education, labor-education | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 7.96 + 先验 1.0 = 8.96） | 家庭与母亲（3.5） · 劳动与创造（3.0） |
| sk-0200 | quote | labor-education, teacher-growth | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 5.31 + 先验 2.5 = 7.81） | 幸福与精神生活（7.7） · 全面发展与个性（4.4） |
| sk-0201 | quote | teacher-growth, child-study | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 4.98 + 先验 1.0 = 5.98） | 全面发展与个性（4.4） · 思维与智力（4.0） |
| sk-0202 | quote | child-study, teacher-growth | A4 自我教育 | 旧标签先验 + 文本证据（关键词 17.19 + 先验 1.0 = 18.19） | 道德判断与品德培养（3.0） · 幸福与精神生活（3.0） |
| sk-0204 | quote | love-education, child-study | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 4.90 + 先验 2.5 = 7.40） | 全面发展与个性（4.4） · 自我教育（3.8） |
| sk-0206 | quote | teacher-growth, child-study | A10 教师 | 旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88） | 评价与分数（4.7） · 幸福与精神生活（3.8） |
| sk-0207 | method | assessment-grading, teacher-growth | A16 评价与分数 | 旧标签先验 + 文本证据（关键词 14.36 + 先验 2.5 = 16.86） | 思维与智力（3.4） · 劳动与创造（2.3） |
| sk-0208 | quote | love-education, teacher-growth | A10 教师 | 旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88） | （除建议条目外无其他关键词命中） |
| sk-0209 | quote | love-education, child-study | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 3.31 + 先验 1.0 = 4.31） | 教师（2.4） |
| sk-0210 | quote | labor-education, collective-education | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 9.90 + 先验 2.5 = 12.40） | 公民与祖国（4.0） · 幸福与精神生活（4.0） |
| sk-0211 | quote | collective-education, child-study | A2 公民与祖国 | 旧标签先验 + 文本证据（关键词 4.05 + 先验 1.0 = 5.05） | 评价与分数（4.8） · 劳动与创造（2.3） |
| sk-0212 | quote | love-education, collective-education | A2 公民与祖国 | 旧标签先验 + 文本证据（关键词 9.28 + 先验 1.0 = 10.28） | 习惯与纪律（5.0） · 集体与同伴（3.2） |
| sk-0213 | practice | love-education, labor-education | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 2.33 + 先验 2.5 = 4.83） | 全面发展与个性（4.4） · 家庭与母亲（3.5） · 幸福与精神生活（3.0） |
| sk-0214 | quote | teacher-growth, child-study | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 10.33 + 先验 1.0 = 11.33） | 尊严、爱与信任（4.4） · 幸福与精神生活（3.3） |
| sk-0215 | quote | teacher-growth, child-study | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 4.23 + 先验 1.0 = 5.23） | 全面发展与个性（4.4） · 思维与智力（4.0） |
| sk-0216 | quote | reading-and-books, learning-difficulties | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 6.83 + 先验 2.5 = 9.33） | 了解儿童（3.8） |
| sk-0217 | quote | child-study, learning-difficulties | A12 自然与思维课 | 文本证据推翻旧标签（关键词 5.19，压过旧标签项 4.31） | 思维与智力（3.3） |
| sk-0218 | quote | child-study, thinking-and-nature | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 11.09 + 先验 2.5 = 13.59） | 评价与分数（4.8） · 幸福与精神生活（3.8） |
| sk-0219 | quote | thinking-and-nature, child-study | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 7.74 + 先验 2.5 = 10.24） | 自然与思维课（5.5） · 了解儿童（3.4） |
| sk-0220 | quote | love-education, teacher-growth | A8 家庭与母亲 | 文本证据推翻旧标签（关键词 7.64，压过旧标签项 4.88） | 教师（2.4） |
| sk-0221 | quote | child-study, teacher-growth | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 4.23 + 先验 1.0 = 5.23） | 习惯与纪律（5.0） · 教师（2.4） |
| sk-0222 | quote | child-study, teacher-growth | A10 教师 | 旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88） | 公民与祖国（4.0） · 集体与同伴（3.7） · 幸福与精神生活（3.7） |
| sk-0223 | quote | family-school, child-study | A8 家庭与母亲 | 旧标签先验 + 文本证据（关键词 3.50 + 先验 2.5 = 6.00） | 思维与智力（3.3） |
| sk-0224 | quote | teacher-growth, child-study | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 7.44 + 先验 1.0 = 8.44） | 自我教育（3.8） · 思维与智力（3.3） |
| sk-0225 | quote | love-education, child-study | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 6.41 + 先验 1.0 = 7.41） | 教师（6.6） · 公民与祖国（3.9） |
| sk-0226 | quote | love-education, teacher-growth | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 4.98 + 先验 2.5 = 7.48） | 评价与分数（4.8） · 教师（2.4） |
| sk-0227 | quote | family-school, love-education | A8 家庭与母亲 | 旧标签先验 + 文本证据（关键词 3.50 + 先验 2.5 = 6.00） | （除建议条目外无其他关键词命中） |
| sk-0228 | quote | family-school, love-education | A11 劳动与创造 | 文本证据推翻旧标签（关键词 7.66，压过旧标签项 7.40） | 尊严、爱与信任（4.9） · 家庭与母亲（3.5） |
| sk-0229 | quote | teacher-growth, reading-and-books | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 11.67 + 先验 2.5 = 14.17） | 思维与智力（3.3） · 集体与同伴（3.2） |
| sk-0230 | quote | love-education, child-study | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 3.42 + 先验 1.0 = 4.42） | 劳动与创造（3.0） · 教师（2.4） |
| sk-0231 | quote | teacher-growth, love-education | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 9.07 + 先验 2.5 = 11.57） | 思维与智力（4.0） · 幸福与精神生活（3.0） |
| sk-0232 | quote | collective-education, child-study | A2 公民与祖国 | 旧标签先验 + 文本证据（关键词 5.67 + 先验 1.0 = 6.67） | 幸福与精神生活（3.0） |
| sk-0233 | quote | collective-education, teacher-growth | A4 自我教育 | 旧标签先验 + 文本证据（关键词 6.44 + 先验 1.0 = 7.44） | 公民与祖国（5.7） · 尊严、爱与信任（4.4） |
| sk-0234 | quote | reading-and-books, teacher-growth | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 15.63 + 先验 2.5 = 18.13） | 劳动与创造（8.4） · 美与艺术（4.5） |
| sk-0235 | quote | family-school, labor-education | A8 家庭与母亲 | 旧标签先验 + 文本证据（关键词 5.93 + 先验 2.5 = 8.43） | （除建议条目外无其他关键词命中） |
| sk-0236 | quote | family-school, love-education | A20 检查知识与考查 | 文本证据推翻旧标签（关键词 5.10，压过旧标签项 4.42） | 集体与同伴（3.7） · 幸福与精神生活（3.4） |
| sk-0237 | quote | reading-and-books, teacher-growth | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 7.10 + 先验 2.5 = 9.60） | 幸福与精神生活（7.4） |
| sk-0238 | principle | child-study, teacher-growth | A19 道德判断与品德培养 | 文本证据推翻旧标签（关键词 6.44，压过旧标签项 4.88） | 自我教育（3.8） · 幸福与精神生活（3.0） |
| sk-0239 | principle | labor-education, collective-education | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 2.33 + 先验 2.5 = 4.83） | 尊严、爱与信任（4.6） · 健康与作息（4.3） · 思维与智力（4.0） |
| sk-0240 | quote | teacher-growth, labor-education | A4 自我教育 | 旧标签先验 + 文本证据（关键词 4.43 + 先验 1.0 = 5.43） | 全面发展与个性（4.4） · 公民与祖国（4.0） |
| sk-0241 | principle | collective-education, teacher-growth | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 6.83 + 先验 1.0 = 7.83） | 思维与智力（7.5） · 自我教育（3.8） |
| sk-0242 | quote | collective-education, child-study | A2 公民与祖国 | 旧标签先验 + 文本证据（关键词 7.98 + 先验 1.0 = 8.98） | 健康与作息（4.8） · 家庭与母亲（3.5） |
| sk-0243 | quote | child-study, collective-education | A7 健康与作息 | 文本证据推翻旧标签（关键词 9.08，压过旧标签项 6.44） | 道德判断与品德培养（6.4） · 全面发展与个性（4.4） |
| sk-0244 | principle | labor-education, collective-education | A2 公民与祖国 | 旧标签先验 + 文本证据（关键词 4.05 + 先验 1.0 = 5.05） | 幸福与精神生活（3.8） · 劳动与创造（2.3） |
| sk-0245 | quote | labor-education, collective-education | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 10.14 + 先验 2.5 = 12.64） | （除建议条目外无其他关键词命中） |
| sk-0246 | quote | aesthetic-nature-education, thinking-and-nature | A12 自然与思维课 | 旧标签先验 + 文本证据（关键词 9.81 + 先验 1.0 = 10.81） | 全面发展与个性（5.1） · 自我教育（3.8） |
| sk-0247 | quote | labor-education, aesthetic-nature-education | A12 自然与思维课 | 旧标签先验 + 文本证据（关键词 4.14 + 先验 1.0 = 5.14） | 劳动与创造（2.3） |
| sk-0248 | quote | child-study, love-education | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 4.38 + 先验 2.5 = 6.88） | 思维与智力（3.7） · 幸福与精神生活（3.0） |
| sk-0249 | method | child-study, love-education | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 3.99 + 先验 1.0 = 4.99） | 健康与作息（4.3） · 集体与同伴（3.7） |
| sk-0250 | quote | labor-education, family-school | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 15.45 + 先验 2.5 = 17.95） | （除建议条目外无其他关键词命中） |
| sk-0251 | quote | labor-education, teacher-growth | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 7.79 + 先验 2.5 = 10.29） | 幸福与精神生活（4.0） · 思维与智力（3.7） |
| sk-0252 | quote | family-school, love-education | A11 劳动与创造 | 文本证据推翻旧标签（关键词 7.79，压过旧标签项 2.50） | （除建议条目外无其他关键词命中） |
| sk-0253 | quote | family-school, labor-education | A19 道德判断与品德培养 | 文本证据推翻旧标签（关键词 10.13，压过旧标签项 8.43） | 家庭与母亲（5.9） · 劳动与创造（2.3） |
| sk-0254 | quote | teacher-growth, love-education | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 5.10 + 先验 1.0 = 6.10） | 评价与分数（4.2） · 道德判断与品德培养（3.0） |
| sk-0255 | quote | teacher-growth, child-study | A3 幸福与精神生活 | 文本证据推翻旧标签（关键词 8.08，压过旧标签项 6.30） | 检查知识与考查（6.0） · 全面发展与个性（5.2） |
| sk-0256 | quote | teacher-growth, child-study | A4 自我教育 | 旧标签先验 + 文本证据（关键词 4.43 + 先验 1.0 = 5.43） | 美与艺术（4.2） · 幸福与精神生活（3.0） |
| sk-0257 | quote | love-education, child-study | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 6.95 + 先验 1.0 = 7.95） | 健康与作息（5.9） · 劳动与创造（2.3） |
| sk-0258 | quote | family-school, love-education | A2 公民与祖国 | 旧标签先验 + 文本证据（关键词 9.39 + 先验 1.0 = 10.39） | 全面发展与个性（4.4） · 道德判断与品德培养（3.0） |
| sk-0259 | quote | family-school, love-education | A1 全面发展与个性 | 文本证据推翻旧标签（关键词 4.43，压过旧标签项 2.50） | 劳动与创造（2.3） |
| sk-0260 | quote | child-study, reading-and-books | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 7.10 + 先验 2.5 = 9.60） | 评价与分数（4.8） · 幸福与精神生活（4.0） |
| sk-0261 | principle | thinking-and-nature, labor-education | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 6.67 + 先验 2.5 = 9.17） | 了解儿童（3.4） · 教师（2.4） |
| sk-0262 | principle | learning-difficulties, teacher-growth | A10 教师 | 旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88） | 学习困难学生（5.8） · 劳动与创造（3.0） |
| sk-0263 | quote | teacher-growth, learning-difficulties | A6 了解儿童 | 旧标签先验 + 文本证据（关键词 3.37 + 先验 2.5 = 5.87） | 评价与分数（4.2） · 思维与智力（3.3） |
| sk-0264 | principle | labor-education, collective-education | A2 公民与祖国 | 旧标签先验 + 文本证据（关键词 9.28 + 先验 1.0 = 10.28） | 幸福与精神生活（6.3） · 评价与分数（4.8） |
| sk-0265 | quote | labor-education, family-school | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 7.01 + 先验 2.5 = 9.51） | 习惯与纪律（4.8） · 幸福与精神生活（4.0） |
| sk-0266 | quote | collective-education, teacher-growth | A4 自我教育 | 旧标签先验 + 文本证据（关键词 9.75 + 先验 1.0 = 10.75） | 评价与分数（4.8） · 道德判断与品德培养（3.0） |
| sk-0267 | principle | labor-education, collective-education | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 5.31 + 先验 2.5 = 7.81） | 评价与分数（4.8） · 集体与同伴（3.2） |
| sk-0268 | principle | labor-education, collective-education | A3 幸福与精神生活 | 文本证据推翻旧标签（关键词 12.39，压过旧标签项 10.31） | 劳动与创造（7.8） · 集体与同伴（5.9） |
| sk-0269 | quote | labor-education, child-study | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 5.31 + 先验 2.5 = 7.81） | 全面发展与个性（4.4） |
| sk-0270 | quote | labor-education, teacher-growth | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 10.98 + 先验 2.5 = 13.48） | 思维与智力（11.2） · 幸福与精神生活（3.8） |
| sk-0271 | principle | learning-difficulties, teacher-growth | A10 教师 | 全无关键词证据，按旧标签先验定夺 | 学习困难学生（6.4） |
| sk-0272 | quote | child-study, teacher-growth | A6 了解儿童 | 旧标签先验 + 文本证据（关键词 3.37 + 先验 2.5 = 5.87） | 学习困难学生（5.8） · 思维与智力（3.4） |
| sk-0273 | quote | child-study, teacher-growth | A10 教师 | 旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88） | 劳动与创造（3.0） |
| sk-0274 | principle | labor-education, thinking-and-nature | A3 幸福与精神生活 | 文本证据推翻旧标签（关键词 7.64，压过旧标签项 4.83） | 了解儿童（3.8） · 劳动与创造（2.3） |
| sk-0275 | method | labor-education, teacher-growth | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 2.33 + 先验 2.5 = 4.83） | 自然与思维课（4.1） · 阅读与书籍（2.9） |
| sk-0276 | quote | teacher-growth, labor-education | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 16.30 + 先验 2.5 = 18.80） | 美与艺术（4.2） · 教师（2.4） |
| sk-0277 | quote | teacher-growth | A10 教师 | 旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88） | 劳动与创造（2.3） |
| sk-0278 | quote | child-study, teacher-growth | A6 了解儿童 | 旧标签先验 + 文本证据（关键词 3.80 + 先验 2.5 = 6.30） | 全面发展与个性（4.4） · 劳动与创造（3.0） |
| sk-0279 | quote | collective-education, teacher-growth | A9 集体与同伴 | 旧标签先验 + 文本证据（关键词 3.16 + 先验 2.5 = 5.66） | 劳动与创造（5.3） |
| sk-0280 | quote | labor-education, family-school | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 22.28 + 先验 2.5 = 24.78） | （除建议条目外无其他关键词命中） |
| sk-0281 | principle | labor-education, family-school | A8 家庭与母亲 | 旧标签先验 + 文本证据（关键词 4.14 + 先验 2.5 = 6.64） | 评价与分数（4.8） · 幸福与精神生活（3.4） |
| sk-0282 | quote | labor-education, child-study | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 5.31 + 先验 2.5 = 7.81） | 幸福与精神生活（7.8） · 全面发展与个性（5.0） |
| sk-0283 | quote | labor-education | A5 尊严、爱与信任 | 文本证据推翻旧标签（关键词 9.70，压过旧标签项 7.81） | 劳动与创造（5.3） |
| sk-0284 | quote | teacher-growth | A10 教师 | 旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88） | 美与艺术（4.2） · 思维与智力（4.0） |
| sk-0285 | quote | teacher-growth, reading-and-books | A10 教师 | 旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88） | 美与艺术（4.2） · 思维与智力（4.0） · 幸福与精神生活（3.0） |
| sk-0286 | quote | labor-education, child-study | A3 幸福与精神生活 | 文本证据推翻旧标签（关键词 7.39，压过旧标签项 7.14） | 公民与祖国（7.1） · 尊严、爱与信任（4.9） |
| sk-0287 | quote | labor-education, family-school | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 9.99 + 先验 2.5 = 12.49） | 幸福与精神生活（3.4） |
| sk-0288 | quote | collective-education, child-study | A4 自我教育 | 文本证据推翻旧标签（关键词 21.31，压过旧标签项 3.31） | 幸福与精神生活（3.3） · 道德判断与品德培养（3.0） |
| sk-0289 | principle | collective-education, child-study | A19 道德判断与品德培养 | 文本证据推翻旧标签（关键词 2.99，压过旧标签项 2.50） | （除建议条目外无其他关键词命中） |
| sk-0290 | quote | child-study, collective-education | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 4.62 + 先验 1.0 = 5.62） | （除建议条目外无其他关键词命中） |
| sk-0291 | principle | teacher-growth, child-study | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 6.67 + 先验 1.0 = 7.67） | 全面发展与个性（5.1） · 自我教育（3.8） |
| sk-0292 | quote | health-first, labor-education | A7 健康与作息 | 旧标签先验 + 文本证据（关键词 13.77 + 先验 2.5 = 16.27） | 幸福与精神生活（7.3） · 劳动与创造（5.3） |
| sk-0293 | principle | aesthetic-nature-education, child-study | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 7.66 + 先验 1.0 = 8.66） | 美与艺术（4.2） · 自然与思维课（4.1） |
| sk-0294 | quote | learning-difficulties, child-study | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 7.46 + 先验 1.0 = 8.46） | 了解儿童（3.4） |
| sk-0295 | principle | learning-difficulties, child-study | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 3.35 + 先验 1.0 = 4.35） | 学习困难学生（6.2） · 幸福与精神生活（4.0） |
| sk-0296 | quote | collective-education, child-study | A16 评价与分数 | 文本证据推翻旧标签（关键词 18.18，压过旧标签项 2.99） | 道德判断与品德培养（3.0） |
| sk-0297 | principle | teacher-growth, learning-difficulties | A10 教师 | 旧标签先验 + 文本证据（关键词 8.42 + 先验 2.5 = 10.92） | （除建议条目外无其他关键词命中） |
| sk-0298 | principle | assessment-grading, teacher-growth | A16 评价与分数 | 旧标签先验 + 文本证据（关键词 8.93 + 先验 2.5 = 11.43） | 教师（7.2） · 检查知识与考查（5.6） |
| sk-0299 | principle | teacher-growth, child-study | A16 评价与分数 | 文本证据推翻旧标签（关键词 4.16，压过旧标签项 3.87） | 阅读与书籍（2.9） |
| sk-0300 | quote | collective-education | A2 公民与祖国 | 旧标签先验 + 文本证据（关键词 6.04 + 先验 1.0 = 7.04） | 全面发展与个性（5.1） · 自我教育（3.8） |
| sk-0301 | quote | collective-education, child-study | A4 自我教育 | 文本证据推翻旧标签（关键词 8.24，压过旧标签项 2.99） | 道德判断与品德培养（3.0） |
| sk-0302 | quote | teacher-growth | A10 教师 | 旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88） | 自我教育（3.8） · 幸福与精神生活（3.0） · 阅读与书籍（2.9） |
| sk-0303 | quote | teacher-growth, child-study | A1 全面发展与个性 | 文本证据推翻旧标签（关键词 5.06，压过旧标签项 4.35） | 思维与智力（3.4） · 道德判断与品德培养（3.0） |
| sk-0304 | quote | love-education | A4 自我教育 | 文本证据推翻旧标签（关键词 8.24，压过旧标签项 4.31） | 幸福与精神生活（3.3） · 道德判断与品德培养（3.0） |
| sk-0305 | quote | love-education | A2 公民与祖国 | 旧标签先验 + 文本证据（关键词 4.05 + 先验 1.0 = 5.05） | 幸福与精神生活（3.3） · 劳动与创造（3.0） |
| sk-0306 | quote | family-school, love-education | A8 家庭与母亲 | 旧标签先验 + 文本证据（关键词 3.50 + 先验 2.5 = 6.00） | （除建议条目外无其他关键词命中） |
| sk-0307 | quote | child-study | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 8.61 + 先验 1.0 = 9.61） | 评价与分数（4.8） · 教师（2.4） |
| sk-0308 | quote | teacher-growth, love-education | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 6.65 + 先验 1.0 = 7.65） | 了解儿童（3.4） · 劳动与创造（3.0） |
| sk-0309 | quote | learning-difficulties, teacher-growth | A16 评价与分数 | 文本证据推翻旧标签（关键词 4.16，压过旧标签项 2.50） | 学习困难学生（4.9） |
| sk-0310 | quote | labor-education, child-study | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 15.81 + 先验 2.5 = 18.31） | 思维与智力（3.7） |
| sk-0311 | quote | child-study, teacher-growth | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 4.62 + 先验 1.0 = 5.62） | 教师（2.4） |
| sk-0312 | quote | labor-education, collective-education | A1 全面发展与个性 | 文本证据推翻旧标签（关键词 5.02，压过旧标签项 4.90） | 尊严、爱与信任（4.9） · 劳动与创造（2.3） |
| sk-0313 | principle | thinking-and-nature | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 3.35 + 先验 2.5 = 5.85） | 劳动与创造（5.3） · 全面发展与个性（5.1） |
| sk-0314 | quote | love-education, teacher-growth | A4 自我教育 | 旧标签先验 + 文本证据（关键词 3.82 + 先验 1.0 = 4.82） | 幸福与精神生活（3.3） |
| sk-0315 | principle | love-education, collective-education | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 10.96 + 先验 1.0 = 11.96） | 自我教育（9.7） · 道德判断与品德培养（8.4） |
| sk-0316 | quote | aesthetic-nature-education | A14 美与艺术 | 旧标签先验 + 文本证据（关键词 4.21 + 先验 2.5 = 6.71） | 尊严、爱与信任（4.2） · 健康与作息（4.1） |
| sk-0317 | quote | child-study, love-education | A6 了解儿童 | 人工裁定（「判断学生要看他将成为什么样的人」= 了解学生的志向，与评分机制无关（外部评审意见）） | 评价与分数（4.8） · 道德判断与品德培养（3.0） |
| sk-0318 | principle | aesthetic-nature-education, child-study | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 13.95 + 先验 1.0 = 14.95） | 检查知识与考查（5.1） · 美与艺术（4.7） |
| sk-0319 | principle | child-study, teacher-growth | A7 健康与作息 | 文本证据推翻旧标签（关键词 8.94，压过旧标签项 5.43） | 自我教育（4.4） · 教师（2.4） |
| sk-0320 | quote | collective-education, child-study | A6 了解儿童 | 旧标签先验 + 文本证据（关键词 3.37 + 先验 2.5 = 5.87） | 幸福与精神生活（3.0） · 劳动与创造（3.0） |
| sk-0321 | principle | collective-education, teacher-growth | A9 集体与同伴 | 旧标签先验 + 文本证据（关键词 3.16 + 先验 2.5 = 5.66） | 全面发展与个性（5.2） · 美与艺术（4.7） · 公民与祖国（4.0） |
| sk-0322 | quote | collective-education, love-education | A9 集体与同伴 | 旧标签先验 + 文本证据（关键词 9.09 + 先验 2.5 = 11.59） | 尊严、爱与信任（5.0） |
| sk-0323 | method | collective-education, teacher-growth | A9 集体与同伴 | 旧标签先验 + 文本证据（关键词 3.68 + 先验 2.5 = 6.18） | 教师（2.4） |
| sk-0324 | quote | assessment-grading, learning-difficulties | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 8.37 + 先验 1.0 = 9.37） | 评价与分数（5.5） · 了解儿童（3.4） |
| sk-0325 | quote | collective-education, labor-education | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 4.60 + 先验 2.5 = 7.10） | 公民与祖国（5.3） · 自然与思维课（4.1） |
| sk-0326 | quote | family-school, child-study | A8 家庭与母亲 | 旧标签先验 + 文本证据（关键词 4.14 + 先验 2.5 = 6.64） | 评价与分数（4.2） · 幸福与精神生活（3.0） |
| sk-0327 | principle | family-school, child-study | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 3.31 + 先验 1.0 = 4.31） | 道德判断与品德培养（3.0） |
| sk-0328 | method | teacher-growth, thinking-and-nature | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 11.15 + 先验 2.5 = 13.65） | 教师（2.4） |
| sk-0329 | principle | reading-and-books, learning-difficulties | A6 了解儿童 | 旧标签先验 + 文本证据（关键词 3.80 + 先验 2.5 = 6.30） | 尊严、爱与信任（4.3） · 思维与智力（3.7） |
| sk-0330 | quote | reading-and-books, child-study | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 11.40 + 先验 2.5 = 13.90） | 尊严、爱与信任（4.4） · 自我教育（4.3） |
| sk-0331 | quote | labor-education | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 6.93 + 先验 2.5 = 9.43） | 健康与作息（5.9） · 全面发展与个性（4.4） |
| sk-0332 | quote | labor-education, teacher-growth | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 11.84 + 先验 2.5 = 14.34） | 自我教育（4.3） · 思维与智力（4.1） |
| sk-0333 | quote | teacher-growth | A4 自我教育 | 旧标签先验 + 文本证据（关键词 4.34 + 先验 1.0 = 5.34） | 思维与智力（3.3） · 幸福与精神生活（3.3） |
| sk-0334 | quote | family-school, love-education | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 7.21 + 先验 1.0 = 8.21） | 全面发展与个性（5.2） · 检查知识与考查（5.1） |
| sk-0335 | quote | child-study, family-school | A8 家庭与母亲 | 旧标签先验 + 文本证据（关键词 3.50 + 先验 2.5 = 6.00） | 思维与智力（4.1） · 教师（2.4） |
| sk-0348 | quote | family-school | A11 劳动与创造 | 文本证据推翻旧标签（关键词 6.93，压过旧标签项 6.00） | 家庭与母亲（3.5） · 思维与智力（3.3） |
| sk-0349 | quote | love-education, collective-education | A19 道德判断与品德培养 | 文本证据推翻旧标签（关键词 6.44，压过旧标签项 5.05） | 习惯与纪律（4.8） · 公民与祖国（4.0） |
| sk-0350 | quote | labor-education, family-school | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 4.38 + 先验 1.0 = 5.38） | 劳动与创造（2.3） |
| sk-0351 | principle | labor-education | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 7.01 + 先验 2.5 = 9.51） | 自我教育（3.8） |
| sk-0352 | quote | labor-education, collective-education | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 2.33 + 先验 2.5 = 4.83） | 思维与智力（4.0） |
| sk-0353 | quote | teacher-growth, love-education | A4 自我教育 | 旧标签先验 + 文本证据（关键词 4.34 + 先验 1.0 = 5.34） | （除建议条目外无其他关键词命中） |
| sk-0354 | method | labor-education | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 15.81 + 先验 2.5 = 18.31） | 健康与作息（4.8） · 评价与分数（4.2） |
| sk-0355 | quote | labor-education | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 5.31 + 先验 2.5 = 7.81） | 幸福与精神生活（3.4） |
| sk-0356 | principle | child-study, reading-and-books | A4 自我教育 | 旧标签先验 + 文本证据（关键词 14.70 + 先验 1.0 = 15.70） | 全面发展与个性（4.4） · 了解儿童（3.4） |
| sk-0358 | quote | labor-education, family-school | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 2.33 + 先验 2.5 = 4.83） | 公民与祖国（4.0） |
| sk-0359 | quote | thinking-and-nature | A12 自然与思维课 | 旧标签先验 + 文本证据（关键词 9.60 + 先验 1.0 = 10.60） | 思维与智力（3.7） · 了解儿童（3.4） |
| sk-0360 | quote | love-education, collective-education | A2 公民与祖国 | 旧标签先验 + 文本证据（关键词 3.93 + 先验 1.0 = 4.93） | （除建议条目外无其他关键词命中） |
| sk-0361 | quote | love-education, child-study | A17 习惯与纪律 | 文本证据推翻旧标签（关键词 5.84，压过旧标签项 2.99） | 道德判断与品德培养（3.0） |
| sk-0362 | quote | love-education | A4 自我教育 | 文本证据推翻旧标签（关键词 8.24，压过旧标签项 4.43） | 全面发展与个性（4.4） · 幸福与精神生活（3.3） |
| sk-0363 | quote | child-study, love-education | A19 道德判断与品德培养 | 人工裁定（谈的是对邪恶不妥协的**道德判断**，不是「怎么了解儿童」（外部评审意见）） | （除建议条目外无其他关键词命中） |
| sk-0364 | quote | love-education | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 4.90 + 先验 2.5 = 7.40） | 公民与祖国（4.0） · 幸福与精神生活（3.3） |
| sk-0365 | quote | child-study, love-education | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 7.09 + 先验 1.0 = 8.09） | 习惯与纪律（5.0） · 劳动与创造（4.6） |
| sk-0366 | quote | teacher-growth, collective-education | A10 教师 | 旧标签先验 + 文本证据（关键词 9.01 + 先验 2.5 = 11.51） | 劳动与创造（5.3） · 自我教育（3.8） |
| sk-0367 | quote | teacher-growth, child-study | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 9.42 + 先验 1.0 = 10.42） | 自我教育（4.3） · 教师（2.4） |
| sk-0368 | quote | teacher-growth | A10 教师 | 旧标签先验 + 文本证据（关键词 4.83 + 先验 2.5 = 7.33） | （除建议条目外无其他关键词命中） |
| sk-0369 | quote | teacher-growth | A15 思维与智力 | 文本证据推翻旧标签（关键词 9.02，压过旧标签项 4.88） | 尊严、爱与信任（4.3） · 集体与同伴（3.2） |
| sk-0370 | quote | reading-and-books | A15 思维与智力 | 文本证据推翻旧标签（关键词 7.49，压过旧标签项 6.46） | 阅读与书籍（4.0） · 劳动与创造（2.3） |
| sk-0371 | quote | health-first | A7 健康与作息 | 旧标签先验 + 文本证据（关键词 4.80 + 先验 2.5 = 7.30） | 评价与分数（5.8） · 自我教育（4.4） |
| sk-0372 | quote | love-education | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 13.35 + 先验 2.5 = 15.85） | 道德判断与品德培养（9.1） · 幸福与精神生活（6.3） |
| sk-0373 | quote | child-study, thinking-and-nature | A1 全面发展与个性 | 文本证据推翻旧标签（关键词 5.06，压过旧标签项 3.82） | 自我教育（3.8） · 劳动与创造（2.3） |
| sk-0374 | quote | labor-education | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 9.18 + 先验 2.5 = 11.68） | （除建议条目外无其他关键词命中） |
| sk-0375 | quote | aesthetic-nature-education | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 2.98 + 先验 1.0 = 3.98） | 道德判断与品德培养（3.0） |
| sk-0376 | quote | teacher-growth | A10 教师 | 旧标签先验 + 文本证据（关键词 7.21 + 先验 2.5 = 9.71） | 全面发展与个性（4.4） · 自我教育（3.8） |
| sk-0377 | principle | child-study, thinking-and-nature | A6 了解儿童 | 旧标签先验 + 文本证据（关键词 3.37 + 先验 2.5 = 5.87） | 劳动与创造（5.3） · 思维与智力（3.4） |
| sk-0378 | principle | health-first | A7 健康与作息 | 旧标签先验 + 文本证据（关键词 4.14 + 先验 2.5 = 6.64） | 劳动与创造（2.3） |
| sk-0379 | principle | reading-and-books, aesthetic-nature-education | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 6.83 + 先验 2.5 = 9.33） | 美与艺术（4.5） |
| sk-0380 | quote | health-first, teacher-growth | A10 教师 | 旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88） | 尊严、爱与信任（4.7） · 思维与智力（4.0） · 幸福与精神生活（3.0） |
| sk-0381 | principle | aesthetic-nature-education, child-study | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 6.65 + 先验 1.0 = 7.65） | （除建议条目外无其他关键词命中） |
| sk-0382 | principle | labor-education, collective-education | A1 全面发展与个性 | 文本证据推翻旧标签（关键词 11.01，压过旧标签项 7.81） | 劳动与创造（5.3） · 公民与祖国（4.0） |
| sk-0383 | quote | collective-education, child-study | A2 公民与祖国 | 旧标签先验 + 文本证据（关键词 9.72 + 先验 1.0 = 10.72） | （除建议条目外无其他关键词命中） |
| sk-0384 | quote | love-education, child-study | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 6.77 + 先验 1.0 = 7.77） | 集体与同伴（5.4） · 尊严、爱与信任（4.6） |
| sk-0385 | quote | labor-education, collective-education | A4 自我教育 | 文本证据推翻旧标签（关键词 9.75，压过旧标签项 7.04） | 公民与祖国（6.0） · 集体与同伴（3.2） |
| sk-0386 | quote | collective-education, child-study | A2 公民与祖国 | 旧标签先验 + 文本证据（关键词 6.85 + 先验 1.0 = 7.85） | 美与艺术（4.2） · 自我教育（3.8） |
| sk-0387 | quote | family-school, love-education | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 11.83 + 先验 2.5 = 14.33） | 劳动与创造（7.0） · 习惯与纪律（4.8） |
| sk-0388 | quote | love-education, collective-education | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 4.23 + 先验 2.5 = 6.73） | 全面发展与个性（6.6） · 评价与分数（4.2） |
| sk-0389 | quote | love-education | A11 劳动与创造 | 文本证据推翻旧标签（关键词 7.57，压过旧标签项 4.42） | 思维与智力（4.1） · 幸福与精神生活（3.4） |
| sk-0390 | quote | teacher-growth, reading-and-books | A15 思维与智力 | 文本证据推翻旧标签（关键词 10.33，压过旧标签项 6.04） | 检查知识与考查（6.0） · 美与艺术（4.5） |
| sk-0391 | quote | child-study, thinking-and-nature | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 7.04 + 先验 2.5 = 9.54） | 美与艺术（4.2） · 了解儿童（3.4） |
| sk-0392 | quote | aesthetic-nature-education, child-study | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 10.64 + 先验 1.0 = 11.64） | 自我教育（4.3） · 尊严、爱与信任（4.2） |
| sk-0393 | quote | assessment-grading, child-study | A16 评价与分数 | 旧标签先验 + 文本证据（关键词 9.51 + 先验 2.5 = 12.01） | 健康与作息（4.3） · 幸福与精神生活（4.0） |
| sk-0394 | quote | love-education, aesthetic-nature-education | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 6.29 + 先验 1.0 = 7.29） | 公民与祖国（5.3） · 思维与智力（4.1） |
| sk-0395 | quote | collective-education, teacher-growth | A9 集体与同伴 | 旧标签先验 + 文本证据（关键词 3.16 + 先验 2.5 = 5.66） | 全面发展与个性（4.4） |
| sk-0396 | quote | child-study, health-first | A3 幸福与精神生活 | 文本证据推翻旧标签（关键词 3.97，压过旧标签项 2.50） | （除建议条目外无其他关键词命中） |
| sk-0397 | quote | child-study, teacher-growth | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 4.90 + 先验 1.0 = 5.90） | 美与艺术（4.2） · 道德判断与品德培养（3.0） |
| sk-0398 | quote | thinking-and-nature, child-study | A6 了解儿童 | 旧标签先验 + 文本证据（关键词 3.80 + 先验 2.5 = 6.30） | 自然与思维课（4.1） |
| sk-0399 | quote | labor-education, collective-education | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 7.01 + 先验 2.5 = 9.51） | 美与艺术（4.5） · 集体与同伴（3.2） |
| sk-0400 | quote | love-education, collective-education | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 4.90 + 先验 2.5 = 7.40） | 集体与同伴（3.2） · 道德判断与品德培养（3.0） |
| sk-0401 | quote | child-study, learning-difficulties | A6 了解儿童 | 旧标签先验 + 文本证据（关键词 6.85 + 先验 2.5 = 9.35） | 幸福与精神生活（4.0） · 教师（2.4） |
| sk-0402 | quote | learning-difficulties, reading-and-books | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 11.40 + 先验 2.5 = 13.90） | 学习困难学生（11.5） · 思维与智力（10.8） |
| sk-0403 | quote | learning-difficulties, teacher-growth | A6 了解儿童 | 旧标签先验 + 文本证据（关键词 3.80 + 先验 2.5 = 6.30） | 检查知识与考查（5.6） · 劳动与创造（5.3） · 思维与智力（4.1） |
| sk-0404 | quote | child-study, health-first | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 7.83 + 先验 1.0 = 8.83） | 教师（6.8） · 全面发展与个性（5.0） |
| sk-0405 | quote | health-first, learning-difficulties | A7 健康与作息 | 旧标签先验 + 文本证据（关键词 9.49 + 先验 2.5 = 11.99） | 劳动与创造（5.3） · 习惯与纪律（4.8） |
| sk-0406 | quote | teacher-growth, reading-and-books | A15 思维与智力 | 文本证据推翻旧标签（关键词 10.33，压过旧标签项 9.60） | 阅读与书籍（7.1） · 健康与作息（4.1） |
| sk-0407 | quote | labor-education | A1 全面发展与个性 | 文本证据推翻旧标签（关键词 14.59，压过旧标签项 4.83） | 幸福与精神生活（3.8） · 集体与同伴（3.2） |
| sk-0408 | quote | family-school, reading-and-books | A8 家庭与母亲 | 旧标签先验 + 文本证据（关键词 10.07 + 先验 2.5 = 12.57） | 阅读与书籍（7.4） · 思维与智力（5.7） |
| sk-0409 | practice | health-first | A7 健康与作息 | 旧标签先验 + 文本证据（关键词 4.14 + 先验 2.5 = 6.64） | 自然与思维课（4.2） · 家庭与母亲（4.1） |
| sk-0410 | principle | love-education, collective-education | A19 道德判断与品德培养 | 文本证据推翻旧标签（关键词 8.39，压过旧标签项 2.50） | （除建议条目外无其他关键词命中） |
| sk-0411 | quote | labor-education | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 2.33 + 先验 2.5 = 4.83） | 教师（2.4） |
| sk-0412 | quote | reading-and-books, thinking-and-nature | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 11.40 + 先验 2.5 = 13.90） | 思维与智力（7.0） |
| sk-0413 | quote | teacher-growth, family-school | A8 家庭与母亲 | 旧标签先验 + 文本证据（关键词 4.14 + 先验 2.5 = 6.64） | 尊严、爱与信任（4.2） · 阅读与书籍（2.9） |
| sk-0414 | quote | aesthetic-nature-education | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 6.29 + 先验 1.0 = 7.29） | 美与艺术（4.5） · 健康与作息（4.3） |
| sk-0415 | quote | thinking-and-nature, aesthetic-nature-education | A12 自然与思维课 | 旧标签先验 + 文本证据（关键词 4.14 + 先验 1.0 = 5.14） | 劳动与创造（2.3） |
| sk-0416 | quote | child-study, love-education | A4 自我教育 | 文本证据推翻旧标签（关键词 5.84，压过旧标签项 5.05） | 公民与祖国（4.0） · 思维与智力（3.3） |
| sk-0417 | quote | aesthetic-nature-education, child-study | A1 全面发展与个性 | 文本证据推翻旧标签（关键词 4.38，压过旧标签项 2.98） | 劳动与创造（3.0） |
| sk-0418 | quote | aesthetic-nature-education, thinking-and-nature | A14 美与艺术 | 旧标签先验 + 文本证据（关键词 10.38 + 先验 2.5 = 12.88） | 自然与思维课（8.3） · 幸福与精神生活（3.7） |
| sk-0419 | quote | child-study, thinking-and-nature | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 8.37 + 先验 2.5 = 10.87） | 美与艺术（4.2） · 了解儿童（3.4） |
| sk-0420 | quote | labor-education, love-education | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 3.97 + 先验 1.0 = 4.97） | 道德判断与品德培养（3.0） · 劳动与创造（2.3） |
| sk-0421 | quote | health-first | A7 健康与作息 | 旧标签先验 + 文本证据（关键词 13.23 + 先验 2.5 = 15.73） | （除建议条目外无其他关键词命中） |
| sk-0422 | quote | reading-and-books, child-study | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 9.80 + 先验 2.5 = 12.30） | 了解儿童（3.4） · 幸福与精神生活（3.0） |
| sk-0423 | quote | teacher-growth, child-study | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 4.26 + 先验 1.0 = 5.26） | 健康与作息（4.3） · 幸福与精神生活（4.0） |
| sk-0424 | quote | aesthetic-nature-education, labor-education | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 5.31 + 先验 2.5 = 7.81） | 幸福与精神生活（3.0） |
| sk-0425 | quote | child-study, teacher-growth | A1 全面发展与个性 | 文本证据推翻旧标签（关键词 4.43，压过旧标签项 3.42） | 幸福与精神生活（3.4） · 劳动与创造（3.0） |
| sk-0426 | quote | health-first | A7 健康与作息 | 旧标签先验 + 文本证据（关键词 4.14 + 先验 2.5 = 6.64） | 全面发展与个性（5.2） · 劳动与创造（2.3） |
| sk-0427 | quote | family-school, love-education | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 8.89 + 先验 2.5 = 11.39） | 家庭与母亲（3.5） · 劳动与创造（3.0） |
| sk-0428 | quote | love-education, teacher-growth | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 3.97 + 先验 1.0 = 4.97） | 劳动与创造（3.0） |
| sk-0429 | quote | reading-and-books, learning-difficulties | A6 了解儿童 | 旧标签先验 + 文本证据（关键词 7.17 + 先验 2.5 = 9.67） | 阅读与书籍（2.9） |
| sk-0430 | quote | labor-education | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 2.33 + 先验 2.5 = 4.83） | （除建议条目外无其他关键词命中） |
| sk-0431 | quote | aesthetic-nature-education, labor-education | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 5.31 + 先验 2.5 = 7.81） | 幸福与精神生活（4.0） |
| sk-0432 | quote | thinking-and-nature, child-study | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 3.31 + 先验 2.5 = 5.81） | 教师（2.4） |
| sk-0994 | principle | learning-difficulties, teacher-growth, thinking-and-nature | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 10.82 + 先验 2.5 = 13.32） | 劳动与创造（10.0） · 了解儿童（3.8） |
| sk-0995 | method | learning-difficulties, reading-and-books, child-study | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 11.40 + 先验 2.5 = 13.90） | 思维与智力（10.8） · 学习困难学生（5.7） |
| sk-0996 | principle | reading-and-books, learning-difficulties | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 6.83 + 先验 2.5 = 9.33） | 学习困难学生（12.2） · 思维与智力（7.5） |
| sk-0997 | method | assessment-grading, learning-difficulties, child-study | A16 评价与分数 | 旧标签先验 + 文本证据（关键词 14.36 + 先验 2.5 = 16.86） | 尊严、爱与信任（9.6） · 学习困难学生（5.6） |
| sk-0998 | principle | thinking-and-nature, reading-and-books, learning-difficulties | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 14.50 + 先验 2.5 = 17.00） | 阅读与书籍（4.0） |
| sk-0999 | method | thinking-and-nature, child-study, learning-difficulties | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 7.83 + 先验 2.5 = 10.33） | 幸福与精神生活（7.3） · 自我教育（4.4） |
| sk-1000 | method | teacher-growth, child-study, love-education | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 7.47 + 先验 1.0 = 8.47） | 家庭与母亲（7.6） · 评价与分数（4.8） |
| sk-1001 | method | family-school, child-study, love-education | A16 评价与分数 | 文本证据推翻旧标签（关键词 14.37，压过旧标签项 8.09） | 幸福与精神生活（7.1） · 尊严、爱与信任（4.4） |
| sk-1002 | principle | family-school, love-education, child-study | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 9.71 + 先验 1.0 = 10.71） | 劳动与创造（6.9） · 尊严、爱与信任（4.3） |
| sk-1004 | principle | collective-education, labor-education, child-study | A2 公民与祖国 | 旧标签先验 + 文本证据（关键词 7.98 + 先验 1.0 = 8.98） | 自我教育（4.4） · 道德判断与品德培养（3.0） |
| sk-1005 | principle | child-study, learning-difficulties, teacher-growth | A16 评价与分数 | 文本证据推翻旧标签（关键词 8.93，压过旧标签项 4.88） | 家庭与母亲（3.5） · 思维与智力（3.4） |
| sk-1006 | principle | collective-education, love-education, child-study | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 13.52 + 先验 2.5 = 16.02） | 幸福与精神生活（11.0） · 集体与同伴（6.8） |
| sk-1007 | principle | aesthetic-nature-education, reading-and-books, thinking-and-nature | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 14.49 + 先验 2.5 = 16.99） | 幸福与精神生活（11.0） · 公民与祖国（3.9） |
| sk-1008 | method | reading-and-books, child-study, family-school | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 6.83 + 先验 2.5 = 9.33） | 美与艺术（4.5） · 自我教育（4.3） |
| sk-1009 | principle | health-first, child-study, family-school | A7 健康与作息 | 旧标签先验 + 文本证据（关键词 10.22 + 先验 2.5 = 12.72） | 思维与智力（11.2） · 幸福与精神生活（7.0） |
| sk-1010 | principle | thinking-and-nature, learning-difficulties, teacher-growth | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 3.35 + 先验 2.5 = 5.85） | 评价与分数（4.8） · 教师（2.4） |
| sk-1011 | method | teacher-growth, assessment-grading, child-study | A10 教师 | 旧标签先验 + 文本证据（关键词 7.21 + 先验 2.5 = 9.71） | 思维与智力（7.5） · 阅读与书籍（7.4） |
| sk-1013 | principle | child-study, teacher-growth, love-education | A4 自我教育 | 旧标签先验 + 文本证据（关键词 14.61 + 先验 1.0 = 15.61） | 评价与分数（9.0） · 习惯与纪律（4.9） |
| sk-1014 | principle | teacher-growth, child-study | A10 教师 | 旧标签先验 + 文本证据（关键词 7.21 + 先验 2.5 = 9.71） | 全面发展与个性（5.0） · 思维与智力（3.7） |
| sk-1015 | principle | teacher-growth, labor-education | A1 全面发展与个性 | 文本证据推翻旧标签（关键词 9.44，压过旧标签项 5.87） | 习惯与纪律（4.9） · 幸福与精神生活（3.8） |
| sk-1016 | method | love-education, health-first, child-study | A7 健康与作息 | 旧标签先验 + 文本证据（关键词 4.80 + 先验 2.5 = 7.30） | 自我教育（4.4） · 幸福与精神生活（3.3） |
| sk-1017 | method | health-first, aesthetic-nature-education | A7 健康与作息 | 旧标签先验 + 文本证据（关键词 13.71 + 先验 2.5 = 16.21） | 学习困难学生（16.2） · 习惯与纪律（10.8） |
| sk-1018 | method | teacher-growth, reading-and-books | A15 思维与智力 | 文本证据推翻旧标签（关键词 7.51，压过旧标签项 7.33） | 教师（4.8） |
| sk-1019 | principle | love-education, family-school | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 4.90 + 先验 2.5 = 7.40） | 幸福与精神生活（3.0） |
| sk-1020 | method | teacher-growth, child-study | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 11.52 + 先验 1.0 = 12.52） | 教师（7.2） · 了解儿童（7.2） |
| sk-1021 | method | collective-education, reading-and-books, teacher-growth | A9 集体与同伴 | 旧标签先验 + 文本证据（关键词 3.16 + 先验 2.5 = 5.66） | 检查知识与考查（5.6） · 全面发展与个性（5.1） · 自我教育（4.3） |
| sk-1022 | principle | love-education, child-study, reading-and-books | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 7.10 + 先验 2.5 = 9.60） | 全面发展与个性（5.1） · 尊严、爱与信任（4.4） |
| sk-1023 | principle | teacher-growth, child-study, love-education | A10 教师 | 旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88） | 全面发展与个性（4.4） · 幸福与精神生活（3.8） |
| sk-1024 | principle | teacher-growth, family-school, child-study | A11 劳动与创造 | 文本证据推翻旧标签（关键词 10.71，压过旧标签项 10.21） | 全面发展与个性（10.2） · 美与艺术（8.9） |
| sk-1025 | principle | child-study, reading-and-books, teacher-growth | A6 了解儿童 | 旧标签先验 + 文本证据（关键词 3.80 + 先验 2.5 = 6.30） | 集体与同伴（5.2） · 全面发展与个性（5.0） |
| sk-1026 | principle | teacher-growth, health-first | A7 健康与作息 | 旧标签先验 + 文本证据（关键词 4.14 + 先验 2.5 = 6.64） | 劳动与创造（5.3） · 幸福与精神生活（3.8） |
| sk-1027 | method | teacher-growth, reading-and-books | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 11.40 + 先验 2.5 = 13.90） | 教师（2.4） |
| sk-1028 | principle | thinking-and-nature, child-study | A6 了解儿童 | 旧标签先验 + 文本证据（关键词 3.80 + 先验 2.5 = 6.30） | 幸福与精神生活（3.8） · 集体与同伴（3.2） |
| sk-1029 | method | learning-difficulties, assessment-grading | A20 检查知识与考查 | 文本证据推翻旧标签（关键词 6.16，压过旧标签项 5.28） | 全面发展与个性（5.1） · 健康与作息（4.3） |
| sk-1030 | principle | teacher-growth, love-education | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 4.62 + 先验 2.5 = 7.12） | 劳动与创造（4.6） · 思维与智力（4.1） |
| sk-1031 | principle | health-first, family-school | A7 健康与作息 | 旧标签先验 + 文本证据（关键词 9.49 + 先验 2.5 = 11.99） | 家庭与母亲（7.6） · 检查知识与考查（5.1） |
| sk-1032 | quote | teacher-growth, labor-education, child-study | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 5.31 + 先验 2.5 = 7.81） | 自我教育（4.3） · 美与艺术（4.2） |
| sk-1033 | principle | teacher-growth | A10 教师 | 旧标签先验 + 文本证据（关键词 7.21 + 先验 2.5 = 9.71） | 学习困难学生（6.2） · 劳动与创造（5.3） |
| sk-1034 | principle | love-education, labor-education | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 10.77 + 先验 1.0 = 11.77） | 道德判断与品德培养（10.1） · 习惯与纪律（4.8） |
| sk-1035 | method | learning-difficulties, reading-and-books | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 11.20 + 先验 1.0 = 12.20） | 幸福与精神生活（3.3） · 教师（2.4） |
| sk-1036 | method | assessment-grading, learning-difficulties | A20 检查知识与考查 | 文本证据推翻旧标签（关键词 6.85，压过旧标签项 4.31） | 思维与智力（3.3） · 教师（2.4） |
| sk-1037 | principle | thinking-and-nature, child-study | A20 检查知识与考查 | 文本证据推翻旧标签（关键词 11.25，压过旧标签项 10.38） | 美与艺术（10.4） · 思维与智力（7.5） |
| sk-1038 | principle | love-education, family-school | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 10.64 + 先验 1.0 = 11.64） | 习惯与纪律（4.8） · 尊严、爱与信任（4.4） |
| sk-1039 | method | learning-difficulties, reading-and-books | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 4.14 + 先验 1.0 = 5.14） | 学习困难学生（4.9） · 评价与分数（4.2） |
| sk-1040 | principle | learning-difficulties, thinking-and-nature | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 7.40 + 先验 2.5 = 9.90） | 阅读与书籍（6.8） · 教师（2.4） |
| sk-1041 | principle | thinking-and-nature, child-study | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 11.18 + 先验 2.5 = 13.68） | 阅读与书籍（7.4） · 习惯与纪律（5.0） |
| sk-1043 | method | teacher-growth, learning-difficulties | A12 自然与思维课 | 文本证据推翻旧标签（关键词 11.96，压过旧标签项 9.71） | 教师（7.2） · 全面发展与个性（5.2） |
| sk-1044 | principle | collective-education | A9 集体与同伴 | 旧标签先验 + 文本证据（关键词 12.24 + 先验 2.5 = 14.74） | 思维与智力（13.2） · 阅读与书籍（7.1） |
| sk-1045 | principle | child-study | A6 了解儿童 | 旧标签先验 + 文本证据（关键词 3.80 + 先验 2.5 = 6.30） | 幸福与精神生活（3.3） · 集体与同伴（3.2） |
| sk-1046 | principle | health-first, learning-difficulties | A7 健康与作息 | 旧标签先验 + 文本证据（关键词 9.43 + 先验 2.5 = 11.93） | 习惯与纪律（10.8） · 阅读与书籍（6.8） |
| sk-1047 | method | aesthetic-nature-education | A14 美与艺术 | 旧标签先验 + 文本证据（关键词 18.44 + 先验 2.5 = 20.94） | 思维与智力（12.4） · 自然与思维课（4.2） |
| sk-1048 | practice | family-school | A8 家庭与母亲 | 旧标签先验 + 文本证据（关键词 7.64 + 先验 2.5 = 10.14） | 教师（7.2） |
| sk-1049 | method | learning-difficulties, family-school | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 4.98 + 先验 1.0 = 5.98） | 幸福与精神生活（3.0） · 劳动与创造（2.3） |
| sk-1050 | quote | love-education | A15 思维与智力 | 文本证据推翻旧标签（关键词 7.51，压过旧标签项 4.60） | 劳动与创造（4.6） · 了解儿童（3.4） |
| sk-1051 | practice | reading-and-books, teacher-growth | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 15.63 + 先验 2.5 = 18.13） | 幸福与精神生活（13.9） · 思维与智力（7.5） |
| sk-1052 | principle | learning-difficulties, child-study | A10 教师 | 文本证据推翻旧标签（关键词 7.21，压过旧标签项 5.67） | 学习困难学生（11.8） · 自然与思维课（5.7） |
| sk-1053 | method | teacher-growth, learning-difficulties | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 11.40 + 先验 1.0 = 12.40） | 思维与智力（6.7） · 检查知识与考查（5.6） |
| sk-1054 | principle | teacher-growth, child-study | A16 评价与分数 | 文本证据推翻旧标签（关键词 9.99，压过旧标签项 6.41） | 幸福与精神生活（6.4） · 美与艺术（5.9） |
| sk-1055 | method | reading-and-books, learning-difficulties | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 11.40 + 先验 2.5 = 13.90） | 了解儿童（7.2） · 思维与智力（3.4） |
| sk-1056 | method | family-school, love-education | A8 家庭与母亲 | 旧标签先验 + 文本证据（关键词 7.64 + 先验 2.5 = 10.14） | 评价与分数（4.8） · 自我教育（4.4） |
| sk-1057 | principle | love-education, child-study | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 15.18 + 先验 1.0 = 16.18） | 尊严、爱与信任（4.9） · 健康与作息（4.8） |
| sk-1058 | practice | thinking-and-nature, aesthetic-nature-education | A19 道德判断与品德培养 | 文本证据推翻旧标签（关键词 12.25，压过旧标签项 7.24） | 美与艺术（4.7） · 自然与思维课（4.1） |
| sk-1059 | principle | learning-difficulties, child-study | A6 了解儿童 | 旧标签先验 + 文本证据（关键词 3.80 + 先验 2.5 = 6.30） | 习惯与纪律（4.8） · 美与艺术（4.5） · 自然与思维课（4.1） |
| sk-1060 | method | aesthetic-nature-education | A14 美与艺术 | 旧标签先验 + 文本证据（关键词 8.95 + 先验 2.5 = 11.45） | 幸福与精神生活（6.3） · 尊严、爱与信任（4.2） |
| sk-1061 | principle | collective-education, teacher-growth | A4 自我教育 | 旧标签先验 + 文本证据（关键词 8.77 + 先验 1.0 = 9.77） | 道德判断与品德培养（9.1） · 尊严、爱与信任（4.8） |
| sk-1062 | principle | child-study, thinking-and-nature | A3 幸福与精神生活 | 文本证据推翻旧标签（关键词 10.77，压过旧标签项 2.50） | （除建议条目外无其他关键词命中） |
| sk-1063 | principle | collective-education, love-education | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 14.07 + 先验 1.0 = 15.07） | 自我教育（10.3） · 思维与智力（4.1） |
| sk-1064 | principle | thinking-and-nature, teacher-growth, reading-and-books | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 6.67 + 先验 2.5 = 9.17） | 劳动与创造（5.3） · 道德判断与品德培养（3.0） |
| sk-1065 | principle | love-education, collective-education, labor-education | A2 公民与祖国 | 旧标签先验 + 文本证据（关键词 9.72 + 先验 1.0 = 10.72） | 幸福与精神生活（7.2） · 劳动与创造（7.0） |
| sk-1066 | method | collective-education, teacher-growth, love-education | A9 集体与同伴 | 旧标签先验 + 文本证据（关键词 6.84 + 先验 2.5 = 9.34） | 自我教育（4.4） · 道德判断与品德培养（3.0） |
| sk-1067 | method | learning-difficulties, teacher-growth, child-study | A15 思维与智力 | 人工裁定（标题问「怎样激起求知欲」，正文讲的是**学习动机**（让孩子想到自己的成年）；原文摘录里没有「求知欲」三个字，只有标题有，算法看不见（外部评审意见）） | 家庭与母亲（9.4） · 道德判断与品德培养（3.0） |
| sk-1068 | principle | family-school, teacher-growth, love-education | A8 家庭与母亲 | 旧标签先验 + 文本证据（关键词 13.57 + 先验 2.5 = 16.07） | 幸福与精神生活（3.8） · 教师（2.4） |
| sk-1069 | principle | love-education, reading-and-books, teacher-growth | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 3.31 + 先验 1.0 = 4.31） | 思维与智力（3.3） · 集体与同伴（3.2） |
| sk-1070 | method | teacher-growth, learning-difficulties, thinking-and-nature | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 11.20 + 先验 2.5 = 13.70） | 检查知识与考查（5.1） · 了解儿童（3.8） |
| sk-1071 | method | love-education, teacher-growth, thinking-and-nature | A10 教师 | 旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88） | 道德判断与品德培养（3.0） · 幸福与精神生活（3.0） |
| sk-1072 | principle | love-education, family-school, health-first | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 10.95 + 先验 1.0 = 11.95） | 思维与智力（8.0） · 公民与祖国（5.7） |
| sk-1073 | principle | labor-education, thinking-and-nature, love-education | A1 全面发展与个性 | 文本证据推翻旧标签（关键词 21.22，压过旧标签项 9.99） | 思维与智力（7.5） · 劳动与创造（5.3） |
| sk-1074 | principle | love-education, child-study | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 10.77 + 先验 1.0 = 11.77） | 道德判断与品德培养（10.1） · 集体与同伴（9.1） |
| sk-1075 | principle | collective-education, child-study | A9 集体与同伴 | 旧标签先验 + 文本证据（关键词 14.28 + 先验 2.5 = 16.78） | 全面发展与个性（8.8） · 学习困难学生（6.2） |
| sk-1076 | principle | love-education, child-study | A4 自我教育 | 文本证据推翻旧标签（关键词 9.97，压过旧标签项 7.40） | 健康与作息（5.9） · 尊严、爱与信任（4.9） |
| sk-1077 | method | family-school, love-education | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 6.29 + 先验 1.0 = 7.29） | 全面发展与个性（4.4） · 尊严、爱与信任（4.3） |
| sk-1078 | principle | collective-education, teacher-growth | A11 劳动与创造 | 文本证据推翻旧标签（关键词 10.71，压过旧标签项 9.40） | 全面发展与个性（9.4） · 美与艺术（9.2） |
| sk-1079 | principle | labor-education, thinking-and-nature | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 7.04 + 先验 2.5 = 9.54） | 自我教育（7.5） · 劳动与创造（5.3） |
| sk-1080 | method | child-study, family-school | A6 了解儿童 | 旧标签先验 + 文本证据（关键词 10.50 + 先验 2.5 = 13.00） | 思维与智力（10.4） · 健康与作息（4.1） |
| sk-1081 | practice | labor-education | A17 习惯与纪律 | 旧标签先验 + 文本证据（关键词 9.82 + 先验 1.0 = 10.82） | 公民与祖国（5.7） · 美与艺术（4.7） |
| sk-1082 | principle | thinking-and-nature, teacher-growth | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 4.16 + 先验 2.5 = 6.66） | 幸福与精神生活（6.3） · 劳动与创造（5.4） |
| sk-1083 | method | reading-and-books, learning-difficulties, teacher-growth | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 17.24 + 先验 2.5 = 19.74） | 学习困难学生（11.4） · 思维与智力（11.2） |
| sk-1089 | quote | aesthetic-nature-education, thinking-and-nature, love-education | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 4.68 + 先验 2.5 = 7.18） | 劳动与创造（4.8） · 公民与祖国（4.0） |
| sk-1090 | practice | aesthetic-nature-education, thinking-and-nature, teacher-growth | A12 自然与思维课 | 旧标签先验 + 文本证据（关键词 9.35 + 先验 1.0 = 10.35） | 了解儿童（3.4） |
| sk-1091 | practice | aesthetic-nature-education, thinking-and-nature, teacher-growth | A14 美与艺术 | 旧标签先验 + 文本证据（关键词 4.45 + 先验 2.5 = 6.95） | 自然与思维课（4.2） |
| sk-1092 | practice | aesthetic-nature-education, thinking-and-nature, child-study | A12 自然与思维课 | 旧标签先验 + 文本证据（关键词 4.16 + 先验 1.0 = 5.16） | （除建议条目外无其他关键词命中） |
| sk-1093 | practice | aesthetic-nature-education, thinking-and-nature, love-education | A12 自然与思维课 | 旧标签先验 + 文本证据（关键词 4.16 + 先验 1.0 = 5.16） | （除建议条目外无其他关键词命中） |
| sk-1094 | method | teacher-growth, child-study | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 6.67 + 先验 1.0 = 7.67） | 劳动与创造（5.3） · 教师（2.4） |
| sk-1095 | method | family-school, teacher-growth, labor-education | A8 家庭与母亲 | 旧标签先验 + 文本证据（关键词 15.18 + 先验 2.5 = 17.68） | 阅读与书籍（11.7） · 幸福与精神生活（10.1） |
| sk-1096 | method | learning-difficulties, reading-and-books, child-study | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 10.81 + 先验 1.0 = 11.81） | 阅读与书籍（6.8） |
| sk-1097 | principle | love-education, family-school | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 6.65 + 先验 1.0 = 7.65） | 劳动与创造（4.6） · 道德判断与品德培养（3.0） |
| sk-1098 | principle | child-study, thinking-and-nature | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 11.20 + 先验 2.5 = 13.70） | 了解儿童（7.2） · 评价与分数（4.8） |
| sk-1099 | practice | child-study, labor-education, collective-education | A19 道德判断与品德培养 | 文本证据推翻旧标签（关键词 2.99，压过旧标签项 2.50） | 教师（2.4） |
| sk-1100 | principle | teacher-growth, collective-education | A4 自我教育 | 旧标签先验 + 文本证据（关键词 10.44 + 先验 1.0 = 11.44） | 幸福与精神生活（6.8） · 美与艺术（4.5） |
| sk-1101 | principle | teacher-growth, child-study, reading-and-books | A6 了解儿童 | 旧标签先验 + 文本证据（关键词 3.37 + 先验 2.5 = 5.87） | 检查知识与考查（5.1） · 思维与智力（4.0） |
| sk-1102 | principle | love-education, family-school | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 4.26 + 先验 2.5 = 6.76） | 习惯与纪律（5.0） · 幸福与精神生活（3.3） |
| sk-1103 | principle | love-education, collective-education, child-study | A4 自我教育 | 文本证据推翻旧标签（关键词 14.09，压过旧标签项 9.57） | 评价与分数（9.6） · 习惯与纪律（4.8） |
| sk-1112 | principle | love-education, child-study | A4 自我教育 | 文本证据推翻旧标签（关键词 15.59，压过旧标签项 8.85） | 思维与智力（7.8） · 劳动与创造（5.3） |
| sk-1113 | principle | collective-education, child-study, thinking-and-nature | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 6.67 + 先验 2.5 = 9.17） | 幸福与精神生活（7.1） · 道德判断与品德培养（6.2） |
| sk-1114 | method | teacher-growth, learning-difficulties | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 6.83 + 先验 1.0 = 7.83） | 学习困难学生（11.5） · 思维与智力（4.2） |
| sk-1115 | method | learning-difficulties, thinking-and-nature | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 7.46 + 先验 2.5 = 9.96） | （除建议条目外无其他关键词命中） |
| sk-1116 | method | love-education, family-school | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 10.26 + 先验 1.0 = 11.26） | 家庭与母亲（7.6） · 劳动与创造（5.3） |
| sk-1117 | practice | thinking-and-nature, learning-difficulties, child-study | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 7.04 + 先验 2.5 = 9.54） | 劳动与创造（5.3） · 全面发展与个性（5.2） |
| sk-1118 | principle | love-education, child-study | A4 自我教育 | 文本证据推翻旧标签（关键词 9.75，压过旧标签项 4.74） | 美与艺术（4.7） · 全面发展与个性（4.4） |
| sk-1119 | method | aesthetic-nature-education, labor-education, health-first | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 17.20 + 先验 2.5 = 19.70） | 幸福与精神生活（7.1） · 习惯与纪律（4.8） |
| sk-1120 | method | health-first, child-study, aesthetic-nature-education | A14 美与艺术 | 旧标签先验 + 文本证据（关键词 4.74 + 先验 2.5 = 7.24） | 劳动与创造（5.3） · 习惯与纪律（4.8） |
| sk-1121 | principle | labor-education, child-study, teacher-growth | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 5.31 + 先验 2.5 = 7.81） | 了解儿童（3.8） |
| sk-1132 | method | learning-difficulties, thinking-and-nature, child-study | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 14.50 + 先验 2.5 = 17.00） | 学习困难学生（5.7） · 自然与思维课（4.1） |
| sk-1133 | principle | love-education, child-study, collective-education | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 7.46 + 先验 1.0 = 8.46） | 道德判断与品德培养（5.4） · 劳动与创造（4.8） |
| sk-1134 | method | labor-education, child-study, teacher-growth | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 5.31 + 先验 2.5 = 7.81） | 幸福与精神生活（7.6） · 全面发展与个性（4.4） |
| sk-1135 | method | love-education, collective-education | A19 道德判断与品德培养 | 文本证据推翻旧标签（关键词 2.99，压过旧标签项 2.50） | 教师（2.4） |
| sk-1136 | principle | love-education, aesthetic-nature-education, learning-difficulties | A1 全面发展与个性 | 文本证据推翻旧标签（关键词 4.43，压过旧标签项 4.31） | 自我教育（3.8） · 幸福与精神生活（3.3） |
| sk-1138 | practice | teacher-growth, collective-education | A17 习惯与纪律 | 文本证据推翻旧标签（关键词 10.80，压过旧标签项 9.71） | 教师（7.2） · 健康与作息（5.3） |
| sk-1139 | method | teacher-growth, thinking-and-nature, collective-education | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 11.05 + 先验 2.5 = 13.55） | 自然与思维课（4.1） · 幸福与精神生活（3.3） |
| sk-1140 | principle | collective-education, love-education, child-study | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 9.71 + 先验 1.0 = 10.71） | 学习困难学生（5.8） · 全面发展与个性（4.4） |
| sk-1152 | principle | love-education, collective-education, child-study | A2 公民与祖国 | 旧标签先验 + 文本证据（关键词 7.98 + 先验 1.0 = 8.98） | 道德判断与品德培养（5.4） · 集体与同伴（3.2） |
| sk-1153 | method | teacher-growth, family-school, reading-and-books | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 11.40 + 先验 2.5 = 13.90） | 思维与智力（13.7） · 家庭与母亲（3.5） |
| sk-1154 | method | love-education, teacher-growth, collective-education | A15 思维与智力 | 文本证据推翻旧标签（关键词 8.20，压过旧标签项 6.88） | 尊严、爱与信任（4.4） · 集体与同伴（3.2） |
| sk-1155 | principle | family-school, teacher-growth, love-education | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 7.10 + 先验 1.0 = 8.10） | 自然与思维课（4.1） · 教师（2.4） |
| sk-1156 | principle | labor-education, thinking-and-nature, child-study | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 16.38 + 先验 2.5 = 18.88） | 全面发展与个性（5.0） · 健康与作息（4.8） |
| sk-1158 | principle | child-study, love-education, health-first | A7 健康与作息 | 旧标签先验 + 文本证据（关键词 4.28 + 先验 2.5 = 6.78） | 劳动与创造（5.3） · 公民与祖国（3.9） |
| sk-1159 | principle | thinking-and-nature, labor-education, child-study | A3 幸福与精神生活 | 文本证据推翻旧标签（关键词 11.27，压过旧标签项 8.17） | 思维与智力（5.7） · 全面发展与个性（5.1） |
| sk-1161 | principle | collective-education, family-school, teacher-growth | A9 集体与同伴 | 旧标签先验 + 文本证据（关键词 9.09 + 先验 2.5 = 11.59） | 幸福与精神生活（9.7） · 家庭与母亲（3.5） |
| sk-1162 | principle | reading-and-books, thinking-and-nature, teacher-growth | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 15.50 + 先验 2.5 = 18.00） | 阅读与书籍（11.1） · 集体与同伴（5.2） |
| sk-1163 | principle | thinking-and-nature, learning-difficulties, child-study | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 15.30 + 先验 2.5 = 17.80） | 幸福与精神生活（7.0） · 教师（2.4） |
| sk-1164 | method | reading-and-books, child-study, teacher-growth | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 17.51 + 先验 2.5 = 20.01） | 了解儿童（3.8） · 思维与智力（3.7） |
| sk-1165 | method | learning-difficulties, child-study, labor-education | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 7.16 + 先验 2.5 = 9.66） | 思维与智力（7.5） · 阅读与书籍（6.8） |
| sk-1166 | method | reading-and-books, thinking-and-nature, health-first | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 11.06 + 先验 2.5 = 13.56） | 思维与智力（10.8） · 劳动与创造（5.3） |
| sk-1167 | principle | thinking-and-nature, teacher-growth, collective-education | A12 自然与思维课 | 旧标签先验 + 文本证据（关键词 5.67 + 先验 1.0 = 6.67） | 评价与分数（4.7） · 自我教育（3.8） |
| sk-1168 | principle | love-education, family-school, child-study | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 4.38 + 先验 2.5 = 6.88） | 习惯与纪律（5.8） · 美与艺术（4.5） |
| sk-1169 | principle | love-education, collective-education, family-school | A19 道德判断与品德培养 | 人工裁定（谦虚属于待人分寸/品德培养；纪律只是它的外壳（外部评审建议 A4，据内容改判 A19）） | 习惯与纪律（10.9） · 自我教育（8.8） |
| sk-1170 | quote | love-education, teacher-growth, child-study | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 15.98 + 先验 2.5 = 18.48） | 幸福与精神生活（6.4） · 自我教育（3.8） |
| sk-1171 | principle | love-education, family-school | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 9.07 + 先验 2.5 = 11.57） | 家庭与母亲（3.5） · 道德判断与品德培养（3.0） |
| sk-1172 | principle | learning-difficulties, child-study, assessment-grading | A6 了解儿童 | 旧标签先验 + 文本证据（关键词 13.98 + 先验 2.5 = 16.48） | 学习困难学生（4.9） · 评价与分数（4.2） |
| sk-1173 | method | thinking-and-nature, teacher-growth, child-study | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 7.04 + 先验 2.5 = 9.54） | 阅读与书籍（2.9） · 教师（2.4） |
| sk-1174 | method | labor-education, thinking-and-nature, child-study | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 14.40 + 先验 2.5 = 16.90） | 美与艺术（10.4） · 阅读与书籍（7.4） |
| sk-1175 | method | health-first, child-study, teacher-growth | A7 健康与作息 | 旧标签先验 + 文本证据（关键词 8.42 + 先验 2.5 = 10.92） | 自然与思维课（5.7） · 全面发展与个性（5.0） |
| sk-1176 | principle | labor-education, learning-difficulties, thinking-and-nature | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 14.50 + 先验 2.5 = 17.00） | 劳动与创造（10.1） · 阅读与书籍（7.1） |
| sk-1177 | method | collective-education, teacher-growth | A15 思维与智力 | 文本证据推翻旧标签（关键词 7.36，压过旧标签项 5.66） | 自我教育（4.3） · 美与艺术（4.2） |
| sk-1178 | principle | collective-education, child-study, teacher-growth | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 9.07 + 先验 1.0 = 10.07） | 劳动与创造（5.3） · 全面发展与个性（4.4） |
| sk-1179 | principle | aesthetic-nature-education, family-school, child-study | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 10.08 + 先验 1.0 = 11.08） | 自我教育（8.8） · 思维与智力（6.7） |
| sk-1180 | principle | family-school, love-education, child-study | A19 道德判断与品德培养 | 文本证据推翻旧标签（关键词 9.15，压过旧标签项 7.65） | 幸福与精神生活（6.7） · 习惯与纪律（5.8） |
| sk-1181 | principle | collective-education, labor-education, family-school | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 5.31 + 先验 2.5 = 7.81） | 全面发展与个性（4.4） · 道德判断与品德培养（3.0） |
| sk-1182 | principle | teacher-growth, love-education | A4 自我教育 | 旧标签先验 + 文本证据（关键词 10.28 + 先验 1.0 = 11.28） | 幸福与精神生活（6.8） · 尊严、爱与信任（4.3） |
| sk-1183 | method | health-first, child-study, labor-education | A7 健康与作息 | 旧标签先验 + 文本证据（关键词 8.94 + 先验 2.5 = 11.44） | 自然与思维课（9.8） · 幸福与精神生活（7.1） |
| sk-1184 | principle | love-education, labor-education, family-school | A2 公民与祖国 | 旧标签先验 + 文本证据（关键词 7.14 + 先验 1.0 = 8.14） | 劳动与创造（5.3） · 幸福与精神生活（3.4） |
| sk-1185 | principle | love-education, family-school, collective-education | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 9.53 + 先验 2.5 = 12.03） | 道德判断与品德培养（9.1） · 全面发展与个性（4.4） |
| sk-1186 | principle | love-education, collective-education, child-study | A19 道德判断与品德培养 | 文本证据推翻旧标签（关键词 8.39，压过旧标签项 6.76） | 公民与祖国（5.7） · 习惯与纪律（4.9） |
| sk-1187 | method | love-education, child-study, family-school | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 9.12 + 先验 2.5 = 11.62） | 思维与智力（3.7） |
| sk-1188 | method | family-school, love-education, collective-education | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 11.83 + 先验 1.0 = 12.83） | 习惯与纪律（4.9） · 劳动与创造（4.6） |
| sk-1189 | principle | love-education, family-school, collective-education | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 4.38 + 先验 2.5 = 6.88） | 公民与祖国（4.0） · 幸福与精神生活（3.0） |
| sk-1190 | principle | learning-difficulties, reading-and-books, thinking-and-nature | A3 幸福与精神生活 | 文本证据推翻旧标签（关键词 14.06，压过旧标签项 9.60） | 评价与分数（9.0） · 阅读与书籍（7.1） |
| sk-1191 | principle | love-education, collective-education, labor-education | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 9.71 + 先验 1.0 = 10.71） | 自我教育（4.4） · 尊严、爱与信任（4.2） |
| sk-1192 | method | child-study, health-first, thinking-and-nature | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 7.04 + 先验 2.5 = 9.54） | 劳动与创造（5.3） · 全面发展与个性（5.0） |
| sk-1193 | principle | love-education, family-school | A15 思维与智力 | 文本证据推翻旧标签（关键词 6.67，压过旧标签项 6.00） | 家庭与母亲（3.5） · 幸福与精神生活（3.3） |
| sk-1194 | method | learning-difficulties, thinking-and-nature | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 7.47 + 先验 2.5 = 9.97） | 劳动与创造（7.0） · 评价与分数（4.2） |
| sk-1195 | principle | collective-education, labor-education | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 5.31 + 先验 2.5 = 7.81） | 全面发展与个性（4.4） · 自我教育（4.3） |
| sk-1196 | principle | love-education, family-school | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 4.90 + 先验 2.5 = 7.40） | （除建议条目外无其他关键词命中） |
| sk-1197 | method | love-education, collective-education | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 4.26 + 先验 2.5 = 6.76） | 公民与祖国（5.3） · 了解儿童（3.4） |
| sk-1198 | method | teacher-growth, reading-and-books | A10 教师 | 旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88） | 评价与分数（4.8） · 思维与智力（3.3） |
| sk-1199 | principle | love-education, family-school | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 9.29 + 先验 2.5 = 11.79） | 全面发展与个性（4.4） · 公民与祖国（4.0） |
| sk-1200 | method | teacher-growth, reading-and-books, child-study | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 7.44 + 先验 2.5 = 9.94） | 思维与智力（7.5） · 幸福与精神生活（7.0） |
| sk-1201 | method | child-study, family-school, health-first | A7 健康与作息 | 旧标签先验 + 文本证据（关键词 10.07 + 先验 2.5 = 12.57） | 家庭与母亲（7.6） · 阅读与书籍（7.4） |
| sk-1202 | principle | love-education, reading-and-books | A1 全面发展与个性 | 文本证据推翻旧标签（关键词 8.81，压过旧标签项 7.40） | 尊严、爱与信任（4.9） · 道德判断与品德培养（3.0） |
| sk-1203 | method | labor-education, family-school | A8 家庭与母亲 | 旧标签先验 + 文本证据（关键词 4.14 + 先验 2.5 = 6.64） | 幸福与精神生活（3.0） · 劳动与创造（2.3） |
| sk-1205 | method | family-school, love-education | A7 健康与作息 | 文本证据推翻旧标签（关键词 10.22，压过旧标签项 10.14） | 家庭与母亲（7.6） · 幸福与精神生活（7.1） |
| sk-1206 | method | teacher-growth, collective-education, reading-and-books | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 12.94 + 先验 2.5 = 15.44） | 评价与分数（10.0） · 思维与智力（7.5） |
| sk-1207 | practice | collective-education, assessment-grading | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 9.60 + 先验 1.0 = 10.60） | 学习困难学生（5.7） · 评价与分数（4.7） |
| sk-1208 | principle | teacher-growth, love-education | A2 公民与祖国 | 旧标签先验 + 文本证据（关键词 7.98 + 先验 1.0 = 8.98） | 思维与智力（7.5） · 劳动与创造（5.3） |
| sk-1209 | principle | love-education, family-school | A19 道德判断与品德培养 | 文本证据推翻旧标签（关键词 9.44，压过旧标签项 6.76） | 尊严、爱与信任（4.3） · 幸福与精神生活（3.8） |
| sk-1210 | principle | love-education, teacher-growth | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 6.73 + 先验 1.0 = 7.73） | 劳动与创造（4.7） · 自我教育（4.4） |
| sk-1211 | principle | love-education, teacher-growth | A7 健康与作息 | 文本证据推翻旧标签（关键词 13.23，压过旧标签项 10.71） | 劳动与创造（10.7） · 思维与智力（10.4） |
| sk-1212 | practice | collective-education, teacher-growth | A15 思维与智力 | 人工裁定（「传播知识」= 向他人讲解以加深理解，集体只是场景（外部评审意见）） | （除建议条目外无其他关键词命中） |
| sk-1213 | principle | love-education, child-study | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 10.08 + 先验 1.0 = 11.08） | 尊严、爱与信任（4.9） · 习惯与纪律（4.8） |
| sk-1214 | practice | labor-education, collective-education | A9 集体与同伴 | 旧标签先验 + 文本证据（关键词 9.09 + 先验 2.5 = 11.59） | 劳动与创造（2.3） |
| sk-1215 | practice | family-school, love-education | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 11.50 + 先验 1.0 = 12.50） | 尊严、爱与信任（4.9） · 家庭与母亲（3.5） |
| sk-1216 | principle | collective-education, child-study | A9 集体与同伴 | 旧标签先验 + 文本证据（关键词 8.56 + 先验 2.5 = 11.06） | 评价与分数（9.6） · 学习困难学生（4.9） |
| sk-1217 | principle | teacher-growth, love-education | A10 教师 | 旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88） | 道德判断与品德培养（3.0） · 幸福与精神生活（3.0） |
| sk-1218 | method | teacher-growth | A10 教师 | 旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88） | 思维与智力（3.7） · 集体与同伴（3.2） · 劳动与创造（3.0） |
| sk-1220 | method | teacher-growth, reading-and-books | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 12.67 + 先验 2.5 = 15.17） | 学习困难学生（4.9） · 幸福与精神生活（3.8） |
| sk-1221 | principle | love-education, aesthetic-nature-education | A2 公民与祖国 | 旧标签先验 + 文本证据（关键词 13.32 + 先验 1.0 = 14.32） | 了解儿童（7.2） · 全面发展与个性（5.2） |
| sk-1222 | method | family-school, love-education | A8 家庭与母亲 | 旧标签先验 + 文本证据（关键词 7.64 + 先验 2.5 = 10.14） | 幸福与精神生活（6.4） · 劳动与创造（5.3） |
| sk-1223 | principle | love-education, collective-education, teacher-growth | A2 公民与祖国 | 旧标签先验 + 文本证据（关键词 13.32 + 先验 1.0 = 14.32） | 全面发展与个性（9.5） · 检查知识与考查（5.1） |
| sk-1224 | principle | health-first, love-education, labor-education | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 8.97 + 先验 2.5 = 11.47） | 幸福与精神生活（3.0） · 劳动与创造（2.3） |
| sk-1225 | method | collective-education, love-education | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 10.40 + 先验 1.0 = 11.40） | 尊严、爱与信任（8.5） · 劳动与创造（4.6） |
| sk-1226 | practice | labor-education, collective-education | A5 尊严、爱与信任 | 文本证据推翻旧标签（关键词 9.01，压过旧标签项 5.66） | 教师（4.8） · 评价与分数（4.8） |
| sk-1227 | principle | teacher-growth, child-study | A11 劳动与创造 | 文本证据推翻旧标签（关键词 5.31，压过旧标签项 4.88） | 幸福与精神生活（4.0） · 阅读与书籍（2.9） |
| sk-1228 | method | collective-education, love-education | A9 集体与同伴 | 旧标签先验 + 文本证据（关键词 6.84 + 先验 2.5 = 9.34） | 评价与分数（4.8） · 美与艺术（4.2） |
| sk-1229 | method | love-education, family-school, collective-education | A2 公民与祖国 | 旧标签先验 + 文本证据（关键词 13.32 + 先验 1.0 = 14.32） | 幸福与精神生活（10.6） · 尊严、爱与信任（4.7） |
| sk-1231 | method | collective-education, love-education, teacher-growth | A2 公民与祖国 | 旧标签先验 + 文本证据（关键词 13.32 + 先验 1.0 = 14.32） | 集体与同伴（9.1） · 习惯与纪律（4.9） |
| sk-1232 | method | love-education, teacher-growth, family-school | A2 公民与祖国 | 旧标签先验 + 文本证据（关键词 7.98 + 先验 1.0 = 8.98） | 尊严、爱与信任（4.9） · 全面发展与个性（4.4） |
| sk-1233 | method | love-education, collective-education, teacher-growth | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 11.40 + 先验 1.0 = 12.40） | 公民与祖国（9.3） · 思维与智力（7.4） |
| sk-1234 | principle | love-education, teacher-growth, collective-education | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 13.51 + 先验 1.0 = 14.51） | 劳动与创造（9.9） · 公民与祖国（8.0） |
| sk-1235 | method | collective-education, love-education, teacher-growth | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 9.29 + 先验 2.5 = 11.79） | 劳动与创造（5.3） · 评价与分数（4.8） |
| sk-1236 | method | love-education, teacher-growth, family-school | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 4.90 + 先验 2.5 = 7.40） | 幸福与精神生活（6.3） · 习惯与纪律（5.8） · 集体与同伴（5.4） |
| sk-1237 | principle | collective-education, love-education, teacher-growth | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 11.06 + 先验 1.0 = 12.06） | 自我教育（8.2） · 幸福与精神生活（6.4） |
| sk-1238 | practice | collective-education, love-education, teacher-growth | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 10.75 + 先验 1.0 = 11.75） | 劳动与创造（9.9） · 集体与同伴（9.1） |
| sk-1240 | practice | learning-difficulties, child-study, assessment-grading | A6 了解儿童 | 旧标签先验 + 文本证据（关键词 13.98 + 先验 2.5 = 16.48） | 教师（8.4） · 美与艺术（4.2） |
| sk-1241 | principle | assessment-grading, teacher-growth, love-education | A16 评价与分数 | 旧标签先验 + 文本证据（关键词 14.36 + 先验 2.5 = 16.86） | 尊严、爱与信任（9.6） · 幸福与精神生活（7.1） |
| sk-1242 | practice | assessment-grading, learning-difficulties, teacher-growth | A16 评价与分数 | 旧标签先验 + 文本证据（关键词 5.46 + 先验 2.5 = 7.96） | 检查知识与考查（6.8） · 习惯与纪律（4.8） |
| sk-1245 | practice | learning-difficulties, reading-and-books, teacher-growth | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 18.62 + 先验 1.0 = 19.62） | 学习困难学生（4.9） · 评价与分数（4.2） |
| sk-1246 | principle | teacher-growth, learning-difficulties, collective-education | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 11.06 + 先验 1.0 = 12.06） | 思维与智力（10.8） · 全面发展与个性（5.2） |
| sk-1247 | principle | collective-education, love-education, teacher-growth | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 13.79 + 先验 2.5 = 16.29） | 集体与同伴（6.8） · 评价与分数（4.8） |
| sk-1248 | method | family-school, love-education, child-study | A7 健康与作息 | 文本证据推翻旧标签（关键词 15.53，压过旧标签项 12.00） | 习惯与纪律（12.0） · 思维与智力（10.7） |
| sk-1249 | practice | family-school, love-education, labor-education | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 5.31 + 先验 2.5 = 7.81） | 幸福与精神生活（6.4） · 自我教育（5.8） |
| sk-1252 | method | assessment-grading, teacher-growth | A20 检查知识与考查 | 文本证据推翻旧标签（关键词 12.48，压过旧标签项 7.83） | 阅读与书籍（6.8） · 劳动与创造（5.3） |
| sk-1253 | practice | reading-and-books, thinking-and-nature, learning-difficulties | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 11.40 + 先验 2.5 = 13.90） | 思维与智力（10.4） · 检查知识与考查（5.1） |
| sk-1254 | method | thinking-and-nature, learning-difficulties, teacher-growth | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 11.16 + 先验 2.5 = 13.66） | 学习困难学生（12.2） · 美与艺术（4.2） |
| sk-1255 | method | learning-difficulties, teacher-growth, health-first | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 11.06 + 先验 1.0 = 12.06） | 劳动与创造（10.0） · 自我教育（8.8） |
| sk-1256 | practice | family-school, reading-and-books, love-education | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 8.71 + 先验 2.5 = 11.21） | 幸福与精神生活（7.5） · 公民与祖国（3.9） |
| sk-1257 | practice | collective-education, love-education, teacher-growth | A2 公民与祖国 | 旧标签先验 + 文本证据（关键词 13.32 + 先验 1.0 = 14.32） | 幸福与精神生活（10.3） · 自我教育（8.2） |
| sk-1258 | principle | collective-education, love-education, teacher-growth | A2 公民与祖国 | 旧标签先验 + 文本证据（关键词 12.89 + 先验 1.0 = 13.89） | 劳动与创造（5.3） · 自我教育（3.8） |
| sk-1259 | principle | love-education, child-study, teacher-growth | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 13.41 + 先验 2.5 = 15.91） | 幸福与精神生活（6.7） · 习惯与纪律（5.8） |
| sk-1260 | method | love-education, collective-education, family-school | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 12.88 + 先验 2.5 = 15.38） | 集体与同伴（12.3） · 幸福与精神生活（6.7） |
| sk-1261 | method | love-education, family-school, labor-education | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 13.95 + 先验 1.0 = 14.95） | 尊严、爱与信任（9.6） · 全面发展与个性（4.4） |
| sk-1262 | principle | aesthetic-nature-education, love-education, labor-education | A1 全面发展与个性 | 文本证据推翻旧标签（关键词 9.44，压过旧标签项 7.81） | 劳动与创造（5.3） · 自我教育（4.4） |
| sk-1264 | method | learning-difficulties, child-study, teacher-growth | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 14.50 + 先验 1.0 = 15.50） | 劳动与创造（14.2） · 自然与思维课（10.7） |
| sk-1265 | method | learning-difficulties, reading-and-books, teacher-growth | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 17.24 + 先验 2.5 = 19.74） | 学习困难学生（17.1） · 健康与作息（10.7） |
| sk-1266 | method | learning-difficulties, health-first, teacher-growth | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 10.81 + 先验 1.0 = 11.81） | 劳动与创造（5.3） · 全面发展与个性（5.2） |
| sk-1267 | method | love-education, collective-education, teacher-growth | A2 公民与祖国 | 旧标签先验 + 文本证据（关键词 9.39 + 先验 1.0 = 10.39） | 评价与分数（8.9） · 尊严、爱与信任（4.8） |
| sk-1268 | method | collective-education, teacher-growth, love-education | A16 评价与分数 | 文本证据推翻旧标签（关键词 16.10，压过旧标签项 9.34） | 自我教育（8.2） · 集体与同伴（6.8） |
| sk-1269 | method | love-education, teacher-growth, child-study | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 11.39 + 先验 1.0 = 12.39） | 劳动与创造（5.4） · 尊严、爱与信任（4.9） |
| sk-1270 | method | love-education, aesthetic-nature-education, child-study | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 22.47 + 先验 1.0 = 23.47） | 劳动与创造（5.3） · 健康与作息（4.3） |
| sk-1271 | method | teacher-growth, love-education, child-study | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 8.71 + 先验 1.0 = 9.71） | 检查知识与考查（6.0） · 尊严、爱与信任（4.7） |
| sk-1272 | method | teacher-growth, love-education, collective-education | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 14.09 + 先验 2.5 = 16.59） | 评价与分数（10.2） · 了解儿童（7.1） |
| sk-1273 | method | child-study, love-education, labor-education | A12 自然与思维课 | 文本证据推翻旧标签（关键词 11.01，压过旧标签项 9.67） | 思维与智力（7.8） · 了解儿童（7.2） |
| sk-1274 | practice | child-study, labor-education, collective-education | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 7.93 + 先验 2.5 = 10.43） | 了解儿童（3.8） · 集体与同伴（3.7） |
| sk-1275 | method | child-study, health-first, family-school | A7 健康与作息 | 旧标签先验 + 文本证据（关键词 8.42 + 先验 2.5 = 10.92） | 思维与智力（7.5） · 学习困难学生（5.7） |
| sk-1279 | practice | aesthetic-nature-education, thinking-and-nature, health-first | A12 自然与思维课 | 旧标签先验 + 文本证据（关键词 30.29 + 先验 1.0 = 31.29） | 集体与同伴（6.8） · 健康与作息（6.4） |
| sk-1280 | practice | family-school, love-education, collective-education | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 13.63 + 先验 2.5 = 16.13） | 幸福与精神生活（10.1） · 美与艺术（4.7） |
| sk-1281 | practice | family-school, love-education, child-study | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 10.40 + 先验 1.0 = 11.40） | 家庭与母亲（7.6） · 评价与分数（4.8） |
| sk-1282 | method | labor-education, child-study, love-education | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 15.39 + 先验 2.5 = 17.89） | 评价与分数（4.8） · 全面发展与个性（4.4） |
| sk-1283 | practice | love-education, family-school, collective-education | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 8.65 + 先验 2.5 = 11.15） | 劳动与创造（10.0） · 幸福与精神生活（9.7） |
| sk-1284 | method | learning-difficulties, teacher-growth, child-study | A10 教师 | 旧标签先验 + 文本证据（关键词 8.42 + 先验 2.5 = 10.92） | 学习困难学生（17.2） · 评价与分数（8.9） |
| sk-1285 | method | labor-education, thinking-and-nature, teacher-growth | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 11.20 + 先验 2.5 = 13.70） | 自然与思维课（11.0） · 全面发展与个性（5.1） |
| sk-1286 | method | teacher-growth, collective-education, family-school | A10 教师 | 旧标签先验 + 文本证据（关键词 7.21 + 先验 2.5 = 9.71） | 习惯与纪律（4.9） · 评价与分数（4.8） |
| sk-1287 | practice | labor-education, child-study, love-education | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 9.90 + 先验 2.5 = 12.40） | 全面发展与个性（5.0） · 思维与智力（3.4） |
| sk-1288 | method | teacher-growth, love-education, child-study | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 7.36 + 先验 1.0 = 8.36） | 幸福与精神生活（6.7） · 尊严、爱与信任（4.6） |
| sk-1289 | principle | love-education, child-study, health-first | A4 自我教育 | 文本证据推翻旧标签（关键词 40.23，压过旧标签项 4.99） | 评价与分数（4.8） · 全面发展与个性（4.4） |
| sk-1290 | method | love-education, collective-education, teacher-growth | A16 评价与分数 | 文本证据推翻旧标签（关键词 10.26，压过旧标签项 7.14） | 习惯与纪律（7.1） · 道德判断与品德培养（5.4） |
| sk-1291 | practice | love-education, labor-education, family-school | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 9.90 + 先验 2.5 = 12.40） | 幸福与精神生活（11.1） · 尊严、爱与信任（8.5） |
| sk-1292 | method | reading-and-books, thinking-and-nature, teacher-growth | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 11.06 + 先验 2.5 = 13.56） | 思维与智力（7.5） · 自然与思维课（5.2） |
| sk-1293 | method | teacher-growth, love-education, child-study | A10 教师 | 旧标签先验 + 文本证据（关键词 7.21 + 先验 2.5 = 9.71） | 幸福与精神生活（6.8） · 习惯与纪律（4.8） |
| sk-1295 | practice | love-education, collective-education, child-study | A9 集体与同伴 | 旧标签先验 + 文本证据（关键词 6.84 + 先验 2.5 = 9.34） | 劳动与创造（7.8） · 幸福与精神生活（7.0） |
| sk-1296 | practice | family-school, love-education, child-study | A8 家庭与母亲 | 旧标签先验 + 文本证据（关键词 7.64 + 先验 2.5 = 10.14） | 劳动与创造（10.0） · 幸福与精神生活（6.7） |
| sk-1297 | method | love-education, child-study, collective-education | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 11.50 + 先验 1.0 = 12.50） | 尊严、爱与信任（9.7） · 习惯与纪律（5.8） |
| sk-1298 | practice | reading-and-books, love-education, aesthetic-nature-education | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 15.63 + 先验 2.5 = 18.13） | 幸福与精神生活（10.1） · 美与艺术（8.7） |
| sk-1299 | method | reading-and-books, child-study, family-school | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 20.17 + 先验 1.0 = 21.17） | 阅读与书籍（15.6） · 了解儿童（6.6） |
| sk-1300 | practice | aesthetic-nature-education, labor-education, thinking-and-nature | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 16.99 + 先验 2.5 = 19.49） | 思维与智力（7.5） · 全面发展与个性（5.1） |
| sk-1301 | method | labor-education, love-education, child-study | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 11.99 + 先验 1.0 = 12.99） | 劳动与创造（7.8） · 阅读与书籍（6.8） |
| sk-1302 | method | teacher-growth, love-education, family-school | A4 自我教育 | 旧标签先验 + 文本证据（关键词 10.58 + 先验 1.0 = 11.58） | 劳动与创造（7.0） · 健康与作息（4.8） |
| sk-1303 | practice | family-school, love-education, labor-education | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 12.47 + 先验 2.5 = 14.97） | 幸福与精神生活（6.4） · 家庭与母亲（4.1） |
| sk-1304 | method | teacher-growth, love-education, collective-education | A15 思维与智力 | 文本证据推翻旧标签（关键词 11.50，压过旧标签项 10.92） | 教师（8.4） · 幸福与精神生活（6.3） |
| sk-1305 | method | teacher-growth, collective-education, love-education | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 15.63 + 先验 1.0 = 16.63） | 自我教育（6.4） · 幸福与精神生活（6.3） |
| sk-1306 | method | love-education, teacher-growth, child-study | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 10.28 + 先验 1.0 = 11.28） | 美与艺术（4.5） · 思维与智力（4.0） |
| sk-1307 | practice | family-school, child-study, love-education | A6 了解儿童 | 旧标签先验 + 文本证据（关键词 3.37 + 先验 2.5 = 5.87） | 习惯与纪律（5.0） · 集体与同伴（3.7） |
| sk-1308 | method | teacher-growth, love-education, child-study | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 14.68 + 先验 2.5 = 17.18） | 幸福与精神生活（10.2） · 评价与分数（8.9） |
| sk-1309 | practice | family-school, love-education, child-study | A2 公民与祖国 | 旧标签先验 + 文本证据（关键词 7.14 + 先验 1.0 = 8.14） | 幸福与精神生活（6.4） · 劳动与创造（5.3） |
| sk-1310 | practice | family-school, love-education, labor-education | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 10.77 + 先验 2.5 = 13.27） | 家庭与母亲（9.4） · 检查知识与考查（5.1） |
| sk-1311 | method | teacher-growth, family-school, love-education | A2 公民与祖国 | 旧标签先验 + 文本证据（关键词 9.39 + 先验 1.0 = 10.39） | 评价与分数（4.8） · 全面发展与个性（4.4） |
| sk-1313 | practice | love-education, collective-education, child-study | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 14.09 + 先验 2.5 = 16.59） | 自我教育（4.3） · 公民与祖国（3.9） |
| sk-1315 | method | love-education, family-school, child-study | A11 劳动与创造 | 文本证据推翻旧标签（关键词 7.57，压过旧标签项 6.76） | 自我教育（6.2） · 集体与同伴（5.4） |
| sk-1316 | practice | family-school, love-education, child-study | A7 健康与作息 | 文本证据推翻旧标签（关键词 10.22，压过旧标签项 10.14） | 家庭与母亲（7.6） · 阅读与书籍（7.4） |
| sk-1317 | method | learning-difficulties, teacher-growth, assessment-grading | A16 评价与分数 | 旧标签先验 + 文本证据（关键词 4.16 + 先验 2.5 = 6.66） | 学习困难学生（4.9） · 集体与同伴（3.7） |
| sk-1318 | method | learning-difficulties, reading-and-books, teacher-growth | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 12.67 + 先验 2.5 = 15.17） | 思维与智力（3.3） · 教师（2.4） |
| sk-1321 | practice | learning-difficulties, assessment-grading, teacher-growth | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 7.51 + 先验 1.0 = 8.51） | 劳动与创造（7.9） · 检查知识与考查（6.2） |
| sk-1323 | method | health-first, teacher-growth, child-study | A7 健康与作息 | 旧标签先验 + 文本证据（关键词 14.36 + 先验 2.5 = 16.86） | 尊严、爱与信任（13.8） · 幸福与精神生活（10.0） |
| sk-1327 | principle | love-education, teacher-growth, child-study | A19 道德判断与品德培养 | 文本证据推翻旧标签（关键词 9.44，压过旧标签项 8.90） | 评价与分数（8.9） · 集体与同伴（8.9） |
| sk-1328 | practice | teacher-growth, reading-and-books, collective-education | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 6.83 + 先验 2.5 = 9.33） | 集体与同伴（5.2） · 全面发展与个性（4.4） |
| sk-1329 | practice | love-education, family-school, child-study | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 17.18 + 先验 1.0 = 18.18） | 尊严、爱与信任（13.2） · 思维与智力（4.2） |
| sk-1330 | method | love-education, family-school, child-study | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 4.26 + 先验 2.5 = 6.76） | 公民与祖国（4.0） · 家庭与母亲（3.5） |
| sk-1331 | principle | love-education, child-study, teacher-growth | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 13.97 + 先验 2.5 = 16.47） | 思维与智力（11.2） · 劳动与创造（9.9） |
| sk-1332 | method | child-study, love-education, collective-education | A4 自我教育 | 文本证据推翻旧标签（关键词 14.61，压过旧标签项 9.34） | 劳动与创造（7.0） · 集体与同伴（6.8） |
| sk-1334 | method | family-school, love-education, teacher-growth | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 4.74 + 先验 2.5 = 7.24） | 幸福与精神生活（3.4） · 思维与智力（3.3） |
| sk-1335 | practice | learning-difficulties, teacher-growth, thinking-and-nature | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 7.47 + 先验 2.5 = 9.97） | 检查知识与考查（6.2） · 评价与分数（4.2） |
| sk-1336 | practice | health-first, child-study, love-education | A7 健康与作息 | 旧标签先验 + 文本证据（关键词 20.68 + 先验 2.5 = 23.18） | 自然与思维课（14.0） · 劳动与创造（7.9） |
| sk-1337 | practice | learning-difficulties, reading-and-books, teacher-growth | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 10.71 + 先验 1.0 = 11.71） | 幸福与精神生活（7.1） · 学习困难学生（5.7） |
| sk-1338 | method | thinking-and-nature, learning-difficulties, child-study | A12 自然与思维课 | 旧标签先验 + 文本证据（关键词 9.81 + 先验 1.0 = 10.81） | 美与艺术（10.4） · 思维与智力（7.5） |
| sk-1339 | practice | reading-and-books, learning-difficulties, teacher-growth | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 6.83 + 先验 2.5 = 9.33） | 学习困难学生（12.2） · 思维与智力（7.5） |
| sk-1341 | practice | learning-difficulties, thinking-and-nature, teacher-growth | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 11.40 + 先验 1.0 = 12.40） | 评价与分数（8.9） · 集体与同伴（8.4） |
| sk-1342 | method | child-study, thinking-and-nature, teacher-growth | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 14.52 + 先验 2.5 = 17.02） | 阅读与书籍（7.1） · 美与艺术（4.2） |
| sk-1343 | practice | family-school, teacher-growth, child-study | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 7.10 + 先验 1.0 = 8.10） | 尊严、爱与信任（4.3） · 自然与思维课（4.1） |
| sk-1344 | practice | family-school, teacher-growth, collective-education | A13 阅读与书籍 | 旧标签先验 + 文本证据（关键词 7.44 + 先验 1.0 = 8.44） | 思维与智力（7.5） · 美与艺术（4.7） |
| sk-1345 | practice | assessment-grading, family-school, teacher-growth | A16 评价与分数 | 旧标签先验 + 文本证据（关键词 14.36 + 先验 2.5 = 16.86） | 幸福与精神生活（11.3） · 学习困难学生（10.5） |
| sk-1347 | practice | collective-education, child-study, love-education | A14 美与艺术 | 文本证据推翻旧标签（关键词 13.40，压过旧标签项 11.40） | 阅读与书籍（11.4） · 劳动与创造（10.7） |
| sk-1348 | practice | collective-education, love-education, teacher-growth | A2 公民与祖国 | 旧标签先验 + 文本证据（关键词 7.98 + 先验 1.0 = 8.98） | 思维与智力（8.2） · 幸福与精神生活（7.0） |
| sk-1349 | practice | collective-education, teacher-growth, child-study | A9 集体与同伴 | 旧标签先验 + 文本证据（关键词 6.84 + 先验 2.5 = 9.34） | 劳动与创造（5.3） · 全面发展与个性（4.4） |
| sk-1350 | practice | collective-education, teacher-growth, love-education | A9 集体与同伴 | 旧标签先验 + 文本证据（关键词 8.56 + 先验 2.5 = 11.06） | 家庭与母亲（7.6） · 习惯与纪律（5.0） |
| sk-1351 | practice | teacher-growth, love-education, child-study | A4 自我教育 | 旧标签先验 + 文本证据（关键词 10.58 + 先验 1.0 = 11.58） | 劳动与创造（10.0） · 尊严、爱与信任（4.6） |
| sk-1352 | method | love-education, family-school, child-study | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 6.65 + 先验 1.0 = 7.65） | 习惯与纪律（5.8） · 劳动与创造（4.6） |
| sk-1353 | practice | family-school, love-education, child-study | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 14.62 + 先验 2.5 = 17.12） | 幸福与精神生活（6.7） · 习惯与纪律（4.8） |
| sk-1354 | practice | love-education, family-school, collective-education | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 8.08 + 先验 1.0 = 9.08） | 检查知识与考查（6.2） · 尊严、爱与信任（4.9） |
| sk-1355 | method | teacher-growth, love-education, child-study | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 6.41 + 先验 1.0 = 7.41） | 自我教育（6.2） · 全面发展与个性（4.4） |
| sk-1357 | practice | love-education, child-study, family-school | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 10.08 + 先验 1.0 = 11.08） | 劳动与创造（6.9） · 思维与智力（6.7） |
| sk-1358 | practice | child-study, thinking-and-nature, teacher-growth | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 10.81 + 先验 2.5 = 13.31） | 幸福与精神生活（10.9） · 阅读与书籍（8.7） |
| sk-1359 | practice | love-education, labor-education, family-school | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 10.08 + 先验 1.0 = 11.08） | 尊严、爱与信任（4.9） · 习惯与纪律（4.8） |
| sk-1360 | practice | love-education, collective-education, family-school | A11 劳动与创造 | 文本证据推翻旧标签（关键词 11.84，压过旧标签项 10.72） | 公民与祖国（9.7） · 幸福与精神生活（7.4） |
| sk-1361 | method | love-education, child-study, family-school | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 10.28 + 先验 1.0 = 11.28） | 劳动与创造（4.6） · 思维与智力（4.1） |
| sk-1363 | practice | love-education, family-school, child-study | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 9.36 + 先验 2.5 = 11.86） | 幸福与精神生活（10.1） · 习惯与纪律（5.8） |
| sk-1364 | method | love-education, child-study, teacher-growth | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 10.64 + 先验 1.0 = 11.64） | 道德判断与品德培养（9.4） · 思维与智力（7.5） |
| sk-1365 | method | love-education, child-study, teacher-growth | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 6.97 + 先验 1.0 = 7.97） | 习惯与纪律（5.8） · 尊严、爱与信任（4.4） |
| sk-1366 | method | love-education, collective-education, child-study | A19 道德判断与品德培养 | 文本证据推翻旧标签（关键词 8.39，压过旧标签项 6.67） | 公民与祖国（5.7） · 全面发展与个性（5.0） |
| sk-1367 | practice | love-education, child-study, teacher-growth | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 6.41 + 先验 1.0 = 7.41） | 习惯与纪律（4.8） · 尊严、爱与信任（4.7） |
| sk-1368 | method | love-education, collective-education, teacher-growth | A4 自我教育 | 旧标签先验 + 文本证据（关键词 12.59 + 先验 1.0 = 13.59） | 劳动与创造（12.5） · 幸福与精神生活（9.7） |
| sk-1369 | practice | love-education, collective-education, teacher-growth | A20 检查知识与考查 | 文本证据推翻旧标签（关键词 5.10，压过旧标签项 5.05） | 评价与分数（4.8） · 公民与祖国（4.0） |
| sk-1370 | method | teacher-growth, child-study, reading-and-books | A6 了解儿童 | 旧标签先验 + 文本证据（关键词 7.14 + 先验 2.5 = 9.64） | 尊严、爱与信任（5.0） · 健康与作息（4.8） |
| sk-1371 | practice | love-education, collective-education, family-school | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 14.81 + 先验 1.0 = 15.81） | 思维与智力（8.2） · 尊严、爱与信任（4.7） |
| sk-1372 | practice | teacher-growth, love-education, child-study | A4 自我教育 | 旧标签先验 + 文本证据（关键词 10.28 + 先验 1.0 = 11.28） | 幸福与精神生活（6.8） · 尊严、爱与信任（4.3） |
| sk-1373 | method | collective-education, love-education, teacher-growth | A19 道德判断与品德培养 | 文本证据推翻旧标签（关键词 9.15，压过旧标签项 7.04） | 公民与祖国（6.0） · 自我教育（3.8） |
| sk-1374 | practice | love-education, family-school, child-study | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 12.51 + 先验 1.0 = 13.51） | 尊严、爱与信任（9.1） · 美与艺术（8.7） |
| sk-1376 | practice | love-education, collective-education, family-school | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 10.39 + 先验 1.0 = 11.39） | 劳动与创造（10.0） · 自然与思维课（9.3） |
| sk-1377 | practice | learning-difficulties, thinking-and-nature, teacher-growth | A15 思维与智力 | 旧标签先验 + 文本证据（关键词 16.85 + 先验 2.5 = 19.35） | 健康与作息（11.2） · 自然与思维课（9.6） |
| sk-1378 | practice | love-education, family-school, child-study | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 15.18 + 先验 1.0 = 16.18） | 自然与思维课（5.2） · 评价与分数（4.8） |
| sk-1379 | practice | love-education, family-school, child-study | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 13.97 + 先验 2.5 = 16.47） | 思维与智力（7.5） · 自我教育（3.8） |
| sk-1380 | practice | aesthetic-nature-education, love-education, labor-education | A11 劳动与创造 | 旧标签先验 + 文本证据（关键词 5.31 + 先验 2.5 = 7.81） | 幸福与精神生活（6.7） · 美与艺术（4.5） |
| sk-1381 | practice | love-education, collective-education, teacher-growth | A2 公民与祖国 | 旧标签先验 + 文本证据（关键词 7.98 + 先验 1.0 = 8.98） | 幸福与精神生活（6.4） · 劳动与创造（5.3） |
| sk-1382 | practice | love-education, collective-education, teacher-growth | A1 全面发展与个性 | 文本证据推翻旧标签（关键词 9.49，压过旧标签项 7.46） | 思维与智力（7.5） · 公民与祖国（5.3） |
| sk-1383 | practice | love-education, child-study, collective-education | A5 尊严、爱与信任 | 旧标签先验 + 文本证据（关键词 9.12 + 先验 2.5 = 11.62） | 思维与智力（7.5） · 幸福与精神生活（6.7） |
| sk-1385 | method | collective-education, love-education, teacher-growth | A2 公民与祖国 | 旧标签先验 + 文本证据（关键词 12.89 + 先验 1.0 = 13.89） | 劳动与创造（5.3） · 尊严、爱与信任（4.4） |
| sk-1387 | practice | collective-education, love-education, teacher-growth | A3 幸福与精神生活 | 旧标签先验 + 文本证据（关键词 6.29 + 先验 1.0 = 7.29） | 劳动与创造（5.3） · 健康与作息（4.8） |
| sk-1388 | method | family-school, love-education, child-study | A4 自我教育 | 文本证据推翻旧标签（关键词 9.75，压过旧标签项 6.76） | 尊严、爱与信任（4.3） · 思维与智力（4.1） |

## 逐条内容（判断用）

### sk-0001　后进生是花园里最娇嫩的花

- 旧标签：learning-difficulties
- 建议：**A6 了解儿童**（全无关键词证据，按旧标签先验定夺）
- 其他命中：学习困难学生（11.6）
- 转述：苏霍姆林斯基反对把学习困难儿童从普通学校中“隔离”出去，认为专门设校反而违背基本人道。他说这些孩子并不丑陋，只是人类花园里最娇嫩脆弱的花；他们的薄弱不是自己的过错。
- 出处：On Education (Progress Publishers, 1977), Foreword by S. Soloveichik, p. 22（EPUB page 23）

### sk-0002　先让孩子变得“可教”，而不是吼叫与说教

- 旧标签：learning-difficulties
- 建议：**A16 评价与分数**（文本证据推翻旧标签（关键词 4.80，压过旧标签项 4.14））
- 其他命中：学习困难学生（15.1） · 家庭与母亲（4.1）
- 转述：面对“说不动”的孩子，教师常以为问题是孩子不听话；苏霍姆林斯基认为真正要做的是先恢复孩子的“可教育性”——让儿童处于能听进教师话语的状态。对弱生不吼叫，而是给额外帮助；对道德引导也同样，不用惩罚和向家长告状开路。
- 出处：On Education (Progress Publishers, 1977), p. 34（EPUB page 35）

### sk-0003　教育失灵不是孩子不可救药，而是路径错了

- 旧标签：learning-difficulties
- 建议：**A20 检查知识与考查**（文本证据推翻旧标签（关键词 5.10，压过旧标签项 2.50））
- 其他命中：学习困难学生（6.2） · 教师（2.4）
- 转述：教师面对“难教的孩子”感到无能为力，通常不是因为孩子真的不可救药，而是教育路径错了——只想着“纠错”或“防错”。苏霍姆林斯基主张从孩子入学第一天起就发现并持续巩固、发展他的积极潜能，而不是整天盯着缺陷。
- 出处：On Education (Progress Publishers, 1977), p. 72（EPUB page 73）

### sk-0005　85% 学业失败的首要原因是健康

- 旧标签：learning-difficulties
- 建议：**A7 健康与作息**（旧标签先验 + 文本证据（关键词 10.07 + 先验 1.0 = 11.07））
- 其他命中：学习困难学生（4.9） · 家庭与母亲（4.1）
- 转述：苏霍姆林斯基根据长期观察提出：约 85% 的学业落后首要原因不是智力，而是健康——往往是家长和教师不易察觉的轻微不适或疾病。要解决它，需要母亲、父亲、医生和教师协同努力。
- 出处：On Education (Progress Publishers, 1977), p. 114（EPUB page 115）

### sk-0007　思维必须被教会，否则孩子只会死记硬背

- 旧标签：learning-difficulties
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 7.83 + 先验 1.0 = 8.83））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：慢学习者的问题常常被误判为“记不住”；苏霍姆林斯基认为真正的解法是教他们“想”——如果只逼记忆和背诵，孩子的思维会更钝。思维本身是需要教学的能力。
- 出处：To Children I Give My Heart, Part “The Years of Childhood”, p. 83

### sk-0008　用民间谜题单独训练“思维步数”

- 旧标签：learning-difficulties
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 3.69 + 先验 1.0 = 4.69））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：实践要点：
- 出处：To Children I Give My Heart, Part “The Years of Childhood”, pp. 82–83

### sk-0009　孩子是父母道德生活的一面镜子

- 旧标签：family-school
- 建议：**A8 家庭与母亲**（旧标签先验 + 文本证据（关键词 3.50 + 先验 2.5 = 6.00））
- 其他命中：尊严、爱与信任（4.2） · 了解儿童（3.4）
- 转述：孩子不是靠听父母“讲道理”长大的，而是通过观察父母如何对待他人、如何生活形成最初的道德面貌。父母内心真正的善良会“毫不费力”地传递给孩子；反之，利己主义与盲目溺爱也会成为祸根。
- 出处：把心献给孩子（中文），《我的学生家长》

### sk-0010　教师只有与父母一同努力，才能带给孩子巨大幸福

- 旧标签：family-school
- 建议：**A8 家庭与母亲**（旧标签先验 + 文本证据（关键词 7.64 + 先验 2.5 = 10.14））
- 其他命中：幸福与精神生活（3.4） · 道德判断与品德培养（3.0）
- 转述：学校与家庭不是“交接孩子的两端”，而是共同承担同一任务：让每个孩子感到幸福。幸福不是单靠学校或单靠家庭能完成的，教师必须与父母形成合力。
- 出处：把心献给孩子（中文），《我的学生家长》

### sk-0011　家长培训班：在孩子入学前就培训家长

- 旧标签：family-school
- 建议：**A13 阅读与书籍**（文本证据推翻旧标签（关键词 7.10，压过旧标签项 6.67））
- 其他命中：思维与智力（6.7） · 检查知识与考查（5.6）
- 转述：帕夫雷什中学的“家长学校/家长培训班”在孩子入学前就已开始，面向 2–6 岁儿童的家长。内容覆盖身体、心理、智力、道德、审美发展，特别教家长如何应对孩子的提问、如何带孩子走进自然、如何营造家庭读书氛围。
- 出处：把心献给孩子（中文），《生活习题集里的一千道题》

### sk-0012　85% 学业落后与健康有关，需要家校医合力

- 旧标签：family-school, learning-difficulties
- 建议：**A7 健康与作息**（旧标签先验 + 文本证据（关键词 14.36 + 先验 1.0 = 15.36））
- 其他命中：学习困难学生（10.5） · 评价与分数（4.2）
- 转述：这是“85% 学业失败与健康有关”论断的中文版本，与 On Education 中的英文表述相互印证。它说明：当孩子成绩落后时，学校不能只从教学找原因，需要父母、医生、教师三方协同排查健康。
- 出处：把心献给孩子（中文），《大自然是健康之源》

### sk-0013　学校不能完全取代家庭，教师要对缺失温暖的孩子格外留心

- 旧标签：family-school
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 4.98 + 先验 1.0 = 5.98））
- 其他命中：教师（2.4）
- 转述：苏霍姆林斯基承认学校无法完全替代家庭，尤其是母亲的角色；正因如此，当孩子在家中缺少温暖与关怀时，教师更要格外关注他的需要。
- 出处：On Education (Progress Publishers, 1977), EPUB page 67（The Need to Understand the Workings

### sk-0014　劳动像食物一样必不可少，要系统且完整地完成

- 旧标签：labor-education
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 2.33 + 先验 2.5 = 4.83））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：劳动不是临时“帮忙”或“救火”，而是像食物一样必须规律、系统。帕夫雷什中学刻意让孩子把已开始的工作做完，走完“明确目标 → 坚持完成 → 收获满足”的全过程，避免只做零散、随机的杂务。
- 出处：On Education (Progress Publishers, 1977), p. 199（EPUB page 200）

### sk-0016　从种麦到粮食盛典：让劳动成为可庆祝的成果

- 旧标签：labor-education
- 建议：**A3 幸福与精神生活**（文本证据推翻旧标签（关键词 7.96，压过旧标签项 7.81））
- 其他命中：劳动与创造（5.3） · 思维与智力（4.1）
- 转述：帕夫雷什的孩子不是“象征性”劳动：他们真实松土、选种、播种、收割、脱粒、磨面、烤面包，最后举办“粮食盛典”邀请父母品尝。劳动教育的关键不是口号，而是让孩子从完整劳动中体验“我能创造、我能带给他人快乐”。
- 出处：把心献给孩子（中文），《劳动是崇高的》

### sk-0017　为他人创造美而劳动的孩子，不会成为冷酷的人

- 旧标签：labor-education
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 5.31 + 先验 2.5 = 7.81））
- 其他命中：幸福与精神生活（7.1） · 道德判断与品德培养（3.0）
- 转述：劳动与美育在这里汇合：孩子不是为了“完成作业”而种花，而是为了让母亲、让他人欣赏到美。这种“为他人创造美”的劳动具有道德塑造力，使孩子难以变得残忍冷酷。
- 出处：把心献给孩子（中文），《劳动是崇高的》

### sk-0018　用“体力 + 脑力”结合改造最懒散、最被忽视的孩子

- 旧标签：labor-education, learning-difficulties
- 建议：**A13 阅读与书籍**（文本证据推翻旧标签（关键词 7.10，压过旧标签项 4.83））
- 其他命中：家庭与母亲（4.1） · 思维与智力（3.4）
- 转述：对家长从未让其劳动、又懒散被忽视的孩子，直接逼他“用功读书”很难；苏霍姆林斯基的方法是先让他承担一定体力劳动，再逐步让他在劳动中看到“理解与驾驭自然/事物”的智力意义，从而真正克服懒惰。
- 出处：On Education (Progress Publishers, 1977), p. 200（EPUB page 201）

### sk-0019　关注健康是教育者最重要的工作

- 旧标签：health-first
- 建议：**A7 健康与作息**（旧标签先验 + 文本证据（关键词 8.94 + 先验 2.5 = 11.44））
- 其他命中：检查知识与考查（5.1） · 全面发展与个性（5.1）
- 转述：苏霍姆林斯基把健康放在教育工作的首位：不是“先学习、再锻炼”，而是孩子的精神生活、智力发展和自信都建立在健康与朝气之上。
- 出处：把心献给孩子（中文），《健康，健康，还是健康》

### sk-0020　与家庭约定作息：户外、早睡、开窗睡、院子安睡角

- 旧标签：health-first, family-school
- 建议：**A7 健康与作息**（旧标签先验 + 文本证据（关键词 14.78 + 先验 2.5 = 17.28））
- 其他命中：阅读与书籍（11.1） · 家庭与母亲（4.1）
- 转述：健康管理不是学校单方面规定，而是学校与家庭共同约定：多户外、早睡早起、开窗睡觉、夏季在院子安睡。学校甚至推动每个有学生的家庭建“读书亭/安睡角”，让儿童在新鲜空气中阅读和休息。
- 出处：把心献给孩子（中文），《健康，健康，还是健康》

### sk-0021　新鲜空气与户外作息是健康的“灵丹妙药”

- 旧标签：health-first
- 建议：**A7 健康与作息**（旧标签先验 + 文本证据（关键词 14.78 + 先验 2.5 = 17.28））
- 其他命中：自然与思维课（4.2） · 家庭与母亲（4.1）
- 转述：苏霍姆林斯基把“富含植物杀菌素的新鲜空气”称为健康灵药：常带孩子到田野草场呼吸，建议家长在儿童卧室窗外种核桃树，在院子里装夏季淋浴。健康措施往往落在家庭环境和户外作息上。
- 出处：On Education (Progress Publishers, 1977), EPUB page 114

### sk-0023　睡前长时间做作业，孩子会开始落后

- 旧标签：health-first, learning-difficulties
- 建议：**A7 健康与作息**（旧标签先验 + 文本证据（关键词 10.63 + 先验 2.5 = 13.13））
- 其他命中：学习困难学生（4.9）
- 转述：如果孩子把本应户外活动的时间用来熬夜写作业，反而会开始落后；课堂上的“假性用功/被动”往往正是户外时间被挤占的结果。苏霍姆林斯基据此强调作业与作息安排，而不是简单增加学习时长。
- 出处：On Education (Progress Publishers, 1977), EPUB page 118

### sk-0024　自然、书籍与人中的美，能使心灵变得高尚

- 旧标签：aesthetic-nature-education
- 建议：**A13 阅读与书籍**（文本证据推翻旧标签（关键词 7.44，压过旧标签项 6.71））
- 其他命中：美与艺术（4.2） · 道德判断与品德培养（3.0）
- 转述：苏霍姆林斯基把美育列为最重要的教育原则之一：自然、书籍和他人身上的美能提升儿童心灵的敏感性，使其更容易接受道德影响。偏重实用的教育必须用“看似无用”的艺术与美来平衡。
- 出处：On Education (Progress Publishers, 1977), EPUB page 36

### sk-0025　美的唤醒需要耐心：不是指给孩子看，而是等待他真正被触动

- 旧标签：aesthetic-nature-education
- 建议：**A11 劳动与创造**（文本证据推翻旧标签（关键词 2.98，压过旧标签项 2.50））
- 其他命中：教师（2.4）
- 转述：带儿童看风景很容易，但“真正被美触动”不能靠讲解或命令。教师能做的是持续创造接触美的机会，并耐心等待那个可能数年之后才到来的时刻。
- 出处：On Education (Progress Publishers, 1977), EPUB page 36

### sk-0026　到户外去：画你眼中觉得美的东西

- 旧标签：aesthetic-nature-education
- 建议：**A14 美与艺术**（旧标签先验 + 文本证据（关键词 6.85 + 先验 2.5 = 9.35））
- 其他命中：健康与作息（5.3） · 幸福与精神生活（3.8）
- 转述：帕夫雷什的绘画课不是“老师定主题、学生照画”，而是带孩子到草地上，让他们选择自己眼中觉得美的事物来画。画画因此成为儿童精神生活与自我表现的一部分，而不是单纯技巧训练。
- 出处：把心献给孩子（中文），《每个孩子都是画家》

### sk-0027　不要把孩子想象中的奇妙语言改成大人的语言

- 旧标签：aesthetic-nature-education
- 建议：**A14 美与艺术**（旧标签先验 + 文本证据（关键词 11.06 + 先验 2.5 = 13.56））
- 其他命中：思维与智力（12.4） · 全面发展与个性（5.1）
- 转述：苏霍姆林斯基并不反对教儿童绘画技法（比例、透视、对称），但他强调不要用成人写实标准去“纠正”孩子的想象表达。孩子有自己的世界观和艺术语言，需要被尊重。
- 出处：把心献给孩子（中文），《每个孩子都是画家》

### sk-0028　欣赏美只是善良情感的萌芽，必须化为积极行动

- 旧标签：aesthetic-nature-education
- 建议：**A14 美与艺术**（旧标签先验 + 文本证据（关键词 4.74 + 先验 2.5 = 7.24））
- 其他命中：尊严、爱与信任（4.2） · 了解儿童（3.4）
- 转述：苏霍姆林斯基观察到同一个孩子可能既被美吸引又对生物冷漠。仅“会欣赏”还不够；教育必须把审美情感发展为保护美、创造美的积极行动。
- 出处：把心献给孩子（中文），《爱护生物和美好事物》

### sk-0029　集体教育不压制个性，反而让每个孩子发展全部才能

- 旧标签：collective-education
- 建议：**A9 集体与同伴**（旧标签先验 + 文本证据（关键词 3.16 + 先验 2.5 = 5.66））
- 其他命中：评价与分数（4.8） · 全面发展与个性（4.4）
- 转述：针对“集体会磨平个性”的批评，苏霍姆林斯基明确反驳：脱离集体无法完成现代教育；真正的集体教育不仅不压制个性，反而是个人发展全部能力的条件。
- 出处：On Education (Progress Publishers, 1977), EPUB page 34

### sk-0030　集体只有当它能提升个人时，才成为教育力量

- 旧标签：collective-education
- 建议：**A9 集体与同伴**（旧标签先验 + 文本证据（关键词 3.16 + 先验 2.5 = 5.66））
- 其他命中：尊严、爱与信任（4.8）
- 转述：集体不是“管住个人”的工具，它的教育力量来自能否帮助每个成员提升、树立自尊与自重。若集体只带来从众、羞辱或压抑，就失去了教育意义。
- 出处：把心献给孩子（中文），《我们的集体是一个友爱的大家庭》

### sk-0031　集体传统：为没有过过生日的孩子庆祝生日

- 旧标签：collective-education
- 建议：**A9 集体与同伴**（旧标签先验 + 文本证据（关键词 3.16 + 先验 2.5 = 5.66））
- 其他命中：尊严、爱与信任（5.0） · 幸福与精神生活（4.0） · 家庭与母亲（3.5）
- 转述：帕夫雷什的集体不是抽象组织，而是用具体传统传递关怀：给每个孩子过生日，为家庭从未庆祝过生日的孩子补上第一次节日；孩子没来上学，小伙伴晚上会去看望。这些传统让“关心他人”成为可体验的生活。
- 出处：把心献给孩子（中文），《我们的集体是一个友爱的大家庭》

### sk-0032　孩子对一切冷漠时，为他匹配一位热忱的教师/同伴

- 旧标签：collective-education, learning-difficulties
- 建议：**A9 集体与同伴**（旧标签先验 + 文本证据（关键词 5.46 + 先验 2.5 = 7.96））
- 其他命中：了解儿童（3.8） · 教师（2.4）
- 转述：当孩子对一切无感时，苏霍姆林斯基的做法不是给他贴“冷漠”标签，而是在教师或高年级学生中寻找一个能与他建立共同劳动/共同兴趣的人。个别化教育从“为这个孩子选一个合适的大朋友”开始。
- 出处：On Education (Progress Publishers, 1977), EPUB page 202

### sk-0033　集体生活应以个人提升为宗旨

- 旧标签：collective-education
- 建议：**A9 集体与同伴**（旧标签先验 + 文本证据（关键词 3.16 + 先验 2.5 = 5.66））
- 其他命中：尊严、爱与信任（4.8） · 劳动与创造（3.0）
- 转述：集体不是目的，个人提升才是目的。苏霍姆林斯基希望集体生活始终指向每个孩子的自尊、自爱与才能发展，而不是反过来让孩子服从集体的抽象要求。
- 出处：把心献给孩子（中文），《我们的集体是一个友爱的大家庭》

### sk-0034　没有对孩子的信念，就没有教育；没有信念就是没有爱

- 旧标签：teacher-growth
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88））
- 其他命中：自我教育（3.8）
- 转述：苏霍姆林斯基把“对孩子的信念”视为教师不可让渡的底线：相信孩子有力量、有能力、有“变好”的愿望。没有信念的教育在他看来不可能成立，缺少信念就是缺少爱。
- 出处：On Education (Progress Publishers, 1977), EPUB page 21

### sk-0035　教师的自由时间，是滋养创造力的根

- 旧标签：teacher-growth
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 9.23 + 先验 2.5 = 11.73））
- 其他命中：劳动与创造（3.0） · 阅读与书籍（2.9）
- 转述：帕夫雷什的管理刻意保护教师时间：不要求书面报告、不设固定值班表、不要求逐本批改所有作业。苏霍姆林斯基认为教师创造力的根是自由时间，而不是被行政事务填满。
- 出处：On Education (Progress Publishers, 1977), EPUB page 20

### sk-0036　小学教师对孩子必须像母亲一样亲近

- 旧标签：teacher-growth
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88））
- 其他命中：尊严、爱与信任（4.6）
- 转述：对低龄儿童而言，教师不是“知识传递者”的抽象角色，而应是像母亲一样可亲近的人。教育从师生信任与相互信赖开始；教师眼中的人性温度是最基本也最复杂的教育规则。
- 出处：把心献给孩子（中文），《学校校长》

### sk-0037　教师不仅是导师，也是朋友和同伴

- 旧标签：teacher-growth
- 建议：**A9 集体与同伴**（文本证据推翻旧标签（关键词 8.62，压过旧标签项 8.10））
- 其他命中：阅读与书籍（7.1） · 幸福与精神生活（7.0）
- 转述：教师的情感修养需要在与儿童的多样共同生活中养成：一起劳动、游戏、远足、读书。如果师生只在课堂见面，教育影响就难以进入孩子的情感世界。
- 出处：把心献给孩子（中文），《学校校长》

### sk-0038　真正的教师即使批评，也不扑灭孩子“还有目标要追”的念头

- 旧标签：teacher-growth
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88））
- 其他命中：评价与分数（4.8） · 自我教育（3.8）
- 转述：教师可以批评、可以不满甚至可以有情绪，但有一条底线：不能扼杀孩子心中“我还有值得追求的目标”的信念。批评若让孩子认定自己无可救药，教育就失败了。
- 出处：On Education (Progress Publishers, 1977), EPUB page 72

### sk-0039　要成为真正的儿童教育者，就必须把自己的心奉献给他们

- 旧标签：love-education
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 4.90 + 先验 2.5 = 7.40））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：苏霍姆林斯基在序言中回忆教育家科尔恰克为孩子们牺牲的故事，由此领悟：真正的儿童教育不是职业表演，而是把自己的心交给孩子。
- 出处：把心献给孩子（中文），序言

### sk-0040　爱不是溺爱，而是让孩子获得幸福与自信

- 旧标签：love-education
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 7.39 + 先验 1.0 = 8.39））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：苏霍姆林斯基区分“忘乎所以的爱”与真正的教育之爱：爱不是一味宠溺，而是要帮助孩子获得真实幸福，尤其是通过成功与自信带来的快乐。只有让孩子在自己努力中感到快乐，爱才真正发生作用。
- 出处：On Education (Progress Publishers, 1977), EPUB page 24

### sk-0041　教育者的爱：厚爱 + 明智的严厉 + 父母般的严格要求

- 旧标签：love-education, teacher-growth
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 15.08 + 先验 2.5 = 17.58））
- 其他命中：家庭与母亲（3.5）
- 转述：教育者的“人性/爱”不是无原则的温和，而是厚爱与明智严厉、父母般严格要求的结合。真正的教育爱包含要求和界限。
- 出处：把心献给孩子（中文），《学校校长》

### sk-0042　察觉孩子不对劲时，不要当众立刻追问

- 旧标签：love-education, teacher-growth
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 4.90 + 先验 2.5 = 7.40））
- 其他命中：思维与智力（4.2） · 教师（2.4）
- 转述：敏感的教师能从孩子眼神发现异样，但不立刻当众追问，而是先用某种方式让孩子知道“老师注意到你了”，等独处时再询问。这保护了孩子的尊严与脆弱。
- 出处：On Education (Progress Publishers, 1977), EPUB page 64

### sk-0043　家中缺少疼爱的孩子，教师更要倍加关心

- 旧标签：love-education
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 9.20 + 先验 2.5 = 11.70））
- 其他命中：教师（2.4）
- 转述：爱不是“锦上添花”，而是童年的基本需要。学校无法替代家庭，但对在家庭中缺少疼爱的孩子，教师负有补偿性关心的责任；否则孩子可能在冷漠中长大，对善良与美好满不在乎。
- 出处：把心献给孩子（中文），《我们的集体是一个友爱的大家庭》

### sk-0044　评分应只反映积极脑力劳动成果，而不是惩罚工具

- 旧标签：assessment-grading
- 建议：**A16 评价与分数**（旧标签先验 + 文本证据（关键词 14.42 + 先验 2.5 = 16.92））
- 其他命中：学习困难学生（5.6） · 习惯与纪律（4.9）
- 转述：苏霍姆林斯基主张“只给积极成果评分”：没有成果就先不给分，而不是用低分惩罚孩子。家长也被告知不能要求孩子必须得最高分，不能把不及格等同于懒惰或不认真。
- 出处：把心献给孩子（中文），《让孩子感受到脑力劳动的快乐和取得优异成绩的喜悦》

### sk-0045　绝不能拿不及格去“让家长惩罚孩子”

- 旧标签：assessment-grading
- 建议：**A16 评价与分数**（旧标签先验 + 文本证据（关键词 13.70 + 先验 2.5 = 16.20））
- 其他命中：学习困难学生（5.6） · 尊严、爱与信任（4.6）
- 转述：如果教师给低分是为了借家长之手惩罚孩子，孩子会把学校、教师、家长和脑力劳动一起推向对立面。分数一旦变成“告状工具”，就会摧毁信任。
- 出处：把心献给孩子（中文），《让孩子感受到脑力劳动的快乐和取得优异成绩的喜悦》

### sk-0046　不要求家长在记分册签名，信任比监督更重要

- 旧标签：assessment-grading, family-school
- 建议：**A16 评价与分数**（旧标签先验 + 文本证据（关键词 4.74 + 先验 2.5 = 7.24））
- 其他命中：尊严、爱与信任（4.6） · 家庭与母亲（4.1）
- 转述：苏霍姆林斯基反对用“家长签名”监督孩子；他认为这背后是师生不信任、分数变成鞭策。真正的教育基础是信任，而不是互相防范。
- 出处：把心献给孩子（中文），《让孩子感受到脑力劳动的快乐和取得优异成绩的喜悦》

### sk-0047　不公平的低分是孩子撒谎与欺骗的温床

- 旧标签：assessment-grading
- 建议：**A16 评价与分数**（旧标签先验 + 文本证据（关键词 4.16 + 先验 2.5 = 6.66））
- 其他命中：道德判断与品德培养（6.4） · 尊严、爱与信任（4.6）
- 转述：孩子撒谎、隐瞒成绩，常常不是天生品行问题，而是“不公平低分+不信任”逼出来的。苏霍姆林斯基甚至说“懒惰是不信任的产物”。
- 出处：把心献给孩子（中文），《让孩子感受到脑力劳动的快乐和取得优异成绩的喜悦》

### sk-0048　评价时避免“谁好谁差”的公开比较

- 旧标签：assessment-grading, learning-difficulties
- 建议：**A16 评价与分数**（旧标签先验 + 文本证据（关键词 4.77 + 先验 2.5 = 7.27））
- 其他命中：尊严、爱与信任（4.8）
- 转述：苏霍姆林斯基指出，对能力不同的学生进行学业评价需要高度 tact（分寸感）。他们避免公开说“谁好谁差”，因为比较会伤害学生的自尊与学习动力。
- 出处：On Education (Progress Publishers, 1977), EPUB page 77

### sk-0049　要了解孩子，就要清楚了解他的家庭

- 旧标签：child-study
- 建议：**A6 了解儿童**（旧标签先验 + 文本证据（关键词 7.14 + 先验 2.5 = 9.64））
- 其他命中：家庭与母亲（3.5） · 教师（2.4）
- 转述：苏霍姆林斯基把“了解家庭”作为“了解儿童”的前提。孩子不是孤立个体，他来自具体的家庭关系网络；教师若只盯着课堂表现，就难以理解孩子行为背后的原因。
- 出处：把心献给孩子（中文），《我的学生家长》

### sk-0050　开学前几周，先熟悉每一个家庭

- 旧标签：child-study, family-school
- 建议：**A8 家庭与母亲**（旧标签先验 + 文本证据（关键词 15.18 + 先验 2.5 = 17.68））
- 其他命中：幸福与精神生活（7.4） · 尊严、爱与信任（4.3）
- 转述：帕夫雷什的做法是在开学前逐户家访，系统了解每个家庭。这不只是礼貌性走访，而是为了发现哪些孩子缺少幸福与尊重，以便提前准备教育支持。
- 出处：把心献给孩子（中文），《我的学生家长》

### sk-0051　对很多教师来说，后进生是一本紧闭的书

- 旧标签：child-study, learning-difficulties
- 建议：**A1 全面发展与个性**（文本证据推翻旧标签（关键词 5.06，压过旧标签项 4.69））
- 其他命中：学习困难学生（12.0） · 思维与智力（3.7）
- 转述：后进生之所以“难教”，首先因为教师没有真正读到他这本“紧闭的书”。不理解孩子独特的思维方式和世界观，任何所谓敏感与技巧都无从谈起。
- 出处：On Education (Progress Publishers, 1977), EPUB page 63

### sk-0052　真正的公平来自对每个儿童内心世界的深入了解

- 旧标签：child-study
- 建议：**A6 了解儿童**（旧标签先验 + 文本证据（关键词 3.80 + 先验 2.5 = 6.30））
- 其他命中：幸福与精神生活（3.3） · 教师（2.4）
- 转述：苏霍姆林斯基认为没有脱离具体个人的“抽象公平”。教师若不了解每个孩子的兴趣、情感与内心世界，就无法真正做到公平；教育就是不断加深对每个孩子的认识。
- 出处：On Education (Progress Publishers, 1977), EPUB page 66

### sk-0053　学龄前缺乏照看与信息，会熄灭好奇心

- 旧标签：child-study
- 建议：**A6 了解儿童**（旧标签先验 + 文本证据（关键词 9.99 + 先验 2.5 = 12.49））
- 其他命中：思维与智力（5.7）
- 转述：苏霍姆林斯基通过长期观察发现：学龄前缺少照看和丰富信息，会使大脑长期处于消极状态，表现为好奇心和求知欲消失、态度冷漠。儿童研究要追溯“入学前发生了什么”。
- 出处：把心献给孩子（中文），《三百页〈大自然的书〉》

### sk-0054　会阅读，是对词句含义与美感保持敏感

- 旧标签：reading-and-books
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 9.80 + 先验 2.5 = 12.30））
- 其他命中：美与艺术（5.9） · 幸福与精神生活（3.3）
- 转述：苏霍姆林斯基区分“识字/流利朗读”和真正的“会阅读”。真正的阅读是词句在孩子脑中唤起形象、色彩、旋律与情感，而不只是解码文字。
- 出处：把心献给孩子（中文），《书在儿童精神生活中的作用》

### sk-0055　孩子第一次读之前，先听老师和父母朗读

- 旧标签：reading-and-books
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 21.47 + 先验 2.5 = 23.97））
- 其他命中：幸福与精神生活（7.7） · 美与艺术（4.2）
- 转述：阅读启蒙不是直接丢书给孩子，而是先让成人大声朗读，让孩子通过听觉感受语言与艺术形象之美；阅读还应与大自然的观察和生活体验连接。
- 出处：把心献给孩子（中文），《书在儿童精神生活中的作用》

### sk-0056　建班级藏书库，让孩子反复读喜爱的书

- 旧标签：reading-and-books
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 6.83 + 先验 2.5 = 9.33））
- 其他命中：集体与同伴（5.2） · 幸福与精神生活（4.0）
- 转述：帕夫雷什在一年级就建班级藏书库，精选故事、诗歌、神话等；孩子对喜爱作品会反复阅读 10 遍以上仍不觉厌倦。反复不是机械重复，而是不断从作品中获得新的精神体验。
- 出处：把心献给孩子（中文），《书在儿童精神生活中的作用》

### sk-0057　自我教育与精神生活，从读书开始

- 旧标签：reading-and-books
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 11.06 + 先验 2.5 = 13.56））
- 其他命中：自我教育（4.3） · 幸福与精神生活（3.8）
- 转述：阅读不只是学科能力，更是自我教育的基础。当孩子把书变成精神需求，教师才可能“放手”，让他走向精神独立。
- 出处：把心献给孩子（中文），《书在儿童精神生活中的作用》

### sk-0058　“思考室”只放三百本值得反复读的世界杰作

- 旧标签：reading-and-books
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 8.71 + 先验 2.5 = 11.21））
- 其他命中：思维与智力（3.3）
- 转述：帕夫雷什的“思考室”不是大而全的图书馆，而是只放 300 本精选世界文学杰作，目标不是“读过很多”，而是“反复读、读得深”。
- 出处：On Education (Progress Publishers, 1977), EPUB page 39

### sk-0059　每周两次走进大自然，是去学习思考，不是游玩

- 旧标签：thinking-and-nature
- 建议：**A12 自然与思维课**（旧标签先验 + 文本证据（关键词 15.89 + 先验 1.0 = 16.89））
- 其他命中：思维与智力（7.0） · 了解儿童（3.4）
- 转述：帕夫雷什的“大自然课”不是放松式散步，而是有明确教学目的的思维课：孩子通过观察自然现象学习比较、因果与抽象思考。
- 出处：把心献给孩子（中文），《三百页〈大自然的书〉》

### sk-0060　别把孩子变成知识的仓库，要教他思考

- 旧标签：thinking-and-nature, learning-difficulties
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 7.46 + 先验 2.5 = 9.96））
- 其他命中：了解儿童（7.2）
- 转述：苏霍姆林斯基反对“填装知识”式教育：用记忆代替思考、用背诵代替理解，会让孩子变迟钝并丧失学习兴趣。教育的关键是教会孩子思考。
- 出处：把心献给孩子（中文），《三百页〈大自然的书〉》

### sk-0061　大自然没有自动教育魔力，必须让人思考因果

- 旧标签：thinking-and-nature
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 6.67 + 先验 2.5 = 9.17））
- 其他命中：自我教育（4.4） · 自然与思维课（4.1）
- 转述：苏霍姆林斯基提醒：把孩子放进大自然并不会自动发展智力。只有当孩子认识自然、思考现象之间的因果关系时，大自然才成为教育资源。
- 出处：把心献给孩子（中文），《三百页〈大自然的书〉》

### sk-0062　《大自然的书》：四年 300 次观察的思维课程

- 旧标签：thinking-and-nature
- 建议：**A12 自然与思维课**（旧标签先验 + 文本证据（关键词 9.60 + 先验 1.0 = 10.60））
- 其他命中：思维与智力（7.0） · 了解儿童（3.4）
- 转述：帕夫雷什把自然观察课程化：系统规划四年 300 次观察，每周两次“思维课”。观察对象不是随机风景，而是围绕因果、比较与思维发展的设计。
- 出处：把心献给孩子（中文），《三百页〈大自然的书〉》

### sk-0063　大自然是教育资源，唯当人理解因果关系时

- 旧标签：thinking-and-nature
- 建议：**A12 自然与思维课**（旧标签先验 + 文本证据（关键词 4.14 + 先验 1.0 = 5.14））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：这是“大自然没有自动魔力”的英文对应表述：只有当人认识自然、理解因果关系时，自然才成为强大的教育资源。
- 出处：To Children I Give My Heart, Part “The Years of Childhood”, p. 71

### sk-0064　每一节课都是用一生来备课的

- 旧标签：teacher-growth, reading-and-books
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 8.42 + 先验 2.5 = 10.92））
- 其他命中：阅读与书籍（7.1） · 思维与智力（4.2）
- 转述：一位有三十年教龄的历史教师上公开课，课后被问“花了多少时间备这节课”，他回答：直接准备只用了约十五分钟，但每一节课都是用终生时间来备的。苏霍姆林斯基由此指出，教师不抱怨没时间的奥秘在于持续读书——不是为应付明天那节课而读，而是出于内心对知识的渴求；教科书里的知识在教师的知识海洋里只是“沧海之一粟”。知识背景越宽广，教师
- 出处：《给教师的建议》（杜殿坤编译，教育科学出版社），(二)教师的时间从哪里来？一昼夜只有二十四小时；OCR 原PDF页段: p0000-0099 (0-based)

### sk-0065　评分宁可少一些，但每次都要有分量

- 旧标签：assessment-grading, child-study
- 建议：**A16 评价与分数**（旧标签先验 + 文本证据（关键词 10.20 + 先验 2.5 = 12.70））
- 其他命中：阅读与书籍（6.8） · 学习困难学生（5.6）
- 转述：苏霍姆林斯基认为，评分不应是从教学过程中孤立出来的“验收”动作，而应是建立在师生互信基础上的精细工具。他主张少打分，但每次评分都要包含学生在一段时期内的多种劳动：课堂回答、补充他人回答、书面作业、课外阅读、实际作业等。他从不凭学生一节课的表现就打分；如果学生还没有掌握，就暂时不打分，先帮助他学会，尤其不要急于给不及格分
- 出处：《给教师的建议》（杜殿坤编译，教育科学出版社），(一三)评分应当是有分量的；OCR 原PDF页段: p0000-0099 (0-based)

### sk-0066　儿童的智慧在他的手指尖上

- 旧标签：labor-education, learning-difficulties
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 10.14 + 先验 2.5 = 12.64））
- 其他命中：思维与智力（11.1） · 学习困难学生（5.7）
- 转述：苏霍姆林斯基从观察中得出：双手灵巧、热爱复杂创造性劳动的孩子，往往形成聪敏好钻研的智慧。这里说的不是随便什么劳动，而是含有思想、技能、技艺和步骤间依存关系的劳动。他特别指出，学习困难儿童往往“离开事实就不能思考”，而劳动能让事物之间的关系以直观形态呈现，是帮助他们学会因果联系、发展思维的有效途径。
- 出处：《给教师的建议》（杜殿坤编译，教育科学出版社），(二八)用劳动的爱好来教育学生；OCR 原PDF页段: p0000-0099 (0-based)

### sk-0067　到自然界去上'思维课'：在观察中形成概念

- 旧标签：thinking-and-nature, child-study, aesthetic-nature-education
- 建议：**A12 自然与思维课**（旧标签先验 + 文本证据（关键词 11.13 + 先验 1.0 = 12.13））
- 其他命中：思维与智力（7.0） · 健康与作息（5.3）
- 转述：苏霍姆林斯基所说的“思维课”，不是带学生到户外随便散步，而是有目的地“上课”：他给学生编制了《自然界的书》300页，相当于300次观察，小学四年里每周到自然界去两次，让学生亲眼比较生物与非生物、植物与砂土、不同环境下的生命现象，鼓励他们提出“为什么”“是不是”“从哪里来”的问题，再由具体事实一步步走向“生物”“非生物”
- 出处：《给教师的建议》（杜殿坤编译，教育科学出版社），(五八)“思维课”——到自然界去“旅行”；OCR 原PDF页段: p0200-0299 (0-based)

### sk-0069　关心儿童的健康是教育者最重要的工作

- 旧标签：health-first, family-school
- 建议：**A7 健康与作息**（旧标签先验 + 文本证据（关键词 19.06 + 先验 2.5 = 21.56））
- 其他命中：幸福与精神生活（7.1） · 检查知识与考查（5.1）
- 转述：苏霍姆林斯基把健康放在教育工作的首位，认为儿童的精神、智力、信心都以身体活力为基础。他在小学阶段实际把一半精力用于健康：与家长约定孩子多在户外活动、早睡早起、开窗睡觉，夏天在室外睡觉；坚持早操、洗淋浴、赤脚走路、滑雪和户外劳动；关注早餐营养，反对用零食刺激食欲；并指出厌烦情绪本身也会损害消化。他把健康理解为学校、家庭、
- 出处：《给教师的建议》（杜殿坤编译，教育科学出版社），(八二)关心儿童的健康，是教育者的最重要的工作；OCR 原PDF页段: p0400-0499 (0-based)

### sk-0070　教育的核心是让学生体验到自己的尊严感

- 旧标签：love-education, teacher-growth
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 9.53 + 先验 2.5 = 12.03））
- 其他命中：幸福与精神生活（10.8） · 公民与祖国（8.0）
- 转述：苏霍姆林斯基说，教育有一个“简单又复杂”的秘诀：教师必须先关心学生作为人的尊严感，教育才可能发生。儿童不是被动装知识的容器，师生关系每时每刻都是心灵的接触。他在实践中从不给小学生打不及格分，而是让学生重试、到课前一起思考；当学生靠自己的努力解开难题时，他让学生自己把分数写进记分册，以培养自豪感和尊严。爱护儿童对你的信任
- 出处：《给教师的建议》（杜殿坤编译，教育科学出版社），(七五)教师，要爱护儿童对你的信任；OCR 原PDF页段: p0300-0399 (0-based)

### sk-0071　家长学校：从孩子入学前两年开始持续培训家长

- 旧标签：family-school, child-study
- 建议：**A10 教师**（文本证据推翻旧标签（关键词 7.21，压过旧标签项 6.64））
- 其他命中：全面发展与个性（4.4） · 家庭与母亲（4.1）
- 转述：苏霍姆林斯基认为，只有学校和家庭“志同道合”，教育才能完整。为此他在帕夫雷什中学开办家长学校：家长在孩子入学前两年就报名，一直学到孩子中学毕业；课程按孩子年龄分五组（学前、一二年级、三四年级、五至七年级、七至十年级），每月活动两次，由校长、教导主任和有经验教师主讲，内容突出年龄心理学、个性心理学及体育、智育、德育、美育
- 出处：《给教师的建议》（杜殿坤编译，教育科学出版社），(八四)我们的“家长学校”；OCR 原PDF页段: p0400-0499 (0-based)

### sk-0072　让每个少年都有一本心爱的书，自我教育从好书开始

- 旧标签：reading-and-books
- 建议：**A4 自我教育**（旧标签先验 + 文本证据（关键词 10.18 + 先验 1.0 = 11.18））
- 其他命中：阅读与书籍（6.8） · 思维与智力（3.3）
- 转述：苏霍姆林斯基把阅览室命名为“思考之室”，强调真正的阅读不是为应付识记，而是吸引理智与心灵、促使少年认识自己和自己的未来。他特别看重名人传记：少年用英雄人物的生活作为尺度衡量自己，就是自我教育的开端。他并不急于追问学生“你读后有什么感想”，而是让书先在心里发酵；如果一个少年还没有一本反复读、反复想的心爱之书，教育者就还没
- 出处：《给教师的建议》（杜殿坤编译，教育科学出版社），(八三)“思考之室”——我们的阅览室；OCR 原PDF页段: p0400-0499 (0-based)

### sk-0073　每个孩子天性都是诗人，要让诗的琴弦响起来

- 旧标签：aesthetic-nature-education, thinking-and-nature
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 4.05 + 先验 2.5 = 6.55））
- 其他命中：自然与思维课（4.1） · 了解儿童（3.4）
- 转述：苏霍姆林斯基带六岁学前儿童每周到果园、树林、河岸“读大自然这本书”，让学生把词语和鲜明画面、情感色彩联系起来。他认为儿童本来就会用自己的语言创造故事，但需要成人教他观察事物之间的众多联系；例如面对一棵开花的树，当儿童发现阳光、花瓣、蜜蜂、树枝、蝴蝶之间的几十种联系后，他就能编出成千上万个独特的故事。学生自编的《花瓣儿和
- 出处：《给教师的建议》（杜殿坤编译，教育科学出版社），(五六)让孩子们心里的诗的琴弦响起来；OCR 原PDF页段: p0100-0199 (0-based)

### sk-0075　不给低年级学生打两分：两分就是鞭子和棍棒

- 旧标签：assessment-grading, child-study, learning-difficulties
- 建议：**A16 评价与分数**（旧标签先验 + 文本证据（关键词 10.20 + 先验 2.5 = 12.70））
- 其他命中：学习困难学生（6.4） · 自我教育（5.9）
- 转述：这是把儿童心理研究与评分方法结合的做法。低年级儿童的自我认识尚不稳定，持续的低分不是鞭策，而是让他相信自己天生是差生，甚至让孩子深夜偷偷起来涂改分数、想“找一个没有学校的地方生活”。因此评分应服务于“做优等生的愿望”，让学生先体验“我能行”，再用自尊心驱动他达到要求。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《要慎待儿童》，OCR原文页码段 `<!-- OCR 原PDF页段: p0600-0699 (0-based)

### sk-0077　独立阅读才能真正挽救智力落后学生

- 旧标签：reading-and-books, learning-difficulties
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 6.83 + 先验 2.5 = 9.33））
- 其他命中：健康与作息（6.4） · 学习困难学生（4.9）
- 转述：这是苏霍姆林斯基针对“学习低能”学生的判断。学生的独立阅读能力越弱，越需要教师像医生为虚弱病人安排饮食一样，长期苦思该给他读什么；如果教师培养不出他认真思索书中内容的能力，任何逼他死记硬背的企图都不会有预期效果。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《教会学生学习》，OCR原文页码段 `<!-- OCR 原PDF页段: p0600-0699 (0-based

### sk-0078　在教材的‘症结’处制造悬念，让旧知识成为获取新知的工具

- 旧标签：teacher-growth, child-study
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 8.42 + 先验 2.5 = 10.92））
- 其他命中：思维与智力（7.0） · 检查知识与考查（5.6）
- 转述：教学不是把新材料讲完，而是把新知识变成需要解决的谜。苏霍姆林斯基在这篇论文中强调：学生复述读过的内容并不等于思维积极，真正的知识是能启发思维、激发兴趣、并用来获取新知的“活工具”。教师备课时要找到教材中不易发现的“症结”（因果、时间、从属等关系），由此产生问题；讲解时善于“引而不发”，让学生动用自己的旧知识去解释未知。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《课堂教学与知识》，OCR原文页码段 `<!-- OCR 原PDF页段: p0500-0599 (0-base

### sk-0079　高技术时代，仍要先掌握手工基本功

- 旧标签：labor-education, child-study
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 13.40 + 先验 2.5 = 15.90））
- 其他命中：评价与分数（4.8） · 思维与智力（3.3）
- 转述：苏霍姆林斯基在1960年就反驳“有了机器还要手工做什么”的观点：手工劳动并未消失，而是进入更高阶段；掌握多种手工技能的人更容易在不同工种间迁移。以育人为主的手工劳动应包含脑力因素——学生要思考结构、因果关系、工艺与目的，从而发展概括、分析、综合与批判性评价能力。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《智慧与双手》，OCR原文页码段 `<!-- OCR 原PDF页段: p0100-0199 (0-based)

### sk-0080　最怪诞的是不相信人：没有信任便没有教育

- 旧标签：teacher-growth, child-study
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 8.85 + 先验 1.0 = 9.85））
- 其他命中：教师（7.2） · 幸福与精神生活（3.0）
- 转述：面对校长和班主任禁止16岁学生去旅游的来信事件，苏霍姆林斯基认为这种“禁令”把青年变成软弱无力的孩子，迫使他们心灵锁闭、不说真话。教育不是长辈的断然命令与晚辈的恭顺服从，而是双方共同的精神活动；教师最应珍视的，是学生仍愿意前来商量和恳求允许的那份信任。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《没有信任便没有教育》，OCR原文页码段 `<!-- OCR 原PDF页段: p0500-0599 (0-ba

### sk-0082　活生生的大自然，不能被技术影像取代

- 旧标签：thinking-and-nature, aesthetic-nature-education
- 建议：**A11 劳动与创造**（文本证据推翻旧标签（关键词 8.38，压过旧标签项 6.19））
- 其他命中：自然与思维课（4.1） · 思维与智力（3.7）
- 转述：苏霍姆林斯基承认电影、电视等可以把蜜蜂世界、果树开花过程“简化”地呈现在儿童眼前，这是好事也是坏事：技术缩短了儿童与世界的时间距离，却也使儿童远离真实自然。大自然是思维的摇篮，儿童在直接接触中不断发现问题、产生惊奇，这种活经验远非任何影像信息可比。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《学校与大自然》，OCR原文页码段 `<!-- OCR 原PDF页段: p0800-0899 (0-based

### sk-0083　负担过重的根源不在页数，而在把该理解的东西变成死记

- 旧标签：learning-difficulties, health-first
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 5.31 + 先验 1.0 = 6.31））
- 其他命中：思维与智力（4.1） · 阅读与书籍（2.9）
- 转述：“减负”不是简单删教材，而是区分两类知识：一类靠理解因果和规律来掌握，一类靠专门记忆来保持。检查方式也要相应改变——不是复述教师讲过的话，而是分析事实、揭示关系。这样知识成为“温故知新的利器”，脑力劳动从僵死积累变成创造性劳动。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《负担过重揭秘》，OCR原文页码段 `<!-- OCR 原PDF页段: p0300-0399 (0-based

### sk-0084　知道道德规范，不等于形成道德信念

- 旧标签：teacher-growth, child-study
- 建议：**A4 自我教育**（旧标签先验 + 文本证据（关键词 9.75 + 先验 1.0 = 10.75））
- 其他命中：幸福与精神生活（7.3） · 道德判断与品德培养（3.0）
- 转述：道德教育与知识教育不同：学生记住“应该如何对待劳动、公共财产、他人”并不等于形成了信念；知道更多规范的人，不一定在行动上更道德。教育者如果把“学生能复述规范”当作德育成功，就忽视了从知识到信念需要情感体验、行动练习和内心认同。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《年轻一代共产主义信念的形成》绪论，OCR 原PDF页段: p0000-0099 (0-based)

### sk-0085　劳动教育任务：不是体力强度，而是动员精神力量

- 旧标签：labor-education
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 2.33 + 先验 2.5 = 4.83））
- 其他命中：自我教育（4.4） · 思维与智力（4.2） · 幸福与精神生活（3.3）
- 转述：苏霍姆林斯基以“栽 100 棵树”和“长期培植一棵果树”对比：后者的体力消耗少得多，却要持续照管、牵挂、等待，更能考验意志。劳动作为教育手段，重点不在孩子出多少汗、做了多少件，而在于他是否把自己的注意、情感、坚持都投入进去。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《年轻一代共产主义信念的形成》第1章“信念对形成人的精神面貌的作用”之“共产主义信念是个人意志力的源泉”，OCR 原PDF页

### sk-0086　持续数年的劳动任务，比频繁换活动更能炼意志

- 旧标签：labor-education, collective-education
- 建议：**A9 集体与同伴**（旧标签先验 + 文本证据（关键词 3.16 + 先验 2.5 = 5.66））
- 其他命中：自我教育（4.4） · 幸福与精神生活（4.0）
- 转述：这条原则把“长期性”本身当作教育变量：跨学期的集体任务让学生反复体验目标、中断、回归、克服困难，意志力正是在这种反复中形成的。短时任务容易带来一时兴奋，却难以把意识集中在长远目标上。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《年轻一代共产主义信念的形成》第1章“信念对形成人的精神面貌的作用”之“共产主义信念是个人意志力的源泉”，OCR 原PDF页

### sk-0088　真正为他人做好事，不必让人看见

- 旧标签：love-education, collective-education
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 9.13 + 先验 2.5 = 11.63））
- 其他命中：评价与分数（11.3） · 道德判断与品德培养（5.4）
- 转述：需要人、奉献人的情感是“最羞怯的情感之一”。苏霍姆林斯基提醒：当做好事变成墙报上的表扬、竞赛中的加分，孩子容易学会表演善良，伪君子反而从中获益。真正的教育理想，是让孩子把为他人奉献看作隐秘而珍贵的内心财富，而不是等待观众。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》“怎样培养需要人的情感”，OCR 原PDF页段: p0200-0299 (0-based)

### sk-0089　家校共同遵守的“十不准”

- 旧标签：family-school
- 建议：**A4 自我教育**（文本证据推翻旧标签（关键词 10.95，压过旧标签项 9.44））
- 其他命中：道德判断与品德培养（9.4） · 尊严、爱与信任（4.3）
- 转述：“十不准”表面是礼貌清单，实质是把尊重老人、体谅父母、节制欲望变成可反复练习的行为。苏霍姆林斯基特别指出，如果教育者的话与行为脱节，就会培养出两面三刀的人；不尊重别人的孩子，也不可能尊重真理。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》“怎样培养父辈和孩子们之间的和谐关系”，OCR 原PDF页段: p0200-0299 (0-based)

### sk-0091　图书的节日与永久性学校图书馆

- 旧标签：reading-and-books, collective-education
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 12.67 + 先验 2.5 = 15.17））
- 其他命中：家庭与母亲（3.5）
- 转述：“图书的节日”把“个人阅读”变成“代际公共财富”：书既是父母送给孩子的礼物，又是孩子留给未来学生的纪念。永久性图书馆不同于普通借阅馆，它的存在让学生直观感到：书是人民精神与文化中值得永存的东西，学校因书而成为精神摇篮。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》“培养对待学校的态度要像对待人民精神生活的最重要的发源地那样”，OCR 原PDF页段: p0300-03

### sk-0092　带五岁孩子“去寻求美”：把美与早起劳动连在一起

- 旧标签：aesthetic-nature-education, family-school
- 建议：**A14 美与艺术**（旧标签先验 + 文本证据（关键词 9.19 + 先验 2.5 = 11.69））
- 其他命中：劳动与创造（10.0） · 自然与思维课（4.2）
- 转述：这是家庭中美育与劳动一体化的方法：不是把自然美景当作偶尔的奖励或参观，而是用“去寻求美”这样有仪式感的召唤让孩子自愿早起；审美体验被嵌入日常劳动节奏，孩子为看日出、听鸟鸣付出努力，美因而成为他“挣来”的精神财富。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》“怎样把孩子行为中的‘应当’、‘困难’和‘好’连接起来”，OCR 原PDF页段: p0400-0499 

### sk-0093　一堂好课，应让学生想知道的比教师讲的更多

- 旧标签：teacher-growth, reading-and-books
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 11.06 + 先验 2.5 = 13.56））
- 其他命中：幸福与精神生活（3.7） · 思维与智力（3.4）
- 转述：苏霍姆林斯基认为课堂最重要的教育目的是点燃求知火花。一节课是否成功，不能只看当堂“教会了什么”，还要看下课后学生是否带着更多问题去阅读、追问和探索。知识只有进入个人持续的智力生活，才不是僵死的教材内容。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》“怎样教孩子正确对待脑力劳动”，OCR 原PDF页段: p0300-0399 (0-based)

### sk-0094　完满的脑力劳动来自细心组织而非速度

- 旧标签：health-first
- 建议：**A7 健康与作息**（旧标签先验 + 文本证据（关键词 8.42 + 先验 2.5 = 10.92））
- 其他命中：思维与智力（6.7） · 全面发展与个性（5.2）
- 转述：苏霍姆林斯基批评把儿童头脑当作“可以无限输入的电子机构”的快速教学观。他认为孩子是活人，大脑是精细娇嫩的器官；脑力劳动的质量不取决于一节课塞进多少内容、推进得多快，而取决于是否细心组织、是否兼顾身体、智力和审美等多方面发展。帕夫雷什中学因此警惕“高速度”“高密度”的课堂，强调正常完满的脑力劳动来自合乎儿童健康节奏的安排
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》第3章“关注健康与体育”（学生的健康与精神生活），OCR 原PDF页段：p0200-0299 (0-base

### sk-0095　第一次工资前，先充分体验为社会无酬劳动

- 旧标签：labor-education
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 5.31 + 先验 2.5 = 7.81））
- 其他命中：公民与祖国（5.7） · 尊严、爱与信任（4.9）
- 转述：苏霍姆林斯基并不反对劳动报酬本身，而是强调顺序：在儿童和少年期，先让他们大量从事不取报酬的公益劳动，体验“为社会创造财富”的荣誉感、义务感和尊严感；过早用金钱回报刺激劳动，容易让孩子把劳动只看成获取私利的手段，养成自私、贪婪。这是劳动教育原则中“劳动的崇高道德性及其明确的公益目的性”的具体体现。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》第6章“劳动教育”（劳动教育原则），OCR 原PDF页段：p0400-0499 (0-based)

### sk-0096　亲手培育的花草胜过买来的细瓷花瓶

- 旧标签：aesthetic-nature-education, labor-education
- 建议：**A14 美与艺术**（旧标签先验 + 文本证据（关键词 8.95 + 先验 2.5 = 11.45））
- 其他命中：劳动与创造（5.3） · 幸福与精神生活（3.3）
- 转述：这不是贬低艺术珍品，而是强调审美教育中“亲手参与创造”的价值。儿童对自己劳动过的对象会产生深切的情感联结：泥盆里那棵并不艳丽的花草，因为灌注了他的关注、等待和劳作，成为他精神世界的一部分；买来的精致花瓶虽然美，却没有经过他的创造，因而不能像他自己做出的泥瓶那样“珍贵”。美育不能只靠消费现成的美，还要让孩子通过劳动去创造
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》第7章“美育”（周围环境和劳动在美育中的作用），OCR 原PDF页段：p0500-0599 (0-based

### sk-0097　对教师用说服，不用行政压服

- 旧标签：teacher-growth
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 7.21 + 先验 2.5 = 9.71））
- 其他命中：尊严、爱与信任（4.3） · 自我教育（3.8）
- 转述：苏霍姆林斯基领导教师的方式是“说服”而非“压服”：校长不靠发指令管理教育过程，也不把教师最复杂的错误或争论拿到大会上公开批判。他主张先个别地、亲切友好地谈话，把道理讲透，直到教师心悦诚服并用行动证明自己已转变，才算完成领导者的使命。这背后是对教师人格的尊重，也说明教育过程的改变只能靠信念认同，不能靠行政命令。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》第1章“全体教师团结一致是教育教学工作成功的保证”（深思如何领导好学校），OCR 原PDF页段：p0000-

### sk-0098　教育有三个源泉：科学、技巧和艺术

- 旧标签：teacher-growth
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 7.21 + 先验 2.5 = 9.71））
- 其他命中：尊严、爱与信任（4.7） · 美与艺术（4.2）
- 转述：苏霍姆林斯基告诫青年校长：领导学校不是靠行政职务，而是靠精通教育科学、教学技巧和影响人的艺术；教育现象有深刻个别性，同一条真理在不同情境下可能正确、中性甚至荒谬。因此校长必须不断自我充实、自我更新，并把“教育教学”和“研究了解儿童”这些最本质的事放在第一位，才能成为“教师的教师”。这与“对学校的领导首先是教育思想的领导
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《和青年校长的谈话》第1次谈话“教师创造性劳动的几个基本问题”（关键在于领导全体教师进行创造性劳动），OCR 原PDF页段：

### sk-0100　把时间还给教师：少开会、少写计划

- 旧标签：teacher-growth
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 13.25 + 先验 2.5 = 15.75））
- 其他命中：阅读与书籍（7.1） · 集体与同伴（5.2）
- 转述：苏霍姆林斯基认为，教师自由支配的时间像空气对健康一样必不可少。为此他建议学校管理层把教师从文牍主义中解脱出来：需要统计报表时查班级日志，需要书面报告时用校长和教导主任的日常观察记录；学校工作计划由校长草拟，而不是用教师写的材料拼凑；教师在一学年里只写教育工作和授课进度两份计划；上课以外的会议、课外活动每周不超过两次，以
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《和青年校长的谈话》第3次谈话“学校集体的精神生活”（教师的业余时间及其一般素养的提高），OCR 原PDF页段：p0600-

### sk-0101　检查知识时让全班用草稿本同步思考

- 旧标签：assessment-grading
- 建议：**A20 检查知识与考查**（文本证据推翻旧标签（关键词 12.44，压过旧标签项 3.31））
- 其他命中：思维与智力（3.3） · 教师（2.4）
- 转述：许多课的严重缺点是检查家庭作业时只提问三四个学生并给分，其余学生无事可做或紧张等待。苏霍姆林斯基建议：每个学生备一个草稿本，教师提问时全班都动笔写出答案要点、图表或算式；例如一个学生上黑板求公分母，其余学生在草稿本里各自写例题并比较。这样检查知识不再是少数人的表演，而让所有学生持续进行独立的脑力劳动，也便于教师了解全班
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《和青年校长的谈话》第7次谈话“关于听课和分析课的几点建议”（为什么以及如何检查学生的知识），OCR 原PDF页段：p080

### sk-0103　小学的首要任务是教会儿童学习

- 旧标签：reading-and-books, learning-difficulties
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 6.83 + 先验 2.5 = 9.33））
- 其他命中：学习困难学生（5.6） · 了解儿童（3.4）
- 转述：苏霍姆林斯基分析五至七年级不及格人数远多于低年级的现象，发现许多学生不是不努力，而是不会使用“学习的工具”——观察、思考、表达、阅读和书写，尤其不会流畅地边读边想。低年级若只赶进度而没有把阅读、书写训练到接近“半自动化”，中年级教师又不断往学生“机床”上堆新材料，学生就会越来越吃力，最终跟不上。因此小学阶段的首要任务不
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《和青年校长的谈话》第1次谈话“教师创造性劳动的几个基本问题”（集体的教育信念和教师的个人创造），OCR 原PDF页段：p0

### sk-0104　学校如精致乐器，教师人格负责调音

- 旧标签：teacher-growth, collective-education
- 建议：**A14 美与艺术**（文本证据推翻旧标签（关键词 5.93，压过旧标签项 4.88））
- 其他命中：习惯与纪律（4.9） · 自我教育（3.8）
- 转述：苏霍姆林斯基用“乐器调音”比喻教师人格在整个学校育人系统中的位置。学校可以设计出丰富的活动与制度，但真正决定这些制度能否影响学生心灵的，是教育者以怎样的人格、信念与精神面貌出现在学生面前。教师人格是“调音”的关键，否则再好的旋律也无法奏出。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《全面发展的人的培养问题》“教师的人格、教师集体与学生的全面发展”章（OCR 原PDF页段: p0200-0299, 0-b

### sk-0105　大脑是最精密柔嫩的器官，要小心爱护

- 旧标签：health-first, child-study
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 2.33 + 先验 1.0 = 3.33））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：苏霍姆林斯基反对把儿童的大脑当作“可以无限制贮存信息的电子机器”，警惕那些只追求速度和紧张程度的“高效快速”教学法。脑力劳动的完满与否，首先取决于劳动组织得是否正确、周密与合理，而不是越快越好、塞得越多越好。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《全面发展的人的培养问题》“关心年轻一代的健康与体育”章（OCR 原PDF页段: p0200-0299, 0-based）

### sk-0106　素质像火药，需要用灵感火星点燃

- 旧标签：labor-education, teacher-growth
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88））
- 其他命中：幸福与精神生活（3.0） · 劳动与创造（2.3）
- 转述：苏霍姆林斯基认为，每个孩子身上都有未萌芽的素质，教师的任务不是把知识灌进去，而是提供“火星”——一个令人入迷的劳动、一种技艺、一位年长或同龄人的热情。真正的教育是让某颗心灵里的火药被点燃，让天赋与才能有机会充分显现。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《全面发展的人的培养问题》“劳动教育和人的全面发展”章（OCR 原PDF页段: p0200-0299, 0-based）

### sk-0107　爱情不是易蒸发的液体，而是点滴积累的财富

- 旧标签：love-education, family-school
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 6.77 + 先验 1.0 = 7.77））
- 其他命中：家庭与母亲（3.5） · 劳动与创造（3.0）
- 转述：苏霍姆林斯基反对“爱情消亡论”式的粗俗爱情观。他认为爱情的真正本质是紧张的精神生活、人类心灵最艰难的劳作，需要责任、忠诚与日复一日的创造来积累。学校应当让青少年为未来的婚姻与做父母做好准备，而不是把恋爱只当作短暂的激情。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《全面发展的人的培养问题》“爱情的道德修养和对结婚、做父母的准备”章（OCR 原PDF页段: p0200-0299, 0-b

### sk-0108　让认识周围世界成为儿童真正的活动

- 旧标签：thinking-and-nature, child-study
- 建议：**A3 幸福与精神生活**（文本证据推翻旧标签（关键词 11.09，压过旧标签项 6.19））
- 其他命中：思维与智力（3.7） · 了解儿童（3.4）
- 转述：苏霍姆林斯基强调“认识”不等于“被告知”。低年级学生的思维具体、形象，但如果教学只让他们记住事物的名称和表面特征，精神生活就会贫乏。真正有效的教学要让观察、惊讶、发现和情感体验同时发生，使儿童在认识世界时成为一个主动的探索者。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《学生的精神世界》“（3）学龄初期儿童思维与感觉相互联系的一些特点”节（OCR 原PDF页段: p0300-0399, 0-

### sk-0109　发展爱好：让特长领域比大纲多学十倍

- 旧标签：child-study, teacher-growth
- 建议：**A11 劳动与创造**（文本证据推翻旧标签（关键词 7.93，压过旧标签项 6.30））
- 其他命中：全面发展与个性（5.0） · 幸福与精神生活（4.0）
- 转述：当学生在某个领域表现出兴趣时，不应只按统一大纲“齐步走”，而要给他超大纲的阅读、实验、制作和研究机会。一个人在自己擅长且热爱的领域获得成功体验后，会更愿意去克服其他领域的困难；这种“以特长养信心”的做法，不是放弃全面发展，而是全面发展的入口。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《学生的精神世界》“（6）发展个人爱好在少年精神生活中的意义”节（OCR 原PDF页段: p0400-0499, 0-bas

### sk-0110　思维有快慢，要给迟钝的学生留足思考时间

- 旧标签：learning-difficulties, child-study
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 10.36 + 先验 1.0 = 11.36））
- 其他命中：教师（2.4） · 劳动与创造（2.3）
- 转述：苏霍姆林斯基反对用同一速度、同一方式要求所有学生。思维慢不等于不聪明或不肯学；他们需要的是更长的时间、更充分的感知材料、更细的步骤和独立摸索的机会。给他们足够的等待，他们反而会在以后形成更强的判断力和对结论的审慎。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《学生的精神世界》“（7）少年的情感”节（OCR 原PDF页段: p0400-0499, 0-based）

### sk-0112　讲台上的彩色菊花：让集体情绪可被看见

- 旧标签：collective-education, teacher-growth
- 建议：**A5 尊严、爱与信任**（文本证据推翻旧标签（关键词 8.89，压过旧标签项 7.63））
- 其他命中：自我教育（6.6） · 思维与智力（4.0）
- 转述：教师需要为学生提供安全、非对抗的表达通道，让学生连“对老师不满”也能说出口。彩色菊花是一种无声的情感信号系统：它既训练儿童觉察和命名集体情绪，也要求教师认真对待负面信号、反思自己的行为并向学生作出解释或修复。这不是纵容学生，而是把师生关系建立在诚实与相互尊重的基础上。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《培养集体的方法》“（3）情感洋溢的集体生活”节（OCR 原PDF页段: p0600-0699, 0-based）

### sk-0113　不要剥夺儿童观察童话这面魔镜的幸福

- 旧标签：aesthetic-nature-education, reading-and-books
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 5.84 + 先验 2.5 = 8.34））
- 其他命中：幸福与精神生活（6.4） · 了解儿童（3.4）
- 转述：苏霍姆林斯基记述了一次失败的教学：教师在树林里给一年级学生朗读“白云像长着翅膀的雏鸽”的童话，孩子们正陶醉其中，教师随即解释“云不是鸟，它没有翅膀，只是灰色的小水珠”，孩子们眼里的幻想火花熄灭了，回家后甚至有人向鸟窝扔土块。他由此提醒教育者：儿童有自己认识世界的方式，童话和幻想不是需要被立刻拆穿的“错误”，而是他们进入
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《培养集体的方法》“（6）集体中的创作活动　童话在儿童集体生活中的作用”节（OCR 原PDF页段: p0600-0699, 

### sk-0115　保护少年内心世界的隐秘，是教育的最重要任务

- 旧标签：child-study, teacher-growth
- 建议：**A3 幸福与精神生活**（文本证据推翻旧标签（关键词 6.98，压过旧标签项 5.62））
- 其他命中：尊严、爱与信任（4.6） · 教师（2.4）
- 转述：少年正在形成独立的内心世界；教师若强行窥探、公开或“深挖”他不愿示人的感受，并不会让孩子更听话，反而会损伤其情感敏感度，最终造成麻木与冷漠。苏霍姆林斯基把“不侵犯隐秘”列为少年教育的重要原则，并主张用个别谈话、替孩子保守秘密来赢得信任，而不是把内心“全部摊开”。
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《公民的诞生》“当代人的精神世界与童年期、少年期的教育方法”，OCR 原PDF页段 p0400-0499 (0-based)

### sk-0116　用“您”称呼少年：以尊重的语言确认人格

- 旧标签：teacher-growth, collective-education
- 建议：**A15 思维与智力**（文本证据推翻旧标签（关键词 7.40，压过旧标签项 4.88））
- 其他命中：全面发展与个性（4.4） · 尊严、爱与信任（4.3）
- 转述：苏霍姆林斯基所在学校的教师对少年学生用敬称“您”。这不只是礼貌形式，而是让学生从语言中感到：教师看见的不只是“今天成绩如何的学生”，更是一个正在走向成熟的、有创造潜能的个性。他主张通过这种尊重让少年体会到：教师尊重他已经取得的，也尊重他依靠努力将要达到的更高发展。
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《公民的诞生》“基本的道德素养”，OCR 原PDF页段 p0600-0699 (0-based)

### sk-0117　感知色彩训练：在自然里辨认二十多种绿色

- 旧标签：aesthetic-nature-education, thinking-and-nature
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 6.98 + 先验 1.0 = 7.98））
- 其他命中：自然与思维课（4.2） · 了解儿童（3.4）
- 转述：苏霍姆林斯基把情感与美育的基础放在“感觉素养和知觉素养”上：视觉、听觉长期受训练，人才能分辨出春天绿色的二十多种层次、秋天叶片上的多种色变。做法不是让孩子记住颜色名称，而是反复到田野、树林、池塘边去观察朝霞、四季与光影，让细腻的知觉带出细腻的感情，再由感情发展为精神需求。
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《公民的诞生》“感觉素养和知觉素养”，OCR 原PDF页段 p0700-0799 (0-based)

### sk-0118　读完文学后不当堂追问：别把感动变成解剖

- 旧标签：reading-and-books, assessment-grading
- 建议：**A14 美与艺术**（文本证据推翻旧标签（关键词 9.19，压过旧标签项 6.97））
- 其他命中：幸福与精神生活（7.0） · 自我教育（5.9）
- 转述：苏霍姆林斯基认为，文学教育的目的不是让学生日后复述背诵，而是让作品在心灵中留下痕迹、促进自我认识。因此读完一篇文艺作品后立刻要求“讲出思想内容/写作特点”，正如听完音乐立刻要求说出“它讲了什么”一样，会破坏审美体验。他更愿意从学生日常如何对待父母、祖辈、异性同伴等真实关系，来判断文学是否真正影响了他的精神世界。
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《公民的诞生》“世界观与信念”，OCR 原PDF页段 p0500-0599 (0-based)

### sk-0119　劳动的乐趣如同攀登顶峰，在艰难之后获得自豪

- 旧标签：labor-education
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 7.01 + 先验 2.5 = 9.51））
- 其他命中：幸福与精神生活（7.7） · 尊严、爱与信任（4.8）
- 转述：苏霍姆林斯基用登山比喻真正的劳动教育：劳动乐趣不是轻松舒适，而是克服困难后“登上顶峰”的自我确认。少年在严冬给畜牧场运草，疲惫不堪却心情愉快兴奋；他写道：“这种自豪感只有通过劳动能体验到，它在学校生活的任何其他情况下都是感受不到的。”因此劳动应当成为锻炼意志的手段，让每个少年在少年期至少登上一次这样的顶峰。
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《公民的诞生》“劳动和意志的培养”，OCR 原PDF页段 p0800-0899 (0-based)

### sk-0120　爱情首先意味着对所爱的人的命运、前途承担责任

- 旧标签：love-education, family-school
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 4.90 + 先验 2.5 = 7.40））
- 其他命中：自我教育（4.4） · 幸福与精神生活（3.4）
- 转述：苏霍姆林斯基在给大学儿子的信中谈“爱情的道德纯洁性”：真正的爱情不是情欲满足或消愁解闷，而是对所爱的人的命运、前途承担责任；爱首先是奉献自己的精神力量，为对方创造幸福。他反对把“感情自由”当作放纵的遮羞布，主张用理智、意志与道德责任感使人的感情高尚起来。
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《给儿子的信》第14封信，OCR 原PDF页段 p0900-0993 (0-based)

### sk-0122　大学学习时间法：天天读书与两栏笔记

- 旧标签：reading-and-books, teacher-growth
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 11.06 + 先验 2.5 = 13.56））
- 其他命中：劳动与创造（5.3） · 习惯与纪律（4.9）
- 转述：苏霍姆林斯基给读大学的儿子提出一套“赢得时间”的脑力劳动方法：上课时就开始消化并整理知识，笔记分两栏——一栏记讲课要点，一栏记需要思考的中心问题；平时每天读 4~6 页与课程相关的科学文献，使课外阅读成为理解课内知识的“底子”和“接触点”。这样就能避免考前突击、开夜车式的“紧急动员”。他还强调早晨用于最复杂的创造性脑力
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《给儿子的信》第21封信，OCR 原PDF页段 p0900-0993 (0-based)

### sk-0123　人类美的标准同时也是道德的标准

- 旧标签：aesthetic-nature-education
- 建议：**A7 健康与作息**（文本证据推翻旧标签（关键词 8.42，压过旧标签项 7.24））
- 其他命中：劳动与创造（5.3） · 尊严、爱与信任（4.9）
- 转述：苏霍姆林斯基在谈审美观时指出：人的外表美不是孤立的身体条件，而是内在精神、道德尊严与劳动的创造在面容和举止上的显现；无所事事与不道德会毁掉美，忘我劳动和创造则会使人容光焕发。因此可以说，人类美的标准同时也是道德的标准；健康的身体、崇高的道德、高尚的美感构成和谐。每个人是自己精神美的创造者，而这种美会影响周围人。
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《给儿子的信》第18封信，OCR 原PDF页段 p0900-0993 (0-based)

### sk-0124　分数成了衡量人的尺度：人在分数后面消失了

- 旧标签：assessment-grading, child-study
- 建议：**A16 评价与分数**（旧标签先验 + 文本证据（关键词 18.47 + 先验 2.5 = 20.97））
- 其他命中：全面发展与个性（4.4） · 公民与祖国（4.0）
- 转述：苏霍姆林斯基在《公民的起点》中批评学校用分数给儿童整体“定性”：5分即好学生，3分凑合，2分便“毫无指望”。当分数变成衡量人的唯一标尺，儿童丰富的精神世界、潜在的才能与个性都在分数后面消失。这种评价方式首先导致成绩下降和对学习的冷淡——许多儿童少年早晨上学“像是去受刑”，离开学校后回忆起来仍终生痛心。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《公民的起点》，OCR原文页码段 `<!-- OCR 原PDF页段: p0500-0599 (0-based)

### sk-0126　把身体锻炼放进自我教育：冷水浴、雪擦身靠‘自我强制’

- 旧标签：health-first, child-study
- 建议：**A4 自我教育**（文本证据推翻旧标签（关键词 21.33，压过旧标签项 15.73））
- 其他命中：健康与作息（13.2） · 评价与分数（10.6）
- 转述：健康习惯不能靠教师天天盯、家长时时催，而应转化为少年自己的自我教育。苏霍姆林斯基强调，如果教师简单强迫，学生很可能会欺骗老师，假装已经做到；关键是要让学生自己“强制自己”。当孩子第一次用冷水或雪团战胜自己的惰性，体验到克服弱点的欢悦，他才会开始用批判眼光看自己，形成自我认识和自律。集体在此不是监视者，而是用风气、评价和
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《教育与自我教育》，OCR原文页码段 `<!-- OCR 原PDF页段: p0300-0399 (0-base

### sk-0127　儿童认识世界从父母开始：妈妈怎样说话、爸爸怎样待妈妈

- 旧标签：family-school, child-study
- 建议：**A8 家庭与母亲**（旧标签先验 + 文本证据（关键词 3.50 + 先验 2.5 = 6.00））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：苏霍姆林斯基在《您家的氛围》中提出，孩子面前有“物的大千世界”，也有“人的世界”；他对人的世界的认识从父母开始。妈妈怎样同自己说话、爸爸怎样对待妈妈，构成了孩子关于善与恶的最初概念。家庭若只有物质的“安乐窝”，没有夫妻间互敬互爱、与人为善的精神氛围，就不能成为教育力量。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《您家的氛围》，OCR原文页码段 `<!-- OCR 原PDF页段: p0600-0699 (0-based)

### sk-0128　幸福不能当遗产传给孩子：童年要修‘愿望’，用劳动为幸福奠基

- 旧标签：family-school, labor-education
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 9.90 + 先验 2.5 = 12.40））
- 其他命中：幸福与精神生活（11.1） · 健康与作息（5.9）
- 转述：苏霍姆林斯基在给年轻父亲的信中把“给孩子幸福”重新定义为“教孩子配得上幸福、会创造幸福”。父母把现成享受源源不断递到孩子手里，不是爱，而是剥夺了他认识世界与认识自己的机会。童年的幸福应该有，但“炉火的热度”要靠父母管理：孩子应当从小学会控制自己的愿望，用劳动把愿望变成对他人有益的行动。他举例：牧羊人彼得一家“跟孩子们一
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《致年轻父亲的信》，OCR原文页码段 `<!-- OCR 原PDF页段: p0600-0699 (0-base

### sk-0129　没有惩罚的教育：让为大众的劳动成为童年欢乐的源泉

- 旧标签：collective-education, labor-education
- 建议：**A17 习惯与纪律**（旧标签先验 + 文本证据（关键词 9.88 + 先验 1.0 = 10.88））
- 其他命中：家庭与母亲（7.6） · 幸福与精神生活（7.0）
- 转述：这是把“无惩罚”落实到学校日常制度的思路，不是放任不管，而是用预防取代惩罚。苏霍姆林斯基学校的具体做法包括：办持续15年的家长大学（从年轻夫妇到不同年龄段学生家长）；从孩子7岁入学前夕起，让每个儿童在自家院里种一棵苹果树，把第一颗苹果献给母亲；让儿童和少年从早年起持续“为人们创造些什么”。当公益劳动和创造成为童年欢乐的
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《没有惩罚的教育》，OCR原文页码段 `<!-- OCR 原PDF页段: p0500-0599 (0-base

### sk-0130　给每个孩子手里放一把小提琴：真正的美与恶不能相容

- 旧标签：aesthetic-nature-education, teacher-growth
- 建议：**A14 美与艺术**（旧标签先验 + 文本证据（关键词 4.45 + 先验 2.5 = 6.95））
- 其他命中：幸福与精神生活（3.7） · 道德判断与品德培养（3.0）
- 转述：苏霍姆林斯基引用乌克兰谚语说明美育的道德意义：一个手里“拿着小提琴”的孩子不可能作恶。教师的比喻性任务，不是把每个孩子都培养成音乐家，而是让每个孩子都有机会亲手接触美、感受“音乐如何诞生”，从而避免新一代只做美的消费者。
- 出处：To Children I Give My Heart (Progress Publishers, Moscow; text shows no year), “Music and 

### sk-0131　不必填满课堂每一分钟：急迫的脑力节奏会拖垮孩子

- 旧标签：health-first, child-study
- 建议：**A7 健康与作息**（旧标签先验 + 文本证据（关键词 14.36 + 先验 2.5 = 16.86））
- 其他命中：了解儿童（3.4） · 教师（2.4）
- 转述：苏霍姆林斯基观察到：潜伏疾病和身体不适在教师“把课堂每一分钟都填满高难度脑力劳动”时最容易暴露。这种“一分钟也不浪费”的做法让部分孩子超负荷，而且急迫的节奏对完全健康的孩子同样有害。他主张健康第一，课堂要留有呼吸感，而不是用持续紧张把儿童逼到目光呆滞。
- 出处：To Children I Give My Heart (Progress Publishers, Moscow; text shows no year), Nature— the

### sk-0133　一生只能读约两千本书：童年选书要精，让好书值得反复读

- 旧标签：reading-and-books, child-study
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 6.83 + 先验 2.5 = 9.33））
- 其他命中：评价与分数（5.8） · 幸福与精神生活（3.3）
- 转述：苏霍姆林斯基把阅读选书上升到“一生资源”的高度：人一辈子大约只能读两千本书，因此童年和少年时期读什么必须深思熟虑。他主张宁可让孩子少读，也要让每一本都产生情感与思想冲击，使人愿意反复回到书中、每次发现新的价值。这正是他反对“阅读量竞赛”、重视反复精读与内心吸收的原因。
- 出处：To Children I Give My Heart (Progress Publishers, Moscow; text shows no year), The Book in

### sk-0134　把共情当技能来教：不围观、不追问、不夸耀自己的善行

- 旧标签：collective-education, love-education, teacher-growth
- 建议：**A9 集体与同伴**（旧标签先验 + 文本证据（关键词 6.84 + 先验 2.5 = 9.34））
- 其他命中：道德判断与品德培养（6.8） · 思维与智力（4.7）
- 转述：同学 Sasha 的奶奶住院后，苏霍姆林斯基没有简单号召“大家要关心他”，而是趁 Sasha 不在时教全班“换位”：回忆路上遇到的那位眼神悲伤的老人，想象如果自己唯一的亲人进了医院会怎样。他给出可操作的集体规则——看到同学悲伤不要惊讶围观，不要追问刺探，不要说教式安慰；要做的是悄悄帮助，而且绝不能把自己的善行拿来炫耀。
- 出处：To Children I Give My Heart (Progress Publishers, Moscow; text shows no year), One Must No

### sk-0136　与孩子相处是内在需要而非义务：人道天赋造就教育者

- 旧标签：teacher-growth, love-education
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88））
- 其他命中：幸福与精神生活（3.4） · 了解儿童（3.4）
- 转述：苏霍姆林斯基观察十二岁的高年级少先队员 Olya（她主动申请负责带低年级的“十月儿童”入队）：与儿童相处对她而言不是“任务”而是内在需要。他称这种需要为“人道天赋”，并说拥有这种天赋的人会成为优秀教育者，在工作中获得巨大幸福。随后他还提醒教师：男孩身上那股想当领头人、静不下来的沸腾能量不要压制，淘气的孩子往往正是潜在的
- 出处：To Children I Give My Heart (Progress Publishers, Moscow; text shows no year), You Are the

### sk-0137　没有诗意与审美情感的迸发，就无法充分发展儿童的智力

- 旧标签：thinking-and-nature, aesthetic-nature-education
- 建议：**A12 自然与思维课**（旧标签先验 + 文本证据（关键词 13.76 + 先验 1.0 = 14.76））
- 其他命中：思维与智力（7.0） · 美与艺术（4.7）
- 转述：在孩子们看到甜蔷薇上的露珠与蛛网、被词语的音韵之美点燃并即兴联诗之后，苏霍姆林斯基写下这句判断：没有诗意的、情感审美的迸发，儿童智力不可能得到充分发展。他认为儿童思维天生要求诗意创造；美与活生生的思维如同太阳与花朵一样内在相连。因此他建议最初的思维课不要对着黑板，而要到田野、公园和大自然里去。
- 出处：To Children I Give My Heart (Progress Publishers, Moscow; text shows no year), The School 

### sk-0138　儿童身上没有需要教师严酷对待的东西

- 旧标签：teacher-growth, love-education
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 8.85 + 先验 2.5 = 11.35））
- 其他命中：评价与分数（4.8） · 健康与作息（4.1）
- 转述：苏霍姆林斯基反对把儿童当作“存心作恶的歹徒”来严酷对待。即使儿童心灵中出现了问题，首先也要用善良、亲切、热爱去驱除，而不是用严厉惩罚或怀疑去回应。他强调这不是放弃对抗邪恶，而是对儿童世界的现实看法：教育者的乐观主义与对人的信任，既是儿童成长的土壤，也是教师自己神经与心脏健康的源泉；不信任、幸灾乐祸和不友善，最先伤害的是
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》“怎样在日常活动过程中防止神经衰弱”，OCR 原PDF页段: p0500-0599 (0-based

### sk-0139　集体的四块基石：共同思想、共同智力、共同情感、共同组织

- 旧标签：collective-education, teacher-growth, labor-education
- 建议：**A5 尊严、爱与信任**（文本证据推翻旧标签（关键词 13.23，压过旧标签项 10.85））
- 其他命中：集体与同伴（8.4） · 阅读与书籍（7.4）
- 转述：这条原则纠正一种常见误区：把班集体建设等同于“建机构、定制度、立规矩”。苏霍姆林斯基给出的顺序是：先有共同的价值判断与情感体验（尤其通过有公益意义的集体劳动），再谈组织和服从。所谓“智力的共同性”也不是所有人兴趣相同，而是大家都渴求知识、尊重书籍与有教养的人；每个人以不同的爱好充实集体，集体的智力生活才真正丰富。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》“集体是教育的工具，怎样建立集体，它靠什么来维持”，OCR 原PDF页段: p0700-0799 (

### sk-0141　能力只能由能力来培养，志向只能由志向培养

- 旧标签：teacher-growth
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 7.44 + 先验 1.0 = 8.44））
- 其他命中：习惯与纪律（4.9） · 全面发展与个性（4.4）
- 转述：苏霍姆林斯基强调，教育的力量来自教育者活生生的个性，而不是制度、纲领或机构。教师不只是把知识从自己的头脑搬进学生头脑；学生认识世界时，也同时在认识教师这个人，知识是和学生如何对待教师的“知识明灯”融合在一起的。热爱自己学科的教师会唤起学生对知识、科学和书籍的热爱；只有个性才能影响个性，只有性格才能养成性格。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》“作为教育者的教师应具备什么品质”，OCR 原PDF页段: p0700-0799 (0-based)

### sk-0142　用‘母亲永远在看着你’培养独处时的良心

- 旧标签：teacher-growth, family-school, child-study
- 建议：**A3 幸福与精神生活**（文本证据推翻旧标签（关键词 6.29，压过旧标签项 5.38））
- 其他命中：尊严、爱与信任（4.4） · 自我教育（4.3）
- 转述：这不是用“被抓住”的恐惧来管住孩子，而是把“母亲的爱与期待”内化成独处时的良心见证人。关键前提是孩子与母亲有真实的情感联结，否则这句话会变成空洞威胁。苏霍姆林斯基还给出从“偷偷摘一朵花”到“对啼哭的小孩不闻不问”的细微起点：道德自我教育要从日常小事中培养敏锐心灵，而不是等到犯大错再处理。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》“怎样激发学生在道德方面进行自我教育”，OCR 原PDF页段: p0800-0889 (0-base

### sk-0143　惩罚使孩子从良心的责备中解脱出来

- 旧标签：teacher-growth, child-study, love-education
- 建议：**A4 自我教育**（旧标签先验 + 文本证据（关键词 10.97 + 先验 1.0 = 11.97））
- 其他命中：自然与思维课（5.2） · 评价与分数（4.8）
- 转述：苏霍姆林斯基提出“绝对正常的教育是与惩罚无缘的”。惩罚把孩子从内疚中“解救”出来：孩子想的是“我已经受过罚了”，而不是“我做错了什么”，于是不再思考自己的行为，良心开始沉睡。他讲了一个反例：三年级学生科斯佳用弹弓打麻雀并折磨它，教师罚他三次不去森林；科斯佳却把没长毛的小麻雀塞进教师桌子里报复。惩罚没有使他反省，反而让他
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》“怎样教学生自己教育自己”，OCR 原PDF页段: p0800-0889 (0-based)

### sk-0144　教育是教师在儿童身上的奇妙再创造

- 旧标签：teacher-growth
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88））
- 其他命中：劳动与创造（3.0）
- 转述：苏霍姆林斯基认为，教育者最悲哀的失败，不是学生考试不好，而是孩子以“面目模糊、灰色无光”的个体离开教师。教育不是单向传递知识，而是教师把自己精神生命中真正有价值的东西，奇妙地“再造”在另一个人的成长里。
- 出处：On Education (Progress Publishers, 1977), Part I “Education and the Educator,” “I Am a Fir

### sk-0145　每个孩子心里都有一根独特的心弦，教师的心要与之和鸣

- 旧标签：child-study, teacher-growth
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88））
- 其他命中：幸福与精神生活（3.0）
- 转述：每个孩子的内心都有自己独特的“音调”。教师的话要能进入孩子心里，前提不是掌握更多谈话技巧，而是先让自己的心与孩子那根弦调在同一频率上。儿童研究不是冷冰冰地“看透”孩子，而是用心灵去听、去共鸣。
- 出处：On Education (Progress Publishers, 1977), Part I “Education and the Educator,” “The Need t

### sk-0146　健康关怀不止是卫生守则，其顶峰是身心和谐与创造之乐

- 旧标签：health-first
- 建议：**A7 健康与作息**（旧标签先验 + 文本证据（关键词 13.71 + 先验 2.5 = 16.21））
- 其他命中：尊严、爱与信任（5.0） · 自然与思维课（4.2）
- 转述：苏霍姆林斯基把“健康第一”提升到比作息表、营养和卫生规则更高的层面：健康是身体与精神能力的和谐完满，而这一和谐的最高点是创造的快乐。孩子被田野、星空和花香吸引并唱出自己的歌，在他看来就是身心和谐的顶峰。因此健康教育必须同时保护儿童的喜悦、美感和创造生活，而不是只做“不许生病”的管理。
- 出处：On Education (Progress Publishers, 1977), Part I “Education and the Educator,” “Half Our W

### sk-0147　人因驻足欣赏美而成为人

- 旧标签：aesthetic-nature-education
- 建议：**A11 劳动与创造**（文本证据推翻旧标签（关键词 10.14，压过旧标签项 2.50））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：苏霍姆林斯基把“看美”和“造工具”并列为人之为人的起源：人不仅靠双手劳动，还因为看见星空、朝霞、露珠而惊叹，才开始创造新的美。教育者的任务不是把美当作知识讲解，而是自己也停下来，真正与儿童一起惊叹；美才会在孩子心里开花。
- 出处：On Education (Progress Publishers, 1977), Part IV “Beauty,” “To the Humane by Way of the B

### sk-0148　写作（创作）不是天生就会：先听教师示范，再走向独立创作

- 旧标签：reading-and-books, aesthetic-nature-education
- 建议：**A11 劳动与创造**（文本证据推翻旧标签（关键词 2.98，压过旧标签项 2.50））
- 其他命中：教师（2.4）
- 转述：很多语文教师抱怨学生不会写作文，却从不亲自示范写作。苏霍姆林斯基指出，创造性写作不是儿童面对美景就能自动发生的本能，它必须被教。他的做法是：先让学生听到教师本人如何把眼前景色变成词语（他曾在水塘边即景写下一篇范文并读给学生听），学生先复现教师的写法，再逐步过渡到独立描写给自己留下印象的自然景物。教师自己不会写、从未说过
- 出处：On Education (Progress Publishers, 1977), Part IV “Beauty,” “School Means First and Foremo

### sk-0149　音乐教育要少而精：每月至多两首乐曲，听完去听田野的寂静

- 旧标签：aesthetic-nature-education
- 建议：**A12 自然与思维课**（旧标签先验 + 文本证据（关键词 8.30 + 先验 1.0 = 9.30））
- 其他命中：幸福与精神生活（7.0） · 美与艺术（4.5）
- 转述：苏霍姆林斯基担心杂乱、过量、无组织的音乐印象会钝化儿童的情感感受力。他的做法是“少而深”：每月至多反复欣赏两首乐曲，让孩子每听一次都发现新的美；听完乐曲后特意安排时间去聆听田野、树叶、云雀等“大自然的音乐”，在寂静中消化音乐印象。音乐教育的目标不是培养音乐家，而是培育能感受美的人。
- 出处：On Education (Progress Publishers, 1977), Part IV “Beauty,” “Music Keeps the Heart Straigh

### sk-0151　劳动本身不会吸引儿童：兴趣来自‘我能影响自然、看到成果’

- 旧标签：labor-education
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 2.33 + 先验 2.5 = 4.83））
- 其他命中：幸福与精神生活（4.0） · 了解儿童（3.8）
- 转述：苏霍姆林斯基提醒：把劳动说成“本来就有趣”是不真实的——孩子看到未挖的花坛和旁边的铁锹，不会因此放弃排球。劳动教育的关键不是挑选“有趣的活动”，而是让儿童在真实劳动中逐渐形成对劳动的兴趣：意识到自己能影响自然、能让植物增产、能让工具和材料变成想要的形状，并看到具体成果。兴趣来自对自身力量的真实体验，而不是娱乐化的包装。
- 出处：On Education (Progress Publishers, 1977), Part III “Work,” “Joy from Work which Enhances E

### sk-0152　独处时也会为自己羞愧、渴望比现在更好——教育成果的试金石

- 旧标签：collective-education, child-study
- 建议：**A4 自我教育**（文本证据推翻旧标签（关键词 14.78，压过旧标签项 5.66））
- 其他命中：习惯与纪律（5.0） · 尊严、爱与信任（4.4）
- 转述：在讨论“纪律和自律”时，苏霍姆林斯基把对集体负责与对自己良心负责放在一起谈：一个人意识不到对自己的责任，就听不到良知的召唤。因此，判断教育和自我教育成果的标准，不是学生当着教师或集体的面是否守规矩，而是他独自一人时是否会为自己的不道德行为感到羞愧，是否真心渴望成为比现在更好的人。当“什么好、什么坏”从外部要求变成他个人
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《公民的诞生》“纪律和自律——集体责任感与个人责任感”（含“让人学会用另外一些人的眼光来看自己”），OCR 原PDF页段 p

### sk-0153　少年最需要帮助却拒绝求助：先建立思想一致，再做精神导师

- 旧标签：child-study, teacher-growth
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：苏霍姆林斯基指出，少年期有一个看似矛盾的心理：少年比一生中任何时候都更需要成年人的帮助和建议，却又特别不愿意显得自己需要帮助、不愿向长者低头请教。直接盘问“你在想什么”会把少年推开；能成为少年精神导师的人，不是靠身份或说教，而是靠与学生有共同关心的事、思想感情一致，能同喜同忧。只有当学生感到教师与他站在一起、能理解他的
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《公民的诞生》“少年期的矛盾”，OCR 原PDF页段 p0400-0499 (0-based)

### sk-0154　让每个少年成为自己心爱工作的能工巧匠：劳动自豪感催生公民

- 旧标签：labor-education, collective-education
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 5.31 + 先验 2.5 = 7.81））
- 其他命中：尊严、爱与信任（4.8） · 全面发展与个性（4.4）
- 转述：苏霍姆林斯基在“公民的劳动本质”一节提出：劳动之所以能塑造公民，不是因为它消耗了体力，而是因为少年在劳动中确认自己“能为大家创造价值”，并产生“我是这一行的能工巧匠”的自尊感。他主张帮助每个少年找到一项心爱的工作，长期投入、真正掌握技巧，在集体中成为某个领域的能手；没有这种个别化的劳动自我肯定，集体就会变成无个性的群众
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《公民的诞生》“劳动对少年精神生活的作用·公民的劳动本质”，OCR 原PDF页段 p0800-0899 (0-based)

### sk-0155　音乐教育不是培养音乐家，而首先是培养人

- 旧标签：aesthetic-nature-education, child-study
- 建议：**A14 美与艺术**（旧标签先验 + 文本证据（关键词 10.38 + 先验 2.5 = 12.88））
- 其他命中：自然与思维课（4.1） · 幸福与精神生活（4.0）
- 转述：在“快乐学校”中，苏霍姆林斯基主张音乐教育的根本目的不是让学生成为音乐家，而是通过音乐培养人：音乐能使人看到大自然的美、道德关系的美、劳动之美，也能帮助儿童认识自身的崇高与美好。他特别强调要让孩子把音乐作品的感知与大自然声音的感知交替进行，在童年打下感知旋律美的能力；错过童年，这种素养很难在成年后弥补。
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《我把心给了孩子们》“快乐学校·我们欣赏大自然的音乐”，OCR 原PDF页段 p0100-0199 (0-based)

### sk-0156　性教育少谈生理、多谈尊严：以崇敬母亲与精神交流使本能高尚

- 旧标签：love-education, child-study
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 11.65 + 先验 1.0 = 12.65））
- 其他命中：尊严、爱与信任（9.6） · 健康与作息（4.3）
- 转述：苏霍姆林斯基在分析少男性成熟时提出，把性教育简单化为向孩子解释生理变化、组织公开辩论，反而会使两性关系粗俗化。他主张：第一，不把注意力集中在女孩子身体发育上，成年人要用道德修养“不去注意”这些变化；第二，通过崇敬母亲、培养人的尊严与贞节感，使性本能变得高尚；第三，让男孩在女孩身上首先看到智慧、精神需要和人的尊严，建立智
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《公民的诞生》“少年的身体发育与心理素养·男孩与女孩—男人与女人”，OCR 原PDF页段 p0500-0599 (0-bas

### sk-0157　专横的爱是可怕摧残：不能把孩子当成自己情绪的玩具

- 旧标签：family-school, love-education
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 11.11 + 先验 2.5 = 13.61））
- 其他命中：家庭与母亲（3.5）
- 转述：苏霍姆林斯基在给儿子的第22封信中，把“忘记今天的小孩子将是明天的成年人”列为教育青年一代最常见的毛病，并由此引出“善于爱孩子”的问题。他反对专横的爱：这种爱完全随父母情绪起伏——高兴时什么都宽恕，甚至容忍孩子打祖母；情绪不好时就虐待孩子。他引用契诃夫的话说，不能把孩子当作自己情绪的玩具，忽而温存亲吻，忽而狂暴脚踢；专
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《给儿子的信》第22封信，OCR 原PDF页段 p0900-0993 (0-based)

### sk-0158　让孩子每天看到的一切都经过安排：环境也是教育者

- 旧标签：collective-education, aesthetic-nature-education
- 建议：**A15 思维与智力**（文本证据推翻旧标签（关键词 7.01，压过旧标签项 6.18））
- 其他命中：幸福与精神生活（3.8） · 集体与同伴（3.7）
- 转述：苏霍姆林斯基把校舍内部的陈设视为一种“无声的教育者”：走廊、教室、活动室里孩子经常看到的东西，不是随便贴上去的装饰，而在塑造他的精神面貌。因此每幅画、每句话都应当与儿童年龄相适应，应当能诱导他思考、启发他对照自己和同学；图片、标语、学生作品不是给成人看的摆设，而是进入儿童精神生活的材料。他还在帕夫雷什中学用大量实例说明
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》第2章“学校的物质基础及学生周围的环境”（校舍内部陈设的教育作用），OCR 原PDF页段：p0200-029

### sk-0159　校长把听课摆在首位：每天听两节课

- 旧标签：teacher-growth
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 7.21 + 先验 2.5 = 9.71））
- 其他命中：习惯与纪律（4.9） · 劳动与创造（3.0）
- 转述：苏霍姆林斯基对青年校长说：上课是学校教育和教学的主要形式，校长若不了解课堂里发生什么，其他一切会议和工作都会失去意义。他给自己立下的制度是每天听两节课；当天因校长会议等事耽误，第二天就补听到四五节；出差前则提前密集听课。听课不是只盯青年教师的毛病，也要常听有经验教师的课，把他们的个人创造变成全校共同财富；听课要贯穿学期
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《和青年校长的谈话》第7次谈话“关于听课和分析课的几点建议”（听谁的课，何时去听，听多少课），OCR 原PDF页段：p080

### sk-0160　清晨做功课、午后不紧张：把下午还给学生的精神生活

- 旧标签：health-first
- 建议：**A7 健康与作息**（旧标签先验 + 文本证据（关键词 10.63 + 先验 2.5 = 13.13））
- 其他命中：习惯与纪律（10.8） · 了解儿童（7.2）
- 转述：帕夫雷什中学的作息制度核心是“把最难的脑力劳动放在早晨”：学生早睡早起，在家做早操和早餐后、上学前完成家庭作业；低年级早晨用20～25分钟，三至五年级用40～45分钟即可完成主要作业。上课之后不再安排紧张的课本学习，而是让儿童在户外和兴趣小组中过丰富的精神生活，下午和晚上不抱着课本“熬”。苏霍姆林斯基用多年观察说明：就
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》第3章“关注健康与体育”（对学生的生活环境、劳动和作息制度的卫生保健要求），OCR 原PDF页段：p0200

### sk-0161　把教师引上研究之路：每位教师常年研究一个教育问题

- 旧标签：teacher-growth, collective-education
- 建议：**A9 集体与同伴**（旧标签先验 + 文本证据（关键词 9.09 + 先验 2.5 = 11.59））
- 其他命中：道德判断与品德培养（6.4） · 思维与智力（3.7）
- 转述：苏霍姆林斯基认为，教师工作就其性质来说不可能不带有研究因素：每个儿童都是一个独一无二的精神世界。他所说的“研究”不是严格的科学课题，而是让教师围绕自己工作中真正感到困惑的问题，观察、记录、分析事实，尝试解释因果关系，并把结论带回实践。苏霍姆林斯基所在的学校十多年来让每位教师持续研究一个问题，如“思维过程迟钝的儿童”“一
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《和青年校长的谈话》第3次谈话“学校集体的精神生活”（教师集体的创造性工作中的研究因素），OCR 原PDF页段：p0600-

### sk-0162　教师的语言修养，决定课堂上的脑力劳动

- 旧标签：teacher-growth
- 建议：**A15 思维与智力**（文本证据推翻旧标签（关键词 14.03，压过旧标签项 9.71））
- 其他命中：教师（7.2） · 健康与作息（5.9）
- 转述：苏霍姆林斯基从一次听课中发现：生物教师讲得混乱、缺乏逻辑，学生下课精疲力竭却几乎没听懂。校长起初没察觉，是因为自己熟悉教材，能用已有知识“填补”教师讲解中的漏洞。他把教师的讲述逐字记录，在校务会议上念给大家听，问：“一个对所讲内容毫无准备的人，能从这样的讲述中听懂什么？”答案是什么也听不懂。此后全校把教师语言修养作为长
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《和青年校长的谈话》第2次谈话“教育现象之间的相互依存性”（教师的教育素养），OCR 原PDF页段：p0600-0699 (

### sk-0163　首铃与末铃：用学校传统把高低年级和校友连成一体

- 旧标签：collective-education
- 建议：**A9 集体与同伴**（旧标签先验 + 文本证据（关键词 12.24 + 先验 2.5 = 14.74））
- 其他命中：阅读与书籍（2.9） · 教师（2.4）
- 转述：帕夫雷什中学把开学、毕业等人生节点做成代代相传的集体仪式：一年级开学第一天举行“首次铃声”节，毕业班学生向新生赠书并祝贺他们加入学校大家庭，把自己十年前入学第一天亲手栽的树移交给新生照管，毕业生再与新生同栽一棵“学校友谊树”；毕业时举行“最后铃声”节，低年级学生给毕业生献花、赠书，由小同学摇铃，毕业生代表致谢师词。学校
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》第1章“全体教师团结一致是教育教学工作成功的保证”（我们的传统），OCR 原PDF页段：p0100-0199

### sk-0164　儿童的错误多数不必交给集体讨论：教师独自知道更好

- 旧标签：collective-education, teacher-growth
- 建议：**A5 尊严、爱与信任**（文本证据推翻旧标签（关键词 9.42，压过旧标签项 9.34））
- 其他命中：集体与同伴（6.8） · 了解儿童（3.4）
- 转述：苏霍姆林斯基在“彩色铅笔”事件中观察到：一个孩子拿了同学的彩色铅笔，教师没有发动集体“审问”和谴责，而是把铅笔说成是自己误带回家，第二天悄悄归还，保全了孩子的信任与自尊。他由此提出：儿童犯错多数并非出于恶意，而是轻率与幼稚；如果已经真诚后悔，再把错误交给集体评判，只会让儿童心灵受伤、变得麻木，甚至使集体学会用现成的批判
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《培养集体的方法》第4章“(3)教师对学生个人和集体拥有的合理权力”节（OCR 原PDF页段: p0800-0875, 0-

### sk-0165　班上有个淘气学生是你的幸福，唯唯诺诺才是你的不幸

- 旧标签：teacher-growth, child-study, collective-education
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 9.03 + 先验 1.0 = 10.03））
- 其他命中：评价与分数（4.8） · 自我教育（4.4）
- 转述：苏霍姆林斯基警告教师：不要用强制、呵斥和惩罚把“不听话”的学生压成顺从的影子。儿童敢于表达意见、好动甚至捣乱，说明他的意志和个性还活着；真正危险的是那些被教育手段彻底驯服、唯唯诺诺的学生，他们可能变得冷漠甚至残酷。教师的合理权力不在于让学生害怕，而在于保护并引导儿童的自尊感、主动性和内在善良。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《培养集体的方法》第4章“(3)教师对学生个人和集体拥有的合理权力”节（OCR 原PDF页段: p0800-0875, 0-

### sk-0166　不要把淘气男孩安排坐女孩旁边当纪律手段

- 旧标签：love-education, collective-education, child-study
- 建议：**A9 集体与同伴**（旧标签先验 + 文本证据（关键词 8.56 + 先验 2.5 = 11.06））
- 其他命中：幸福与精神生活（6.8） · 习惯与纪律（5.0）
- 转述：苏霍姆林斯基观察到，把“淘气男生”和女生配对，表面是让女生“管住”男生，实际常使女孩苦恼、孤僻，也让男孩把异性关系视为惩罚与监督。少年期男女交往是正常的精神需要，需要的是健康的集体氛围与有分寸的引导；教师的过度干涉、以性别互相牵制，反而会伤害正在形成的心灵。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《学生的精神世界》“少年时期”章“(9) 少年的友谊”节（OCR 原PDF页段: p0400-0499, 0-based）

### sk-0167　作息制度：早晨做最难作业，下午户外自由，睡前不做紧张脑力劳动

- 旧标签：health-first, learning-difficulties
- 建议：**A7 健康与作息**（旧标签先验 + 文本证据（关键词 16.57 + 先验 2.5 = 19.07））
- 其他命中：习惯与纪律（10.8） · 幸福与精神生活（7.8）
- 转述：苏霍姆林斯基把作息制度当作脑力卫生的一部分：不是简单减少作业，而是把高难度脑力劳动放在精力最好的早晨，下午用户外体力劳动、个人爱好和阅读来恢复与丰富精神生活，睡前留出缓冲时间。自由时间不是浪费，而是智力生活、审美体验和劳动创造的必要土壤；缺少这种恢复与多样活动，所谓发展爱好和培养能力都会落空。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《全面发展的人的培养问题》“关心年轻一代的健康与体育”章（OCR 原PDF页段: p0200-0299, 0-based）

### sk-0169　所有学生都必须参加体力劳动，包括不吸引人的劳动

- 旧标签：labor-education, collective-education
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 7.79 + 先验 2.5 = 10.29））
- 其他命中：尊严、爱与信任（4.3） · 健康与作息（4.1）
- 转述：苏霍姆林斯基提出“生产劳动的普及性”：无论学生对哪些活动有天赋和爱好，在校期间都必须参加生产劳动，尤其不能只做有趣、能展示特长的事，也要承担枯燥、不吸引人的体力操作。这不是过早职业化，而是让每个学生都理解劳动的整体，使集体不因“谁做什么”而分裂；普通、艰苦的劳动能形成对劳动者的尊重和共同的精神基础。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《全面发展的人的培养问题》“劳动教育和人的全面发展”章（OCR 原PDF页段: p0200-0299, 0-based）

### sk-0170　道德教育的“空弹”：故事唤起的热情必须有行善的出口

- 旧标签：love-education, collective-education
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 3.31 + 先验 1.0 = 4.31））
- 其他命中：道德判断与品德培养（3.0） · 教师（2.4）
- 转述：本卡主要使用 Cockerill 的分析性转述，说明苏霍姆林斯基的“空弹”概念：如果教师用英雄故事、自我牺牲的故事激起儿童的情感，却不给儿童任何真实的利他行动出口，这些激动就会像“空弹”一样白白放掉。儿童经历的空弹越多，思想越难推动行动，对教师言辞也会越来越麻木。关键不是少讲故事，而是让“言辞”与“实践”互为表里。
- 出处：Each One Must Shine (Cockerill, 2009 electronic ed.), Chapter 2 The School at Pavlysh, Aim

### sk-0171　学习只是教育这朵花的一枚花瓣——教育无小事、无主次

- 旧标签：teacher-growth, collective-education
- 建议：**A1 全面发展与个性**（文本证据推翻旧标签（关键词 6.63，压过旧标签项 4.88））
- 其他命中：评价与分数（4.2） · 了解儿童（3.8）
- 转述：这是苏霍姆林斯基直接论述“全面和谐发展”的段落：学业只是整朵教育之花的一枚花瓣。教育中没有可以忽略的“小事”，也没有可以独占的“主瓣”；课堂、课外兴趣发展和学生之间的相互关系都同样重要。教师如果只把目光盯在成绩上，就等同于只培养花瓣而毁掉整朵花。
- 出处：Each One Must Shine (Cockerill, 2009 electronic ed.), Chapter 2 The School at Pavlysh, Aim

### sk-0173　音乐教育不是培养音乐家，首先是培养人

- 旧标签：aesthetic-nature-education
- 建议：**A14 美与艺术**（旧标签先验 + 文本证据（关键词 4.45 + 先验 2.5 = 6.95））
- 其他命中：自我教育（4.3） · 道德判断与品德培养（3.0）
- 转述：这是苏霍姆林斯基广被引用的音乐教育名言，在本书第四章经卡巴列夫斯基引用、第五章又由 Cockerill 转述：音乐教育的对象不是未来的演奏者，而是每一个人的心灵。苏霍姆林斯基认为音乐能打开人对自然、道德关系与劳动之美的眼睛，让人在自身中觉察崇高与优美；音乐因此是一种强大的自我教育手段。卡片按第四章原文引录到 `huma
- 出处：Each One Must Shine (Cockerill, 2009 electronic ed.), Chapter 4 Intellectual, Vocational a

### sk-0174　孩子不懂时，把他干涸的“意识池塘”接回大自然

- 旧标签：thinking-and-nature, learning-difficulties
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 3.69 + 先验 2.5 = 6.19））
- 其他命中：自然与思维课（4.1） · 教师（2.4）
- 转述：苏霍姆林斯基给教师的直接建议：学生不懂、思维像笼中鸟一样乱撞时，先别急着加大讲解或练习，而要检查儿童是否被切断了与“活生生的思想源泉”——物体世界与自然现象——的联系。他用了两个意象：干涸的意识池塘与生命之思的大海；重新接通二者，思想的泉水才会重新流动。
- 出处：Each One Must Shine (Cockerill, 2009 electronic ed.), Chapter 4 Intellectual Education — n

### sk-0175　在儿童闻到词语的芬芳之前，不要开始识字教学

- 旧标签：reading-and-books, aesthetic-nature-education
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 6.98 + 先验 1.0 = 7.98））
- 其他命中：劳动与创造（4.7）
- 转述：苏霍姆林斯基描述他带六岁儿童“走向词语源头”的做法：词不只是指称事物的标签，而应带着情感色彩、自己的芬芳与细微层次。他主张先让儿童通过自然和美感经验爱上词、感受到词的美，再开始识字；否则识字会成为苦役，孩子即使最终学会也付出了过高代价。
- 出处：Each One Must Shine (Cockerill, 2009 electronic ed.), Chapter 4 Intellectual Education — s

### sk-0176　460 个犯罪少年家庭中没有一个有家庭藏书

- 旧标签：family-school, reading-and-books, child-study
- 建议：**A6 了解儿童**（旧标签先验 + 文本证据（关键词 3.80 + 先验 2.5 = 6.30））
- 其他命中：美与艺术（4.7） · 道德判断与品德培养（3.0）
- 转述：苏霍姆林斯基在研究 460 个少年违法/犯罪家庭后指出：罪行越严重、越不人道和冷酷，其家庭中的智识、审美与道德兴趣就越贫乏；这 460 个家庭中竟没有一个拥有哪怕很小的家庭藏书，也没有一个少年能说出任何一部交响乐、歌剧或室内乐作品或一位古典/当代作曲家。Cockerill 据此指出，苏霍姆林斯基相信智育与美育的贫乏和“
- 出处：Each One Must Shine (Cockerill, 2009 electronic ed.), Chapter 5 Education of the Heart — S

### sk-0177　集体还没形成时，用一对一谈话教孩子读懂他人的哀乐

- 旧标签：collective-education, child-study, teacher-growth
- 建议：**A9 集体与同伴**（旧标签先验 + 文本证据（关键词 3.16 + 先验 2.5 = 5.66））
- 其他命中：美与艺术（4.2） · 幸福与精神生活（3.0）
- 转述：上方英文摘录为苏霍姆林斯基论述的英文转引/译文；以下是中文转述。苏霍姆林斯基认为，一二年级还没有真正意义上的“集体”，集体正在形成中；这时教师直接对每个儿童施加影响的艺术至关重要。做法是：与六至八岁儿童进行大量个别谈话，教会他们从他人的眼睛、动作和话语中辨认悲伤与喜悦、失望与忧虑。只有每个成员先具有这种“心灵敏感性”，
- 出处：Each One Must Shine (Cockerill, 2009 electronic ed.), Chapter 5 Education of the Heart — c

### sk-0178　别让分数变成束缚思维的枷锁：给最慢的孩子思考时间

- 旧标签：assessment-grading, learning-difficulties
- 建议：**A16 评价与分数**（旧标签先验 + 文本证据（关键词 10.20 + 先验 2.5 = 12.70））
- 其他命中：思维与智力（11.2） · 尊严、爱与信任（4.8）
- 转述：苏霍姆林斯基把评分比作可能“捆住思想”的锁链：孩子答不出，常常不是没有能力，而是没有来得及想、没有集中注意力。他尤其注意给最弱、看似“迟钝”的学生留出思考时间，不急着用分数或“坐下，你不会”来宣判。教师一旦匆忙用评分结束思考，孩子可能就在答案刚浮现时被误判为不会，从而对学习失去兴趣与自尊。
- 出处：To Children I Give My Heart (Progress Publishers), section “Give the Child the Joy of Inte

### sk-0179　评分既要看知识水平也要看努力：在3分旁写‘学习很认真’

- 旧标签：assessment-grading, learning-difficulties
- 建议：**A16 评价与分数**（旧标签先验 + 文本证据（关键词 23.93 + 先验 2.5 = 26.43））
- 其他命中：教师（2.4） · 劳动与创造（2.3）
- 转述：苏霍姆林斯基批评只看结果的评分：同样的“3分”或“4分”背后，不同孩子的努力程度可能完全不同。只按结果给分，会让需要鼓励的孩子更不相信自己，也会让轻易得高分的孩子形成错误的劳动观。他建议：评分首先要反映真实知识水平，同时必须把“努力程度”一并纳入评价——对认真但暂时只得3分的孩子，在分数旁写“学习很认真”；对轻松得4分
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》，『教学目的和教育目的的统一』相关节；OCR 原PDF页段: p0100-0199 (0-based)

### sk-0180　学业成绩评分不是道德评分：分数好不等于孩子好

- 旧标签：assessment-grading, family-school
- 建议：**A16 评价与分数**（旧标签先验 + 文本证据（关键词 14.36 + 先验 2.5 = 16.86））
- 其他命中：家庭与母亲（7.6） · 幸福与精神生活（4.0）
- 转述：苏霍姆林斯基在家长学校中反复提醒父母：孩子某门课得了好分，不等于他在道德上是好孩子；得了低分，也不等于“没达标、没出息”。把学科评分和道德面貌划等号，是“教育上无知的观点”，会看不见人是由许多特点、品质、能力和爱好构成的和谐统一体。这种误读一旦进入家庭，孩子会把“分数不好”直接体验为“我是个坏孩子”。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》，『为使儿童愿意好好学习该做些什么』；OCR 原PDF页段: p0700-0799 (0-based)

### sk-0181　别把知识当存货：学生不该只为明天的评分而读书

- 旧标签：assessment-grading
- 建议：**A16 评价与分数**（旧标签先验 + 文本证据（关键词 10.26 + 先验 2.5 = 12.76））
- 其他命中：阅读与书籍（7.1） · 检查知识与考查（5.6）
- 转述：苏霍姆林斯基批评一种陈旧的知识观：把知识当作头脑里的“存货”，教师一提问就要取出来展示；记住了算有知识，没记住算没知识。这种观念把学习变成“一份儿一份儿地”应付提问，学生在家准备功课只是为了“明天的评分”。他指出，真正证明一个人有知识的，不是能背出来，而是能运用知识去思考、解决问题。
- 出处：《给教师的建议》（杜殿坤编译，教育科学出版社），(五二) 为什么学生感到越学越难了呢？；OCR 原PDF页段: p0100-0199 (0-based)

### sk-0182　三分也是合格成绩：不同孩子取得3分可能已是了不起的成绩

- 旧标签：assessment-grading, family-school
- 建议：**A16 评价与分数**（旧标签先验 + 文本证据（关键词 4.16 + 先验 2.5 = 6.66））
- 其他命中：劳动与创造（4.7） · 家庭与母亲（4.1）
- 转述：苏霍姆林斯基针对当时流行的“3分可耻”“3分不中用”风气指出：3分是知识完全合格的成绩，不应被视为差劲。儿童能力不同，对某个孩子轻而易举的“5分”“4分”，对另一个孩子也许要付出极大努力才能得到“3分”；这个“3分”对他而言就是不小的成功。家长若一律要求孩子达到自己达不到的高度，只会让孩子觉得“我是有罪的人”，并养成蒙
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》，『为使儿童愿意好好学习该做些什么』；OCR 原PDF页段: p0700-0799 (0-based)

### sk-0184　食欲不振的根源是‘氧饥饿’：久坐室内、缺乏户外活动

- 旧标签：health-first
- 建议：**A7 健康与作息**（旧标签先验 + 文本证据（关键词 13.77 + 先验 2.5 = 16.27））
- 其他命中：了解儿童（3.4） · 劳动与创造（2.3）
- 转述：苏霍姆林斯基在多年观察和专门调查中发现，相当比例的学龄初期儿童不吃早饭或早餐量不足；他并没有把食欲不振简单归为“挑食”“娇气”，而是指出其重要根源是长时间坐在通风不良的教室里从事单调脑力劳动、缺少户外活动所造成的“氧饥饿”。他还观察到，长期呼吸富含二氧化碳的室内空气可能影响内分泌腺，进而损害消化功能；若再以零食、甜食去
- 出处：《给教师的建议》（杜殿坤编译，教育科学出版社），(八二)“关心儿童的健康，是教育者的最重要的工作”（早餐与食欲/氧饥饿段），OCR 原PDF页段: p0400-0499 (0-ba

### sk-0186　让迟钝的脑细胞活起来：好饮食、新鲜空气与户外活动，再加智力活动

- 旧标签：health-first, learning-difficulties
- 建议：**A7 健康与作息**（旧标签先验 + 文本证据（关键词 25.01 + 先验 2.5 = 27.51））
- 其他命中：思维与智力（11.2） · 自然与思维课（4.1）
- 转述：苏霍姆林斯基面对“最无望”的沃洛佳时，先从生理层面找原因：这个孩子面色苍白、记忆差、思维贫乏，脑细胞像整个机体一样缺少生气。他的对策不是马上灌知识，而是先改善健康生活条件——吃好、呼吸新鲜空气、晒太阳、在大自然中积极活动，让身体先“活过来”。但他同时强调，健康生活只是前提而非终点：大脑还需要像肌肉锻炼一样接受充分激发活
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《我们的职责是培养人》（沃洛佳案例段），OCR 原PDF页段: p0300-0399 (0-based)

### sk-0187　少年期需要专门的睡眠与营养制度：早睡、铁磷、水果、睡前忌高蛋白

- 旧标签：health-first, child-study
- 建议：**A7 健康与作息**（旧标签先验 + 文本证据（关键词 26.09 + 先验 2.5 = 28.59））
- 其他命中：习惯与纪律（4.9） · 自我教育（4.3）
- 转述：这条方法把健康管理精细到“少年期”这一特殊年龄：不能把儿童作息原样套到少年身上。少年生长快、易疲劳、血压可能有暂时波动，需要比儿童更明确的睡眠“上限”和营养结构；同时因为自我意识增强，外部监督效果有限，必须让少年理解身体变化并参与制定自己的作息。营养上特别强调铁、磷、水果糖分与维生素 C，以及睡前避免高蛋白带来的消化和
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《公民的诞生》“少年的身体发育与心理素养”（含“体 育”“饮食制度、劳动制度和休息制度”相关段落），OCR 原PDF页段: 

### sk-0188　冬季户外劳动按年龄定时长：轻度寒冷是锻炼和预防感冒的最好手段

- 旧标签：health-first, labor-education
- 建议：**A7 健康与作息**（旧标签先验 + 文本证据（关键词 18.57 + 先验 2.5 = 21.07））
- 其他命中：自然与思维课（5.7） · 劳动与创造（2.3）
- 转述：苏霍姆林斯基没有把冬季看作“只能躲在屋里”的季节，而是把适度寒冷的室外劳动纳入健康计划。他给出按年龄递增的劳动时长：8 岁每周 2 小时，9～10 岁每周 3 小时，11 岁每周 4 小时；劳动内容（包树干、抬雪护植物）同时服务学校和自然环境，不是为锻炼而锻炼。他把这种劳动称为“锻炼身体和预防感冒的最好手段”，强调渐进
- 出处：《给教师的建议》（杜殿坤编译，教育科学出版社），(八二)“关心儿童的健康，是教育者的最重要的工作”（冬季户外劳动/锻炼段），OCR 原PDF页段: p0400-0499 (0-ba

### sk-0189　成年时的健康，植根于童年的营养与作息制度

- 旧标签：health-first
- 建议：**A7 健康与作息**（旧标签先验 + 文本证据（关键词 30.30 + 先验 2.5 = 32.80））
- 其他命中：习惯与纪律（10.8） · 了解儿童（3.4）
- 转述：苏霍姆林斯基把健康看作一条“时间线”：成年的体质并非到中年才决定，而是在童年、少年和青年早期的营养、睡眠、劳动、空气与锻炼中逐步打下基础。因此，学校和家庭为儿童安排的每一天——早餐有没有、几点睡、户外多久、是否劳动锻炼——都不只是当下的保健，而是几十年后的健康投资。营养不是孤立的“多吃”，必须与作息、户外空气和身体锻炼
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》第3章“关注健康与体育”之“对学生的生活环境、劳动和作息制度的卫生保健要求”（营养、作息与终身健康），OCR

### sk-0190　观察是思考和识记知识之母：有观察力的学生不会落后

- 旧标签：thinking-and-nature, learning-difficulties
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 6.67 + 先验 2.5 = 9.17））
- 其他命中：检查知识与考查（6.2） · 学习困难学生（4.9）
- 转述：苏霍姆林斯基把“观察”从解释课题的辅助手段提升为一种积极的智力活动和发展智力的途径。知识不只是“存”进头脑，还要在观察中周转、运用、活跃起来；复习帮助保持，观察则直接喂养思考与识记。因此观察力强的学生不容易成为学业落后或文理不通的学生。
- 出处：《给教师的建议》（杜殿坤编译，教育科学出版社），(一七)“教给学生观察”；OCR 原PDF页段: p0000-0099 (0-based)

### sk-0191　大自然不会自动教会思考：只有能作抽象思维，自然才成为思维的学校

- 旧标签：thinking-and-nature
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 7.01 + 先验 2.5 = 9.51））
- 其他命中：自然与思维课（4.1） · 劳动与创造（2.3）
- 转述：这条原则比“大自然是教育资源”更进一步：自然中的具体形象只是原料；如果没有抽象思维，儿童面对大量事物仍会像隔着一堵墙，看不见现象之间的关系。原文紧接着说：只有当儿童能从具体事物中抽身、进行自己的抽象思考时，大自然才成为“脑力劳动的学校”。生动形象必不可少，但必须服务于发现周围世界的联系。
- 出处：On Education (Progress Publishers, 1977), Part II “Study,” “Children Should Live in a Worl

### sk-0192　在自然中让孩子沉默、看、听、想：少讲话也是思维课

- 旧标签：thinking-and-nature, child-study
- 建议：**A12 自然与思维课**（旧标签先验 + 文本证据（关键词 9.60 + 先验 1.0 = 10.60））
- 其他命中：思维与智力（3.7） · 幸福与精神生活（3.7）
- 转述：这是“思维课”容易被忽略的操作细节：带儿童到大自然中，不等于教师不断讲解。苏霍姆林斯基在土丘上听蚱蜢（grasshopper）鸣声一片时强调，儿童需要“不说话”的瞬间——正是在沉默中，他消化刚刚看见和听见的东西。理解一个形象需要时间和神经力量；教师最细腻的素养之一，是学会“让孩子想”，在自然中给孩子看、听、感受的机会。
- 出处：To Children I Give My Heart (Progress Publishers, Moscow), chapter “The School of Joy” — b

### sk-0193　教儿童观察自然界，是为了教会他读书

- 旧标签：thinking-and-nature, reading-and-books
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 17.51 + 先验 2.5 = 20.01））
- 其他命中：自然与思维课（16.1） · 思维与智力（6.7）
- 转述：苏霍姆林斯基把“大自然观察”与“读书”接成一条链：儿童先在活生生的自然界中学习观察、提问、发现联系，再把这种主动探究的态度迁移到书籍世界。会读书不等于会流利朗读；真正的读者是爱钻研、会思考的人，而这种读者的基础在观察自然中就已经打下。
- 出处：《给教师的建议》（杜殿坤编译，教育科学出版社），(五四)“怎样使小学生愿意学习？”；OCR 原PDF页段: p0100-0199 (0-based)

### sk-0194　每一堂思维课，都是对自然之谜的一次观察、惊讶与发现

- 旧标签：thinking-and-nature
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 7.04 + 先验 2.5 = 9.54））
- 其他命中：幸福与精神生活（7.3） · 自然与思维课（5.5）
- 转述：这是苏霍姆林斯基给“思维课”下的一个情感—认识论定义：思维课不是把自然知识讲完，而是让儿童面对“自然之谜”经历一次完整的智力事件——观察现象、感到惊讶、思索并发现真理、体验到知识的欢乐和自己作为思想家的骄傲。同段说明，学校第一学年的思维教育共有六十个主题，其中仅观察樱桃幼芽就安排了十二次，因为一次真正的发现需要时间。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》“怎样使学生们具有知识的欢乐/思维课”段；OCR 原PDF页段: p0300-0399 (0-based

### sk-0196　教师首先是孩子学习生活的人

- 旧标签：teacher-growth, child-study
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88））
- 其他命中：家庭与母亲（3.5）
- 转述：苏霍姆林斯基把教师职业的定义从“知识传递者”扩展为“生活榜样”：孩子通过模仿身边有威信的人来认识世界，教师和父母一样，是最早被孩子仿效的活榜样。所以教师的专业身份首先不是学科，而是他作为一个人的活法。
- 出处：《教师与孩子们》｜OCR 原PDF页段: p0300-0399

### sk-0197　言行不一的教育者是对善的嘲弄

- 旧标签：teacher-growth, child-study
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 8.85 + 先验 1.0 = 9.85））
- 其他命中：思维与智力（4.0） · 道德判断与品德培养（3.0）
- 转述：孩子对成人有两副面孔极其敏感。文中女教师对学生温柔，却对农庄女庄员恶语相向，孩子立刻发现“善良”是装出来的，因而心灵受伤、不再信任。苏霍姆林斯基认为，教育者若没有以善与真教导孩子的道德资格，其语言反而成为对善的讽刺。
- 出处：《教师与孩子们》｜OCR 原PDF页段: p0300-0399

### sk-0198　人至高无上的快乐是为他人而生活

- 旧标签：love-education, child-study
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 14.61 + 先验 1.0 = 15.61））
- 其他命中：家庭与母亲（3.5） · 道德判断与品德培养（3.0）
- 转述：儿童天生只图自己的欢乐，不会自发产生道德感。要预防孩子长成自私的人，不能靠说教，而要帮儿童“行善”：从为父母、长辈做实实在在的好事中，体验到为他人而生活是更大的快乐。感恩与回报感必须通过行动习得。
- 出处：《善的萌生》｜OCR 原PDF页段: p0300-0399

### sk-0199　秋季玫瑰节：让儿童为亲人种花行善

- 旧标签：love-education, labor-education
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 7.96 + 先验 1.0 = 8.96））
- 其他命中：家庭与母亲（3.5） · 劳动与创造（3.0）
- 转述：一年级学生从学校领回玫瑰苗，在自家院子里种下并长期照料，在秋季玫瑰节把花献给父母、祖父母。学校负责提供花苗、提醒照料，家庭负责让献花成为真正的生活仪式。这个方法让“创造美”与“为亲人行善”同时发生，孩子从花朵开放和亲人笑容中体验到无与伦比的快乐。
- 出处：《善的萌生》｜OCR 原PDF页段: p0300-0399

### sk-0200　让每个公民在童年体验劳动的欢乐

- 旧标签：labor-education, teacher-growth
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 5.31 + 先验 2.5 = 7.81））
- 其他命中：幸福与精神生活（7.7） · 全面发展与个性（4.4）
- 转述：人民教师的教育不是空谈理想，而是让儿童在童年就通过真实劳动获得“创造者”的体验。孩子如果只以消费为乐，只从前辈那里获取，道德发展就不会进步；只有亲手参与恢复土地、种出粮食、建起果园，才能把公共利益变成自己内心的自豪与责任。
- 出处：《人民教师》｜OCR 原PDF页段: p0300-0399

### sk-0201　真正的人民教育不滥用华丽词藻

- 旧标签：teacher-growth, child-study
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 4.98 + 先验 1.0 = 5.98））
- 其他命中：全面发展与个性（4.4） · 思维与智力（4.0）
- 转述：苏霍姆林斯基警惕“漂亮话满天飞”：越把神圣、高尚挂在嘴边，它们越容易在学生心中贬值成空谈，甚至腐蚀心灵。他自述一年里很少对孩子说“你们是共产主义建设者”，而是用日常劳动与真实关怀去承载同样的教育目标。教育语言必须与行为血肉相连，而不是装饰。
- 出处：《人民教师》｜OCR 原PDF页段: p0300-0399

### sk-0202　真正教育让少年认识世界时也认识自己

- 旧标签：child-study, teacher-growth
- 建议：**A4 自我教育**（旧标签先验 + 文本证据（关键词 17.19 + 先验 1.0 = 18.19））
- 其他命中：道德判断与品德培养（3.0） · 幸福与精神生活（3.0）
- 转述：德育若只教少年“什么是善、什么是恶”，往往到此为止；苏霍姆林斯基认为这只是教育的开始。真正的教育要让学生在领悟道德美时反观自己，用最高标准衡量自己，追问“我是怎样一个人”。没有这种内在精神活动，道德知识不会变成个人信念。
- 出处：《休叫心灵空荡荡——论精神生活在德育中的作用》（OCR 标题作“休叫心灵空荡荡———论精神活动在德育中的作用①”，待校）｜OCR 原PDF页段: p0300-0399

### sk-0204　孩子的幸福是欢乐的今天

- 旧标签：love-education, child-study
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 4.90 + 先验 2.5 = 7.40））
- 其他命中：全面发展与个性（4.4） · 自我教育（3.8）
- 转述：对成人来说幸福常指向未来理想，但儿童无法靠“未来”生活。孩子的幸福必须是今天可感的充实与欢乐，是把创造欢乐的力量奉献给他人的愿望。苏霍姆林斯基在“奥莉娅”案例中正是用这种“今日幸福”的乐观主义，抵御死亡恐惧和宗教慰藉对孩子的吸引。
- 出处：《幸福·理想·宗教》｜OCR 原PDF页段: p0400-0499

### sk-0206　教学首先是师生活生生的人际关系

- 旧标签：teacher-growth, child-study
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88））
- 其他命中：评价与分数（4.7） · 幸福与精神生活（3.8）
- 转述：对“教师劳动中最重要的是什么”，苏霍姆林斯基的回答不是知识、方法或大纲，而是把学生当作活生生的人。教学首先是师生之间的人际交往；学生的成功与挫折属于精神生活，若教师只搬运知识、只盯分数，就切断了教育最核心的力量。
- 出处：《惟有依靠你们——致未来教师的信》｜OCR 原PDF页段: p0400-0499

### sk-0207　把评分当作少用的‘手术器械’

- 旧标签：assessment-grading, teacher-growth
- 建议：**A16 评价与分数**（旧标签先验 + 文本证据（关键词 14.36 + 先验 2.5 = 16.86））
- 其他命中：思维与智力（3.4） · 劳动与创造（2.3）
- 转述：评分是最精细也最危险的教育工具，用多了会变成蜜糖饼干或粗大棍棒。苏霍姆林斯基反对“分数挂帅”和每句答话都打分；只有学生取得哪怕不大的真正成绩时，才应给他的智力劳动评分。教育者要靠信赖与期待促进孩子内在力量的积聚，而不是靠频繁打分催促。
- 出处：《惟有依靠你们——致未来教师的信》｜OCR 原PDF页段: p0400-0499

### sk-0208　不爱学生的教师，如同歌手没有嗓音

- 旧标签：love-education, teacher-growth
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：教师是能影响他人精神世界的力量，而这种力量具体体现于对学生的爱。爱不是教师职业的附加美德，而是这一行必不可少的“感官”。对“我不爱学生怎么办”的争论，苏霍姆林斯基的回答是：要么离开学校，要么培养爱。
- 出处：《怎样爱学生》｜OCR 原PDF页段: p0400-0499

### sk-0209　我爱的不是他现在的模样，而是他应当成为的模样

- 旧标签：love-education, child-study
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 3.31 + 先验 1.0 = 4.31））
- 其他命中：教师（2.4）
- 转述：面对带著“脓疮和溃疡”的儿童，苏霍姆林斯基不否认邪恶的存在，但强调要把儿童本人与邪恶分开：教师的爱指向儿童应当成为的美好样子。正因如此，教师可以嫉恶如仇，却不把仇恨转嫁到学生身上。这是“保护性教育”的情感前提。
- 出处：《怎样爱学生》｜OCR 原PDF页段: p0400-0499

### sk-0210　崇高植根于平凡：劳动和一块面包

- 旧标签：labor-education, collective-education
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 9.90 + 先验 2.5 = 12.40））
- 其他命中：公民与祖国（4.0） · 幸福与精神生活（4.0）
- 转述：文章从牧人伊万·斯捷潘诺维奇珍藏的一块干面包讲起：孩子用面包打梨，不知珍惜。苏霍姆林斯基指出，“公民”“崇高”并不只在宏大叙事里，而植根于日常劳动、一块面包和前人创造的物质财富。让孩子对快乐之源有忧患意识与责任感，是公民教育的起点。
- 出处：《一块面包》（OCR 中为二级标题 ## 一块面包）｜OCR 原PDF页段: p0400-0499

### sk-0211　儿童喜欢玩具，却不喜欢别人把他们变为玩具

- 旧标签：collective-education, child-study
- 建议：**A2 公民与祖国**（旧标签先验 + 文本证据（关键词 4.05 + 先验 1.0 = 5.05））
- 其他命中：评价与分数（4.8） · 劳动与创造（2.3）
- 转述：苏霍姆林斯基批评把儿童变成表演道具的“文明游戏”：学校落成时让7岁女孩接过巨大木钥匙、让少先队员背稿开“示范辩论会”，都是成人用虚假仪式满足自己。真正公民教育应让孩子去感谢建设者、参与真实劳动，而不是在戏中扮演“小主人”。
- 出处：《一块面包》（OCR 中为二级标题 ## 一块面包）｜OCR 原PDF页段: p0400-0499

### sk-0212　爱国主义的形成始于对人的热爱

- 旧标签：love-education, collective-education
- 建议：**A2 公民与祖国**（旧标签先验 + 文本证据（关键词 9.28 + 先验 1.0 = 10.28））
- 其他命中：习惯与纪律（5.0） · 集体与同伴（3.2）
- 转述：苏霍姆林斯基认为集体教育若只谈服从、纪律、领导，却不谈“诚心、热心”，就没有真正的集体。爱国主义是“感情加思想的合金”，它不是从抽象国家概念开始，而是从身边最亲近的人、从对母亲的爱与责任开始。为此他设计“母亲树”等做法，让青少年先学会爱具体的人。
- 出处：《心灵的教育学》｜OCR 原PDF页段: p0400-0499

### sk-0213　给新团员一株‘母亲树’树苗

- 旧标签：love-education, labor-education
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 2.33 + 先验 2.5 = 4.83））
- 其他命中：全面发展与个性（4.4） · 家庭与母亲（3.5） · 幸福与精神生活（3.0）
- 转述：在青少年加入共青团的隆重日子，苏霍姆林斯基让他们回家种一株“母亲型”苹果树，多年照料，等苹果熟了献给母亲。这个仪式把“荣誉”从组织活动引向家庭责任，用多年持续的劳动把抽象理想变成可触摸的亲情行动，也被他视为“心灵教育学”的具体方法。
- 出处：《心灵的教育学》｜OCR 原PDF页段: p0400-0499

### sk-0214　决定教师语言效果的真谛是诚挚

- 旧标签：teacher-growth, child-study
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 10.33 + 先验 1.0 = 11.33））
- 其他命中：尊严、爱与信任（4.4） · 幸福与精神生活（3.3）
- 转述：教师语言的力量不在词藻华丽或声音严厉，而在诚挚。同样一句“你做得多不好……”，有情感修养的教师能激起学生良心自疚，没有情感修养的教师只会让学生无动于衷。学生尤其能识破虚假，因此语言修养与道德修养、人道精神密不可分。
- 出处：《德育中的教师语言》｜OCR 原PDF页段: p0400-0499

### sk-0215　学生认识人的世界，是从教师开始的

- 旧标签：teacher-growth, child-study
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 4.23 + 先验 1.0 = 5.23））
- 其他命中：全面发展与个性（4.4） · 思维与智力（4.0）
- 转述：教师语言技巧的最终条件不是“说什么”，而是教师整个人是什么。学生通过教师日常生活的自我表现来认识人的世界，如果教师的生活中看不到自己宣讲的道理，再动听的语句也会成为空话。因此，教师榜样首先意味着经常在课外与学生交往，让语言与人格一致。
- 出处：《德育中的教师语言》｜OCR 原PDF页段: p0500-0599

### sk-0216　只读教科书，最终连教科书也读不好

- 旧标签：reading-and-books, learning-difficulties
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 6.83 + 先验 2.5 = 9.33））
- 其他命中：了解儿童（3.8）
- 转述：学生负担重的根源之一是把全部精力用于背记教科书，没有时间进行满足兴趣和认知需要的课外阅读。苏霍姆林斯基认为，需要背记的材料占比越大、课外阅读越少，学习就越艰难；多读课外书不是增加负担，而是让教科书变轻松的根本途径。
- 出处：《既要见树木，也要见森林》｜OCR 原PDF页段: p0500-0599

### sk-0217　只见树木不见森林：教学要见整体

- 旧标签：child-study, learning-difficulties
- 建议：**A12 自然与思维课**（文本证据推翻旧标签（关键词 5.19，压过旧标签项 4.31））
- 其他命中：思维与智力（3.3）
- 转述：学生精确背下历史事件的每个细节和日期，却不会对整体作分析、不会概括事件的轮廓和意义——这就是“见树不见林”。苏霍姆林斯基主张组织教学时应让学生对重大课题作整体思考：只有见到森林这个统一整体，才会对每一棵树形成较全面概念。
- 出处：《既要见树木，也要见森林》｜OCR 原PDF页段: p0500-0599

### sk-0218　三大支柱：明晰的思维、生动的语言、创造活动

- 旧标签：child-study, thinking-and-nature
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 11.09 + 先验 2.5 = 13.59））
- 其他命中：评价与分数（4.8） · 幸福与精神生活（3.8）
- 转述：苏霍姆林斯基批评学校让学生年复一年重复别人思想、死记硬背再去复现。他主张教学的基础是把活生生的语言用于儿童创造活动，让学生自己编故事、观察联系、表达思想。明晰的思维、生动的语言、创造活动三者共同构成学生精神生活和智力发展的支柱。
- 出处：《论学生精神生活和智力发展的三大支柱》｜OCR 原PDF页段: p0500-0599

### sk-0219　每个儿童天性都是诗人，要教会他发现联系

- 旧标签：thinking-and-nature, child-study
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 7.74 + 先验 2.5 = 10.24））
- 其他命中：自然与思维课（5.5） · 了解儿童（3.4）
- 转述：儿童不是天生就会“用语言创造”，需要教师引导他们到自然和生活中观察事物之间的联系。例如面对开花的苹果树，让学生看到花瓣、蜜蜂、枝条、飞蛾之间十几条联系，思维被激活后，他们就能自编出独特故事。思维课的本质不是游玩，而是用观察与发现点燃语言和创造。
- 出处：《论学生精神生活和智力发展的三大支柱》｜OCR 原PDF页段: p0500-0599

### sk-0220　休怕成为慈爱的人：引发儿童邪恶的不是慈爱，而是粗暴、冷漠和严酷

- 旧标签：love-education, teacher-growth
- 建议：**A8 家庭与母亲**（文本证据推翻旧标签（关键词 7.64，压过旧标签项 4.88））
- 其他命中：教师（2.4）
- 转述：《休怕成为慈爱的人》以少年谢尔盖的“生活故事”为起点：父母离异、教师当众羞辱、校卫呵斥、父亲鞭打，一次本可被一句慈爱话语化解的委屈，最终累积成纵火伤人的悲剧。苏霍姆林斯基由此提出，慈爱不是纵容或“娃娃腔”，而是仁慈和人道；真正把儿童推向邪恶的，不是教师或家长的慈爱，而是成年人的粗暴、冷漠与严酷。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《休怕成为慈爱的人》，OCR原文页码段 `<!-- OCR 原PDF页段: p0500-0599 (0-bas

### sk-0221　理解童年世界是上升，不是俯就：教师应体察儿童的世界

- 旧标签：child-study, teacher-growth
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 4.23 + 先验 1.0 = 5.23））
- 其他命中：习惯与纪律（5.0） · 教师（2.4）
- 转述：《致女儿的信》用学生季姆科的故事说明：一个爱讲童话、上课偷偷看甲虫的男孩，被前一位女教师当作“纪律问题”反复压制，善良的心逐渐被冷酷积聚起来；转到苏霍姆林斯基班上后，教师悄悄收起火柴盒、课后听他讲独角甲虫，男孩的求知火花才重新燃起。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《致女儿的信》，OCR原文页码段 `<!-- OCR 原PDF页段: p0500-0599 (0-based)

### sk-0222　把小学生看作明天的公民：童年的点滴会汇聚成人的精髓

- 旧标签：child-study, teacher-growth
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88））
- 其他命中：公民与祖国（4.0） · 集体与同伴（3.7） · 幸福与精神生活（3.7）
- 转述：苏霍姆林斯基对女儿说，教师站在两种伟大事物之间：一边是祖辈积累的知识，另一边是需要塑造成“大写的人”的儿童。教育的主要之处，不是只把知识搬进头脑，而是看到眼前这个7岁的孩子10年后将成为公民；他的英雄业绩或平凡人生，都从童年所做的事、所感受的一切中点点滴滴积累起来。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《致女儿的信》，OCR原文页码段 `<!-- OCR 原PDF页段: p0500-0599 (0-based)

### sk-0223　学校没有教会最主要的东西：怎样生活

- 旧标签：family-school, child-study
- 建议：**A8 家庭与母亲**（旧标签先验 + 文本证据（关键词 3.50 + 先验 2.5 = 6.00））
- 其他命中：思维与智力（3.3）
- 转述：《关于学校教育的思考》开头记录了一位年轻母亲奥莉娅的话：她中学毕业、工作结婚后又离婚，说“我们没有学会怎样生活”，不会做妻子和丈夫，不知道怎样做自己儿女的父母。苏霍姆林斯基由此反思：学校教了水在5米深处的状态、汉穆拉比法典、星际空间的原子数，却没有教学生怎样过家庭生活。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《关于学校教育的思考》，OCR原文页码段 `<!-- OCR 原PDF页段: p0500-0599 (0-ba

### sk-0224　教师面对的不是抽象学生，而是活生生具体的人

- 旧标签：teacher-growth, child-study
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 7.44 + 先验 1.0 = 8.44））
- 其他命中：自我教育（3.8） · 思维与智力（3.3）
- 转述：《关于学校教育的思考》中，一位聪慧的妇女因学校只教“可复述的知识”而长期活在“两颗心”的分裂里，最终走进修道院，多年后才靠真正的书籍与思想醒悟。苏霍姆林斯基由此分析：知识不能变成信念，常常因为教师传授知识时没有注入自己的思想、感情、欢乐和痛苦，面对的不是教室里一个个具体的人，而是“抽象的学生”。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《关于学校教育的思考》，OCR原文页码段 `<!-- OCR 原PDF页段: p0500-0599 (0-ba

### sk-0225　思想生活从体察他人开始：对身边人的悲欢保持敏锐

- 旧标签：love-education, child-study
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 6.41 + 先验 1.0 = 7.41））
- 其他命中：教师（6.6） · 公民与祖国（3.9）
- 转述：《我的教育信念》开篇用“石头人”故事提出警示：一个被父母从小用现成家业供养的孩子，长大后对邻居火灾、他人苦难毫无感觉。苏霍姆林斯基相信，人有什么样的幸福观，他就是什么样的人；教育要防止心灵长成“铁石心肠”。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《我的教育信念》，OCR原文页码段 `<!-- OCR 原PDF页段: p0600-0699 (0-based

### sk-0226　冷漠寡情是教育事业最凶恶的敌人：保护儿童对教师的信赖

- 旧标签：love-education, teacher-growth
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 4.98 + 先验 2.5 = 7.48））
- 其他命中：评价与分数（4.8） · 教师（2.4）
- 转述：《寄语后来人》是苏霍姆林斯基写给年轻同行的“教育遗嘱”。他特别强调，儿童是脆弱、没有自卫力的，入学后可能很快经历“别人都会而自己不会”的痛苦；为了躲开不愉快谈话和惩罚，儿童会开始耍滑头、欺骗。因此教师要像爱护最娇柔的鲜花一样，保护儿童对教师的信赖。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《寄语后来人》，OCR原文页码段 `<!-- OCR 原PDF页段: p0600-0699 (0-based)

### sk-0227　真正父亲无可替代：育人比任何生产岗位更细致

- 旧标签：family-school, love-education
- 建议：**A8 家庭与母亲**（旧标签先验 + 文本证据（关键词 3.50 + 先验 2.5 = 6.00））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：《父母教育学》用一位优秀康拜因机手伊万·菲利波维奇的悲剧说明：他在农庄受人敬重、屡获勋章，却因忙于工作与荣誉而溺爱独子；儿子闯祸后，他只会回家狠揍一顿，结果孩子用泥糊住父亲照片上的眼睛——“明白了，但也晚了”。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《父母教育学》，OCR原文页码段 `<!-- OCR 原PDF页段: p0600-0699 (0-based)

### sk-0228　夫妻之爱会化为你未来孩子的精神美

- 旧标签：family-school, love-education
- 建议：**A11 劳动与创造**（文本证据推翻旧标签（关键词 7.66，压过旧标签项 7.40））
- 其他命中：尊严、爱与信任（4.9） · 家庭与母亲（3.5）
- 转述：《父母教育学》在给未来父亲的话中强调：要培育孩子，首先应真心诚意地爱自己的妻子。真诚的爱意味着奉献、创造和付出心智；好的丈夫用自己的爱创造妻子的美，这种爱最终会变成孩子内在的精神美。苏霍姆林斯基说，夫妻之爱像供给树木养分的须根，根坏死了，真正的父爱和母爱也就丧失了。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《父母教育学》，OCR原文页码段 `<!-- OCR 原PDF页段: p0600-0699 (0-based)

### sk-0229　农村学校的特殊使命：做农村最重要的文化中心

- 旧标签：teacher-growth, reading-and-books
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 11.67 + 先验 2.5 = 14.17））
- 其他命中：思维与智力（3.3） · 集体与同伴（3.2）
- 转述：《特殊的使命》指出，农村学校不仅是教学机构，更是农村的文化中心。当时农村青年流失严重，主要原因不是劳动教育不足，而是学校和成年人劳动集体的精神文化生活不能满足青年的需要。苏霍姆林斯基主张，农村学校首先要营造“家庭和学校充满书籍”的氛围，让农村形成善思考、勤读书、崇尚知识的风气。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《特殊的使命》，OCR原文页码段 `<!-- OCR 原PDF页段: p0600-0699 (0-based)

### sk-0230　真正的教育是为他人创造幸福

- 旧标签：love-education, child-study
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 3.42 + 先验 1.0 = 4.42））
- 其他命中：劳动与创造（3.0） · 教师（2.4）
- 转述：《人是最巨大的财富》从战争孤儿与马林娜妈妈的命运讲起。马林娜在渡船上失去三个孩子、丈夫又牺牲在前线，曾在神父那里寻找安慰；苏霍姆林斯基和学生科利亚倾听她的苦难后，科利亚成了马林娜的儿子。作者由此领悟：真正的教育是为他人创造幸福，教师是幸福的创造者。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《人是最巨大的财富》，OCR原文页码段 `<!-- OCR 原PDF页段: p0600-0699 (0-bas

### sk-0231　语言可提高人也可贬低人：最可怕的是让人相信自己微不足道

- 旧标签：teacher-growth, love-education
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 9.07 + 先验 2.5 = 11.57））
- 其他命中：思维与智力（4.0） · 幸福与精神生活（3.0）
- 转述：《人是最巨大的财富》讨论“提高人品”时提出：语言是尊重人和提高人的最重要手段，教师的语言首先应面对学生的理智和心灵。托尔斯泰说语言可以玷污人，也可以净化人；而西梅农所说的“最可怕罪行”，是让一个人相信自己与别人相比微不足道——剥夺自尊可能把人引向绝望、自杀甚至犯罪。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《人是最巨大的财富》，OCR原文页码段 `<!-- OCR 原PDF页段: p0700-0799 (0-bas

### sk-0232　义务感的培养是教育的基础和核心

- 旧标签：collective-education, child-study
- 建议：**A2 公民与祖国**（旧标签先验 + 文本证据（关键词 5.67 + 先验 1.0 = 6.67））
- 其他命中：幸福与精神生活（3.0）
- 转述：《义务感的培养》用尤拉与维克托两种命运对比：两人在同一学校、同一课桌长大，尤拉在战争中成为英雄，维克托逃避入伍、后来成了“像堵石墙”般冷酷的人。老哲人尼古拉爷爷的解释是：尤拉自幼对别人的苦乐知痛知痒，维克托的“心眼儿”却被母亲保护性隔离，从未让别人的命运进入他的心灵。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《义务感的培养》，OCR原文页码段 `<!-- OCR 原PDF页段: p0700-0799 (0-based

### sk-0233　教师说‘你应当’太多，学生说‘我应当’太少

- 旧标签：collective-education, teacher-growth
- 建议：**A4 自我教育**（旧标签先验 + 文本证据（关键词 6.44 + 先验 1.0 = 7.44））
- 其他命中：公民与祖国（5.7） · 尊严、爱与信任（4.4）
- 转述：《义务感的培养》指出，学校里每天百万次地响起“你应当”，教师像用砖头盖“履行义务的人”这座楼，但楼要坚实，必须有基础——人在义务中的表现和自我确认，把“应当”当作自我要求和良心的嘱咐。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《义务感的培养》，OCR原文页码段 `<!-- OCR 原PDF页段: p0700-0799 (0-based

### sk-0234　文学即人学：教师是弹奏青少年心灵音乐的大师

- 旧标签：reading-and-books, teacher-growth
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 15.63 + 先验 2.5 = 18.13））
- 其他命中：劳动与创造（8.4） · 美与艺术（4.5）
- 转述：《强有力的教育手段》讨论书籍与文学在教育中的地位。苏霍姆林斯基忧虑：电影、电视等技术手段把书籍排挤到次要位置，许多学校阅览室空荡无人，学生除了教科书不再读别的。他认为，读书若成为学生的精神需要，就会变成创造性和自我教育的过程；阅读是教育的强大手段。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《强有力的教育手段》，OCR原文页码段 `<!-- OCR 原PDF页段: p0700-0799 (0-bas

### sk-0235　父辈功劳不是儿女资本：儿女越要有自己的发光点

- 旧标签：family-school, labor-education
- 建议：**A8 家庭与母亲**（旧标签先验 + 文本证据（关键词 5.93 + 先验 2.5 = 8.43））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：《致父亲们的话》谈父亲在家庭教育中的“男子汉使命”。苏霍姆林斯基提醒：民间说“水有源，树有根”，但父辈的功劳与荣誉不应变成儿女坐享其成的特权；如果孩子没有自己的根，父辈的根上长出来的只会是荆棘。父辈功劳越辉煌，孩子越需要有自己的发光点。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《致父亲们的话》，OCR原文页码段 `<!-- OCR 原PDF页段: p0700-0799 (0-based

### sk-0236　父亲道德堕落是孩子的痛苦：要保护好儿童对人的爱与信心

- 旧标签：family-school, love-education
- 建议：**A20 检查知识与考查**（文本证据推翻旧标签（关键词 5.10，压过旧标签项 4.42））
- 其他命中：集体与同伴（3.7） · 幸福与精神生活（3.4）
- 转述：《致父亲们的话》用了多个儿童视角的细节：娜塔莎没有父亲，只能幻想“父亲是飞行员”来支撑自己；彼佳在茶馆旁看见醉倒的父亲，第二天上课被问到家庭情况时脸色刷白；米佳的父亲入狱，同学当众说出“米佳他爹坐牢啦”。苏霍姆林斯基指出，当儿童对“正常事物”的信心破灭时，不听话、无礼、蛮横就会出现。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《致父亲们的话》，OCR原文页码段 `<!-- OCR 原PDF页段: p0700-0799 (0-based

### sk-0237　最有诱惑力的享受是读书：让好书成为童年最大的快乐

- 旧标签：reading-and-books, teacher-growth
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 7.10 + 先验 2.5 = 9.60））
- 其他命中：幸福与精神生活（7.4）
- 转述：《今日的小学生》谈当代儿童周围充满足球、篮球、收音机、电视等诱惑。苏霍姆林斯基不反对适当消遣，但担心消遣吞噬全部精力会使人精神空虚。他认为，解决之道是让儿童在童年和少年时代就感到“读书是最有诱惑力的享受”。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《今日的小学生》，OCR原文页码段 `<!-- OCR 原PDF页段: p0700-0799 (0-based

### sk-0238　儿童不是白纸：信念培养是一场针对已有思想影响的斗争

- 旧标签：child-study, teacher-growth
- 建议：**A19 道德判断与品德培养**（文本证据推翻旧标签（关键词 6.44，压过旧标签项 4.88））
- 其他命中：自我教育（3.8） · 幸福与精神生活（3.0）
- 转述：苏霍姆林斯基在《认知与信念》中用“白纸”比喻展开论辩：入学儿童并不是等待教师任意书写的空白纸，家庭、环境和早期生活已经在他心灵上留下难以抹去的痕迹。因此，培养信念不是单向灌输，而是含有“斗争”成分的工作——教育者必须正视已经形成的善恶印象，再以更鲜明的形象和更可信的生活事实去影响儿童。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《认知与信念》，OCR原文页码段 `<!-- OCR 原PDF页段: p0700-0799 (0-based)

### sk-0239　只有亲手劳动让世界变好，道理才转化为信念

- 旧标签：labor-education, collective-education
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 2.33 + 先验 2.5 = 4.83））
- 其他命中：尊严、爱与信任（4.6） · 健康与作息（4.3） · 思维与智力（4.0）
- 转述：“讲道理”本身很难形成信念；只有当道理以真与善的形象出现，并被儿童在劳动中亲身体验到时，思想才真正支配他。苏霍姆林斯基给出的判据非常具体：孩子热汗淋淋、手上磨出趼子，亲眼看到今天的自己让世界比昨天更美好——此时语言的种子才可能生根。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《认知与信念》，OCR原文页码段 `<!-- OCR 原PDF页段: p0700-0799 (0-based)

### sk-0240　学生应当获取知识，而不是消费现成的知识

- 旧标签：teacher-growth, labor-education
- 建议：**A4 自我教育**（旧标签先验 + 文本证据（关键词 4.43 + 先验 1.0 = 5.43））
- 其他命中：全面发展与个性（4.4） · 公民与祖国（4.0）
- 转述：苏霍姆林斯基区分了两种学习状态：“获取知识”和“消费知识”。消费现成知识，就是听讲、记住、背诵、按老师要求“取出资料”；获取知识，则是学生在思想和意志紧张活动中的主动认知。只有后一种状态才使教学具有教育力，才能使关于理想与责任的谈话真正进入学生内心。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《遵循列宁思想办学》，OCR原文页码段 `<!-- OCR 原PDF页段: p0700-0799 (0-bas

### sk-0241　信念不能机械传授，只能在集体智力生活的空气中磨炼

- 旧标签：collective-education, teacher-growth
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 6.83 + 先验 1.0 = 7.83））
- 其他命中：思维与智力（7.5） · 自我教育（3.8）
- 转述：苏霍姆林斯基认为，信念不是知识点的附属品：它不能像作业一样“留下去背”，不能靠记忆硬灌。信念的形成需要磨炼，而这种磨炼只有在集体智力生活丰富时才可能发生——学生在共同的思想交流、阅读、争论、劳动与相互关系中，把自己的认识变成个人立场。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《遵循列宁思想办学》，OCR原文页码段 `<!-- OCR 原PDF页段: p0700-0799 (0-bas

### sk-0242　把学生锻炼成勇敢的战士：用爱武装心，也用恨擦亮眼

- 旧标签：collective-education, child-study
- 建议：**A2 公民与祖国**（旧标签先验 + 文本证据（关键词 7.98 + 先验 1.0 = 8.98））
- 其他命中：健康与作息（4.8） · 家庭与母亲（3.5）
- 转述：《把学生锻炼成胜利者》从三年级的维佳看到战争照片后追问父母的故事出发，说明儿童公民精神可以在具体事件中被点燃。苏霍姆林斯基在此概括教育使命：既要以爱与忠诚使心灵高尚，也要以对不义和压迫的愤怒与不妥协使学生获得精神武器。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《把学生锻炼成胜利者》，OCR原文页码段 `<!-- OCR 原PDF页段: p0700-0799 (0-ba

### sk-0243　思想的勇敢：敢于把世界上发生的事当成自己的事

- 旧标签：child-study, collective-education
- 建议：**A7 健康与作息**（文本证据推翻旧标签（关键词 9.08，压过旧标签项 6.44））
- 其他命中：道德判断与品德培养（6.4） · 全面发展与个性（4.4）
- 转述：苏霍姆林斯基把“勇敢”从身体层面提升到思想层面。儿童如果敢于思考世界上的善恶斗争，并把远处的不义与自己的命运联系起来，就不会自感渺小无力；这种“思想的勇敢”能生长出面向未来、敢于行动的精神状态。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《把学生锻炼成胜利者》，OCR原文页码段 `<!-- OCR 原PDF页段: p0700-0799 (0-ba

### sk-0244　公益劳动要进入儿童的精神生活，成为心爱的劳动

- 旧标签：labor-education, collective-education
- 建议：**A2 公民与祖国**（旧标签先验 + 文本证据（关键词 4.05 + 先验 1.0 = 5.05））
- 其他命中：幸福与精神生活（3.8） · 劳动与创造（2.3）
- 转述：《劳动与斗争》强调的不是“让学生多干活”，而是让公益劳动成为儿童精神生活的核心内容之一。判断标准很形象：孩子是否“睡觉也梦见”自己心爱的劳动——这种热爱不是因为任务轻省，而是因为他感到自己的劳动让世界变得更美好。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《劳动与斗争》，OCR原文页码段 `<!-- OCR 原PDF页段: p0800-0899 (0-based)

### sk-0245　让儿童亲手看到世界因自己的劳动改变，预防坐享其成

- 旧标签：labor-education, collective-education
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 10.14 + 先验 2.5 = 12.64））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：这一段把“劳动教育”与“消费心态”对立起来：如果儿童从小只享受别人创造的成果，就容易把世界看作现成福利，缺少主人翁感。苏霍姆林斯基提出的对策是让儿童用自己的双手、按自己的良好意愿去创造，亲眼看到世界因自己而改变。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《劳动与斗争》，OCR原文页码段 `<!-- OCR 原PDF页段: p0800-0899 (0-based)

### sk-0246　在童年树立终生信念：人类是大自然的孩子

- 旧标签：aesthetic-nature-education, thinking-and-nature
- 建议：**A12 自然与思维课**（旧标签先验 + 文本证据（关键词 9.81 + 先验 1.0 = 10.81））
- 其他命中：全面发展与个性（5.1） · 自我教育（3.8）
- 转述：苏霍姆林斯基在《大自然、劳动和世界观》中反复讲述水塘、草场、土壤等故事，都是为了在学生童年时代种下一种世界观：人不是自然的征服者或旁观者，而是自然的孩子；自然界的和谐一旦被破坏，人类也就失去享用财富的根基。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《大自然、劳动和世界观》，OCR原文页码段 `<!-- OCR 原PDF页段: p0800-0899 (0-b

### sk-0247　大自然和劳动密不可分：不避任何劳动，才能做自然的知恩之子

- 旧标签：labor-education, aesthetic-nature-education
- 建议：**A12 自然与思维课**（旧标签先验 + 文本证据（关键词 4.14 + 先验 1.0 = 5.14））
- 其他命中：劳动与创造（2.3）
- 转述：在苏霍姆林斯基看来，热爱自然不能停留在观赏层面；人对自然的感恩要通过劳动来表达。肥料、铁锹、运土、浇水这些并不浪漫甚至“了无趣味”的劳动，恰恰是人与自然建立真实关系的方式。只愿意欣赏自然之美、不愿为自然出力的人，谈不上对自然的珍爱。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《大自然、劳动和世界观》，OCR原文页码段 `<!-- OCR 原PDF页段: p0800-0899 (0-b

### sk-0248　羞耻心是卑污和丑恶的抗毒素

- 旧标签：child-study, love-education
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 4.38 + 先验 2.5 = 6.88））
- 其他命中：思维与智力（3.7） · 幸福与精神生活（3.0）
- 转述：《清泉》从一名19岁死囚的自白写起，讨论人为何会因“思维幼稚”与心灵空虚而犯罪。苏霍姆林斯基给出的预防性答案是发展羞耻心：一个能在懒惰、闲散、丑恶面前感到羞耻的人，内心才有托住良心、荣誉和人格的“深广水域”。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《清泉》，OCR原文页码段 `<!-- OCR 原PDF页段: p0800-0899 (0-based) --

### sk-0249　用体验自由界限的方法教儿童学会控制愿望（罗曼的一天）

- 旧标签：child-study, love-education
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 3.99 + 先验 1.0 = 4.99））
- 其他命中：健康与作息（4.3） · 集体与同伴（3.7）
- 转述：文中男孩罗曼好斗冲动，常“无缘无故”打同学。苏霍姆林斯基没有长篇说教，而是把罗曼的右手用绷带绑在裤兜里，自己也照样绑起右手陪他度过一整天。罗曼在亲身体验“失去自由”后，开始琢磨假如真的失去自由生活会怎样，慢慢学着控制自己。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《清泉》，OCR原文页码段 `<!-- OCR 原PDF页段: p0800-0899 (0-based) --

### sk-0250　劳动教育是‘应该劳动’、‘劳动艰苦’和‘劳动美好’的统一

- 旧标签：labor-education, family-school
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 15.45 + 先验 2.5 = 17.95））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：苏霍姆林斯基把劳动教育概括为三个缺一不可的因素：“应该劳动”——义务与责任感；“劳动艰苦”——承认劳动需要付出努力、并非享乐；“劳动美好”——从劳动成果与创造中获得精神愉悦。三者必须和谐统一，缺了任何一方都会使劳动教育走样。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《“应该劳动”、“劳动艰苦”和“劳动美好”三个因素的和谐统一》，OCR原文页码段 `<!-- OCR 原PDF

### sk-0251　当思维成为劳动、学校成为劳动王国，学生就会崇尚任何劳动

- 旧标签：labor-education, teacher-growth
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 7.79 + 先验 2.5 = 10.29））
- 其他命中：幸福与精神生活（4.0） · 思维与智力（3.7）
- 转述：苏霍姆林斯基把“善于思维”视为克服职业歧视的根本途径：当学生在学习生活中亲自体验到真正的脑力劳动极其艰苦、也极其美好，他就不再认为只有“当物理学家或数学家”才光荣，而能理解钳工、拖拉机手、饲养员同样需要艰苦而诚实的劳动。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《“应该劳动”、“劳动艰苦”和“劳动美好”三个因素的和谐统一》，OCR原文页码段 `<!-- OCR 原PDF

### sk-0252　爱是一种艰苦劳动：在子女身上延续自己

- 旧标签：family-school, love-education
- 建议：**A11 劳动与创造**（文本证据推翻旧标签（关键词 7.79，压过旧标签项 2.50））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：《我们在儿童身上延续自己》通过老寿星、父亲斯捷潘、被生父抛弃后由继父养大的儿子等故事，讨论家庭与亲子关系的精神本质。苏霍姆林斯基认为，爱不是突来的灵感或祥光，而是一种需要勇气和坚持的“劳动”，其目的不是占有孩子，而是在孩子身上再塑并延续自己内在的精神美。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《我们在儿童身上延续自己》，OCR原文页码段 `<!-- OCR 原PDF页段: p0800-0899 (0-

### sk-0253　儿童通过劳动认识世界，并在劳动中形成道德标准

- 旧标签：family-school, labor-education
- 建议：**A19 道德判断与品德培养**（文本证据推翻旧标签（关键词 10.13，压过旧标签项 8.43））
- 其他命中：家庭与母亲（5.9） · 劳动与创造（2.3）
- 转述：在奥莉娅与奶奶一起做家务的故事中，苏霍姆林斯基看到劳动对幼童认知与道德的双重作用：孩子不是先学抽象道理再劳动，而是在“我俩在干活”“我俩累了”的共同劳动中认识世界、认识他人，并逐渐形成什么是勤快、什么是懒散的道德判断。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《我们在儿童身上延续自己》，OCR原文页码段 `<!-- OCR 原PDF页段: p0800-0899 (0-

### sk-0254　教学首先是人与人之间的关系

- 旧标签：teacher-growth, love-education
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 5.10 + 先验 1.0 = 6.10））
- 其他命中：评价与分数（4.2） · 道德判断与品德培养（3.0）
- 转述：《关于教育道德的一封信》用阿纳托利的故事说明：教师若只把教学看成知识搬运，把成绩当成评判学生的全部，就看不见学生内心积累的委屈、恐惧与孤独。苏霍姆林斯基提出，教学首先不是“知识从教师头脑到学生头脑”的机械过程，而是人与人之间的关系。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《关于教育道德的一封信》，OCR原文页码段 `<!-- OCR 原PDF页段: p0800-0899 (0-b

### sk-0255　教师道德不容许一个学生感到自己孤独

- 旧标签：teacher-growth, child-study
- 建议：**A3 幸福与精神生活**（文本证据推翻旧标签（关键词 8.08，压过旧标签项 6.30））
- 其他命中：检查知识与考查（6.0） · 全面发展与个性（5.2）
- 转述：阿纳托利的故事中，女教师只看见他“不会做题”“不交手册”，却看不见他失去爷爷、被同学嘲笑、把作业本埋进土里等一连串无声的痛苦。苏霍姆林斯基由此提出教师道德的最低要求：不容许学生独自承受痛苦，也不容许学生无人分享欢乐。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《关于教育道德的一封信》，OCR原文页码段 `<!-- OCR 原PDF页段: p0800-0899 (0-b

### sk-0256　教育的艺术：教师每次接触都是对心灵劳动的推动

- 旧标签：teacher-growth, child-study
- 建议：**A4 自我教育**（旧标签先验 + 文本证据（关键词 4.43 + 先验 1.0 = 5.43））
- 其他命中：美与艺术（4.2） · 幸福与精神生活（3.0）
- 转述：《心灵的劳动》提出一个反直觉的机制：教师越少显露强制痕迹，越能激发学生内在力量。教师的意志应当强大，但对学生来说又应“不易觉察”——苏霍姆林斯基称之为心灵劳动的推动力。学生应当感到没有人在敦促他、搀扶他，才能成为自己的教育者。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《心灵的劳动》，OCR原文页码段 `<!-- OCR 原PDF页段: p0800-0899 (0-based)

### sk-0257　心灵劳动是与亲人的忧患与共：不要怕向年轻心灵揭示痛苦

- 旧标签：love-education, child-study
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 6.95 + 先验 1.0 = 7.95））
- 其他命中：健康与作息（5.9） · 劳动与创造（2.3）
- 转述：苏霍姆林斯基把“心灵的劳动”定义为对他人命运的深度参与：不只是分享快乐，更包括与亲人忧患与共、同甘共苦。他反对把孩子隔离在一切痛苦之外；适当让年轻心灵接触家人的辛劳、疾病、忧伤甚至离别，反而能使人高尚。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《心灵的劳动》，OCR原文页码段 `<!-- OCR 原PDF页段: p0800-0899 (0-based)

### sk-0258　人的道德自我不可分割：不能过双重生活

- 旧标签：family-school, love-education
- 建议：**A2 公民与祖国**（旧标签先验 + 文本证据（关键词 9.39 + 先验 1.0 = 10.39））
- 其他命中：全面发展与个性（4.4） · 道德判断与品德培养（3.0）
- 转述：《纯洁与高尚》讨论私人生活与公共人格的关系。苏霍姆林斯基引用车尔尼雪夫斯基“每个人都有一个任何人不该闯入的生活角落”，强调要保护每个人私密的“小天地”，但同时指出这个角落不能与社会大天地割裂：在家庭、爱情、私人关系里阴暗肮脏的人，不可能在公共生活中真正高尚。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《纯洁与高尚》，OCR原文页码段 `<!-- OCR 原PDF页段: p0900-0923 (0-based)

### sk-0259　在爱与忠诚的领域里，做忠实丈夫和父亲比超产更难

- 旧标签：family-school, love-education
- 建议：**A1 全面发展与个性**（文本证据推翻旧标签（关键词 4.43，压过旧标签项 2.50））
- 其他命中：劳动与创造（2.3）
- 转述：文中工程师安德烈在集会上慷慨陈词，愿去遥远国家支援建设，却在女友怀孕时想逃避责任；公众由此看清他“高昂激情”下藏着的自私。苏霍姆林斯基借这个故事指出：一个人最容易被考察的地方，往往不是公共讲台，而是爱与忠诚这类最微妙的私人领域。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《纯洁与高尚》，OCR原文页码段 `<!-- OCR 原PDF页段: p0900-0923 (0-based)

### sk-0260　只有愿意学习并以此为欢乐，学习才会成为骄傲

- 旧标签：child-study, reading-and-books
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 7.10 + 先验 2.5 = 9.60））
- 其他命中：评价与分数（4.8） · 幸福与精神生活（4.0）
- 转述：《致学生们的一席话》是苏霍姆林斯基对学生的告别式讲话。他指出一个时代矛盾：学习普及并成为义务后，有些年轻人反而把它看成负担、惩罚甚至折磨。他提醒学生，如果内心不愿学习，学习和未来的生活都难有成就；只有当学习被体验为欢乐和人的骄傲时，一切才可能实现。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《致学生们的一席话》，OCR原文页码段 `<!-- OCR 原PDF页段: p0900-0923 (0-bas

### sk-0261　课堂之外要有思考的园地：见识、观察、做，三者齐备

- 旧标签：thinking-and-nature, labor-education
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 6.67 + 先验 2.5 = 9.17））
- 其他命中：了解儿童（3.4） · 教师（2.4）
- 转述：苏霍姆林斯基告诫学生：学习不能被封闭在课堂里，不能只是把事实和真理从教师头脑搬进学生头脑。与课堂并存的应有一块“智力劳动的园地”——它不需要很大，哪怕只是一个装土的小箱子，关键是让学生同时“见识、观察、做”。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社，2001），论文《致学生们的一席话》，OCR原文页码段 `<!-- OCR 原PDF页段: p0900-0923 (0-bas

### sk-0262　创造成功的“预感”，是培养学习愿望的最重要任务

- 旧标签：learning-difficulties, teacher-growth
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88））
- 其他命中：学习困难学生（5.8） · 劳动与创造（3.0）
- 转述：苏霍姆林斯基分析八年级学生学业冷漠后发现，后进生并非天生不愿学习，而是长期看不到自己的进步，形成“我只能得3分”的自我定势。教师最重要的任务不是降低难度或空洞鼓励，而是让学生真实地预感到“我也能成功”，把这种成功预感变成推动持续学习的愿望。
- 出处：论文《学习兴趣是学生学习活动的重要动力》，OCR原文页码段 `<!-- OCR 原PDF页段: p0000-0099 (0-based) -->`

### sk-0263　教师课堂上的精神语调，直接影响学习愿望

- 旧标签：teacher-growth, learning-difficulties
- 建议：**A6 了解儿童**（旧标签先验 + 文本证据（关键词 3.37 + 先验 2.5 = 5.87））
- 其他命中：评价与分数（4.2） · 思维与智力（3.3）
- 转述：苏霍姆林斯基观察到，有的课从教学法角度看无懈可击，但教师讲述萎靡不振，学生反而更累；教师对教材无动于衷的态度会“传导”给学生，使教材像一堵高墙立在师生之间。真正能培养学习愿望的课，应激起学生真正的激动、满足和紧张思考后的倦意。
- 出处：论文《学习兴趣是学生学习活动的重要动力》，OCR原文页码段 `<!-- OCR 原PDF页段: p0000-0099 (0-based) -->`

### sk-0264　爱国主义不是漂亮言词，而是见之于行动的公益劳动

- 旧标签：labor-education, collective-education
- 建议：**A2 公民与祖国**（旧标签先验 + 文本证据（关键词 9.28 + 先验 1.0 = 10.28））
- 其他命中：幸福与精神生活（6.3） · 评价与分数（4.8）
- 转述：苏霍姆林斯基批评一种常见缺点：学生谈起对祖国的义务头头是道，却对工厂和集体农庄的劳动避而远之。爱国情感不是说出来的，而是在生活活动中形成，首先要在公益劳动中把观念变成行动；劳动之所以重要，与其说看成果，不如说看它对心灵的教育影响。
- 出处：论文《关于苏维埃爱国主义教育的几点看法》，OCR原文页码段 `<!-- OCR 原PDF页段: p0000-0099 (0-based) -->`

### sk-0265　童年没体验过为集体无偿劳动的欢乐，灵魂会沾上小市民习气

- 旧标签：labor-education, family-school
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 7.01 + 先验 2.5 = 9.51））
- 其他命中：习惯与纪律（4.8） · 幸福与精神生活（4.0）
- 转述：苏霍姆林斯基向家庭提出：只培养孩子做家务、甚至设法让孩子躲避无偿公益劳动，是一种片面且危险的教育。童年若从不曾为集体无偿地付出，人会把一切劳动都折算成个人报酬，道德面貌会与集体主义社会格格不入。
- 出处：论文《关于苏维埃爱国主义教育的几点看法》，OCR原文页码段 `<!-- OCR 原PDF页段: p0000-0099 (0-based) -->`

### sk-0266　道德美不只看怎样评价现实，而首先看积极的活动

- 旧标签：collective-education, teacher-growth
- 建议：**A4 自我教育**（旧标签先验 + 文本证据（关键词 9.75 + 先验 1.0 = 10.75））
- 其他命中：评价与分数（4.8） · 道德判断与品德培养（3.0）
- 转述：苏霍姆林斯基用“见死不救者不受法律追究却丧失人格”的例子说明：不违法不等于有道德。学校的任务不是让学生只会背诵道德规范或口头谴责坏事，而是让违背道德的行为被内心视为严重罪过，并用舍己救人的实际行动证明道德信念。
- 出处：论文《共产主义思想是德育的基础》，OCR原文页码段 `<!-- OCR 原PDF页段: p0000-0099 (0-based) -->`

### sk-0267　劳动的教育价值不在气力大小，而在坚定的目的性

- 旧标签：labor-education, collective-education
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 5.31 + 先验 2.5 = 7.81））
- 其他命中：评价与分数（4.8） · 集体与同伴（3.2）
- 转述：苏霍姆林斯基指出，学生到集体农庄劳动干得不错，但若主要目的只是为自己多赚钱，这种劳动就缺少共产主义教育价值。他主张让学生从入学起就把大部分辛勤劳动献给集体和社会，劳动创造的物质价值越是全民财富，劳动越能塑造高尚道德面貌；他甚至批评用“多交废钢铁给奖金”刺激劳动，因为私欲会遮蔽劳动的光明思想。
- 出处：论文《共产主义思想是德育的基础》，OCR原文页码段 `<!-- OCR 原PDF页段: p0000-0099 (0-based) -->`

### sk-0268　无神论教育不能只靠谈话，要用积极活动见诸行动

- 旧标签：labor-education, collective-education
- 建议：**A3 幸福与精神生活**（文本证据推翻旧标签（关键词 12.39，压过旧标签项 10.31））
- 其他命中：劳动与创造（7.8） · 集体与同伴（5.9）
- 转述：苏霍姆林斯基认为，宗教影响抓住的是人的情感、审美和孤独感；抵御它不能只靠科学谈话，而要靠符合年龄的、能带来胜利喜悦和紧张努力的创造活动。孩子在活动中体验人类双手与思想的创造力，才能从内心摆脱“命运由超自然力量决定”的观念。
- 出处：论文《从小成为无神论者》，OCR原文页码段 `<!-- OCR 原PDF页段: p0000-0099 (0-based) -->`

### sk-0269　在创造性劳动中获得欢乐的人，会成为反对宗教欺骗的积极战士

- 旧标签：labor-education, child-study
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 5.31 + 先验 2.5 = 7.81））
- 其他命中：全面发展与个性（4.4）
- 转述：苏霍姆林斯基从玛丽亚等学生的转变中总结：一个人若把劳动只当作乏味负担，就容易被“来世”之类的许诺吸引；反之，当劳动成为创造、给人生活欢乐，人就能在个人经验中看到现实与理想的统一，并有力量影响周围仍受宗教观念束缚的人。
- 出处：论文《从小成为无神论者》，OCR原文页码段 `<!-- OCR 原PDF页段: p0000-0099 (0-based) -->`

### sk-0270　教育与生活脱节的本质：动手没有丰富智力，智慧没有用于创造

- 旧标签：labor-education, teacher-growth
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 10.98 + 先验 2.5 = 13.48））
- 其他命中：思维与智力（11.2） · 幸福与精神生活（3.8）
- 转述：苏霍姆林斯基反对把“教育与生活脱节”简单理解为脑力劳动太多、体力劳动太少，于是加大体力劳动比例。真正的问题是两种劳动没有有机结合：动手不动脑，动脑不用于创造。只有让动手工作包含思维、让知识用于解决生活问题，精神生活才和谐统一。
- 出处：论文《脑力劳动及学校与生活的联系》，OCR原文页码段 `<!-- OCR 原PDF页段: p0000-0099 (0-based) -->`

### sk-0271　死记的知识越积越多越难学；分析得来的知识越学越轻松

- 旧标签：learning-difficulties, teacher-growth
- 建议：**A10 教师**（全无关键词证据，按旧标签先验定夺）
- 其他命中：学习困难学生（6.4）
- 转述：苏霍姆林斯基发现，不少低年级优等生到中年级变成差生，原因是概念、结论靠死记硬背得来，不会用来认识周围事物，结果知识越多负担越重，形成“积累越多越学不动”的怪圈。反之，凡是通过分析事实和现象形成的知识，能作为工具帮助理解新知识，学得越广反而越轻松。
- 出处：论文《脑力劳动及学校与生活的联系》，OCR原文页码段 `<!-- OCR 原PDF页段: p0100-0199 (0-based) -->`

### sk-0272　所有孩子都有才，关键是找到并开发其独有能力

- 旧标签：child-study, teacher-growth
- 建议：**A6 了解儿童**（旧标签先验 + 文本证据（关键词 3.37 + 先验 2.5 = 5.87））
- 其他命中：学习困难学生（5.8） · 思维与智力（3.4）
- 转述：苏霍姆林斯基以巴甫利克为例：一个被教师判定“没有掌握知识能力”的后进生，在植物栽培劳动中却显露出惊人的观察力和实验才能，由此智力全面觉醒。他由此断言孩子没有“有才无才”之分，教育者的任务是在每个学生身上找到独有才能并加以开发。
- 出处：论文《开发出每个学生独特的人格之美》，OCR原文页码段 `<!-- OCR 原PDF页段: p0100-0199 (0-based) -->`

### sk-0273　教师要做灵巧的珠宝匠，开发每个学生独特的人格之美

- 旧标签：child-study, teacher-growth
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88））
- 其他命中：劳动与创造（3.0）
- 转述：苏霍姆林斯基用珠宝作比：灰暗的宝石经珠宝匠之手会闪闪发光；学生也是如此，一旦创造力被开发，就会放出各具特色的光彩。教育不是把所有人塑造成一个模子，而是把每个人的独特性提升到完美人格的高度。
- 出处：论文《开发出每个学生独特的人格之美》，OCR原文页码段 `<!-- OCR 原PDF页段: p0100-0199 (0-based) -->`

### sk-0274　劳动吸引孩子，是因为通向诱人目的的新世界，而不是重复动作

- 旧标签：labor-education, thinking-and-nature
- 建议：**A3 幸福与精神生活**（文本证据推翻旧标签（关键词 7.64，压过旧标签项 4.83））
- 其他命中：了解儿童（3.8） · 劳动与创造（2.3）
- 转述：苏霍姆林斯基在葡萄园劳动实验中看到，孩子最初热爱劳动，不是因为“挖坑运肥”本身有趣，而是劳动带他们进入一个新世界，脏活累活只是通往诱人成果的通道。一旦新事物变成司空见惯的重复，兴趣就会消退。
- 出处：论文《怎样培养学生热爱劳动》，OCR原文页码段 `<!-- OCR 原PDF页段: p0100-0199 (0-based) -->`

### sk-0275　别把日常劳动当作终点，而要不断翻开“大自然之书”的新页

- 旧标签：labor-education, teacher-growth
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 2.33 + 先验 2.5 = 4.83））
- 其他命中：自然与思维课（4.1） · 阅读与书籍（2.9）
- 转述：面对少年对葡萄园劳动从狂热到冷淡，苏霍姆林斯基没有强迫，而是不断引入新实验——乙烯气催花、根接葡萄、营养筒引根、土壤微生物实验——让同一块园地持续出现“前所未闻”的惊奇。普通劳动因此永远有翻开新页的吸引力。
- 出处：论文《怎样培养学生热爱劳动》，OCR原文页码段 `<!-- OCR 原PDF页段: p0100-0199 (0-based) -->`

### sk-0276　教师对自己工作的热爱，像火一样点燃学生的热情

- 旧标签：teacher-growth, labor-education
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 16.30 + 先验 2.5 = 18.80））
- 其他命中：美与艺术（4.2） · 教师（2.4）
- 转述：苏霍姆林斯基讲述物理教师列昂尼德的故事：他不仅是学科教师，还是技术创造的艺术家，课余亲手制作精美工具、带领学生设计自动化生产线。正是教师自身对创造性劳动的热爱，让学生看见“劳动能带来乐趣”，进而产生模仿与向往。
- 出处：论文《社会与教师》，OCR原文页码段 `<!-- OCR 原PDF页段: p0100-0199 (0-based) -->`

### sk-0277　教师一旦停止知识增长，就不再是学生的知识灯塔

- 旧标签：teacher-growth
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88））
- 其他命中：劳动与创造（2.3）
- 转述：苏霍姆林斯基记述一位老物理教师的故事：乡镇青年工人已在讨论基本粒子等前沿问题，老教师却因多年未更新知识而无法应约开讲座，最终由一位好学的年轻毕业生完成。社会文化水平不断提高，教师必须持续学习，否则连身边的劳动者都会超越他。
- 出处：论文《社会与教师》，OCR原文页码段 `<!-- OCR 原PDF页段: p0100-0199 (0-based) -->`

### sk-0278　让学校里不存在一个没有个性的学生

- 旧标签：child-study, teacher-growth
- 建议：**A6 了解儿童**（旧标签先验 + 文本证据（关键词 3.80 + 先验 2.5 = 6.30））
- 其他命中：全面发展与个性（4.4） · 劳动与创造（3.0）
- 转述：苏霍姆林斯基所说的“没有个性”，指对什么都不感兴趣、什么都不能让他感动或着迷的学生。学校的目标不是让每个孩子门门一样，而是从入学第一天起就帮他找到能投入、能着迷的事，发展创造力并形成生活志向。
- 出处：论文《发展学生的个人能力与爱好》，OCR原文页码段 `<!-- OCR 原PDF页段: p0100-0199 (0-based) -->`

### sk-0279　一个人只有也在教育别人时，才能更好地受教育

- 旧标签：collective-education, teacher-growth
- 建议：**A9 集体与同伴**（旧标签先验 + 文本证据（关键词 3.16 + 先验 2.5 = 5.66））
- 其他命中：劳动与创造（5.3）
- 转述：苏霍姆林斯基认为，把低年级与高年级分开并不利于教育；不同年龄学生在同一创造性劳动集体中，高年级向低年级传授技能，会促使自己把技能练得更好。劳动技能与热爱劳动的品质，正是在“教别人”的过程中代代相传。
- 出处：论文《发展学生的个人能力与爱好》，OCR原文页码段 `<!-- OCR 原PDF页段: p0100-0199 (0-based) -->`

### sk-0280　年轻人应当生活得艰苦些——这是最崇高的人道意义

- 旧标签：labor-education, family-school
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 22.28 + 先验 2.5 = 24.78））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：苏霍姆林斯基看到青年对损坏公物无动于衷，痛感教育把物质财富给得太轻易，使孩子以为一切都是“天上掉下来的”。他主张不必人为制造艰苦，但要善于看到生活中真实存在的艰苦、不绕道而过；人只有付出心血，才会珍惜和珍重。
- 出处：论文《别让心灵锈斑斑》，OCR原文页码段 `<!-- OCR 原PDF页段: p0200-0299 (0-based) -->`

### sk-0281　在孩子面前揭示生活欢乐的劳动本源，是德育的最重要任务

- 旧标签：labor-education, family-school
- 建议：**A8 家庭与母亲**（旧标签先验 + 文本证据（关键词 4.14 + 先验 2.5 = 6.64））
- 其他命中：评价与分数（4.8） · 幸福与精神生活（3.4）
- 转述：苏霍姆林斯基带一年级孩子开垦10平方米“铁板地”，从搬石、运肥、播种到收获小麦、烤成面包请家长吃。孩子们第一次把面包和自己的汗珠联系起来，产生了“道德权利享用生活欢乐”的最初思考。劳动在此不是惩罚，而是揭示幸福来源的教育途径。
- 出处：论文《别让心灵锈斑斑》，OCR原文页码段 `<!-- OCR 原PDF页段: p0200-0299 (0-based) -->`

### sk-0282　一个人全面发展的基础，孕育于自己所喜爱的劳动之中

- 旧标签：labor-education, child-study
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 5.31 + 先验 2.5 = 7.81））
- 其他命中：幸福与精神生活（7.8） · 全面发展与个性（5.0）
- 转述：苏霍姆林斯基从普拉克西、帕纳先科、沙波瓦洛夫等普通劳动者身上看到：真正全面发展的人不是样样浅尝辄止，而是在自己热爱的劳动中深耕细作，由此获得精神生活的丰富、文化修养和创造的快乐。劳动不是全面发展的对立面，而是其根基。
- 出处：论文《劳动是人全面发展的基础》（OCR中该篇为二级标题），OCR原文页码段 `<!-- OCR 原PDF页段: p0200-0299 (0-based) -->`

### sk-0283　热爱的工作是人的根：根扎得越深，自尊感越强

- 旧标签：labor-education
- 建议：**A5 尊严、爱与信任**（文本证据推翻旧标签（关键词 9.70，压过旧标签项 7.81））
- 其他命中：劳动与创造（5.3）
- 转述：护林员沙波瓦洛夫用树根比喻职业与人生：他35年栽育三百多万株树，仍觉得工作越做越珍贵。苏霍姆林斯基借此说明，劳动岗位的转换不是目的；只有在自己热爱的工作中扎根，人才会形成稳定而深刻的尊严感与创造力。
- 出处：论文《劳动是人全面发展的基础》（OCR中该篇为二级标题），OCR原文页码段 `<!-- OCR 原PDF页段: p0200-0299 (0-based) -->`

### sk-0284　语言是教育科学变成教师教学艺术的桥梁

- 旧标签：teacher-growth
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88））
- 其他命中：美与艺术（4.2） · 思维与智力（4.0）
- 转述：苏霍姆林斯基反对轻视谈话教育。他认为行为、劳动虽然重要，但决定它们的是人的内心活动，而语言是影响内心活动的重要工具；没有生动深入的语言，就没有真正的学校与教育。教育科学只有经由教师的语言才能活起来。
- 出处：论文《谈语言的教育作用》，OCR原文页码段 `<!-- OCR 原PDF页段: p0200-0299 (0-based) -->`

### sk-0285　语言如刻刀：能塑造美丽心灵，也能摧毁它

- 旧标签：teacher-growth, reading-and-books
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88））
- 其他命中：美与艺术（4.2） · 思维与智力（4.0） · 幸福与精神生活（3.0）
- 转述：苏霍姆林斯基在文章结尾向教师建议：想使教学成为艺术，就要磨砺语言，从民族语言的宝库中寻找能让孩子眼睛闪光的词语。语言不是次要工具，而是能深入性格细微处、既能塑造也能摧毁心灵的力量，因此必须慎重而精湛地使用。
- 出处：论文《谈语言的教育作用》，OCR原文页码段 `<!-- OCR 原PDF页段: p0200-0299 (0-based) -->`

### sk-0286　找到自己的志向，就是找到自己的幸福与做人尊严

- 旧标签：labor-education, child-study
- 建议：**A3 幸福与精神生活**（文本证据推翻旧标签（关键词 7.39，压过旧标签项 7.14））
- 其他命中：公民与祖国（7.1） · 尊严、爱与信任（4.9）
- 转述：苏霍姆林斯基回答女青年斯维特兰娜的困惑：志向不是天生注定的，而是人在劳动中逐步形成和确认的。一个人若选择了不符合志向的道路，即使工作体面也不会幸福；只有当他在所爱劳动中证实自身价值，个人快乐与社会责任才会融合。
- 出处：论文《劳动·志向·幸福》，OCR原文页码段 `<!-- OCR 原PDF页段: p0200-0299 (0-based) -->`

### sk-0287　幸福靠自己亲手创造，劳动和创造的乐趣不会从天而降

- 旧标签：labor-education, family-school
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 9.99 + 先验 2.5 = 12.49））
- 其他命中：幸福与精神生活（3.4）
- 转述：苏霍姆林斯基劝告青年：不要等待志向自动降临，也不要指望天上掉馅饼。人只有在劳动中付出心血、认识自身价值之后，才会真正爱上工作；也只有这样，幸福才会成为自己挣得的东西。
- 出处：论文《劳动·志向·幸福》，OCR原文页码段 `<!-- OCR 原PDF页段: p0200-0299 (0-based) -->`

### sk-0288　信念不只是知道，而首先是把知识变为行动

- 旧标签：collective-education, child-study
- 建议：**A4 自我教育**（文本证据推翻旧标签（关键词 21.31，压过旧标签项 3.31））
- 其他命中：幸福与精神生活（3.3） · 道德判断与品德培养（3.0）
- 转述：苏霍姆林斯基区分了“知道道德概念”和“形成道德信念”：信念的标志不是能复述知识，而是知识已经进入人的精神世界，与情感、意志融合，并在行动中表现出来。德育的最终结果不是记住道理，而是言行一致。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》第4章“德育”之“从道德概念到道德信念的途径”，OCR 原PDF页段：p0200-0299 (0-based

### sk-0289　全人类道德准则只有通过主动行动才成为个人良知

- 旧标签：collective-education, child-study
- 建议：**A19 道德判断与品德培养**（文本证据推翻旧标签（关键词 2.99，压过旧标签项 2.50））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：帕夫雷什中学把“讲解和诱导、说服和激发”结合起来，但他们强调：光让孩子知道“什么好、什么不好”是不够的。道德准则要内化为个人良知，必须经由孩子主动做出的、具有社会性质的行为。道德教育从儿童有意识生活一开始就进行，但落脚点始终是积极行动。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》第4章“德育”之“公民基础——道德教育的基本环节”，OCR 原PDF页段：p0200-0299 (0-bas

### sk-0290　不要粉饰现实：不能让孩子在家里和会上讲两套话

- 旧标签：child-study, collective-education
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 4.62 + 先验 1.0 = 5.62））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：苏霍姆林斯基反对在儿童周围制造“思想上无菌的环境”。他认为粉饰生活会带来认识上的教条主义、怀疑主义和对崇高目标的不信任；诚实教育的前提，是成人不要求孩子过双重生活——私下说一套、公开说另一套。学校生活应当充满正义和诚挚精神。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》第4章“德育”之“@培养诚实和荣誉感”（OCR标题原带“@”符号，[OCR待校]），OCR 原PDF页段：p

### sk-0291　教师不把知识积累当最终目的，才能实现智育

- 旧标签：teacher-growth, child-study
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 6.67 + 先验 1.0 = 7.67））
- 其他命中：全面发展与个性（5.1） · 自我教育（3.8）
- 转述：智育不等于知识量的堆砌。苏霍姆林斯基认为，智育的核心是世界观的形成和智力的发展；只有当知识变成个人信念、影响人的思想方向和社会积极性时，知识获取过程才成为智育的要素。教师如果把“积累知识”当作终点，就偏离了智育的本质。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》第5章“智育”之“智育的本质及其任务”，OCR 原PDF页段：p0300-0399 (0-based)

### sk-0292　劳动的快乐首先来自劳动的美

- 旧标签：health-first, labor-education
- 建议：**A7 健康与作息**（旧标签先验 + 文本证据（关键词 13.77 + 先验 2.5 = 16.27））
- 其他命中：幸福与精神生活（7.3） · 劳动与创造（5.3）
- 转述：苏霍姆林斯基把体力劳动放在“健康与体育”框架下讨论：协调优美的劳动动作可以同体操媲美，劳动之美又反过来吸引学生投入户外体力劳动。他观察到，长期从事这类劳动的学生身体匀称、体态端正、动作优美，在劳动中寻求美，也创造自身的美。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》第3章“关注健康与体育”之“劳动是增强体质的手段”，OCR 原PDF页段：p0200-0299 (0-bas

### sk-0293　只有进入人的生活的美，才会唤起美感

- 旧标签：aesthetic-nature-education, child-study
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 7.66 + 先验 1.0 = 8.66））
- 其他命中：美与艺术（4.2） · 自然与思维课（4.1）
- 转述：苏霍姆林斯基认为，大自然、艺术作品和环境美的教育影响，不只取决于客观存在的美，还取决于人的活动，取决于这种美以什么方式加入他与周围人们的关系之中。美的感受与美的创造相互联系：孩子越多地在自然中被美触动，就越能从艺术作品中认出并再次体验这种美。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》第7章“美育”之“美育和美的创造”，OCR 原PDF页段：p0500-0599 (0-based)

### sk-0294　死记硬背越多，记忆保持越不牢固

- 旧标签：learning-difficulties, child-study
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 7.46 + 先验 1.0 = 8.46））
- 其他命中：了解儿童（3.4）
- 转述：苏霍姆林斯基通过三年级语法课的观察发现：死记未经充分理解的规则，只能获得表面的知识，而表面的知识很难保持在记忆中；没有弄懂的知识像雪球一样越滚越大。相反，学生在深入思考事实和现象的基础上、不经专门背诵而记住的知识，几乎不会再忘记。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《和青年校长的谈话》第1次谈话“教师创造性劳动的几个基本问题”之“完善的脑力劳动是思考、理解，而不是死记 硬背”，OCR 原

### sk-0295　加强难教儿童对自己力量的信心，耐心等待微小进步

- 旧标签：learning-difficulties, child-study
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 3.35 + 先验 1.0 = 4.35））
- 其他命中：学习困难学生（6.2） · 幸福与精神生活（4.0）
- 转述：苏霍姆林斯基把教师对难教儿童的信心比作医生对重病患者的信心。他认为不能用强制的办法使一个人变聪明；要求教师做到的最重要一点，是加强儿童对自己力量的信心，并耐心等待微小进步。这种进步带来的胜利体验，是难教儿童智育过程的基础。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《和青年校长的谈话》第4次谈话“难教儿童”之“难教儿童是些什么样的孩子”，OCR 原PDF页段：p0700-0799 (0-

### sk-0296　不要只号召讲卫生，而要去打扫

- 旧标签：collective-education, child-study
- 建议：**A16 评价与分数**（文本证据推翻旧标签（关键词 18.18，压过旧标签项 2.99））
- 其他命中：道德判断与品德培养（3.0）
- 转述：苏霍姆林斯基借用伊尔夫和彼得罗夫的话批评“活动月、竞赛、评比”掩盖下的形式主义：如果精力全花在各种突击活动上，教育工作就会失掉远景目标。道德真理必须体现在事物、现象和关系之中，而不是停留在号召里。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《和青年校长的谈话》第5次谈话“关于道德教育的几个问题”之“道德真理(准则、规则、原则)应当在 事物、现象、关系之中体现出来

### sk-0297　新知识只有依附旧知识，才能牢固掌握

- 旧标签：teacher-growth, learning-difficulties
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 8.42 + 先验 2.5 = 10.92））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：苏霍姆林斯基建议教师在备课时找出教材中的“关键点”——各种因果联系和其他有机联系相互交错的地方。围绕关键点激发疑问，让学生把已有知识提取出来解释不懂的东西，新知识就与旧知识牢固联结；教师必须善于找出新旧知识的联结点。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《和青年校长的谈话》第6次谈话“谈谈怎样指导学生的脑力劳动”之“知识的‘关键点’”，OCR 原PDF页段：p0800-089

### sk-0298　评价课的主要标准：全体学生牢固掌握知识

- 旧标签：assessment-grading, teacher-growth
- 建议：**A16 评价与分数**（旧标签先验 + 文本证据（关键词 8.93 + 先验 2.5 = 11.43））
- 其他命中：教师（7.2） · 检查知识与考查（5.6）
- 转述：苏霍姆林斯基提醒校长：不要被“最好的学生做出最好的回答”这种表面现象迷惑。评课要看教师是否给全体学生布置了要求独立完成的作业，是否留出让最差的学生也能完成的时间；对学得快的学生另给补充题，使每个学生都经历紧张的脑力劳动。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《和青年校长的谈话》第7次谈话“关于听课和分析课的几点建议”之“能否让全体学生都牢固地掌握知识是评价课的主要标准”，OCR 

### sk-0299　善于预见，首先要善于回顾走过的道路

- 旧标签：teacher-growth, child-study
- 建议：**A16 评价与分数**（文本证据推翻旧标签（关键词 4.16，压过旧标签项 3.87））
- 其他命中：阅读与书籍（2.9）
- 转述：苏霍姆林斯基认为，学年总结不只是行政程序，而是教育思想领导的重要环节：把现在与过去、未来联系起来分析，才能预见和防止“万尼亚到了六年级还不会解应用题”这类可悲的意外。他保存近20年的学校工作计划、课外活动计划，以及10年前的低年级学生书面作业和多年的听课笔记，作为分析教育过程的一手材料。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《和青年校长的谈话》第8次谈话“怎样做学年总结”之“学年总结为什么是必要的”，OCR 原PDF页段：p0800-0899 (

### sk-0300　共产主义信念把人确立为社会的决定力量

- 旧标签：collective-education
- 建议：**A2 公民与祖国**（旧标签先验 + 文本证据（关键词 6.04 + 先验 1.0 = 7.04））
- 其他命中：全面发展与个性（5.1） · 自我教育（3.8）
- 转述：信念不只是“知道”世界观与道德概念，而是准备按这些准则去行动。苏霍姆林斯基强调：共产主义信念不是束缚，而恰恰把人确立为社会的决定力量——教育的最终目的，是培养行为完全符合共产主义观点和信念的人。
- 出处：《年轻一代共产主义信念的形成》 / 信念是人的道德面貌的决定因素 / <!-- OCR 原PDF页段: p0000-0099 (0-based) -->

### sk-0301　意志就是行为的道德，信念的坚定性就是意志力

- 旧标签：collective-education, child-study
- 建议：**A4 自我教育**（文本证据推翻旧标签（关键词 8.24，压过旧标签项 2.99））
- 其他命中：道德判断与品德培养（3.0）
- 转述：苏霍姆林斯基把“意志”定义为行为的道德：一个人信念是否坚定，看其行为动机在多大程度上反映社会发展的利益。个人需要越是反映社会利益，动机就越高尚，行动也越自觉——意志力不是单纯的“咬牙坚持”，而是有道德方向的坚持。
- 出处：《年轻一代共产主义信念的形成》 / 共产主义信念是个人意志力的源泉 / <!-- OCR 原PDF页段: p0000-0099 (0-based) -->

### sk-0302　知识向信念的转化取决于教书与育人的结合

- 旧标签：teacher-growth
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88））
- 其他命中：自我教育（3.8） · 幸福与精神生活（3.0） · 阅读与书籍（2.9）
- 转述：知识不会自动变成信念。学生能否把所学化为自己的观点和行动，首先取决于师生之间心灵交流的质量，以及教师是否把“教书者”和“育人者”两种职责结合在自己身上。
- 出处：《年轻一代共产主义信念的形成》 / 教学目的和教育目的的统一 / <!-- OCR 原PDF页段: p0100-0199 (0-based) -->

### sk-0303　智力的发展应服从于道德的发展

- 旧标签：teacher-growth, child-study
- 建议：**A1 全面发展与个性**（文本证据推翻旧标签（关键词 5.06，压过旧标签项 4.35））
- 其他命中：思维与智力（3.4） · 道德判断与品德培养（3.0）
- 转述：这是苏霍姆林斯基在论述“世界观、道德意识和道德行为的统一”时提出的一条总原则：智力发展本身不是目的，而要服务于道德发展。知识若不能促使年轻人把力量投入有益于社会的活动，就会变成负担。
- 出处：《年轻一代共产主义信念的形成》 / 世界观、道德意识和道德行为的统一 / <!-- OCR 原PDF页段: p0100-0199 (0-based) -->

### sk-0304　生而为人，就要成为大写的人

- 旧标签：love-education
- 建议：**A4 自我教育**（文本证据推翻旧标签（关键词 8.24，压过旧标签项 4.31））
- 其他命中：幸福与精神生活（3.3） · 道德判断与品德培养（3.0）
- 转述：苏霍姆林斯基把“成为大写的人”作为道德教育的一条红线：真正的人要有一种精神，这种精神表现在信念与情感、意志与追求之中，表现在对待他人和自己的态度上。教育就是要在每个学生身上树立人的自豪感。
- 出处：《怎样培养真正的人》 / 真正的人应当什么样 / <!-- OCR 原PDF页段: p0200-0299 (0-based) -->

### sk-0305　教育技巧的精细处：培养学生需要人的情感

- 旧标签：love-education
- 建议：**A2 公民与祖国**（旧标签先验 + 文本证据（关键词 4.05 + 先验 1.0 = 5.05））
- 其他命中：幸福与精神生活（3.3） · 劳动与创造（3.0）
- 转述：苏霍姆林斯基认为，教育就其实质是长期培训儿童理解“人是最宝贵的财富”。学生怎样看待别人、在别人身上发现什么、给别人留下什么，比完成没完成家庭作业重要百倍。教育技巧的精细处，就在于培养学生“需要人”的情感。
- 出处：《怎样培养真正的人》 / 怎样培养需要人的情感 / <!-- OCR 原PDF页段: p0200-0299 (0-based) -->

### sk-0306　人的最大欢乐就是人的诞生

- 旧标签：family-school, love-education
- 建议：**A8 家庭与母亲**（旧标签先验 + 文本证据（关键词 3.50 + 先验 2.5 = 6.00））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：苏霍姆林斯基把新生命的诞生视为“人民的未来，父母的欢乐”，并主张培养孩子对待人的诞生、对待孕妇和母亲的高尚态度——这既是在培养孩子，也是在培养未来的父亲和母亲。
- 出处：《怎样培养真正的人》 / 最大的欢乐就是人的诞生 / <!-- OCR 原PDF页段: p0200-0299 (0-based) -->

### sk-0307　羞耻比最严厉的惩罚更有力

- 旧标签：child-study
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 8.61 + 先验 1.0 = 9.61））
- 其他命中：评价与分数（4.8） · 教师（2.4）
- 转述：苏霍姆林斯基认为，培养孩子的羞耻感是每位教师需要掌握的一根“魔杖”。外在惩罚只能约束一时，而羞耻是用自己的良心审判自己的良心；年长的人只能点燃善良思想的火花，真正的责备应当来自孩子本人。
- 出处：《怎样培养真正的人》 / 良心是行为的敏锐卫兵 / <!-- OCR 原PDF页段: p0300-0399 (0-based) -->

### sk-0308　教学生用心灵了解人，善意就能创造奇迹

- 旧标签：teacher-growth, love-education
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 6.65 + 先验 1.0 = 7.65））
- 其他命中：了解儿童（3.4） · 劳动与创造（3.0）
- 转述：教师的善意不是口号，而是一种需要培养的品质。苏霍姆林斯基的做法是带学生到“美丽角”去观察和感受路人的眼神与命运，让学生学会用心了解他人的处境。能用心觉察别人情绪的学生，才会以善待人、以心换心。
- 出处：《给教师的100条建议》 / 要善意待人 / <!-- OCR 原PDF页段: p0500-0599 (0-based) -->

### sk-0309　教材首次学习不扎实是落后根源之一

- 旧标签：learning-difficulties, teacher-growth
- 建议：**A16 评价与分数**（文本证据推翻旧标签（关键词 4.16，压过旧标签项 2.50））
- 其他命中：学习困难学生（4.9）
- 转述：苏霍姆林斯基提出“教材的首次学习”概念：从不知向知迈出的第一步，决定后续学习是否越来越省劲。首次学习必须特别明确，让每个学生（尤其是“困难”学生）当堂独立作业，力求首次学习不出差错，否则模糊观念越积越多，落后压力越来越大。
- 出处：《给教师的100条建议》 / 教材的首次学习 / <!-- OCR 原PDF页段: p0600-0699 (0-based) -->

### sk-0310　手脑之间有千丝万缕的联系

- 旧标签：labor-education, child-study
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 15.81 + 先验 2.5 = 18.31））
- 其他命中：思维与智力（3.7）
- 转述：苏霍姆林斯基17年教学生用双手工作的经验表明：最细致灵巧的劳动若左右手都会做，手脑联系会增多，思维会获得一种新的质——能从整体上纵观一系列相互联系的现象。双手并用的能工巧匠，比单手干活的人在同一现象中能看出更多东西。
- 出处：《给教师的100条建议》 / 教儿童用左右手工作 / <!-- OCR 原PDF页段: p0600-0699 (0-based) -->

### sk-0311　儿童是不会故意做坏事的

- 旧标签：child-study, teacher-growth
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 4.62 + 先验 1.0 = 5.62））
- 其他命中：教师（2.4）
- 转述：苏霍姆林斯基提醒教师：儿童不是有意干坏事，他们的不当举动往往出于一时糊涂、无知或误解。硬把儿童的行为断定为“蓄意作恶”，是教育上的无知；这种教师在“砍掉劣根”的同时，会把所有根都砍掉，破坏儿童对教师的无限信任。
- 出处：《给教师的100条建议》 / 怎样爱惜儿童的信任 / <!-- OCR 原PDF页段: p0800-0889 (0-based) -->

### sk-0312　真正的全面发展：贡献与消费之间的和谐

- 旧标签：labor-education, collective-education
- 建议：**A1 全面发展与个性**（文本证据推翻旧标签（关键词 5.02，压过旧标签项 4.90））
- 其他命中：尊严、爱与信任（4.9） · 劳动与创造（2.3）
- 转述：苏霍姆林斯基在梳理个人全面发展思想的历史沿革后指出：全面发展并不意味着一个人不停地从一种职业转到另一种职业，也不是样样都做而又不求甚解。真正全面发展的核心标志，是个人奉献给社会的东西与他从社会取得、消费的东西之间的和谐；如果不发展一个人对劳动的需要，充分满足其各种需要就不可思议。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《全面发展的人的培养问题》第1章“个人全面发展思想的历史沿革”（OCR 原PDF页段: p0000-0099, 0-base

### sk-0313　智育不能归结为积累知识

- 旧标签：thinking-and-nature
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 3.35 + 先验 2.5 = 5.85））
- 其他命中：劳动与创造（5.3） · 全面发展与个性（5.1）
- 转述：智育包括获得知识、形成科学世界观、发展认识能力和创造能力、培养脑力劳动文明等，但它不等于知识的堆积。教养程度不等于智力训练程度，知识分量也不等于智力发展程度。智育还与个人的劳动、社会积极性紧密联系，知识只有在人的复杂活动中才真正具有生命力。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《全面发展的人的培养问题》第3章“智育与人的全面发展”（OCR 原PDF页段: p0100-0199, 0-based）

### sk-0314　真理要像母亲一样亲，才能成为信念

- 旧标签：love-education, teacher-growth
- 建议：**A4 自我教育**（旧标签先验 + 文本证据（关键词 3.82 + 先验 1.0 = 4.82））
- 其他命中：幸福与精神生活（3.3）
- 转述：儿童对真理的感知、认识和理解，还不等于有了信念。真理只有在情感上变得像母亲一样亲切，人才会真正把它当作信念；判断一个人信念是否坚定，要看他是否随时准备为真理的胜利而战斗。信念的养成随时随地都在进行。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《全面发展的人的培养问题》第4章“共产主义的信念和坚定的、不可动摇的世界观的形成”（OCR 原PDF页段: p0100-01

### sk-0315　从道德概念到道德信念，要从情感行为开始

- 旧标签：love-education, collective-education
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 10.96 + 先验 1.0 = 11.96））
- 其他命中：自我教育（9.7） · 道德判断与品德培养（8.4）
- 转述：道德概念不会自动变成道德信念。情感是道德信念的血肉：从概念到信念的转化，必须从充满深刻情感的行为开始。当一个人多次因做好事而体验到欢乐，他才会把别人的坏事当作自己的痛苦来感受，从而实现行为与认识的统一。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《全面发展的人的培养问题》第5章“共产主义道德的培养”（OCR 原PDF页段: p0100-0199, 0-based）

### sk-0316　美是道德纯洁、精神丰富、体魄健全的源泉

- 旧标签：aesthetic-nature-education
- 建议：**A14 美与艺术**（旧标签先验 + 文本证据（关键词 4.21 + 先验 2.5 = 6.71））
- 其他命中：尊严、爱与信任（4.2） · 健康与作息（4.1）
- 转述：美育不只是教儿童欣赏风景或艺术品，它的首要任务是让儿童从自然美和人际关系的美中辨认出精神的高尚、善良和诚恳，进而把这种美确立在自己身上。美由此成为道德、精神和体魄健康发展的源泉。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《全面发展的人的培养问题》“美育和情感修养”章（OCR 原PDF页段: p0200-0299, 0-based）

### sk-0317　判断学生要看他想成为什么样的人

- 旧标签：child-study, love-education
- 建议：**A6 了解儿童**（人工裁定（「判断学生要看他将成为什么样的人」= 了解学生的志向，与评分机制无关（外部评审意见）））
- 其他命中：评价与分数（4.8） · 道德判断与品德培养（3.0）
- 转述：苏霍姆林斯基强调，职业选择本身并不决定一个人的道德面貌。评价学生的道德是否纯洁高尚，关键要看他希望自己成为什么样的人——即他的人生目标和精神追求，而不是他将来从事哪一行。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《学生的精神世界》“共产主义思想性是人的丰富的精神世界的基础”章（OCR 原PDF页段: p0300-0399, 0-bas

### sk-0318　学龄初期美感影响终生

- 旧标签：aesthetic-nature-education, child-study
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 13.95 + 先验 1.0 = 14.95））
- 其他命中：检查知识与考查（5.1） · 美与艺术（4.7）
- 转述：7~11岁儿童的审美感知和与审美感受相关的积极活动，会在情感记忆里留下终生难忘的印象。苏霍姆林斯基的调查表明，儿童期对大自然、劳动和创作之美的体验，不仅不会被后来的印象冲淡，还会为“祖国”“故乡”等概念奠定情绪底色，并深刻影响成年后的审美要求。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《学生的精神世界》“从幼年时期到少年时期”章“(5) 学龄初期儿童的美感”节（OCR 原PDF页段: p0300-0399,

### sk-0319　不要讥笑少年隐秘的意志考验

- 旧标签：child-study, teacher-growth
- 建议：**A7 健康与作息**（文本证据推翻旧标签（关键词 8.94，压过旧标签项 5.43））
- 其他命中：自我教育（4.4） · 教师（2.4）
- 转述：少年会自觉寻找考验和锻炼意志的途径，例如在严寒中开窗睡觉、用绝食考验耐力等。苏霍姆林斯基认为，教师最好不要干涉这些隐秘的事情（除非危害健康）；任何责备和讥笑，都会玷污少年心中最宝贵的东西，把崇高的事情庸俗化。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《学生的精神世界》“少年时期”章“(2)少年意志的特点”节（OCR 原PDF页段: p0400-0499, 0-based）

### sk-0320　每个学生心灵深处都藏着献身愿望

- 旧标签：collective-education, child-study
- 建议：**A6 了解儿童**（旧标签先验 + 文本证据（关键词 3.37 + 先验 2.5 = 5.87））
- 其他命中：幸福与精神生活（3.0） · 劳动与创造（3.0）
- 转述：苏霍姆林斯基多年的观察表明：即使是沉默、腼腆、看似平庸的学生，内心深处也珍藏着为人民利益英勇献身的愿望，只是他们把它当作最珍贵、最隐秘的东西深藏不露。教师的任务是创造各种环境，让每个学生在青年早期就能把巨大的精神力量化为实际的献身行动。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《学生的精神世界》“青年早期”章“(4)献身精神是精神生活的顶峰”节（OCR 原PDF页段: p0500-0599, 0-b

### sk-0321　儿童在学校不光是学习，而且在那里生活

- 旧标签：collective-education, teacher-growth
- 建议：**A9 集体与同伴**（旧标签先验 + 文本证据（关键词 3.16 + 先验 2.5 = 5.66））
- 其他命中：全面发展与个性（5.2） · 美与艺术（4.7） · 公民与祖国（4.0）
- 转述：苏霍姆林斯基在阐述培养学校集体的原则时指出，学校集体必须建立思想、公民、智力、劳动、审美等多方面的关系，师生和生生的兴趣交织在一起。儿童在学校不只是学习，更是在生活；教师若忘记这一点，学习就会变成沉重的负担。哪所学校把学习只当作丰富精神生活的一部分，哪所学校的儿童就乐意学习。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《培养集体的方法》“学校集体及其培养的原则”章“(1) 培养学校集体的原则”节（OCR 原PDF页段: p0500-0599

### sk-0322　自己发光时，也要让别人发光

- 旧标签：collective-education, love-education
- 建议：**A9 集体与同伴**（旧标签先验 + 文本证据（关键词 9.09 + 先验 2.5 = 11.59））
- 其他命中：尊严、爱与信任（5.0）
- 转述：苏霍姆林斯基认为，把学校集体成员团结起来的主要力量，是人关心人、人对人负责。集体主义教育的逻辑是：每个学生刚刚“发光”时，就应当让身边的人也发光；如果不能让别人发光，自己的光也会熄灭。只有在这种互相关怀与负责中，不同年龄、不同需要的学生才能结成真正的精神统一体。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《培养集体的方法》“学校集体及其培养的原则”章“(2)人关心人、人对人负责，是学校集体在组织上和道德上统一的基础”节（OCR

### sk-0323　孩子发笑时，教师绝不可生气

- 旧标签：collective-education, teacher-growth
- 建议：**A9 集体与同伴**（旧标签先验 + 文本证据（关键词 3.68 + 先验 2.5 = 6.18））
- 其他命中：教师（2.4）
- 转述：儿童的生活中不能没有笑声。当孩子因同学机智俏皮的言行而发出喜悦的惊讶时，教师往往大发雷霆，苏霍姆林斯基认为这是教育工作中最令人痛心的错误之一。正确的做法是：用幽默让发出不必要、不恰当笑声的学生感到羞愧；教师对付儿童的淘气行为时，永远不应失去幽默感。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《培养集体的方法》“集体对个人教育影响的形成”章“(10)集体精神生活中的幽默感”节（OCR 原PDF页段: p0700-0

### sk-0324　别用评分这根树条去抽打这条壮阔的大河

- 旧标签：assessment-grading, learning-difficulties
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 8.37 + 先验 1.0 = 9.37））
- 其他命中：评价与分数（5.5） · 了解儿童（3.4）
- 转述：在“幻想之角”观察孩子的想象时，苏霍姆林斯基借“水流缓慢的大河”比喻思维迟缓的孩子：强迫大河加速是不可能的，它按自己的本性流动，终会到达预定标界。教师不应性急，更不能用评分这根“树条”去抽打这样的孩子——那无济于事。
- 出处：《我把心给了孩子们》我们的“幻想之角” / OCR 原PDF页段: p0000-0099 (0-based)

### sk-0325　对故乡土地的主人翁感是最重要的爱国主义感情

- 旧标签：collective-education, labor-education
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 4.60 + 先验 2.5 = 7.10））
- 其他命中：公民与祖国（5.3） · 自然与思维课（4.1）
- 转述：在“要像列宁那样斗争和胜利”一节中，孩子们成立了少年自然保护小组：巡查护田林带、制止毁树、给懒散庄员递送《大自然少年保护者的警告书》、精选麦种并关心公共果园里的毛虫。苏霍姆林斯基由此总结：孩子对公共田地里的每一个麦穗、公共果园的每一棵树像对自己的东西一样珍惜时，才会成为真正的爱国主义者。
- 出处：《我把心给了孩子们》要像列宁那样斗争和胜利 / OCR 原PDF页段: p0400-0499 (0-based)

### sk-0326　体罚是教育方法极端不文明的标志

- 旧标签：family-school, child-study
- 建议：**A8 家庭与母亲**（旧标签先验 + 文本证据（关键词 4.14 + 先验 2.5 = 6.64））
- 其他命中：评价与分数（4.2） · 幸福与精神生活（3.0）
- 转述：苏霍姆林斯基把体罚视为教育工作者的耻辱：用皮带抽、打后脑勺、拳打脚踢，会使儿童心灵变得迟钝、凶狠、冷若冰霜。皮带和拳头扼杀细腻敏锐的感情，培植愚昧本能，最终用撒谎和奉承麻醉人；用皮带培养出来的儿童会变成麻木不仁、没有心肝的人。教师若把成绩问题告诉会打孩子的家长，等于是把鞭子放进学生书包。
- 出处：《公民的诞生》一切都取决于童年期的教育 / OCR 原PDF页段: p0400-0499 (0-based)

### sk-0327　儿童周围的复杂关系是不自觉的教育源泉

- 旧标签：family-school, child-study
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 3.31 + 先验 1.0 = 4.31））
- 其他命中：道德判断与品德培养（3.0）
- 转述：柯利亚·兹（一个文静谦逊的少年）夜间从录音机里偷走了电动机、并弄坏了一些零件，促使苏霍姆林斯基思考道德教育的两个源泉：第一个是预先计划好的教育工作；第二个则是儿童周围的复杂关系——父亲每天下班总要带一点小东西回来（电线、金属片、小管子、轴承），这种未加掩饰的关系给孩子上了“直观课”。成年人越是不把周围关系当成教育手段，
- 出处：《公民的诞生》童年期和少年期教育的两个源泉 / OCR 原PDF页段: p0400-0499 (0-based)

### sk-0328　在学生面前进行思维

- 旧标签：teacher-growth, thinking-and-nature
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 11.15 + 先验 2.5 = 13.65））
- 其他命中：教师（2.4）
- 转述：少年期的逆反心理往往从否定单调的学校作业开始：他们觉得作业与宇宙飞行相比像蚂蚁搬东西。苏霍姆林斯基提出，克服这一矛盾的关键不是把现成知识塞给学生，而是教师在学生面前“进行思维”，展示思考过程，让学生感觉自己是一个研究者和思想家，而不只是“知识购买者”。
- 出处：《公民的诞生》少年期的矛盾 / OCR 原PDF页段: p0500-0599 (0-based)

### sk-0329　第二个大纲：非必修知识的大纲

- 旧标签：reading-and-books, learning-difficulties
- 建议：**A6 了解儿童**（旧标签先验 + 文本证据（关键词 3.80 + 先验 2.5 = 6.30））
- 其他命中：尊严、爱与信任（4.3） · 思维与智力（3.7）
- 转述：苏霍姆林斯基提出“智育的两个大纲”：第一大纲是必修知识（课堂教学）；第二大纲是非必修知识——大纲范围之外、由科学视野和学生兴趣决定的知识。少年在课外读得越多、知道得越多，就越珍视知识、尊重教师和课堂。对于思维迟钝的学生，读一定量大纲规定以外的科普文艺反而是理解必修教材的条件。
- 出处：《公民的诞生》少年的智育和教学·智育的两个大纲 / OCR 原PDF页段: p0600-0699 (0-based)

### sk-0330　同自己说话，对着自己良心说话

- 旧标签：reading-and-books, child-study
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 11.40 + 先验 2.5 = 13.90））
- 其他命中：尊严、爱与信任（4.4） · 自我教育（4.3）
- 转述：在“思想教育室”里，少年们反复阅读描写优秀人物生平的书籍，开始用英雄的眼光观察自己、衡量自己。苏霍姆林斯基认为，真正的自我教育就是同自己说话、对着自己良心说话——前提是人在人类道德财富中找到了自己的榜样。
- 出处：《公民的诞生》思想教育室 / OCR 原PDF页段: p0600-0699 (0-based)

### sk-0331　粮食、劳动、人民：三根支柱

- 旧标签：labor-education
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 6.93 + 先验 2.5 = 9.43））
- 其他命中：健康与作息（5.9） · 全面发展与个性（4.4）
- 转述：苏霍姆林斯基给上大学的儿子写第一封信，转述自己父亲的话：面包是神圣的，永远不要忘本。他把“粮食、劳动、人民”列为应当放在第一位的三个词，是国家赖以生存的三根支柱——忘记劳动、汗水和疲劳是什么，就不会珍惜粮食；丧失人民的精神品质，就会成为脱离集体、没有个性的人。
- 出处：《给儿子的信》第1封信 / OCR 原PDF页段: p0800-0899 (0-based)

### sk-0332　志向是天才的幼苗

- 旧标签：labor-education, teacher-growth
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 11.84 + 先验 2.5 = 14.34））
- 其他命中：自我教育（4.3） · 思维与智力（4.1）
- 转述：苏霍姆林斯基告诉儿子：志向不是别人强加的。他从中学二年级起钻研收音机小意图、付出劳动，才形成无线电物理学的志向。志向这棵幼苗要靠热爱劳动的双手和自我教育来培育，否则会连根枯死。他还用巴赫家族、园艺家耶菲姆·菲利波维奇说明：人的智慧在指尖上，每个人应当成为本行的主人。
- 出处：《给儿子的信》第5 封信 / OCR 原PDF页段: p0800-0899 (0-based)

### sk-0333　五年寒窗培养工程师，学会做人需要一辈子

- 旧标签：teacher-growth
- 建议：**A4 自我教育**（旧标签先验 + 文本证据（关键词 4.34 + 先验 1.0 = 5.34））
- 其他命中：思维与智力（3.3） · 幸福与精神生活（3.3）
- 转述：苏霍姆林斯基在信中谈青年精神空虚的问题：熟记、背诵多于思考，人文科学教育薄弱，人们彼此冷漠。他认为普通学校和大学教育的头等任务是“变知识为人所有，使教学充满高尚美好的情感”。工程师可以五年培养出来，但学会做人需要一辈子——人道主义教育也是自我教育的内容。
- 出处：《给儿子的信》第9封信 / OCR 原PDF页段: p0900-0993 (0-based)

### sk-0334　爱情之火需要添加多方面的精神生活

- 旧标签：family-school, love-education
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 7.21 + 先验 1.0 = 8.21））
- 其他命中：全面发展与个性（5.2） · 检查知识与考查（5.1）
- 转述：苏霍姆林斯基在信中谈婚姻与家庭：年轻人以为结婚后爱情会自动带来取之不尽的幸福，却忘了爱情之火需要不断添加“好燃料”——多方面的精神生活。缺少精神生活，爱情之火会熄灭并冒出浓烟。他还强调：婚后创造应当超过需求，年轻人应是爱情的创造者，而不只是乐趣的需求者。
- 出处：《给儿子的信》第 14 封信 / OCR 原PDF页段: p0900-0993 (0-based)

### sk-0335　在小孩子身上看到明天的成年人

- 旧标签：child-study, family-school
- 建议：**A8 家庭与母亲**（旧标签先验 + 文本证据（关键词 3.50 + 先验 2.5 = 6.00））
- 其他命中：思维与智力（4.1） · 教师（2.4）
- 转述：苏霍姆林斯基在最后一封信中回答“教育青年最严重的缺点是什么”：深信就是忘记今天的小孩子将是明天的成年人（OCR“今大”待校）。很多父母和教师总把孩子当永远的孩子看待，直到孩子突然到了结婚年龄才大吃一惊。他引用契诃夫的话强调：孩子是神圣和纯洁的，不能把他们当成自己情绪的玩具。
- 出处：《给儿子的信》第 22 封信 / OCR 原PDF页段: p0900-0993 (0-based)

### sk-0348　致年轻的朋友：你飞出了父母的巢

- 旧标签：family-school
- 建议：**A11 劳动与创造**（文本证据推翻旧标签（关键词 6.93，压过旧标签项 6.00））
- 其他命中：家庭与母亲（3.5） · 思维与智力（3.3）
- 转述：父亲写给离家上大学的儿子的第一封信，点出年轻人刚独立时容易被新生活吸引、不念家。这是全书开篇的第一句话，引出父亲对儿子终生保存书信、反复思考教诲、珍惜劳动与粮食的劝告。
- 出处：《给儿子的信》第1封信；OCR 原PDF页段: p0800-0899 (0-based)

### sk-0349　做一个公民：别对邪恶无动于衷

- 旧标签：love-education, collective-education
- 建议：**A19 道德判断与品德培养**（文本证据推翻旧标签（关键词 6.44，压过旧标签项 5.05））
- 其他命中：习惯与纪律（4.8） · 公民与祖国（4.0）
- 转述：父亲告诉儿子：比死亡更可怕的是面对邪恶与虚伪时无动于衷——看见了却装作没看见，不去思考所见之事，善恶不分。一个人若养成对事情毫不在乎的习惯，很快就会对任何事情都满不在乎。
- 出处：《给儿子的信》第2封信；OCR 原PDF页段: p0800-0899 (0-based)

### sk-0350　致年轻的朋友：面包是神圣的

- 旧标签：labor-education, family-school
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 4.38 + 先验 1.0 = 5.38））
- 其他命中：劳动与创造（2.3）
- 转述：父亲转述自己父亲（儿子的爷爷）在第一封家信中的教诲：面包是神圣的，它来自人类的劳动，是未来的希望，也是衡量你和你的子女们良心的一把尺子；永远不要忘本。
- 出处：《给儿子的信》第1封信；OCR 原PDF页段: p0800-0899 (0-based)

### sk-0351　最困难的事应成为最喜爱的事

- 旧标签：labor-education
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 7.01 + 先验 2.5 = 9.51））
- 其他命中：自我教育（3.8）
- 转述：信念的形成有其辩证法：人终生珍视的东西，恰恰是他付出昂贵代价才获得的东西。劳动的热爱不是轻而易举能得到的，只有通过劳动本身、通过克服困难，才能把“最困难的事”变成“最喜爱的事”。
- 出处：《给儿子的信》第8封信；OCR 原PDF页段: p0900-0993 (0-based)

### sk-0352　生活的根：粮食、劳动、人民

- 旧标签：labor-education, collective-education
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 2.33 + 先验 2.5 = 4.83））
- 其他命中：思维与智力（4.0）
- 转述：父亲告诉儿子：在千千万万个词汇中，应当把“粮食、劳动、人民”放在第一位。这三者是国家赖以生存的三根支柱，彼此不可分割；谁败坏其中任何一个，谁就不能成为真正的人。
- 出处：《给儿子的信》第1封信；OCR 原PDF页段: p0800-0899 (0-based)

### sk-0353　学会做人需要一辈子

- 旧标签：teacher-growth, love-education
- 建议：**A4 自我教育**（旧标签先验 + 文本证据（关键词 4.34 + 先验 1.0 = 5.34））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：父亲提醒正在读大学的儿子：专业学习固然重要，但首要的是成为一个人。人道主义教育也是自我教育的内容，把自己培养成人，是头等重要的事。
- 出处：《给儿子的信》第9封信；OCR 原PDF页段: p0900-0993 (0-based)

### sk-0354　让手成为创造者：从最粗的活练起

- 旧标签：labor-education
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 15.81 + 先验 2.5 = 18.31））
- 其他命中：健康与作息（4.8） · 评价与分数（4.2）
- 转述：父亲建议学无线电物理的儿子：不要满足于一般成绩，第一次失败要从头再来；决不要轻视最简单的粗活，要把双手锻炼成能胜任各种劳动的最重要工具。手工劳动是创造性活动的起点。
- 出处：《给儿子的信》第5封信；OCR 原PDF页段: p0800-0899 (0-based)

### sk-0355　人间的幸福在劳动中

- 旧标签：labor-education
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 5.31 + 先验 2.5 = 7.81））
- 其他命中：幸福与精神生活（3.4）
- 转述：父亲以一位普通挤奶女工为例说明：她并没有丰功伟绩，但她的全部生活就是一份功绩——因为她用自己的劳动给人们以崇高的精神。人间的幸福不在索取，而在为他人、为人类的创造性劳动之中。
- 出处：《给儿子的信》第4封信；OCR 原PDF页段: p0800-0899 (0-based)

### sk-0356　自我教育从自我认识开始

- 旧标签：child-study, reading-and-books
- 建议：**A4 自我教育**（旧标签先验 + 文本证据（关键词 14.70 + 先验 1.0 = 15.70））
- 其他命中：全面发展与个性（4.4） · 了解儿童（3.4）
- 转述：父亲告诉儿子：培养意志是自我教育的重要方面，但意志是自我教育的结果而非起点。自我教育要从自我认识开始——学会从侧面观察自己，用理想主义、英雄主义的尺度审视自己；为此要多读描写达到人类最美境界的人的书。
- 出处：《给儿子的信》第10封信；OCR 原PDF页段: p0900-0993 (0-based)

### sk-0358　你在大地上的足迹：童年的汗水

- 旧标签：labor-education, family-school
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 2.33 + 先验 2.5 = 4.83））
- 其他命中：公民与祖国（4.0）
- 转述：父亲劝儿子将来教育自己的子女：童年时期流的每一滴汗水，价值超过成年时期许多紧张劳动；童年种出的每一捧粮食，其意义如同堆积如山的金色小麦。童年的劳动会在人生和土地上留下最深的足迹，是公民自豪感的起点。
- 出处：《给儿子的信》第8封信；OCR 原PDF页段: p0900-0993 (0-based)

### sk-0359　300页《大自然的书》：300次观察，学习思索

- 旧标签：thinking-and-nature
- 建议：**A12 自然与思维课**（旧标签先验 + 文本证据（关键词 9.60 + 先验 1.0 = 10.60））
- 其他命中：思维与智力（3.7） · 了解儿童（3.4）
- 转述：苏霍姆林斯基为四年小学生活设计了一部“300页的《大自然的书》”：全书就是300次到大自然中去观察，300幅铭刻在孩子意识中的鲜明图画。每周两次出行不是散步，而是“学习思索”——本质上就是思维课。
- 出处：《我把心给了孩子们》·300页《大自然的书》·OCR 原PDF页段 p0200-0299 (0-based)

### sk-0360　你们是土地的主人

- 旧标签：love-education, collective-education
- 建议：**A2 公民与祖国**（旧标签先验 + 文本证据（关键词 3.93 + 先验 1.0 = 4.93））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：孩子们在山冈上为无名英雄种下小橡树，把一小块土地变成活的纪念碑。苏霍姆林斯基借“你们是土地的主人”这句话，把英雄牺牲与儿童对祖国富强所负的责任连在一起：土地是前辈用鲜血浇灌的，孩子要做真正的主人去关心它。
- 出处：《我把心给了孩子们》·少年列宁主义者，你们是祖国未来的主人·OCR 原PDF页段 p0300-0399 (0-based)

### sk-0361　生活由行为举止组成

- 旧标签：love-education, child-study
- 建议：**A17 习惯与纪律**（文本证据推翻旧标签（关键词 5.84，压过旧标签项 2.99））
- 其他命中：道德判断与品德培养（3.0）
- 转述：人的整个生活就是由一个个行为举止组成的；道德品质不在宣言里，而在对待他人的日常举动里。因此教育要从具体行为中培养道德意识，而不是停留在说教上。
- 出处：《怎样培养真正的人》·第42篇 怎样启迪孩子们具有高尚的行为举止·OCR 原PDF页段 p0400-0499 (0-based)

### sk-0362　生而为人，要成为大写的人

- 旧标签：love-education
- 建议：**A4 自我教育**（文本证据推翻旧标签（关键词 8.24，压过旧标签项 4.43））
- 其他命中：全面发展与个性（4.4） · 幸福与精神生活（3.3）
- 转述：出生只是生物学事实，“成为人”是道德任务。真正的人要有人的精神——这种精神在信念与情感、意志与追求中，在对他人和自己的态度中，在分明的爱与憎和追求理想中表现出来。
- 出处：《怎样培养真正的人》·第2篇 真正的人应当什么样·OCR 原PDF页段 p0200-0299 (0-based)

### sk-0363　容忍弱点，对邪恶毫不妥协

- 旧标签：child-study, love-education
- 建议：**A19 道德判断与品德培养**（人工裁定（谈的是对邪恶不妥协的**道德判断**，不是「怎么了解儿童」（外部评审意见）））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：敏锐而有分寸的行为意味着两面兼备：对人的个别弱点宽容、心软，对邪恶毫不妥协、毫不留情。两者统一才构成精神素养，而这种分寸来自对“人的复杂世界”的了解。
- 出处：《怎样培养真正的人》·第44篇 怎样教孩子懂得敏锐而有分寸的行为·OCR 原PDF页段 p0400-0499 (0-based)

### sk-0364　懂得爱，才会成为真正的人

- 旧标签：love-education
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 4.90 + 先验 2.5 = 7.40））
- 其他命中：公民与祖国（4.0） · 幸福与精神生活（3.3）
- 转述：成为真正的人的标志不是知识或能力，而是懂得爱——对他人的忠诚、奉献与需要。爱是道德发展的前提，也是进入公民生活大世界的门。苏霍姆林斯基用童话《小驼背和闪闪的小星》让孩子以惊讶的情感领会这一真谛。
- 出处：《怎样培养真正的人》·第24篇 一个人只有在他去爱人们的时候才能成为人·OCR 原PDF页段 p0300-0399 (0-based)

### sk-0365　成为有教养的人，先要有欢乐

- 旧标签：child-study, love-education
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 7.09 + 先验 1.0 = 8.09））
- 其他命中：习惯与纪律（5.0） · 劳动与创造（4.6）
- 转述：孩子成为有教养的人的第一个前提不是纪律或知识，而是欢乐、幸福和对世界的乐观感受。真正的人道主义精神，就在于珍惜孩子有权享受的欢乐和幸福。
- 出处：《怎样培养真正的人》·第1篇 怎样才能使人成为有教养的人·OCR 原PDF页段 p0200-0299 (0-based)

### sk-0366　我校集体的教育信念

- 旧标签：teacher-growth, collective-education
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 9.01 + 先验 2.5 = 11.51））
- 其他命中：劳动与创造（5.3） · 自我教育（3.8）
- 转述：帕夫雷什中学把全体教师在长期实践中形成的共同教育信念作为学校工作的基石；这些信念不是靠命令规定的，而是在共同、有明确目的、创造性的劳动过程中形成并确立的。
- 出处：《帕夫雷什中学》·前言·OCR 原PDF页段 p0000-0099 (0-based)

### sk-0367　信任才能唤起自尊与自我教育

- 旧标签：teacher-growth, child-study
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 9.42 + 先验 1.0 = 10.42））
- 其他命中：自我教育（4.3） · 教师（2.4）
- 转述：教育理论要起作用，必须有教师活生生的人格——炽热的心、高尚的情操和审慎的理智。让孩子真正感觉到“人们在信任他、希望他好”，信任才能唤起自尊感，而自尊感是自我教育的前提。
- 出处：《和青年校长的谈话》·第5次谈话 关于道德教育的几个问题·OCR 原PDF页段 p0800-0899 (0-based)

### sk-0368　向年轻校长提听课建议

- 旧标签：teacher-growth
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 4.83 + 先验 2.5 = 7.33））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：苏霍姆林斯基以过来人身份，就“听课和分析课”向年轻校长提出系统建议：听课和分析课是校长最重要的工作，一天至少听两节课；分析课要着眼全体学生是否牢固掌握知识，而不被个别优等生的好回答迷惑。
- 出处：《和青年校长的谈话》·第7次谈话 关于听课和分析课的几点建议·OCR 原PDF页段 p0800-0899 (0-based)

### sk-0369　教师是学生智力生活的第一盏指路灯

- 旧标签：teacher-growth
- 建议：**A15 思维与智力**（文本证据推翻旧标签（关键词 9.02，压过旧标签项 4.88））
- 其他命中：尊严、爱与信任（4.3） · 集体与同伴（3.2）
- 转述：教师不只是一个知识传授者，他首先点燃学生的求知欲，并把尊重科学、文化和教育变成学生内在的态度。这句话出自苏霍姆林斯基对帕夫雷什中学教师集体的介绍，强调的是教师在学生智力生活中不可替代的引领作用。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》第1章“全体教师团结一致是教育教学工作成功的保证”之“我们的教师和教育者”，OCR 原PDF页段：p0000

### sk-0370　没有课外阅读，课堂阅读就会变成死记硬背

- 旧标签：reading-and-books
- 建议：**A15 思维与智力**（文本证据推翻旧标签（关键词 7.49，压过旧标签项 6.46））
- 其他命中：阅读与书籍（4.0） · 劳动与创造（2.3）
- 转述：苏霍姆林斯基把课外阅读视为课堂脑力劳动的营养来源。课内所学若没有课外的广泛阅读作支撑，学生对文本的理解就只能停留在机械记忆层面，无法变成真正的智力活动。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》第2章“学校的物质基础及学生周围的环境”之“课堂教学和课外活动的环境”，OCR 原PDF页段：p0100-0

### sk-0371　只有当运动成为每个人都喜爱的活动，才能成为教育手段

- 旧标签：health-first
- 建议：**A7 健康与作息**（旧标签先验 + 文本证据（关键词 4.80 + 先验 2.5 = 7.30））
- 其他命中：评价与分数（5.8） · 自我教育（4.4）
- 转述：苏霍姆林斯基反对把学校体育变成少数运动尖子的竞赛和学校博取名次的工具。体育只有成为每个孩子都喜爱的日常活动，才能真正进入教育过程，起到增强体质、培养性格和锻炼意志的作用。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》第3章“关注健康与体育”之“课堂上的体育和运动”，OCR 原PDF页段：p0200-0299 (0-base

### sk-0372　善良情感，是良心的头道防线

- 旧标签：love-education
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 13.35 + 先验 2.5 = 15.85））
- 其他命中：道德判断与品德培养（9.1） · 幸福与精神生活（6.3）
- 转述：苏霍姆林斯基在谈男女青年道德美感教育时指出，对纯洁美好爱情的品德准备，必须从培养儿童心灵中的善良情感做起。一个人若从小能对他人的痛苦产生同情，长大后才不会做出伤害伴侣和家庭的事。善良情感是良心最前面的防线。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》第4章“德育”之“培养男女青年相互关系的道德美感”，OCR 原PDF页段：p0300-0399 (0-bas

### sk-0373　教会儿童积极地看世界，在劳动中恪守信念

- 旧标签：child-study, thinking-and-nature
- 建议：**A1 全面发展与个性**（文本证据推翻旧标签（关键词 5.06，压过旧标签项 3.82））
- 其他命中：自我教育（3.8） · 劳动与创造（2.3）
- 转述：苏霍姆林斯基认为，智育与世界观的统一不在口头说教，而在儿童是否能用积极的态度看待世界、并在劳动中坚持自己的信念。只有当知识转化为个人行动中的信念时，知识才真正产生教育作用。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》第5章“智育”之“智育与世界观”，OCR 原PDF页段：p0300-0399 (0-based)

### sk-0374　普通学校的宗旨不在于职业训练

- 旧标签：labor-education
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 9.18 + 先验 2.5 = 11.68））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：苏霍姆林斯基区分了普通学校劳动教学与职业训练：中学劳动课不是要把学生焊死在某个工种上，而是让他们了解主要生产部门、掌握通用技能，从而能够自觉地选择未来的专业方向。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》第6章“劳动教育”之“劳动教学”，OCR 原PDF页段：p0400-0499 (0-based)

### sk-0375　美是人的道德财富的源泉

- 旧标签：aesthetic-nature-education
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 2.98 + 先验 1.0 = 3.98））
- 其他命中：道德判断与品德培养（3.0）
- 转述：苏霍姆林斯基认为美育与德育密不可分：美是人的道德财富的源泉，学校要在孩子神经系统最敏感的童年期，让美成为德育的有力手段，使人性的源泉真正流入孩子心灵。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》第7章“美育”之“少年和青年时期的审美教育和人的全面发展”，OCR 原PDF页段：p0500-0599 (0

### sk-0376　教师的人格是进行教育的基石

- 旧标签：teacher-growth
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 7.21 + 先验 2.5 = 9.71））
- 其他命中：全面发展与个性（4.4） · 自我教育（3.8）
- 转述：苏霍姆林斯基在与青年校长的谈话中指出，学校之间真正的差别不在统一的教学大纲和教科书，而在教师。各种观点、信念、理想和兴趣最终都要在教师的人格这个焦点上汇合，再通过教师的个人世界影响学生。教师人格因此是整个教育工作的基石。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《和青年校长的谈话》第5次谈话“关于道德教育的几个问题”之“教师是学生的朋友和同志”（OCR 标题原带“@”符号），OCR 

### sk-0377　游戏是儿童智力发展的窗子

- 旧标签：child-study, thinking-and-nature
- 建议：**A6 了解儿童**（旧标签先验 + 文本证据（关键词 3.37 + 先验 2.5 = 5.87））
- 其他命中：劳动与创造（5.3） · 思维与智力（3.4）
- 转述：游戏不是学习的对立面。世界通过游戏向儿童打开，儿童的创造性才能在游戏中显露；没有游戏，就不会有完满的智力发展。因此不能把劳动和游戏用“万里长城”隔开，识字、观察、劳动都可以与游戏结合。
- 出处：《我把心给了孩子们》·快乐学校·第一学年前夕的一些想法；OCR 原PDF页段: p0100-0199 (0-based)

### sk-0378　阳光、空气、水加劳动休息是最佳健康之源

- 旧标签：health-first
- 建议：**A7 健康与作息**（旧标签先验 + 文本证据（关键词 4.14 + 先验 2.5 = 6.64））
- 其他命中：劳动与创造（2.3）
- 转述：“健康乐园”的实践说明：单靠某一种因素不能保证儿童健康。良好营养、阳光、空气、水，再加上适当的劳动和休息，这些因素配合起来，才是无可替代的健康来源。
- 出处：《我把心给了孩子们》·快乐学校·我们生活在“健康乐园”里；OCR 原PDF页段: p0100-0199 (0-based)

### sk-0379　教读写要让孩子置身美与游戏的世界

- 旧标签：reading-and-books, aesthetic-nature-education
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 6.83 + 先验 2.5 = 9.33））
- 其他命中：美与艺术（4.5）
- 转述：识字教学不能变成纯粹跟书本打交道。孩子本来就应生活在美、游戏、童话、音乐、图画、幻想和创作的世界里；教阅读和书写时，更应让他置身其中，让读写成为这个世界的一部分，而不是把世界关在教室门外。
- 出处：《我把心给了孩子们》·快乐学校·我们怎样学习读和写；OCR 原PDF页段: p0100-0199 (0-based)

### sk-0380　保护少年的中枢神经系统就是爱护心脏

- 旧标签：health-first, teacher-growth
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88））
- 其他命中：尊严、爱与信任（4.7） · 思维与智力（4.0） · 幸福与精神生活（3.0）
- 转述：少年期是大脑发生深刻质变的时期，神经系统极度敏感，稍有不慎的触动就会“暴跳”“发火”。保护少年的中枢神经系统，就等于爱护他的心脏和整个机体。教师的语言应是“隐藏着同情心和宽容态度的最巧妙的工具”，而不是灼伤心灵的鞭子。
- 出处：《公民的诞生》·少年的身体发育与心理素养·爱护少年的神经系统；OCR 原PDF页段: p0500-0599 (0-based)

### sk-0381　公正拨开眼睛感受美，不公正如冰甲裹心

- 旧标签：aesthetic-nature-education, child-study
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 6.65 + 先验 1.0 = 7.65））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：美感的源泉是美的知觉素养，而知觉素养首先取决于公正。公正能打开儿童的眼睛和心灵去感受美；不公正则像冰制铠甲裹住年轻的心灵，使心灵迟钝、对美无动于衷。美感教育不能脱离公正的人际关系单独进行。
- 出处：《公民的诞生》·情感教育与美感教育·美感的源泉；OCR 原PDF页段: p0700-0799 (0-based)

### sk-0382　公民感要牢记心里而非挂在口头上

- 旧标签：labor-education, collective-education
- 建议：**A1 全面发展与个性**（文本证据推翻旧标签（关键词 11.01，压过旧标签项 7.81））
- 其他命中：劳动与创造（5.3） · 公民与祖国（4.0）
- 转述：劳动之所以能成为个性和谐发展的基础，是因为人在劳动中确认自己是个公民：不仅获得面包，还能实现自己的才智和创造。劳动教育最重要的准则，是让公民感不挂在口头上，而是牢记在心里。
- 出处：《公民的诞生》·劳动对少年精神生活的作用；OCR 原PDF页段: p0800-0899 (0-based)

### sk-0383　分辨“可以、不行、应该”三件事

- 旧标签：collective-education, child-study
- 建议：**A2 公民与祖国**（旧标签先验 + 文本证据（关键词 9.72 + 先验 1.0 = 10.72））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：自由不是为所欲为。人生活在人们中间，绝对自由不存在。要敏锐分辨“可以”“不可以”“应该”三件事；能分辨这三件事的人，才具有公民最重要的特点——义务感。义务是受崇高思想鼓舞的行动自由。
- 出处：《给儿子的信》·第12封信；OCR 原PDF页段: p0900-0993 (0-based)

### sk-0384　友谊是培养人的感情的学校

- 旧标签：love-education, child-study
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 6.77 + 先验 1.0 = 7.77））
- 其他命中：集体与同伴（5.4） · 尊严、爱与信任（4.6）
- 转述：友谊不是打发时间，而是一所培养人的感情的学校：通过友谊，人在自己身上培养美德。如果缺少对人性美的信任，心灵就会空虚，而心灵空虚必然贪婪地吸收坏东西。爱情如果缺乏以友谊为底色的高尚精神生活，就会变成单纯的感情享受。
- 出处：《给儿子的信》·第16封信；OCR 原PDF页段: p0900-0993 (0-based)

### sk-0385　劳动的社会意义揭示越鲜明，劳动越成为需要

- 旧标签：labor-education, collective-education
- 建议：**A4 自我教育**（文本证据推翻旧标签（关键词 9.75，压过旧标签项 7.04））
- 其他命中：公民与祖国（6.0） · 集体与同伴（3.2）
- 转述：苏霍姆林斯基分析少先队高产玉米小队连续数年的工作后得出结论：小队集体接受任务、只规定工作性质而不规定个人定额，当"为提高农艺而奋斗"的社会意义被鲜明揭示时，儿童反而干得更好，并且越来越少把成果与报酬挂钩——劳动从外部义务变成内在需要。这正是"先进思想是革命道德信念的源泉"一节的核心论据：共产主义信念要在真正落实先进思想
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《年轻一代共产主义信念的形成》第1章“信念对形成人的精神面貌的作用”之“先进思想是革命道德信念的源泉”，OCR 原PDF页段

### sk-0386　教育艺术：让孩子不再是被动受教育者

- 旧标签：collective-education, child-study
- 建议：**A2 公民与祖国**（旧标签先验 + 文本证据（关键词 6.85 + 先验 1.0 = 7.85））
- 其他命中：美与艺术（4.2） · 自我教育（3.8）
- 转述：苏霍姆林斯基在分析"主客观因素对形成新人的信念的作用"时指出：社会主义社会的生产关系本身是一种有意识的自觉过程，因此教育不能把学生变成被严格细则规定的消极客体，而应委以力所能及的责任，让他们成为社会进步的积极参与者。这是利用社会主义生产关系教育可能性、使客观环境与有目的教育有机结合的关键。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《年轻一代共产主义信念的形成》第2章“共产主义信念的形成是社会进步和道德进步的客观必然性”之“主客观因素对形成新人的信念的作

### sk-0387　教孩子学会爱父母，是父母最重要的哲理

- 旧标签：family-school, love-education
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 11.83 + 先验 2.5 = 14.33））
- 其他命中：劳动与创造（7.0） · 习惯与纪律（4.8）
- 转述：苏霍姆林斯基提醒父母：单向付出而不教孩子回报的爱，会在晚年结出苦果。父母最要紧的哲理是，在爱孩子的同时教会孩子爱父母。他举"尤拉每天给爷爷铺床"为例——母亲用一句"走，我们给爷爷重新铺床"的召唤，让儿子在每天的实际照料中既关怀了老人，又逐渐养成主动劳动和爱亲人的习惯。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》“怎样教会孩子们热爱自己的父母”，OCR 原PDF页段: p0200-0299 (0-based)

### sk-0388　善良的情感是骄傲和自私的解毒剂

- 旧标签：love-education, collective-education
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 4.23 + 先验 2.5 = 6.73））
- 其他命中：全面发展与个性（6.6） · 评价与分数（4.2）
- 转述：苏霍姆林斯基认为，善良的祝愿和情感不是客套，而是骄傲与自私的解毒剂；一个真正善良的人今天会比昨天表现得更好。善意感只有在所有学生（无一例外）的才能都得到和谐发展时才能培养——不能让集体中任何人成为"没有任何才能的人"，也不能把学习成绩当作培育人品的唯一土壤。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》“怎样培养孩子具有善意感”，OCR 原PDF页段: p0400-0499 (0-based)

### sk-0389　只有聪慧的人，才会是幸福的人

- 旧标签：love-education
- 建议：**A11 劳动与创造**（文本证据推翻旧标签（关键词 7.57，压过旧标签项 4.42））
- 其他命中：思维与智力（4.1） · 幸福与精神生活（3.4）
- 转述：苏霍姆林斯基与姑娘们谈爱情时，把"聪慧"作为幸福的前提：真正女性的气质是温柔与端庄、抚爱与不屈不挠的结合，女人的智慧能培养出男子的诚实。他反对"爱情消逝论"，认为爱情不是兽欲而是需要精神力量去创造和终生珍惜的；理智、慎重、严格要求的态度，是对自己和未来家庭的责任。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》“怎样向青年们谈爱情”，OCR 原PDF页段: p0500-0599 (0-based)

### sk-0390　学生应当成为语言的音乐家

- 旧标签：teacher-growth, reading-and-books
- 建议：**A15 思维与智力**（文本证据推翻旧标签（关键词 10.33，压过旧标签项 6.04））
- 其他命中：检查知识与考查（6.0） · 美与艺术（4.5）
- 转述：苏霍姆林斯基认为，批改作业之苦的根源不在批改本身，而在学生作业本中的大量错误；错误的祸根是技能与知识之间的比例失调。减轻批改负担的前提，是全校有高度的语言修养：让学生像感受音乐一样感受语言，让词语与亲身所做、所见、所察、所思的事物发生联系，使语言成为创作的手段。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》“怎样减轻批改作业之苦”，OCR 原PDF页段: p0600-0699 (0-based)

### sk-0391　两种思维类型：逻辑分析与艺术形象

- 旧标签：child-study, thinking-and-nature
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 7.04 + 先验 2.5 = 9.54））
- 其他命中：美与艺术（4.2） · 了解儿童（3.4）
- 转述：苏霍姆林斯基依据巴甫洛夫的分类，把人类思维分为逻辑分析思维（数学思维）与艺术思维（形象思维）。他建议教师在儿童入学前一年带他们到秋天的树林中去观察：艺术型儿童用画面、色彩和声音思维，对自然美敏感，爱文学却常对数学感到困难；数学型儿童首先追问因果关系，容易进行抽象思维。教师必须了解每个儿童哪种类型占优势，并把智力发展引向
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》“怎样研究学前儿童的思维”，OCR 原PDF页段: p0600-0699 (0-based)

### sk-0392　美是照耀世界的明亮之光

- 旧标签：aesthetic-nature-education, child-study
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 10.64 + 先验 1.0 = 11.64））
- 其他命中：自我教育（4.3） · 尊严、爱与信任（4.2）
- 转述：苏霍姆林斯基把美称为"心灵的体操"：美是照耀世界的光，借助它人能看到真相、真理和善良，并体验到献身精神和毫不妥协的精神；美能教会人认识恶并与之斗争。因此美是培养敏锐（对他人痛苦、对恶的敏感）最强有力的手段，理解与感受美是自我教育的强大源泉。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》“美是培养敏锐的强有力手段”，OCR 原PDF页段: p0200-0299 (0-based)

### sk-0393　分数不是衡量孩子的唯一标尺

- 旧标签：assessment-grading, child-study
- 建议：**A16 评价与分数**（旧标签先验 + 文本证据（关键词 9.51 + 先验 2.5 = 12.01））
- 其他命中：健康与作息（4.3） · 幸福与精神生活（4.0）
- 转述：学习、上课、作业和经常性的打分，绝不能成为衡量和评价一个孩子的唯一标准。孩子对日常被评价特别敏感、特别脆弱，教育者应当让孩子亲身体验到：人们是用多把尺子来看他的。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《全面发展的人的培养问题》“在实现个人全面发展思想过程中提出来的一些理论与实际问题”章（OCR 原PDF页段: p0100-

### sk-0394　爱国主义教育的第一步是难忘的童年

- 旧标签：love-education, aesthetic-nature-education
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 6.29 + 先验 1.0 = 7.29））
- 其他命中：公民与祖国（5.3） · 思维与智力（4.1）
- 转述：爱国情感不是从口号开始，而是从童年对家乡自然景物的深刻印象开始。教育者要让每个孩子都拥有一个内容丰富、绚丽难忘的童年，让家乡的自然景物成为他一生受鼓舞的形象记忆。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《全面发展的人的培养问题》“培养对社会主义祖国的热爱和忠诚”章（OCR 原PDF页段: p0100-0199, 0-base

### sk-0395　教育技巧在于展示人的全部素质

- 旧标签：collective-education, teacher-growth
- 建议：**A9 集体与同伴**（旧标签先验 + 文本证据（关键词 3.16 + 先验 2.5 = 5.66））
- 其他命中：全面发展与个性（4.4）
- 转述：集体与个人的发展相互制约、相互依存。教育者的真功夫在于研究这种关系，找到让个性形成最有利的条件，从而把每个人的素质、能力、禀赋和天才充分展示出来。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《全面发展的人的培养问题》“全面发展的人的集体主义特征的培养”章（OCR 原PDF页段: p0200-0299, 0-bas

### sk-0396　快乐是儿童精神发展的源泉

- 旧标签：child-study, health-first
- 建议：**A3 幸福与精神生活**（文本证据推翻旧标签（关键词 3.97，压过旧标签项 2.50））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：快乐不是装饰品，而是儿童发展的前提：有了快乐，儿童才会对自己的力量产生乐观和信心，才愿意与周围世界建立丰富的实际关系；没有这些关系，精神发展乃至天赋的充分发展都不可能。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《学生的精神世界》“外部环境是学生精神生活的决定性因素”节（OCR 原PDF页段: p0300-0399, 0-based）

### sk-0397　让少年不感到教育是强加的

- 旧标签：child-study, teacher-growth
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 4.90 + 先验 1.0 = 5.90））
- 其他命中：美与艺术（4.2） · 道德判断与品德培养（3.0）
- 转述：少年把独立性看作道德尊严的表现，因此教育者的关心和爱护越是像强加的东西，少年就越容易反抗。教育的艺术是：既不让少年感到被强加，又给予比儿童期更多、更严格的管教。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《学生的精神世界》“少年时期”章“(1)集体活动对少年道德发展的意义”节（①积极性发展到一个新阶段是少年的一个突出特点）（O

### sk-0398　少年开始关注看不见摸不着的过程

- 旧标签：thinking-and-nature, child-study
- 建议：**A6 了解儿童**（旧标签先验 + 文本证据（关键词 3.80 + 先验 2.5 = 6.30））
- 其他命中：自然与思维课（4.1）
- 转述：儿童对自然的兴趣以鲜明的、直接可感知的景象为中心；到了少年期，兴趣发生质变，真正吸引他们的是看不见、摸不着的过程与实质，是现象背后的因果和规律。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《学生的精神世界》“少年时期”章“(3)少年的认知兴趣和唯物主义世界观的形成”节（①在认识自然界规律过程中的精神发展）（OC

### sk-0399　劳动是无与伦比的欢乐

- 旧标签：labor-education, collective-education
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 7.01 + 先验 2.5 = 9.51））
- 其他命中：美与艺术（4.5） · 集体与同伴（3.2）
- 转述：劳动带来的欢乐与游览、运动、游戏、文艺和音乐带来的欢乐不同，它无与伦比。这种欢乐来自克服困难、付出体力和精力之后登上顶峰的自豪感，是集体劳动生活的基础。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《培养集体的方法》“集体对个人教育影响的形成”章“(5)集体的劳动生活是集体对个人施加教育影响的一个重要前提”节（OCR 原

### sk-0400　女子应当是高不可攀的

- 旧标签：love-education, collective-education
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 4.90 + 先验 2.5 = 7.40））
- 其他命中：集体与同伴（3.2） · 道德判断与品德培养（3.0）
- 转述：苏霍姆林斯基所说的“高不可攀”不是高傲疏远，而是女生在精神上坚强、有尊严、能主宰自己的感情。男女关系的道德文明是集体道德文明的标志，而培养真正的女子，要从培养精神力量开始。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《培养集体的方法》“集体对个人教育影响的形成”章“(9)集体中的男子和女子”节（OCR 原PDF页段: p0700-0799

### sk-0401　请记住：没有也不可能有抽象的学生

- 旧标签：child-study, learning-difficulties
- 建议：**A6 了解儿童**（旧标签先验 + 文本证据（关键词 6.85 + 先验 2.5 = 9.35））
- 其他命中：幸福与精神生活（4.0） · 教师（2.4）
- 转述：每个学生从事脑力劳动所需的力量各不相同：有的感知快、记得牢，有的感知慢、保持不牢固，但后者后来居上的情况并不少见。因此不存在能套用一切规律的“抽象学生”，也没有对所有学生一律适用的成就先决条件。教师应善于判断每个学生此刻能达到什么程度，并据此个别对待，让每个孩子都体验到脑力劳动中成功的乐趣。
- 出处：《给教师的建议》（杜殿坤编译，教育科学出版社），第1条建议(一)请记住：没有也不可能有抽象的学生；OCR 原PDF页段: p0000-0099 (0-based)

### sk-0402　谈谈对“后进生”的工作

- 旧标签：learning-difficulties, reading-and-books
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 11.40 + 先验 2.5 = 13.90））
- 其他命中：学习困难学生（11.5） · 思维与智力（10.8）
- 转述：对“后进生”最有效的手段不是补课和死抠必修教材，而是扩大阅读范围。学习越困难，越要多读；阅读教人思考，思考变成激发智力的刺激。苏霍姆林斯基以费佳为例：给后进生编习题集、配一百到二百本书，只教阅读和思考，最终费佳赶上并成为熟练技师。
- 出处：《给教师的建议》（杜殿坤编译，教育科学出版社），第6条建议(六)谈谈对“后进生”的工作；OCR 原PDF页段: p0000-0099 (0-based)

### sk-0403　知识——既是目的，也是手段

- 旧标签：learning-difficulties, teacher-growth
- 建议：**A6 了解儿童**（旧标签先验 + 文本证据（关键词 3.80 + 先验 2.5 = 6.30））
- 其他命中：检查知识与考查（5.6） · 劳动与创造（5.3） · 思维与智力（4.1）
- 转述：“知识”不等于会背诵、会回答提问。知识意味着能够运用；只有成为精神生活因素、占据思想并激发兴趣的知识，才配称为知识。如果知识只是储存在记忆里等待“倒出来”的货物，学习就会变成令人生厌的事。因此要让学生借助词进行创造，让知识在脑力劳动、集体精神生活和相互关系中都“活起来”。
- 出处：《给教师的建议》（杜殿坤编译，教育科学出版社），第7条建议(七)知识——既是目的，也是手段；OCR 原PDF页段: p0000-0099 (0-based)

### sk-0404　要教会儿童利用自由支配的时间

- 旧标签：child-study, health-first
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 7.83 + 先验 1.0 = 8.83））
- 其他命中：教师（6.8） · 全面发展与个性（5.0）
- 转述：儿童对时间的感知与成人完全不同，硬性计划会束缚儿童，甚至把孩子从“童年的独木舟”上强拉出来。教儿童利用自由时间，不是放任自流，也不是口头说教，而是组织活动、示范和集体劳动，让有趣、惊奇的事物同时发展思维、知识和技能，又不破坏童年的情趣。
- 出处：《给教师的建议》（杜殿坤编译，教育科学出版社），第26条建议(二六)要教会儿童利用自由支配的时间；OCR 原PDF页段: p0000-0099 (0-based)

### sk-0405　逐步养成儿童从事紧张的创造性脑力劳动的习惯

- 旧标签：health-first, learning-difficulties
- 建议：**A7 健康与作息**（旧标签先验 + 文本证据（关键词 9.49 + 先验 2.5 = 11.99））
- 其他命中：劳动与创造（5.3） · 习惯与纪律（4.8）
- 转述：紧张的创造性脑力劳动习惯要“渐渐地”养成，不能靠开学就强制。儿童要学会在特定时刻集中精力达到目标；只有养成专心致志的习惯，脑力劳动才可能成为喜爱之事。同时，低年级不能追求“不浪费一分钟”的满负荷节奏，那样会使儿童精疲力竭；要变换作业形式、安排户外活动、用图画和创造性活动调节，保护儿童的神经与健康。
- 出处：《给教师的建议》（杜殿坤编译，教育科学出版社），第55条建议(五五)逐步养成儿童从事紧张的创造性脑力劳动的习惯；OCR 原PDF页段: p0100-0199 (0-based)

### sk-0406　谈谈教师的教育素养

- 旧标签：teacher-growth, reading-and-books
- 建议：**A15 思维与智力**（文本证据推翻旧标签（关键词 10.33，压过旧标签项 9.60））
- 其他命中：阅读与书籍（7.1） · 健康与作息（4.1）
- 转述：教师的教育素养首先来自对所教学科的深刻知识——教学大纲对教师应只是起码常识；其次是懂得研究儿童的方法，有扎实的心理学基础；再次是语言修养，它极大程度地决定学生课堂脑力劳动的效率。教师语言混乱、逻辑不清，学生只能靠课外抠教科书来弥补，这是以健康为代价的。提升教育素养的根本途径是“读书，读书，再读书”。
- 出处：《给教师的建议》（杜殿坤编译，教育科学出版社），第87条建议(八七)谈谈教师的教育素养；OCR 原PDF页段: p0400-0499 (0-based)

### sk-0407　劳动教育和个性全面发展

- 旧标签：labor-education
- 建议：**A1 全面发展与个性**（文本证据推翻旧标签（关键词 14.59，压过旧标签项 4.83））
- 其他命中：幸福与精神生活（3.8） · 集体与同伴（3.2）
- 转述：劳动教育不是孤立的技能训练，而要紧密联系德育、智育、美育，使劳动进入个性和集体的精神生活，让热爱劳动在少年和青年早期就成为最重要的品质之一。文章提出多项原则：劳动素养与一般发展相结合；在劳动中展示、发现和发展个性；劳动具有高度的道德意义和公益方向；童年期早期参加生产劳动；劳动种类多样化、经常不断、量力而行；劳动与多方面
- 出处：《给教师的建议》（杜殿坤编译，教育科学出版社），第94条建议(九四)劳动教育和个性全面发展；OCR 原PDF页段: p0500-0573 (0-based)

### sk-0408　怎样使学校教育和家庭教育保持一致？

- 旧标签：family-school, reading-and-books
- 建议：**A8 家庭与母亲**（旧标签先验 + 文本证据（关键词 10.07 + 先验 2.5 = 12.57））
- 其他命中：阅读与书籍（7.4） · 思维与智力（5.7）
- 转述：学校教育和家庭教育的影响方向必须一致，否则学校教学过程会像纸房子一样倒塌。实现一致的途径包括：长期开办家长学校（从学前组到青年期组）、让每个家庭过“书籍节”并拥有最低限度藏书、吸引家长参与校务委员会、以及谨慎而有分寸地对家长进行个别指导。家长是儿童最早的教育者，学龄前的家庭环境在很大程度上决定了儿童的精神发展和求知欲。
- 出处：《给教师的建议》（杜殿坤编译，教育科学出版社），第99条建议(九九)怎样使学校教育和家庭教育保持一致？；OCR 原PDF页段: p0500-0573 (0-based)

### sk-0409　谷物芬多精：新鲜空气是健康的灵药

- 旧标签：health-first
- 建议：**A7 健康与作息**（旧标签先验 + 文本证据（关键词 4.14 + 先验 2.5 = 6.64））
- 其他命中：自然与思维课（4.2） · 家庭与母亲（4.1）
- 转述：苏霍姆林斯基把田间谷物（小麦、黑麦、大麦、荞麦等）散发的芬多精空气称为“健康的灵药”。他常带孩子去田野、草地呼吸充满谷物香气的空气，并建议家长在孩子卧室窗下种植榛树——榛树释放的芬多精能杀死多种致病菌和害虫。
- 出处：On Education (1977, Progress Publishers), Part I 'Half Our Work Is Devoted to Health Care'

### sk-0410　孩子做坏事，多半是因为没学过做好事

- 旧标签：love-education, collective-education
- 建议：**A19 道德判断与品德培养**（文本证据推翻旧标签（关键词 8.39，压过旧标签项 2.50））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：苏霍姆林斯基提醒：学生做出不良行为，往往不是有人教他作恶，而是成人从未认真教过他如何行善。道德教育应当把功夫下在“教善”上，而不是等坏事出现后再去追责和纠正。
- 出处：On Education (1977, Progress Publishers), Part VI 'Morals and Convictions / Devotion to an

### sk-0411　劳动教育成功的标志：孩子舍不得回家

- 旧标签：labor-education
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 2.33 + 先验 2.5 = 4.83））
- 其他命中：教师（2.4）
- 转述：苏霍姆林斯基给出一个朴素而鲜明的判断标准：当劳动活动结束时，孩子们不是一哄而散，而是需要教师催促才肯回家，劳动教育才算真正成功。这说明劳动本身已经产生了内在吸引力，而不再依赖外在要求。
- 出处：On Education (1977, Progress Publishers), Part III 'Work / From Technical ABC's to Advance

### sk-0412　真正的学校是积极思维的王国

- 旧标签：reading-and-books, thinking-and-nature
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 11.40 + 先验 2.5 = 13.90））
- 其他命中：思维与智力（7.0）
- 转述：苏霍姆林斯基认为，真正的学校是积极思维的王国。八年级学生若只完成教科书十页的阅读，并不算真正在思维；只有当天还出于“想思考、想发现、想惊奇”的内在需要，主动去读二三十页有趣的书籍或期刊，思维才真正活跃起来。
- 出处：On Education (1977, Progress Publishers), Part II 'Study / A True School Is a Kingdom of A

### sk-0413　教鞭与拳头是教师职业的耻辱

- 旧标签：teacher-growth, family-school
- 建议：**A8 家庭与母亲**（旧标签先验 + 文本证据（关键词 4.14 + 先验 2.5 = 6.64））
- 其他命中：尊严、爱与信任（4.2） · 阅读与书籍（2.9）
- 转述：苏霍姆林斯基强烈谴责一种隐性的体罚链条：教师把学生的不良表现写进记录、通知家长，等于“把棍子塞进学生的书包”，让孩子回家挨父亲打。学校本应是人性、善良与真理的圣地，孩子却因此害怕跨进校门。他打比方说：这无异于在精细手术进行时，让屠夫提着斧头闯进手术室。
- 出处：On Education (1977, Progress Publishers), Part I 'Education and the Educator / One of the 

### sk-0414　体操挺直身体，音乐挺直心灵

- 旧标签：aesthetic-nature-education
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 6.29 + 先验 1.0 = 7.29））
- 其他命中：美与艺术（4.5） · 健康与作息（4.3）
- 转述：苏霍姆林斯基把音乐比作心灵的体操：体操使身体挺拔，音乐使心灵正直。学校生活中渗透音乐活动，能在很大程度上决定教育工作的质量，因为音乐让儿童的情感保持敏感，使心对善良、美好的呼唤保持回应。
- 出处：On Education (1977, Progress Publishers), Part IV 'Beauty / Music Keeps the Heart Straight

### sk-0415　儿童理性的永恒源泉在大自然

- 旧标签：thinking-and-nature, aesthetic-nature-education
- 建议：**A12 自然与思维课**（旧标签先验 + 文本证据（关键词 4.14 + 先验 1.0 = 5.14））
- 其他命中：劳动与创造（2.3）
- 转述：苏霍姆林斯基指出，环绕儿童的世界首先是大自然——一个美与多样性取之不尽的自然世界。儿童的理性有其永恒源泉，这源泉应当到大自然中去寻找。同时他补充：随着儿童成长，与社会关系、劳动相连的环境因素应逐年增加分量；但人始终是大自然之子。
- 出处：On Education (1977, Progress Publishers), Part II 'Study / Children Should Live in a World

### sk-0416　青春期是人的第二次诞生

- 旧标签：child-study, love-education
- 建议：**A4 自我教育**（文本证据推翻旧标签（关键词 5.84，压过旧标签项 5.05））
- 其他命中：公民与祖国（4.0） · 思维与智力（3.3）
- 转述：苏霍姆林斯基把青春期比作“第二次诞生”：第一次诞生的是生命，第二次诞生的是公民——一个不仅能认识周围世界、也能认识自己的积极思考者。少年嘴上说“别管我、我能行”，内心却渴望一位年长朋友的肩膀；教育者要读懂这种矛盾。
- 出处：On Education (1977, Progress Publishers), Part VI 'Morals and Convictions / The World of I

### sk-0417　儿童创造力是自我表达与自我肯定的独特领域

- 旧标签：aesthetic-nature-education, child-study
- 建议：**A1 全面发展与个性**（文本证据推翻旧标签（关键词 4.38，压过旧标签项 2.98））
- 其他命中：劳动与创造（3.0）
- 转述：儿童的创造力是他们内心生活、自我表达与自我肯定的深刻而独特的领域；正是在创造中，每个孩子独特的个性才清晰地显露出来。苏霍姆林斯基由此认为，这种独特性无法用任何普适标准去分类或衡量。
- 出处：To Children I Give My Heart (Progress Publishers, Moscow; text shows no year), The School 

### sk-0418　在大自然的背景中教孩子听懂音乐

- 旧标签：aesthetic-nature-education, thinking-and-nature
- 建议：**A14 美与艺术**（旧标签先验 + 文本证据（关键词 10.38 + 先验 2.5 = 12.88））
- 其他命中：自然与思维课（8.3） · 幸福与精神生活（3.7）
- 转述：音乐欣赏教学应当以大自然为背景：让孩子在静谧的田野与草地、橡树林的沙沙声、蓝天下云雀的歌声、成熟麦穗的低语、蜜蜂与熊蜂的嗡嗡声中，理解并感受音乐之美。这些自然之声正是音乐旋律灵感的源头。
- 出处：To Children I Give My Heart (Progress Publishers, Moscow; text shows no year), The School 

### sk-0419　幻想形象是思维幼芽最肥沃的土壤

- 旧标签：child-study, thinking-and-nature
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 8.37 + 先验 2.5 = 10.87））
- 其他命中：美与艺术（4.2） · 了解儿童（3.4）
- 转述：苏霍姆林斯基在“幻想之角”观察孩子们看黄昏树丛：有的孩子思维像湍急的小溪，有的则像深沉的河流。他认为童年期的思维必须尽量与周围世界鲜活、鲜明的形象相连；孩子先看到活的形象，再在想象中把它消化成自己的概念。幻想形象不是脱离现实的空想，而是思维中艺术化、诗意化的成分，是思维幼芽最肥沃的土壤；情感饱满的感知则是儿童创造力的内
- 出处：To Children I Give My Heart (Progress Publishers, Moscow; text shows no year), The School 

### sk-0420　对劳动者的爱是人的道德之源

- 旧标签：labor-education, love-education
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 3.97 + 先验 1.0 = 4.97））
- 其他命中：道德判断与品德培养（3.0） · 劳动与创造（2.3）
- 转述：苏霍姆林斯基带“快乐学校”的孩子到粮仓、牛奶场、铸造厂和农机站去“旅行”，让孩子亲眼看到劳动者的美：康拜因手十年收获的粮食能供一座城市做面包，塔尼亚的妈妈挤的奶够一千五百人吃，拉里莎爸爸灵巧的手车出没有它发动机就不能转动的螺丝。孩子们对劳动人民产生深深的敬意，这种对劳动者的爱，被苏霍姆林斯基视为人的道德之源。
- 出处：To Children I Give My Heart (Progress Publishers, Moscow; text shows no year), The School 

### sk-0421　只靠夏天不能保住孩子的健康：冬天也是锻炼好时节

- 旧标签：health-first
- 建议：**A7 健康与作息**（旧标签先验 + 文本证据（关键词 13.23 + 先验 2.5 = 15.73））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：针对“只有夏天才能让孩子健康”的成见，苏霍姆林斯基指出：认为孩子只有夏天才能养好身体是大错特错。冬天有适度寒冷的气温、柔软丰厚的雪，是增强孩子体质的好机会；如果不利用冬天来强健身体，夏天也帮不上忙。他训练孩子耐寒、呼吸干净清冷的空气，带他们在雪地游戏、在冰上活动，体弱的孩子也由此变得面色红润。
- 出处：To Children I Give My Heart (Progress Publishers, Moscow; text shows no year), The School 

### sk-0422　只有当词语触动心灵隐秘处，阅读才丰富儿童生活

- 旧标签：reading-and-books, child-study
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 9.80 + 先验 2.5 = 12.30））
- 其他命中：了解儿童（3.4） · 幸福与精神生活（3.0）
- 转述：苏霍姆林斯基观察到，孩子们朗读单调、没有表情，根源在于阅读与内心生活脱节：孩子心里激动的是这件事，嘴里读的却是另一件事。只有当词语触动了孩子心灵最隐秘的角落，阅读才能真正丰富他们的生活。这提醒他：让孩子读的内容必须与孩子的思想、感情和观念相连，而不能只是机械地念字。
- 出处：To Children I Give My Heart (Progress Publishers, Moscow; text shows no year), The School 

### sk-0423　学习应逐步开始：既是艰巨劳动，也是愉快劳动

- 旧标签：teacher-growth, child-study
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 4.26 + 先验 1.0 = 5.26））
- 其他命中：健康与作息（4.3） · 幸福与精神生活（4.0）
- 转述：“快乐学校”结束、孩子即将入学之际，苏霍姆林斯基反思入学衔接：他尊重教学论、反对轻率空想的方案，但生活本身要求掌握知识要一点一点开始；学习是孩子最严肃、最费力的劳动，同时必须是一种愉快的劳动，能增强而不是消耗孩子的精神与身体力量。孩子成为小学生后，应当继续做昨天做过的事，让新东西逐渐进入生活，而不是被“印象雪崩”击晕。
- 出处：To Children I Give My Heart (Progress Publishers, Moscow; text shows no year), The School 

### sk-0424　为创造美而劳动，会使孩子变得更好更美

- 旧标签：aesthetic-nature-education, labor-education
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 5.31 + 先验 2.5 = 7.81））
- 其他命中：幸福与精神生活（3.0）
- 转述：孩子们亲手开辟“美之角”、移植铃兰和椴树、给野蔷薇嫁接玫瑰，全校又建起玫瑰园；收获的花送给老师、妈妈和村里的优秀劳动者。苏霍姆林斯基总结：为创造美而劳动能使年轻的心灵高尚起来，防止冷漠；在创造大地之美的过程中，孩子们自己变得更美好、更纯洁、更美丽。
- 出处：To Children I Give My Heart (Progress Publishers, Moscow; text shows no year), The Years o

### sk-0425　每个人都必须发光：没有人应当成为风中尘埃

- 旧标签：child-study, teacher-growth
- 建议：**A1 全面发展与个性**（文本证据推翻旧标签（关键词 4.43，压过旧标签项 3.42））
- 其他命中：幸福与精神生活（3.4） · 劳动与创造（3.0）
- 转述：苏霍姆林斯基坚信人格不可穷尽，每个人都能成为创造者，在世上留下自己的痕迹。他不接受任何人是“风中尘埃”，主张每个人都必须像银河中的群星一样发光。（本段为苏霍姆林斯基原话英译，非 Cockerill 分析；“communism”为原文时代语汇，可理解为“共同的幸福理想”。）
- 出处：Each One Must Shine (Cockerill, 2009 electronic ed.), Chapter 3, 'Moral Education' section

### sk-0426　儿童是活的生命，大脑是最娇嫩的器官

- 旧标签：health-first
- 建议：**A7 健康与作息**（旧标签先验 + 文本证据（关键词 4.14 + 先验 2.5 = 6.64））
- 其他命中：全面发展与个性（5.2） · 劳动与创造（2.3）
- 转述：苏霍姆林斯基反对以“节奏与强度”换学业进度：儿童是活的生命，大脑是最娇嫩的器官，必须小心呵护。即使小学教育可以三年完成，前提也是持续关心儿童健康和机体的正常发育；有效脑力劳动的基础不在快慢与强度，而在组织得当并同时开展多方面的体育、智育与美育。（本段为苏霍姆林斯基原话英译，非 Cockerill 分析。）
- 出处：Each One Must Shine (Cockerill, 2009 electronic ed.), Chapter 3, 'Physical Education and H

### sk-0427　通过父母之爱创造人

- 旧标签：family-school, love-education
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 8.89 + 先验 2.5 = 11.39））
- 其他命中：家庭与母亲（3.5） · 劳动与创造（3.0）
- 转述：苏霍姆林斯基认为，教育孩子需要精神上的努力，而根本途径是父母之间的爱：父亲爱母亲、母亲爱父亲，同时爱并尊重他人。在这种家庭里长大的孩子内心平静、心理健壮，对人性和教师的话有信任，对善言与美有感应。（本段为苏霍姆林斯基原话英译，非 Cockerill 分析；OCR 中“teacher s word”缺省撇号，应为 tea
- 出处：Each One Must Shine (Cockerill, 2009 electronic ed.), Chapter 3, 'Moral Education' / famil

### sk-0428　每个人身上都有待展开的天赋：以创造他人之乐来吸引

- 旧标签：love-education, teacher-growth
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 3.97 + 先验 1.0 = 4.97））
- 其他命中：劳动与创造（3.0）
- 转述：苏霍姆林斯基认为：只要有得当的教育工作，没有人是“没有天赋”的；也没有哪个活动领域是人无法发光的。关键在于教育者能否用最高尚的创造活动——为他人创造快乐——来吸引人。（本段为苏霍姆林斯基原话英译，非 Cockerill 分析。）
- 出处：Each One Must Shine (Cockerill, 2009 electronic ed.), Chapter 3, 'Moral Education' section

### sk-0429　当学习变成纯书本之事：字母在眼前跳舞

- 旧标签：reading-and-books, learning-difficulties
- 建议：**A6 了解儿童**（旧标签先验 + 文本证据（关键词 7.17 + 先验 2.5 = 9.67））
- 其他命中：阅读与书籍（2.9）
- 转述：苏霍姆林斯基观察到一个反差：当识字教学变成纯书本之事，字母会在孩子眼前“跳舞”，难以分辨；而当学习被兴趣、游戏点亮，且没有“必须记住，否则更糟”的威胁时，孩子却很容易记住字母并拼出词。（本段为苏霍姆林斯基原话英译，非 Cockerill 分析。）
- 出处：Each One Must Shine (Cockerill, 2009 electronic ed.), Chapter 4, 'Intellectual Education' 

### sk-0430　多样劳动是磁铁：吸引孩子找到天职

- 旧标签：labor-education
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 2.33 + 先验 2.5 = 4.83））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：苏霍姆林斯基把儿童从入学起就接触到的多种劳动比作强弱不同的磁铁，吸引着指引人生方向的指南针。劳动越有趣，孩子越投入，其能力、倾向与天职就越清晰地发展出来。（本段为苏霍姆林斯基原话英译，非 Cockerill 分析。）
- 出处：Each One Must Shine (Cockerill, 2009 electronic ed.), Chapter 4, 'Work Education' section,

### sk-0431　美只有在人为创造美而劳动时才能使人高尚

- 旧标签：aesthetic-nature-education, labor-education
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 5.31 + 先验 2.5 = 7.81））
- 其他命中：幸福与精神生活（4.0）
- 转述：苏霍姆林斯基认为，美本身不会自动使人高尚——只有当人通过劳动去创造美时，美才具有使人高尚的力量。因此他努力让学生不仅为糊口而劳动，也为创造快乐而劳动。（本段为苏霍姆林斯基原话英译，非 Cockerill 分析。）
- 出处：Each One Must Shine (Cockerill, 2009 electronic ed.), Chapter 4, 'Aesthetic Education' sec

### sk-0432　儿童用形象思考：先有画面，再理解规律

- 旧标签：thinking-and-nature, child-study
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 3.31 + 先验 2.5 = 5.81））
- 其他命中：教师（2.4）
- 转述：苏霍姆林斯基指出，儿童用形象思考：教师描述一滴水的旅程时，孩子脑中会浮现晨雾、乌云、雷声和春雨的画面；这些画面越鲜明，孩子对自然规律的理解就越深。儿童稚嫩的神经细胞尚未强化，正需要这样的形象与经验来滋养。（本段为苏霍姆林斯基原话英译，非 Cockerill 分析。）
- 出处：Each One Must Shine (Cockerill, 2009 electronic ed.), Chapter 4, 'Intellectual Education' 

### sk-0994　兴趣的奥秘何在

- 旧标签：learning-difficulties, teacher-growth, thinking-and-nature
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 10.82 + 先验 2.5 = 13.32））
- 其他命中：劳动与创造（10.0） · 了解儿童（3.8）
- 转述：苏霍姆林斯基把兴趣的奥秘归结为认知本身：兴趣不是靠花哨的刺激逗出来的，而是学生在发现事物本质、因果联系和知识力量时产生的兴奋、诧异与自豪。求知兴趣的首要源泉在教师对教材的处理方式——能否找到事实之间的“接触点”和“线索”，把隐蔽的、一下子看不出来的东西揭示给学生。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 25“兴趣的奥秘何在”

### sk-0995　关于做“困难”学生的工作

- 旧标签：learning-difficulties, reading-and-books, child-study
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 11.40 + 先验 2.5 = 13.90））
- 其他命中：思维与智力（10.8） · 学习困难学生（5.7）
- 转述：苏霍姆林斯基把“困难”学生——理解和记忆都比别人慢三五倍、第二天就忘——称为教育工作里“最硬的核桃”。他的核心主张不是补课和反复督促，而是扩大阅读：为每个困难儿童挑选最鲜明、有趣、能阐明概念、结论和科学特点的书籍与小册子，让他们在课外阅读中不断遇到惊奇和诧异。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 10“关于做‘困难’学生的工作”

### sk-0996　阅读是“困难”学生智力教育的重要手段

- 旧标签：reading-and-books, learning-difficulties
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 6.83 + 先验 2.5 = 9.33））
- 其他命中：学习困难学生（12.2） · 思维与智力（7.5）
- 转述：针对“困难”学生，常见的错误做法是把他们的脑力劳动范围尽量缩小，甚至只允许读教科书。苏霍姆林斯基明确反对这一点：学习越困难，遇到的理解障碍越多，就越需要多阅读。他用“感光力弱的胶卷需要更长的感光时间”作比，说明成绩差的学生需要更明亮、更持久的科学知识之光来照耀。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 23“阅读是‘困难’学生智力教育的重要手段”

### sk-0997　评分应当有分量

- 旧标签：assessment-grading, learning-difficulties, child-study
- 建议：**A16 评价与分数**（旧标签先验 + 文本证据（关键词 14.36 + 先验 2.5 = 16.86））
- 其他命中：尊严、爱与信任（9.6） · 学习困难学生（5.6）
- 转述：苏霍姆林斯基首先把评分放回师生关系的整体中：评分不能从教学过程中单独划出来，只有师生彼此信任、彼此关怀，分数才会成为推动脑力劳动的力量，否则它只是最微妙也最容易伤人的工具。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 17“评分应当有分量”

### sk-0998　“两个教学大纲”，发展学生的思维

- 旧标签：thinking-and-nature, reading-and-books, learning-difficulties
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 14.50 + 先验 2.5 = 17.00））
- 其他命中：阅读与书籍（4.0）
- 转述：“两个教学大纲”是苏霍姆林斯基智育思想中一个高度浓缩的框架。第一个大纲是必须学会并记住的材料——那些反映事物特性的重要结论、概括、公式、规则和定律；第二个大纲是课外阅读以及其他知识来源。二者不是并列的两套任务，而是“地基”与“承重墙”的关系：需要牢记的材料越复杂，越需要大量无须记住的阅读和思考来打“智力底子”。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 9“‘两个教学大纲’，发展学生的思维”

### sk-0999　怎样培养记忆力

- 旧标签：thinking-and-nature, child-study, learning-difficulties
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 7.83 + 先验 2.5 = 10.33））
- 其他命中：幸福与精神生活（7.3） · 自我教育（4.4）
- 转述：苏霍姆林斯基把记忆力问题放在思维和情感的土壤上来谈：靠自己努力和意志获得的知识、被逻辑认知深深触动过的知识，才记得牢、有条理。一个儿童如果只看见事物表面，在考察内部实质时没有任何“发现”，没有体验过发现意外联系时的惊奇感，就很难记住东西。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 41“怎样培养记忆力”

### sk-1000　要掌握与学生个别谈话的艺术

- 旧标签：teacher-growth, child-study, love-education
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 7.47 + 先验 1.0 = 8.47））
- 其他命中：家庭与母亲（7.6） · 评价与分数（4.8）
- 转述：苏霍姆林斯基把个别谈话看作教育能否发生的前提。孩子本质上具有向教师敞开心灵、倾吐感情和思想的精神要求，但这份信任极其脆弱：只要教师试图借家长或权威来“管束、制服”孩子，或者让孩子觉得教师会把父母变成吓人的东西，心门就会关上。应教育孩子热爱父母和教师，而不是惧怕他们。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 83“要掌握与学生个别谈话的艺术”

### sk-1001　怎样教孩子正确对待批评、责备、惩罚

- 旧标签：family-school, child-study, love-education
- 建议：**A16 评价与分数**（文本证据推翻旧标签（关键词 14.37，压过旧标签项 8.09））
- 其他命中：幸福与精神生活（7.1） · 尊严、爱与信任（4.4）
- 转述：苏霍姆林斯基把批评、责备、惩罚放在“人如何对待他人的评价”这一道德修养问题里。人人都对坏的东西表示批评和责备，这本身就是和睦相处的一部分；一个人怎样对待批评和责备，能反映出他的道德修养。要教孩子理解和感受责备中流露的正义感，学会感谢那些尖锐但中肯的话，因为它们在救人，使人不至于堕落。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》39“怎样教孩子正确对待批评、责备、惩罚”

### sk-1002　父母在孩子生活中的作用

- 旧标签：family-school, love-education, child-study
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 9.71 + 先验 1.0 = 10.71））
- 其他命中：劳动与创造（6.9） · 尊严、爱与信任（4.3）
- 转述：苏霍姆林斯基从孩子对父母的态度谈起：父母给了你生命，为你而活，你应珍惜他们的健康与安宁，尊重他们用劳动、血汗和劳累换来的一切，给家里带来欢乐与平静。但他随即把问题提升到教育的前提条件：父与子是教育中最复杂的问题之一，如果父母本身不是有道德素养、能使孩子生活充实的人，一切教育影响的尝试都会落空。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》20“父母在孩子生活中的作用”

### sk-1004　勇敢精神、对敌人的不可调和性和必胜意志的培养

- 旧标签：collective-education, labor-education, child-study
- 建议：**A2 公民与祖国**（旧标签先验 + 文本证据（关键词 7.98 + 先验 1.0 = 8.98））
- 其他命中：自我教育（4.4） · 道德判断与品德培养（3.0）
- 转述：苏霍姆林斯基把勇敢精神看作公民自觉性的最高表现，而不是与生俱来的气质。勇敢的根不在战场，而在童年日常的细小事情里：不因一点疼痛就叫苦，不处处怜惜自己，敢于为弱者挺身而出，对邪恶与不公正不能无动于衷。他特别警惕成人出于疼爱而让孩子形成“我很软弱、需要被保护”的自我感觉，因为这种自我怜惜会滋生出胆怯、自私和冷漠。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《全面发展的人的培养问题》第7章“勇敢精神、对敌人的不可调和性和必胜意志的培养”

### sk-1005　智力积极性和少年自我意识、自我评价的形成

- 旧标签：child-study, learning-difficulties, teacher-growth
- 建议：**A16 评价与分数**（文本证据推翻旧标签（关键词 8.93，压过旧标签项 4.88））
- 其他命中：家庭与母亲（3.5） · 思维与智力（3.4）
- 转述：少年自我意识的觉醒，首先表现为他意识到“我已经不是儿童”。他因此对别人如何评价自己异常敏感：既渴望得到教师和集体的赞扬，也容易因一句讽刺、一次当众揭短而受伤甚至走向对立。苏霍姆林斯基由此得出教育上的分寸：当少年已经知道自己的缺点并正在努力克服时，成人不应反复强调、讽刺挖苦，而应给他时间和精神力量去自我纠正；不适当的干预
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《学生的精神世界》第5章 (5)“智力积极性和少年自我意识、自我评价的形成”

### sk-1006　儿童集体中的欢乐和善感、力量和良心

- 旧标签：collective-education, love-education, child-study
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 13.52 + 先验 2.5 = 16.02））
- 其他命中：幸福与精神生活（11.0） · 集体与同伴（6.8）
- 转述：苏霍姆林斯基区分了两种“欢乐”：一种是想要什么就得到什么的满足感，另一种是出于关心、忧虑和照料而生的喜悦。前者会让孩子对真正的欢乐源泉变得冷漠，后者才使孩子愿意爱护自己的愿望，进而感受到与同学交往的快乐，并在他人身上发现精神财富。他特别强调，儿童应当先学会爱护比自己更弱小、更需要照料的生命，因为这种温柔的情感是集体道德
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《培养集体的方法》第3章 (7)“儿童集体中的欢乐和善感、力量和良心”

### sk-1007　祖国语言

- 旧标签：aesthetic-nature-education, reading-and-books, thinking-and-nature
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 14.49 + 先验 2.5 = 16.99））
- 其他命中：幸福与精神生活（11.0） · 公民与祖国（3.9）
- 转述：在苏霍姆林斯基看来，祖国语言不只是交流工具，而是人民的精神财富，也是一个人精神修养的镜子。只有先掌握并感受到祖国语言的美，其他民族语言宝库中的财富才可能真正被打开；对母语细微之处的体会越深，掌握其他语言的能力和愿望也越强。因此，语言教育从孩子入学的第一天起就应开始，并且首先指向情感、美学和含义上的色调，而不只是拼读与语
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《我把心给了孩子们》“祖国语言”

### sk-1008　书和儿童的精神生活

- 旧标签：reading-and-books, child-study, family-school
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 6.83 + 先验 2.5 = 9.33））
- 其他命中：美与艺术（4.5） · 自我教育（4.3）
- 转述：苏霍姆林斯基指出，书要在儿童精神生活中真正起作用，前提是孩子“会阅读”——而会阅读不只是能快速认字，更是对语言的含义、优美和细腻文采有敏感。如果阅读只停留在技巧训练，书就不会成为引导孩子攀登智育、德育和美育高峰的小径。
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《我把心给了孩子们》“儿童时代”之“书和儿童的精神生活”

### sk-1009　少年的身体发育与心理素养

- 旧标签：health-first, child-study, family-school
- 建议：**A7 健康与作息**（旧标签先验 + 文本证据（关键词 10.22 + 先验 2.5 = 12.72））
- 其他命中：思维与智力（11.2） · 幸福与精神生活（7.0）
- 转述：苏霍姆林斯基把少年期称为“第二次诞生”：第一次诞生的是生命，第二次诞生的是公民——一个不仅看见世界、也看见自己的积极思考者。少年会突然宣称“别照看我，别束缚我的手脚”，内心却又渴望一位年长朋友的肩膀。这种“要独立”与“要依靠”的矛盾，加上身高猛增、骨骼与肌肉发育不同步、血压升高、性成熟开始等生理变化，共同造成少年容易疲
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《公民的诞生》第4章“少年的身体发育与心理素养”

### sk-1010　智育：知识的内容、掌握过程与智力发展

- 旧标签：thinking-and-nature, learning-difficulties, teacher-growth
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 3.35 + 先验 2.5 = 5.85））
- 其他命中：评价与分数（4.8） · 教师（2.4）
- 转述：苏霍姆林斯基对智育给出一个关键区分：掌握教材不等于智育。评价教学方法的标准，不是学生记住了多少知识，而是这一掌握过程是否带来了最高水平的一般智力发展，而智力发展又反过来让后续学习变得更容易。许多学生越学越吃力，根本原因正是“掌握知识”与“智力发展”脱节——教师把知识量当成了终点，没有把它当作培养发达智力的手段。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》第5章“智育”（“知识的内容与智育”“知识的掌握过程与智力发展”）

### sk-1011　关于听课和分析课的几点建议

- 旧标签：teacher-growth, assessment-grading, child-study
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 7.21 + 先验 2.5 = 9.71））
- 其他命中：思维与智力（7.5） · 阅读与书籍（7.4）
- 转述：苏霍姆林斯基把听课与分析课摆在校长工作的首位：校长若不了解课堂，其他工作都会失去意义。他给自己定下规矩——一天至少听两节课；出差前先补听，学期初不“加速”、学期末也不草率收尾。听课不是只找教师的错误和缺点，更重要的目的是研究教师的眼界、兴趣和精神财富如何在课堂上表现出来，并把个别教师的创造性经验变成全体教师的共同财富。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《和青年校长的谈话》第7次谈话“关于听课和分析课的几点建议”

### sk-1013　认识自己

- 旧标签：child-study, teacher-growth, love-education
- 建议：**A4 自我教育**（旧标签先验 + 文本证据（关键词 14.61 + 先验 1.0 = 15.61））
- 其他命中：评价与分数（9.0） · 习惯与纪律（4.9）
- 转述：本篇以一位少年读者的来信开篇：他成绩不差，却发现自己是个“没有意志力的人”，只会做被迫做的事，于是追问“自我教育从何做起”。苏霍姆林斯基借菲利普爷爷临终的话回答：人生的睿智就是认识自己，而自我教育正是从认识自己开始的。他指出，自我教育的实质是善于强制自己，这种能力扎根于自豪感——一个人在自己的劳动中体会到艰辛，也体会到
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第51篇“认识自己”

### sk-1014　序言：把实际工作与科学研究结合起来

- 旧标签：teacher-growth, child-study
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 7.21 + 先验 2.5 = 9.71））
- 其他命中：全面发展与个性（5.0） · 思维与智力（3.7）
- 转述：这是《全面发展的人的培养问题》的序言。苏霍姆林斯基先交代自己的身份：在同一所普通中学连续做了三十五年教师和校长，因此得以长期观察两代人的成长——即将毕业的学生，正是他最初从教那几年学生的子女。他反复强调，这本书不是坐在书斋里写出来的，而是把理论分析与对集体、个人施加教育影响的实际探索结合在一起。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《全面发展的人的培养问题》序言

### sk-1015　个人全面发展思想的历史沿革

- 旧标签：teacher-growth, labor-education
- 建议：**A1 全面发展与个性**（文本证据推翻旧标签（关键词 9.44，压过旧标签项 5.87））
- 其他命中：习惯与纪律（4.9） · 幸福与精神生活（3.8）
- 转述：这是全书的第一章。苏霍姆林斯基用思想史的线索说明：全面发展的观念并非凭空产生，它经历了古代“身心既美且善”的理想、中世纪教会对理性与欢乐的压制、文艺复兴人文主义的复活、空想社会主义者把劳动与教学结合的幻想，直到马克思、恩格斯揭示出人的全面发展的客观条件，以及列宁把它作为社会主义教育的实际任务。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《全面发展的人的培养问题》第1章“个人全面发展思想的历史沿革”

### sk-1016　怎样培养孩子的精神力量

- 旧标签：love-education, health-first, child-study
- 建议：**A7 健康与作息**（旧标签先验 + 文本证据（关键词 4.80 + 先验 2.5 = 7.30））
- 其他命中：自我教育（4.4） · 幸福与精神生活（3.3）
- 转述：这一篇谈的是意志与精神力量的早期培养。苏霍姆林斯基认为，人的精神力量是无穷的，真正可怕的是“吝惜自己”——这种意志薄弱的情感会把强者变成弱者。他主张从幼年起就让孩子经历并克服困难，让他在做成本来以为做不到的事情时，对自己的精神力量感到惊奇；只有这种惊奇，才能让他真正蔑视懦弱、为软弱感到羞愧。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》第5篇“怎样培养孩子的精神力量”

### sk-1017　大自然——健康的源泉

- 旧标签：health-first, aesthetic-nature-education
- 建议：**A7 健康与作息**（旧标签先验 + 文本证据（关键词 13.71 + 先验 2.5 = 16.21））
- 其他命中：学习困难学生（16.2） · 习惯与纪律（10.8）
- 转述：这一节把“健康”与“学业落后”直接连在一起。苏霍姆林斯基依据多年观察指出，约85%的不及格学生学业落后的主要原因是健康状况不佳，而这种不适往往隐蔽得连孩子自己都察觉不到；所谓“头脑迟钝”，多数并非大脑皮层的生理病变，而是周身不适造成的。他给出的“治本办法”不是补课，而是改变作息制度：多在新鲜空气中逗留、开窗睡觉、早睡早
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《我把心给了孩子们》“快乐学校·大自然——健康的源泉”

### sk-1018　总结的实质及做法

- 旧标签：teacher-growth, reading-and-books
- 建议：**A15 思维与智力**（文本证据推翻旧标签（关键词 7.51，压过旧标签项 7.33））
- 其他命中：教师（4.8）
- 转述：这是《和青年校长的谈话》最后一次谈话中的一节，讲学年总结到底该怎么做。苏霍姆林斯基的答案朴素而具体：校长要有一本记事簿，一年又一年地记录，凡是引起自己注意、哪怕只是模糊想法的每个事实都写进去。这本记事簿既是教育日记，也是长期概括分析的准备；积累到一定程度，就会有一个“顿然领悟”的时刻，长期躲闪的真理实质突然显现。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《和青年校长的谈话》第8次谈话“怎样做学年总结”之“总结的实质及做法”

### sk-1019　孩子应该怎样理解自己对他人的义务

- 旧标签：love-education, family-school
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 4.90 + 先验 2.5 = 7.40））
- 其他命中：幸福与精神生活（3.0）
- 转述：这一篇回答的是：孩子应当怎样理解自己对他人的义务。苏霍姆林斯基把“只做自己想做的事、只在有满足感时才行动”看作一种危险的生活态度，它会让心灵无法理解爱与忠诚，愿望变得鄙俗贫乏，生活空虚凄凉。他给出的出路是“奉献”——把奉献称为培养崇高愿望的惟一学校。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》第7篇“孩子应该怎样理解自己对他人的义务”

### sk-1020　帮助教师完善教育技巧

- 旧标签：teacher-growth, child-study
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 11.52 + 先验 1.0 = 12.52））
- 其他命中：教师（7.2） · 了解儿童（7.2）
- 转述：这一节讲校长怎样做教师的个别工作。苏霍姆林斯基把这项任务概括为一句话：帮助每个教师建立“个人的创造性实验室”。对教师做个别工作有两个方面：一是分析他采用的教育方法，二是给他实际帮助；具体内容取决于教师的教育素养、眼界、兴趣和精神需求。他反复强调，要让教师明白：工作效果取决于自己的知识和素养，取决于读什么书、怎样自学。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》第1章“全体教师团结一致是教育教学工作成功的保证”之“帮助教师完善教育技巧”

### sk-1021　共青团会议怎样才有生气

- 旧标签：collective-education, reading-and-books, teacher-growth
- 建议：**A9 集体与同伴**（旧标签先验 + 文本证据（关键词 3.16 + 先验 2.5 = 5.66））
- 其他命中：检查知识与考查（5.6） · 全面发展与个性（5.1） · 自我教育（4.3）
- 转述：这是《给儿子的信》第20封信，回答儿子“怎样才能使共青团小组生活热情洋溢、生动有趣，会上不感到无聊”的提问。苏霍姆林斯基先诊断弊病：会议之所以乏味，是因为它脱离了集体的精神生活，没有真正的争论和辩论；只有当大家产生“聚在一起集体思考、展开争论、互相商量”的需要时，会议才会真正吸引人。
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《给儿子的信》第20封信

### sk-1022　抽象的学生与活生生的人

- 旧标签：love-education, child-study, reading-and-books
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 7.10 + 先验 2.5 = 9.60））
- 其他命中：全面发展与个性（5.1） · 尊严、爱与信任（4.4）
- 转述：这一节从一位“命运奇特”的妇女的故事出发：她在学校时照本宣科地学《大雷雨》，却直到很久以后才真正理解那些本应在读书时就该明白的事理，甚至一度进了修道院。苏霍姆林斯基由此追问：为什么我们信奉的真理、艺术语言的真与美，有时就是进不了年轻人的心扉？他的回答是，很多教师传授知识时没有注入自己的思想和感情，面对的似乎不是课堂里一
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第39篇“关于学校教育的思考”之“(3)抽象的学生与活生生的人”

### sk-1023　什么是从事教师工作的才能，它是怎样形成的

- 旧标签：teacher-growth, child-study, love-education
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88））
- 其他命中：全面发展与个性（4.4） · 幸福与精神生活（3.8）
- 转述：这是《给教师的100条建议》开篇第一条，回答“教师工作的才能是什么、怎样形成”。苏霍姆林斯基先列出教育工作的几个特点：工作对象是活生生的人；教育结果要过五年、十年才见分晓；影响儿童的因素很多，学校的使命是为人而斗争、克服消极影响；工作对象是正在形成中的个性最细腻的精神生活领域；儿童每天都在变化，今天和昨天不一样。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 1“什么是从事教师工作的才能，它是怎样形成的”

### sk-1024　结束语：为未来培养全面发展的人

- 旧标签：teacher-growth, family-school, child-study
- 建议：**A11 劳动与创造**（文本证据推翻旧标签（关键词 10.71，压过旧标签项 10.21））
- 其他命中：全面发展与个性（10.2） · 美与艺术（8.9）
- 转述：这是《全面发展的人的培养问题》全书结论的核心表述。苏霍姆林斯基把教育定义为面向未来的"播种"：学校不仅要传授当下有用的知识，更要预见学生10年、20年、30年后的样子，为未来社会培养公民。他强调知识教育与思想教育、道德教育的统一，认为没有牢固的知识、丰富的智力修养和多方面的智力兴趣，就不可能有真正高的道德尊严。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《全面发展的人的培养问题》结束语

### sk-1025　学生的精神世界（序言）：知识不只为了劳动

- 旧标签：child-study, reading-and-books, teacher-growth
- 建议：**A6 了解儿童**（旧标签先验 + 文本证据（关键词 3.80 + 先验 2.5 = 6.30））
- 其他命中：集体与同伴（5.2） · 全面发展与个性（5.0）
- 转述：序言交代了《学生的精神世界》的研究基础：作者先后研究、跟踪了29个班级、700余名学生从入学到结业的整个学习期间的生活与劳动，目的在于揭示各种因素对学生精神面貌所起的作用。苏霍姆林斯基反对把知识只当作将来劳动谋生的工具，认为人不是"单纯为劳动而生存"；学习还应满足人认识世界、丰富精神生活的需要。如果学生只用"有没有用"
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《学生的精神世界》序言

### sk-1026　谈谈教师的健康和充实的精神生活

- 旧标签：teacher-growth, health-first
- 建议：**A7 健康与作息**（旧标签先验 + 文本证据（关键词 4.14 + 先验 2.5 = 6.64））
- 其他命中：劳动与创造（5.3） · 幸福与精神生活（3.8）
- 转述：一位45岁的女教师在退休晚会上道出真相：她离开不是因为年龄，而是因为学校工作从未给她乐趣，长期的厌倦和压抑"内伤"了她的心脏。苏霍姆林斯基由此提出：健康、情绪、充实的精神生活、创造性劳动的乐趣，都是紧密联系、互相制约的；其中健康与精神力量的和谐居首位。教师工作是用心脏和神经进行的劳动，长期的情绪激动或压抑最消耗神经系统
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 2“谈谈教师的健康和充实的精神生活问题——有关工作乐趣的几句话”

### sk-1027　从哪儿找时间，一昼夜只有24小时

- 旧标签：teacher-growth, reading-and-books
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 11.40 + 先验 2.5 = 13.90））
- 其他命中：教师（2.4）
- 转述："没有时间"被苏霍姆林斯基称为教育工作的灾难，它不仅打击学校工作，也打击教师的家庭生活。他用一位历史教师的话来回答：一堂好课"准备了一辈子"，而针对具体课题的直接准备只用了约15分钟。区别在于，前者靠的是终生的、出自本性的阅读，而不是临时翻教科书。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 6“从哪儿找时间，一昼夜只有24小时”

### sk-1028　知识既是目的又是手段

- 旧标签：thinking-and-nature, child-study
- 建议：**A6 了解儿童**（旧标签先验 + 文本证据（关键词 3.80 + 先验 2.5 = 6.30））
- 其他命中：幸福与精神生活（3.8） · 集体与同伴（3.2）
- 转述：学生学得吃力，往往不是因为知识太少，而是因为知识被"储存"起来，从未进入运用和流通。苏霍姆林斯基重新定义"知道"：知道就是会运用知识。只有当知识成为精神生活的因素、能吸引思想并激起兴趣时，它才真正是知识。因此他主张把获得知识当作手段而非最终目的，让知识在脑力劳动、集体精神生活和学生相互关系中不断"起作用"，在连续的精神
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 11“知识既是目的又是手段”

### sk-1029　学习之母不应变成后娘

- 旧标签：learning-difficulties, assessment-grading
- 建议：**A20 检查知识与考查**（文本证据推翻旧标签（关键词 6.16，压过旧标签项 5.28））
- 其他命中：全面发展与个性（5.1） · 健康与作息（4.3）
- 转述："复习是学习之母"是民间教育学的常识，但在实践中，复习常常变成"狠毒的后娘"：把几周甚至几个月的教材压缩到一天或几天里复习，大量事实和结论压顶而来，学生还要同时应付其他功课，结果脑子乱成一团、精疲力竭，甚至伤了身体。苏霍姆林斯基主张按课程和教材特点组织复习。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 18“学习之母不应变成后娘”

### sk-1030　教师的权威是什么，应该表现在哪里

- 旧标签：teacher-growth, love-education
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 4.62 + 先验 2.5 = 7.12））
- 其他命中：劳动与创造（4.6） · 思维与智力（4.1）
- 转述：苏霍姆林斯基把教师对学生的权威比作一把手术刀：它最要紧、最锐利，也最不安全，既能做细致的手术，也可能刺伤心灵；一切取决于如何使用，以及怀着怎样的内心动机。孩子带着无限信任走进学校，这种信任使他某种程度上处于"无力自卫"的状态。教师若利用这种状态去任意捉弄、控制孩子，就是把儿童当成笼中的小鸟，最终必然丧失权威。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 94“教师的权威是什么，应该表现在哪里”

### sk-1031　健康、健康，还是健康

- 旧标签：health-first, family-school
- 建议：**A7 健康与作息**（旧标签先验 + 文本证据（关键词 9.49 + 先验 2.5 = 11.99））
- 其他命中：家庭与母亲（7.6） · 检查知识与考查（5.1）
- 转述：这是《我把心给了孩子们》"儿童时代"中的著名一节。苏霍姆林斯基反复强调：对健康的关注是教育工作者首要的工作。孩子的精神生活、世界观、智力发展、知识的巩固和对自己力量的信心，都取决于他们是否乐观愉快、朝气蓬勃。他回顾头四年的教学工作，操劳和焦虑多半是为了孩子们的健康；而这种关心离不开与家庭的经常联系。
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《我把心给了孩子们》儿童时代“健康、健康，还是健康”

### sk-1032　第6封信：天赋与教育，人是自己志向的创造者

- 旧标签：teacher-growth, labor-education, child-study
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 5.31 + 先验 2.5 = 7.81））
- 其他命中：自我教育（4.3） · 美与艺术（4.2）
- 转述：儿子在来信中与父亲争论：父亲是否高估了教育和自我教育，低估了天赋。苏霍姆林斯基的回答是：他并不否认天赋，但强调环境与教育的巨大作用——成千上万人的天赋，正因为缺乏有利于发展才能的环境而得不到发展。他相信教育的艺术在于看到每个孩子"取之不尽的精神世界"和尚未被发现的才能，让数学、语法都学得吃力的孩子也能在别的领域成为有才
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《给儿子的信》第6封信

### sk-1033　作者的话：校长要成为“教师的教师”

- 旧标签：teacher-growth
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 7.21 + 先验 2.5 = 9.71））
- 其他命中：学习困难学生（6.2） · 劳动与创造（5.3）
- 转述：这是《和青年校长的谈话》的"作者的话"，交代了全书的来历与主旨：这些谈话最初发表于1965—1966年的《国民教育》杂志，整理成书时增补了关于学校道德教育问题的一章，并对其余各章补充了新材料。全书围绕学校教育和教学过程的领导展开，涵盖教师集体的创造性劳动、课堂教学、教师的教育学修养、怎样指导教学过程、怎样分析课、怎样做
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《和青年校长的谈话》作者的话

### sk-1034　培养学生精神世界的途径和方法：道德教育的艺术在于行动先行

- 旧标签：love-education, labor-education
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 10.77 + 先验 1.0 = 11.77））
- 其他命中：道德判断与品德培养（10.1） · 习惯与纪律（4.8）
- 转述：苏霍姆林斯基认为，学生精神生活的宽广程度制约着道德教育两种基本方法的实施效果——说服教育和培养道德行为习惯。道德教育的艺术不在于先讲道理再要求学生做到，而在于让孩子一进学校门就通过自己的行动提高认识，再从教师的教导中找到与自己在积极活动中产生的思想、感受相共鸣的东西。高尚的思想与高尚的道德情感融为一体并变成高尚行为之时
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《学生的精神世界》第2章“培养学生精神世界的途径和方法”之 (1)“道德教育诸方法的特点及其统一性”、(2)“鼓励学生积极表

### sk-1035　怎样使学生注意力集中：先形成情绪高涨和智力振奋的内心状态

- 旧标签：learning-difficulties, reading-and-books
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 11.20 + 先验 1.0 = 12.20））
- 其他命中：幸福与精神生活（3.3） · 教师（2.4）
- 转述：苏霍姆林斯基认为，掌握学生的注意力是教师工作中最细致、也研究得最不充分的领域之一。要掌握儿童的注意力，唯一的方法是先形成并保持一种内心状态——情绪高涨和智力振奋，而这种状态又与“真理驾驭感”和“智力自豪感”相连。它不能靠一两件直观教具临时制造，而取决于学生的思维修养、情感和见识广度。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 35“怎样使学生注意力集中”

### sk-1036　用草稿本检查家庭作业：让全班都在进行脑力劳动

- 旧标签：assessment-grading, learning-difficulties
- 建议：**A20 检查知识与考查**（文本证据推翻旧标签（关键词 6.85，压过旧标签项 4.31））
- 其他命中：思维与智力（3.3） · 教师（2.4）
- 转述：苏霍姆林斯基把家庭作业检查从“叫一个学生到黑板前回答”改为全班同时动笔：教师把任务写在黑板上，全体学生把任务记在草稿本上，草稿本暂时代替黑板，教师细心查看每个人的学习情况，随时让个别学生说明“在做什么、为了什么、怎么做”。这样不必复述，教师就能大致掌握全班的知识状况；同时每个学生都在独立作业，检查知识本身成了积极运用知
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 16“怎样使家庭作业的检查成为有效的脑力劳动”

### sk-1037　观察是知识的理解和记忆之母：教学生观察、教学生细看

- 旧标签：thinking-and-nature, child-study
- 建议：**A20 检查知识与考查**（文本证据推翻旧标签（关键词 11.25，压过旧标签项 10.38））
- 其他命中：美与艺术（10.4） · 思维与智力（7.5）
- 转述：苏霍姆林斯基指出，有些学校只把观察当作证实教材的手段，而不把它当作积极的智力活动和发展智力的途径。他认为观察是“知识的理解和记忆之母”：知识在观察中活跃起来、进入流通领域，成为可运用的工具。他带学生到冬日果园里找春天的征兆，让最不细心的孩子也能发现两三个，让会听大自然音乐的孩子听出春天苏醒的旋律；此后每周重访，每次都有
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 21“教学生观察，教学生细看”

### sk-1038　怎样培养良心感：以羞耻心为土壤，让内在的“我”说话

- 旧标签：love-education, family-school
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 10.64 + 先验 1.0 = 11.64））
- 其他命中：习惯与纪律（4.8） · 尊严、爱与信任（4.4）
- 转述：苏霍姆林斯基把良心、羞耻、责任、义务视为高尚道德的四个源泉，其中羞耻心是良心得以存在的基础。良心不是记住几条道德规范，而是一种“几倍于体验和感受的认识”：只有当人从幼年起习惯感受到自己处在众人眼前，内在的“我”的声音才会说话。因此，培养良心感的关键是让孩子用别人的思想感情渗透进自己的内心世界——即使周围无人注视，也感到
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》32“怎样培养良心感”

### sk-1039　让学生记住基本知识：把知识的“骨架”在小学阶段牢牢打好

- 旧标签：learning-difficulties, reading-and-books
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 4.14 + 先验 1.0 = 5.14））
- 其他命中：学习困难学生（4.9） · 评价与分数（4.2）
- 转述：苏霍姆林斯基把“基本知识”比作房子的地基：中高年级的落后和成绩不好，主要不是新知识太难，而是低年级时没有把作为知识基础的基本真理牢牢保存在记忆中。他要求小学教师从一年级起就把四年级乃至五年级的语文、数学大纲拿来对照，弄清“为使学生能在四年级和五年级顺利学习，三年级的学生需要知道什么”。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 8“让学生记住基本知识”

### sk-1040　技能和知识之间不可比例失调：没有工具就塞不进知识

- 旧标签：learning-difficulties, thinking-and-nature
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 7.40 + 先验 2.5 = 9.90））
- 其他命中：阅读与书籍（6.8） · 教师（2.4）
- 转述：苏霍姆林斯基用“没有牙齿的人囫囵吞枣”来比喻技能与知识的比例失调：学生还没有掌握作为学习工具的阅读、书写等技能，教师却不断塞给他新知识，结果消化不良。他认为最可悲的比例失调是不会快速而用心地阅读、不会边读边想——这会直接造成智力上的含糊不清，学生说话像一串互不联系的单词，不能把概念用语言表达出来。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 24“技能和知识之间不可比例失调”

### sk-1041　培养学生的智能：观察力是发达智力的首要特点

- 旧标签：thinking-and-nature, child-study
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 11.18 + 先验 2.5 = 13.68））
- 其他命中：阅读与书籍（7.4） · 习惯与纪律（5.0）
- 转述：苏霍姆林斯基认为，智能是在掌握知识的过程中发展的，但“知识”本身包含两个相互区别的成分：一是必须永远保留在记忆中、不断用来解释新事实的“思维工具”（事实、定理、公式、规则、定义等）；二是无须保存在记忆中、只需要会理解和利用的知识，即善于在书籍这一知识贮存库中确定方向的能力。科学飞速发展而人的记忆有限，因此不能要求学生记
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》第5章“智育”之“培养学生的智能”

### sk-1043　关于听课和分析课的几点建议：教师应当怎样布置家庭作业

- 旧标签：teacher-growth, learning-difficulties
- 建议：**A12 自然与思维课**（文本证据推翻旧标签（关键词 11.96，压过旧标签项 9.71））
- 其他命中：教师（7.2） · 全面发展与个性（5.2）
- 转述：苏霍姆林斯基把布置家庭作业看作校长听课和分析课时必须关注的问题，而不是教师的私事。他要求校长努力做到不让教师把课外作业当成课内作业的量的追加；课外作业应当能使学生的知识向广度和深度发展，能提高他们的学习能力，是他们掌握课堂知识的准备。应当让学生在课外去观察自然界和社会现象，发展个人的爱好和多方面的智力需求。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《和青年校长的谈话》第7次谈话“关于听课和分析课的几点建议”之“教师应当怎样布置家庭作业”

### sk-1044　学校集体中不同年龄的学生之间的多种关系

- 旧标签：collective-education
- 建议：**A9 集体与同伴**（旧标签先验 + 文本证据（关键词 12.24 + 先验 2.5 = 14.74））
- 其他命中：思维与智力（13.2） · 阅读与书籍（7.1）
- 转述：苏霍姆林斯基把学校集体看作由几十个基层集体组成的整体，认为它的精神生活是否丰富，很大程度上取决于班集体之间、高低年级之间的关系是否多样。他把这些关系归纳为智力关系、思想教育关系、教学劳动关系、课余创作和游戏关系四类，其中智力关系最牢固持久：高年级学生指导低年级的学科小组、读书小组，把自己的知识、技能和信仰传给小同学。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《培养集体的方法》第1章“学校集体及其培养的原则”之 (3)“学校集体中不同年龄的学生之间的多种关系”

### sk-1045　学龄初期儿童的思想、兴趣和志向

- 旧标签：child-study
- 建议：**A6 了解儿童**（旧标签先验 + 文本证据（关键词 3.80 + 先验 2.5 = 6.30））
- 其他命中：幸福与精神生活（3.3） · 集体与同伴（3.2）
- 转述：学龄初期儿童的兴趣和志向很不稳定，容易被当时集体活动、故事、电影和身边榜样牵动；这不是缺点，而是这一年龄的特点。他们对“想做什么样的人”的回答往往不是抽象品质，而是一个具体的人的形象——列宁、卓娅、劳动模范。苏霍姆林斯基据此提出一条教育规律：应努力让生产战线的先进人物成为孩子们的亲密朋友并参加教育工作，本校低年级每个班
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《学生的精神世界》第4章“从幼年时期到少年时期”之 (2)“学龄初期儿童的思想、兴趣和志向”

### sk-1046　为了不造成负担过重，必须有自由活动时间

- 旧标签：health-first, learning-difficulties
- 建议：**A7 健康与作息**（旧标签先验 + 文本证据（关键词 9.43 + 先验 2.5 = 11.93））
- 其他命中：习惯与纪律（10.8） · 阅读与书籍（6.8）
- 转述：苏霍姆林斯基指出，把学生全部时间填满课业，反而会造成负担过重和落后；自由活动时间不是浪费，而是智力生活丰富、学习富有成效的前提。这种时间首先产生于高质量的课堂教学——教师讲得清楚、学生知识处于积极活跃状态；其次取决于作息制度。他反对学生课后继续三四个甚至六个钟头紧张脑力劳动，主张把下半天变成自由活动时间，用来阅读课外书
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 31“为了不造成负担过重，必须有自由活动时间”

### sk-1047　培养儿童热爱绘画

- 旧标签：aesthetic-nature-education
- 建议：**A14 美与艺术**（旧标签先验 + 文本证据（关键词 18.44 + 先验 2.5 = 20.94））
- 其他命中：思维与智力（12.4） · 自然与思维课（4.2）
- 转述：苏霍姆林斯基把绘画看作发展创造性思维、想象力和审美能力的手段，而不只是美术课的内容。他带儿童写生树木、花朵、河流、昆虫，也画池塘边的朝霞晚霞、草地上的篝火、飞向温暖地方的鸟群，让认识世界的过程充满鲜明的美感。同样的田野，有的孩子画整片庄稼地、云彩和云雀，有的只画一朵三叶草和落在花瓣上的蜜蜂，图画恰好反映了各自认识、思维
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 43“培养儿童热爱绘画”

### sk-1048　怎样培养母亲和父亲做好学校和家庭的协同教育工作

- 旧标签：family-school
- 建议：**A8 家庭与母亲**（旧标签先验 + 文本证据（关键词 7.64 + 先验 2.5 = 10.14））
- 其他命中：教师（7.2）
- 转述：苏霍姆林斯基把“家长教育学”放在整个教育理论和实践的基础位置：不关心家长的教育修养，任何教育和教学任务都不可能完成。学校因此设立分年龄段的家长教育学校——学前部、一至三年级、四至八年级、九至十一年级，父母在孩子入学前三年就开始学习，每两周听一次课，由校长、副校长和将来要带一年级的教师讲课。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 52“怎样培养母亲和父亲做好学校和家庭的协同教育工作”

### sk-1049　怎样和懒惰作斗争

- 旧标签：learning-difficulties, family-school
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 4.98 + 先验 1.0 = 5.98））
- 其他命中：幸福与精神生活（3.0） · 劳动与创造（2.3）
- 转述：苏霍姆林斯基把懒惰视为一种严重的精神现象，根源是无忧无虑、有求必应的童年和无所用心：孩子从不知道什么叫困难，就会把童年当成永远继续下去的日子。懒惰既表现为手脚懒，也表现为思想懒——生吞活剥地接受别人现成的思想，和坐享别人劳动成果一样危险。因此预防懒惰比治好懒惰更宝贵。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 99“怎样和懒惰作斗争”

### sk-1050　第11封信：培养自己的情感境界

- 旧标签：love-education
- 建议：**A15 思维与智力**（文本证据推翻旧标签（关键词 7.51，压过旧标签项 4.60））
- 其他命中：劳动与创造（4.6） · 了解儿童（3.4）
- 转述：苏霍姆林斯基在给儿子的信中把“情感的自我培养”当作青年最重要的功课之一。他观察到，人际冲突常常不是因为道理讲不清，而是因为人不会控制感情；当一个人无法用思想证明自己正确时，就容易用喊叫、暴躁、凶狠这些“本能的反抗”来填补思想的贫乏。真正的人的感情不能离开思想而存在：感情来自思想，思想滋润感情，丰富的思想使人成为精神世界
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《给儿子的信》第11封信

### sk-1051　学校集体的精神生活：“思想之室”

- 旧标签：reading-and-books, teacher-growth
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 15.63 + 先验 2.5 = 18.13））
- 其他命中：幸福与精神生活（13.9） · 思维与智力（7.5）
- 转述：苏霍姆林斯基发现，许多青少年不会真正阅读，只会读教科书。于是他把学校阅览室命名为“思想之室”：设在校园僻静角落，保持安静，第一次开放时他亲自介绍罗蒙诺索夫的书，并把自己记了二十多年的读书笔记拿给学生看，让学生感受与书籍精神交往的幸福。室内设杰出人物传记专柜，集中布鲁诺、乌里扬诺夫、伏契克等为真理和人民献身者的传记，还设
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《和青年校长的谈话》第3次谈话“学校集体的精神生活”之“‘思想之室’”

### sk-1052　他们为什么变成了难教儿童

- 旧标签：learning-difficulties, child-study
- 建议：**A10 教师**（文本证据推翻旧标签（关键词 7.21，压过旧标签项 5.67））
- 其他命中：学习困难学生（11.8） · 自然与思维课（5.7）
- 转述：苏霍姆林斯基认为，学校出现难教儿童不能完全归咎于教师和校长，但教师的过错在于没有努力考察孩子变成难教儿童的原因。教师应像医生查病源一样，细致研究儿童智力、情感和道德的发展，从每个孩子的困难和特点出发采取措施，并尽可能预防致难的原因。他用医生作比：真正有人道主义精神的医生不会对病人说“你没有希望了”，教师更不能天天让儿童
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《和青年校长的谈话》第4次谈话“难教儿童”之“他们为什么变成了难教儿童”

### sk-1053　学生应当掌握的最重要的技能和技巧

- 旧标签：teacher-growth, learning-difficulties
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 11.40 + 先验 1.0 = 12.40））
- 其他命中：思维与智力（6.7） · 检查知识与考查（5.6）
- 转述：苏霍姆林斯基把“最重要的技能和技巧”看作教养、智力和信念赖以产生的基础，并逐一规定学生在第几学年、第几学季应当达到什么水平。他列出的清单包括十二项：观察、思考（类比、比较、对比、提问）、表达、流利阅读并理解、流畅迅速正确地书写、划分阅读材料的相对独立部分并找出联系、找到相关书籍、在书中找到所需材料、对阅读材料作初步逻辑
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《和青年校长的谈话》第6次谈话“谈谈怎样指导学生的脑力劳动”之“学生应当掌握的最重要的技能和技巧”

### sk-1054　要赢得学生的思想和心灵

- 旧标签：teacher-growth, child-study
- 建议：**A16 评价与分数**（文本证据推翻旧标签（关键词 9.99，压过旧标签项 6.41））
- 其他命中：幸福与精神生活（6.4） · 美与艺术（5.9）
- 转述：苏霍姆林斯基把“赢得学生的思想和心灵”看成教师创造性劳动的一个方面：一位有才华的教师到校两年，就能让一门学科成为学生喜爱的课程，并带出一批有才能的少年。这种“竞赛”不是抢生源，而是每个教师都力求让自己的课程对学生产生真正的吸引力，从而让学校的智力生活朝气蓬勃。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 26“要赢得学生的思想和心灵”

### sk-1055　怎样通过阅读发展知识

- 旧标签：reading-and-books, learning-difficulties
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 11.40 + 先验 2.5 = 13.90））
- 其他命中：了解儿童（7.2） · 思维与智力（3.4）
- 转述：苏霍姆林斯基把“阅读科普和科学读物”看作学龄中晚期与学龄早期“观察”同等重要的智力活动：不越出教科书范围，就不可能有对知识的持久兴趣。他给出的操作办法是“留白”——教师在讲新教材时，用大纲以外知识的火花来照亮某些问题，把知识世界之窗微微打开一点，故意留些东西不完全讲透，让学生带着问题去读科学读物。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 22“怎样通过阅读发展知识”

### sk-1056　作为教育者的父母怎样做到行动统一

- 旧标签：family-school, love-education
- 建议：**A8 家庭与母亲**（旧标签先验 + 文本证据（关键词 7.64 + 先验 2.5 = 10.14））
- 其他命中：评价与分数（4.8） · 自我教育（4.4）
- 转述：苏霍姆林斯基把家校协同的落点放在“父母行动统一”上：首先是父母对“可以、不可以、应当”的看法一致，其次才是与学校要求一致。他点名批评三种不理智的爱——溺爱、暴君式的爱、只管花钱的爱。溺爱使孩子以为一切都理所当然，遇一点困难就觉得承受不起；暴君式的爱把孩子当物品，用物质奖励和威胁来控制；只管花钱的爱则用物质代替精神陪伴，
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 54“作为教育者的父母怎样做到行动统一”

### sk-1057　什么叫痛苦，怎样教孩子们去克服它

- 旧标签：love-education, child-study
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 15.18 + 先验 1.0 = 16.18））
- 其他命中：尊严、爱与信任（4.9） · 健康与作息（4.8）
- 转述：苏霍姆林斯基先给“痛苦”分类：最可怕的是战争与死亡，其次还有丧失民族气节、父母子女彼此抛弃；而在个人层面，最大的不幸是丧失勇敢，其次是孤独，最可怕的是精神空虚。他由此提出教育者的任务——不是回避痛苦，而是让孩子学会分辨：哪一种痛苦能使人高尚、得到锻炼，值得昂起头去承受；哪一种痛苦只会使人失去尊严、蒙受耻辱，必须坚决抵制
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》11“什么叫痛苦，怎样教孩子们去克服它”

### sk-1058　蓝天下的学校

- 旧标签：thinking-and-nature, aesthetic-nature-education
- 建议：**A19 道德判断与品德培养**（文本证据推翻旧标签（关键词 12.25，压过旧标签项 7.24））
- 其他命中：美与艺术（4.7） · 自然与思维课（4.1）
- 转述：“蓝天下的学校”是苏霍姆林斯基为六岁儿童开办的学前预备学校：开学第一天不在教室，而在葡萄园、绿草地、大梨树下。他先让孩子光脚走路、感受阳光和土地，再围坐欣赏果园，用“太阳在洒火花”的童言引出巨人铁匠的童话，边讲边画。孩子分到葡萄，每人留一串带回家给妈妈——审美、幻想与善行从第一天就交织在一起。
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《我把心给了孩子们》“快乐学校”之“蓝天下的学校”

### sk-1059　学习——精神生活的一部分

- 旧标签：learning-difficulties, child-study
- 建议：**A6 了解儿童**（旧标签先验 + 文本证据（关键词 3.80 + 先验 2.5 = 6.30））
- 其他命中：习惯与纪律（4.8） · 美与艺术（4.5） · 自然与思维课（4.1）
- 转述：苏霍姆林斯基提出一个双向要求：一方面，不要把儿童入学前那个由大自然、游戏、美、音乐、幻想和创作构成的世界关在教室门外，否则孩子不会爱上学校；另一方面，也不能为了不让孩子枯燥就刻意减轻学习。真正要培养的，是习惯于“严肃认真、坚毅顽强和埋头苦干的劳动”，而且这种劳动必须紧张地思索。
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《我把心给了孩子们》“儿童时代”之“学习——精神生活的一部分”

### sk-1060　美的认识与情操的培养

- 旧标签：aesthetic-nature-education
- 建议：**A14 美与艺术**（旧标签先验 + 文本证据（关键词 8.95 + 先验 2.5 = 11.45））
- 其他命中：幸福与精神生活（6.3） · 尊严、爱与信任（4.2）
- 转述：苏霍姆林斯基把“感知和领会美”定为审美教育的基础和核心：如果孩子对美无动于衷，任何美的事物都打动不了他。因此美育不是讲抽象的美学道理，而是从学校教育最初的日子起，教孩子去理解大自然、艺术和社会关系中的美，并从中看到精神的高尚、善良与真挚，以此确立自身的美。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》第7章“美育”之“美的认识与情操的培养”

### sk-1061　关于自我教育

- 旧标签：collective-education, teacher-growth
- 建议：**A4 自我教育**（旧标签先验 + 文本证据（关键词 8.77 + 先验 1.0 = 9.77））
- 其他命中：道德判断与品德培养（9.1） · 尊严、爱与信任（4.8）
- 转述：苏霍姆林斯基这里的“自我教育”不是个人闭门修身，而是集体内部学生之间品德与精神财富的相互影响。它的起点是“一个人的独特性引起别人产生仿效的愿望”：集体里总有人在某方面有突出的天赋、才能和志趣，教育技巧就在于让这些鲜明个性通过坚定的意志、高尚的自尊感和正当的自爱心表现出来，成为集体的骨干和榜样。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《和青年校长的谈话》第2次谈话“教育现象之间的相互依存性”之“关于自我教育”

### sk-1062　知觉在学龄初期儿童精神发展中的作用

- 旧标签：child-study, thinking-and-nature
- 建议：**A3 幸福与精神生活**（文本证据推翻旧标签（关键词 10.77，压过旧标签项 2.50））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：苏霍姆林斯基把知觉看作学龄初期儿童精神发展的“主要渠道”：外部世界通过看、听、摸进入孩子的头脑，并直接带上情感色彩。孩子年龄越小，他知觉到的一切就越容易被感染、越容易引发情感反应。他引用马克思的话说明，感性禀赋是孩子与世界连接的第一条纽带。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《学生的精神世界》第4章“从幼年时期到少年时期”之 (1)“知觉在学龄初期儿童精神发展中的作用”

### sk-1063　集体中的交往

- 旧标签：collective-education, love-education
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 14.07 + 先验 1.0 = 15.07））
- 其他命中：自我教育（10.3） · 思维与智力（4.1）
- 转述：苏霍姆林斯基把“人与人交往的美”看作培养集体的核心：一个人会成为怎样的人，取决于他在交往中的表现、交往激起他什么样的思想、把他的志趣引向何方。如果集体生活里缺少美、深厚的情感、丰富的精神生活和充实的思想，就不可能有真正的自我认识和自我教育。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《培养集体的方法》第3章“集体对个人教育影响的形成”之 (2)“集体中的交往”

### sk-1064　何种见解能够培养出成熟的思想

- 旧标签：thinking-and-nature, teacher-growth, reading-and-books
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 6.67 + 先验 2.5 = 9.17））
- 其他命中：劳动与创造（5.3） · 道德判断与品德培养（3.0）
- 转述：苏霍姆林斯基把“思想成熟”当作一项需要从童年就开始培育的道德与智力任务：孩子必须逐渐意识到自己不会永远是孩子，有一天要作为创造者、思想者、劳动者在大地上留下痕迹。但这种意识不能靠说教灌输，只能靠教师“委婉地、细致地、非强加地”提示——哪怕一个小小的提示，也能唤起儿童意识中丰富的思想；喋喋不休的说教反而无效。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》4“何种见解能够培养出成熟的思想”

### sk-1065　在哪些行为之中应表现出义务感

- 旧标签：love-education, collective-education, labor-education
- 建议：**A2 公民与祖国**（旧标签先验 + 文本证据（关键词 9.72 + 先验 1.0 = 10.72））
- 其他命中：幸福与精神生活（7.2） · 劳动与创造（7.0）
- 转述：苏霍姆林斯基把义务感放在“权利与义务的和谐”中来讲：社会给予每个人劳动、精神生活、幸福、爱情、建立家庭的权利，但这些权利若没有公民、劳动者、子女、父母的义务与责任作支撑，就不可思议；只想不尽义务而享受幸福的人，最终会成为令人遗憾的人。一个人精神高尚的根本，是把“应当付出个人幸福”变成一种信念。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》8“在哪些行为之中应表现出义务感”

### sk-1066　怎样培养服从和领导的能力，怎样用高度严格要求的精神进行教育

- 旧标签：collective-education, teacher-growth, love-education
- 建议：**A9 集体与同伴**（旧标签先验 + 文本证据（关键词 6.84 + 先验 2.5 = 9.34））
- 其他命中：自我教育（4.4） · 道德判断与品德培养（3.0）
- 转述：苏霍姆林斯基把“服从”与“领导”看作同一件事的两面，而且都从活动中生长出来：不是先选出干部、再要求大家服从，而是谁在共同活动里真正表现出是行家里手，谁才会被选为领导者；儿童乐意服从这样的人，因为这种服从等于“愿意今天比昨天更好”。离开了由统一目的鼓舞的、有社会意义的积极活动，服从和领导都无从谈起。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 65“怎样培养服从和领导的能力，怎样用高度严格要求的精神进行教育”

### sk-1067　怎样激起求知欲

- 旧标签：learning-difficulties, teacher-growth, child-study
- 建议：**A15 思维与智力**（人工裁定（标题问「怎样激起求知欲」，正文讲的是**学习动机**（让孩子想到自己的成年）；原文摘录里没有「求知欲」三个字，只有标题有，算法看不见（外部评审意见）））
- 其他命中：家庭与母亲（9.4） · 道德判断与品德培养（3.0）
- 转述：苏霍姆林斯基回答“怎样激起求知欲”，没有从趣味游戏入手，而是从“让孩子想到自己的成年”入手。他指出：父母和老师总把孩子当成需要照顾的小孩子，是学校教育和家庭教育的一种不幸；正是忘记了“今天是孩子、明天就会成为大人”这一点，才带来许多令人不愉快的意外。真正的求知动力来自孩子意识到自己正在长大——他将成为什么样的人，取决于
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》26“怎样激起求知欲”

### sk-1068　谁在教育儿童，什么在教育儿童，什么取决于教师，什么取决其他教育者

- 旧标签：family-school, teacher-growth, love-education
- 建议：**A8 家庭与母亲**（旧标签先验 + 文本证据（关键词 13.57 + 先验 2.5 = 16.07））
- 其他命中：幸福与精神生活（3.8） · 教师（2.4）
- 转述：这一篇回答的是“谁在教育儿童、什么在教育儿童”这一根本问题：教育儿童的不只是教师，还有家庭中一切关系与氛围；因此学校和家庭必须先形成统一的教育看法，进而统一对孩子的合理要求——而统一要求的起点，是父母对自己要求的统一。苏霍姆林斯基强调要教给家长“明智的母爱和父爱”，让善与严、柔与刚达到和谐，并且分寸要拿捏得极细，因为家
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 51“谁在教育儿童，什么在教育儿童，在教育方面什么取决于教师，什么取决其他教育者”

### sk-1069　精神素养、道德和无神论

- 旧标签：love-education, reading-and-books, teacher-growth
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 3.31 + 先验 1.0 = 4.31））
- 其他命中：思维与智力（3.3） · 集体与同伴（3.2）
- 转述：苏霍姆林斯基提出一个尖锐的规律：一个人对周围世界了解得愈多，他就应当愈了解人；若忽视这一点，知识与道德之间的协调就会被破坏，他把这种状态称为“道德上的无知”。其表现是：掌握大量关于周围世界的知识，却在历史、社会政治、精神心理和美学方面都不了解人的本质；不去思考是什么使人高于其他生物，情感范畴就无法发展，感情就会变得粗俗
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《公民的诞生》“道德的形成——公民的诞生”之“精神素养、道德和无神论”

### sk-1070　我们是怎样指导课上的智能劳动的

- 旧标签：teacher-growth, learning-difficulties, thinking-and-nature
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 11.20 + 先验 2.5 = 13.70））
- 其他命中：检查知识与考查（5.1） · 了解儿童（3.8）
- 转述：苏霍姆林斯基记录了帕夫雷什中学教师围绕“课上智能劳动”展开的争论：如何引起重视和兴趣、如何应用知识、少年期智能劳动有哪些特点、如何巩固知识；还涉及智能劳动的共同性与个人才能的发展、课堂教学与少年广泛智力生活的联系、理智与动手能力的协调。他提出一个核心判断——少年的劳动素养是教师素养的一面镜子，不能离开教师本人的知识面和
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《公民的诞生》“少年的智育和教学”之“我们是怎样指导课上的智能劳动的”

### sk-1071　思想认识

- 旧标签：love-education, teacher-growth, thinking-and-nature
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88））
- 其他命中：道德判断与品德培养（3.0） · 幸福与精神生活（3.0）
- 转述：苏霍姆林斯基区分了两种“懂”：一种是把真理变成要记牢、背熟、解答、回答并“和盘托出”的知识，内心却对理智所考虑的东西漠不关心；另一种是用理智和心灵一起认识，确立个人对道德真理和原则的态度。他举了一位热衷表格图表的历史教师为例：教师讲述1812年卫国战争中人民的伟大功勋，孩子们凝神屏息地听着，可教师忽然用寥寥数语结束故事
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《公民的诞生》“情感教育与美感教育”之“思想认识”

### sk-1072　敏感性和同情心的培养

- 旧标签：love-education, family-school, health-first
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 10.95 + 先验 1.0 = 11.95））
- 其他命中：思维与智力（8.0） · 公民与祖国（5.7）
- 转述：苏霍姆林斯基把“敏感性和同情心”列为道德教育中起巨大作用的敏锐精细的道德情操，与义务感并列。他认为人道主义教育的入门，是让孩子在精神上给别人以温暖时自己也感受快乐；这一领域需要细心琢磨，核心是让孩子学会感受别人的痛苦、忧伤和不幸，与需要同情帮助的人共忧患。他特别强调年幼时期最为有利，因为小孩子对别人的痛苦反应特别敏锐，
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》第4章“德育”之“敏感性和同情心的培养”

### sk-1073　劳动对人的全面发展的作用

- 旧标签：labor-education, thinking-and-nature, love-education
- 建议：**A1 全面发展与个性**（文本证据推翻旧标签（关键词 21.22，压过旧标签项 9.99））
- 其他命中：思维与智力（7.5） · 劳动与创造（5.3）
- 转述：苏霍姆林斯基先泼了一盆冷水：劳动固然具有强大的教育作用，但少年手上在干活，并不等于劳动的教育力量已经显现。如果脱离了思想教育、智育、德育、美育、情感教育和体育，脱离了创造、兴趣和需求，脱离了学生之间多方面的联系，劳动就只是负担，学生只想推掉它，好去做更有趣的事。他对“怠惰”的解释也很独到：怠惰蔓延不是因为人们什么都不做
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《公民的诞生》“劳动对少年精神生活的作用”之“劳动对人的全面发展的作用”

### sk-1074　道德情感在学龄初期儿童精神发展中的作用

- 旧标签：love-education, child-study
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 10.77 + 先验 1.0 = 11.77））
- 其他命中：道德判断与品德培养（10.1） · 集体与同伴（9.1）
- 转述：苏霍姆林斯基把学龄初期（7—11岁）道德情感的发育看作一个由集体感受走向思想一致的渐进过程。这个年龄的孩子还不能真正理解自己的生活对集体的依赖，集体对他们的作用往往通过共同的感受、鲜明的形象和具体的行为发生；也正因如此，“通过集体给个性以影响”的原则对低年级学生尤其重要。孩子的情感世界起初被简单地划分为好与坏、正义与非
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《学生的精神世界》第4章“从幼年时期到少年时期”之 (4)“道德情感在学龄初期儿童精神发展中的作用”

### sk-1075　集体对少年精神世界形成的影响

- 旧标签：collective-education, child-study
- 建议：**A9 集体与同伴**（旧标签先验 + 文本证据（关键词 14.28 + 先验 2.5 = 16.78））
- 其他命中：全面发展与个性（8.8） · 学习困难学生（6.2）
- 转述：少年集体常被认为是最难教育的集体，苏霍姆林斯基认为表面的解释（少年活泼好动、兴趣不稳定）不足以说明问题，根本原因在于个人与集体的相互关系发生了质的变化：少年对集体的向往从寻求日常精神交流，升级为寻求思想、观点、信仰、道德行为上的一致。14—15岁的少年在班级里看重的，不只是共同兴趣和有趣活动，而是在最关心的问题上观点一
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《学生的精神世界》第5章“少年时期”之 (8)“集体对少年精神世界形成的影响”

### sk-1076　什么是个性的尊严以及怎样培养它

- 旧标签：love-education, child-study
- 建议：**A4 自我教育**（文本证据推翻旧标签（关键词 9.97，压过旧标签项 7.40））
- 其他命中：健康与作息（5.9） · 尊严、爱与信任（4.9）
- 转述：苏霍姆林斯基把“人的个性尊严”称为一种细微而娇嫩、坚强而勇敢、摸不着而又不屈不挠的概念。他认为人应当有尊严地活着、劳动、享受物质与精神财富，有尊严地感受欢乐与痛苦、对待疾病和生命的最后时刻；即便在最艰难的情况下，也不能越过理智控制行为的那条界线。尊严在他看来是“控制自己感情的一种智慧权”，高尚的个性表现为善于明智而细致
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》45“什么是个性的尊严以及怎样培养它”

### sk-1077　怎样使教育者的话进入受教育者的内心

- 旧标签：family-school, love-education
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 6.29 + 先验 1.0 = 7.29））
- 其他命中：全面发展与个性（4.4） · 尊严、爱与信任（4.3）
- 转述：苏霍姆林斯基把“教育者的话能否进入孩子内心”直接归因于家庭情感教育。如果儿童在家里没有受到情感教育，他就不可能用心灵认识世界、接受教师的话；他所能了解的只是听到和读到的内容的逻辑意义，而情感上、心灵上的潜台词他是不会明白的。学校生活开始没几天，孩子对教师的好话毫无反应，教师不得不大声吆喝、敲桌子，甚至一个月后就罚站，问
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 53“怎样使教育者的话进入受教育者的内心”

### sk-1078　怎样通过集体使个性全面发展

- 旧标签：collective-education, teacher-growth
- 建议：**A11 劳动与创造**（文本证据推翻旧标签（关键词 10.71，压过旧标签项 9.40））
- 其他命中：全面发展与个性（9.4） · 美与艺术（9.2）
- 转述：苏霍姆林斯基指出，人是一个不可分割的整体（道德的、智力的、情感的、审美的、创造的），仅靠基层班集体这一种组织形式，无法揭示、表现和发展这个整体，因为班集体在成员相互关系上具有局限性。一个学生爱数学，另一个爱生物，第三个爱文学，第四个爱技术创作，还有音乐、图画、木刻等爱好；随着接近成年，这些志趣所要求从事的活动差异越来越
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 64“怎样通过集体使个性全面发展”

### sk-1079　手和理智

- 旧标签：labor-education, thinking-and-nature
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 7.04 + 先验 2.5 = 9.54））
- 其他命中：自我教育（7.5） · 劳动与创造（5.3）
- 转述：苏霍姆林斯基借恩格斯对人的手的赞颂，批评把学生参加劳动仅仅解释为“克服学校偏重智育倾向”的流行看法。他认为“手不参加工作似乎会产生智力过多的危险”是荒谬的；真正有害的是两件事：一个人闲着不动，以及不动脑筋地拼命干单调、疲乏、不需要任何技能的体力活。他用十年观察140名8—16岁学生发现，长期从事这类体力活、脑力劳动面窄
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《公民的诞生》“少年的智育和教学”之“手和理智”

### sk-1080　第一年——考察孩子

- 旧标签：child-study, family-school
- 建议：**A6 了解儿童**（旧标签先验 + 文本证据（关键词 10.50 + 先验 2.5 = 13.00））
- 其他命中：思维与智力（10.4） · 健康与作息（4.1）
- 转述：苏霍姆林斯基主张在正式上课之前留出一年时间，把6岁孩子提前招进“快乐学校”。他这样做的目的不是提前教功课，而是好好了解每个孩子，深入考察每个人的知觉、思维和智力劳动的个人特点；在传授知识之前，先要教会孩子思考、感知和观察，并清楚地了解每个学生健康上的个人特点，否则无法正常进行教学。他特别区分智力教育与获取知识：没有教学
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《我把心给了孩子们》“快乐学校”之“第一年——考察孩子”

### sk-1081　自我服务

- 旧标签：labor-education
- 建议：**A17 习惯与纪律**（旧标签先验 + 文本证据（关键词 9.82 + 先验 1.0 = 10.82））
- 其他命中：公民与祖国（5.7） · 美与艺术（4.7）
- 转述：苏霍姆林斯基把自我服务看作劳动教育的起点。它是最简单的一种日常劳动，劳动教育一般都从自我服务开始，而且日后不管每个人从事何种生产劳动，自我服务都将成为他的义务和习惯。它也是培养人遵守纪律、培养人对别人的义务感的重要手段：从小自己动手满足一些个人需要，能使人养成尊敬父母、兄弟姐妹和同学的习惯，并使劳动成为人人都负担的平等
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》第6章“劳动教育”之“自我服务”

### sk-1082　是数学的世纪，还是人的世纪

- 旧标签：thinking-and-nature, teacher-growth
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 4.16 + 先验 2.5 = 6.66））
- 其他命中：幸福与精神生活（6.3） · 劳动与创造（5.4）
- 转述：面对“我们生活在数学、物理学和电子学的时代，应当把全部注意力放在这些学科上”的论调，苏霍姆林斯基提出警告：在确定教学、教育内容时过高估计技术成就和自然科学知识的作用，是很危险的；有人甚至建议把文学改为选修课。他并不否认自然科学的重要性，但认为“数学的世纪”这一巧妙用语并没有反映当今世界的全部实质——世界正进入一个“人的
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《和青年校长的谈话》第5次谈话“关于道德教育的几个问题”之“是数学的世纪，还是人的世纪”

### sk-1083　是否注意教会儿童学习

- 旧标签：reading-and-books, learning-difficulties, teacher-growth
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 17.24 + 先验 2.5 = 19.74））
- 其他命中：学习困难学生（11.4） · 思维与智力（11.2）
- 转述：苏霍姆林斯基认为，为教会儿童学习而采取的方法和方式，应当引起校长的特别重视。儿童在课堂上的智力发展表现在两个方面：一是获得关于自然界、社会和人们精神生活的知识，二是在教师指导下独立掌握这些知识的能力；学习成绩、知识面以及对书籍和科学的热爱，都取决于这两方面的统一与和谐。在小学阶段，掌握知识的能力尤其重要，校长要经常关注
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《和青年校长的谈话》第7次谈话“关于听课和分析课的几点建议”之“是否注意教会儿童学习”

### sk-1089　百灵鸟之歌

- 旧标签：aesthetic-nature-education, thinking-and-nature, love-education
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 4.68 + 先验 2.5 = 7.18））
- 其他命中：劳动与创造（4.8） · 公民与祖国（4.0）
- 转述：这是苏霍姆林斯基写在《公民的诞生》“言语和人的情感素养”一节里的诗，写黎明的雨、麦穗上的水珠、西徐亚人古墓边的寂静，最后落到百灵鸟从太阳那边升起的歌声——他把鸟鸣想象成有人把金色的谷种撒向蔚蓝的苍穹。
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《公民的诞生》之“言语和人的情感素养”《百灵鸟之歌》

### sk-1090　秋

- 旧标签：aesthetic-nature-education, thinking-and-nature, teacher-growth
- 建议：**A12 自然与思维课**（旧标签先验 + 文本证据（关键词 9.35 + 先验 1.0 = 10.35））
- 其他命中：了解儿童（3.4）
- 转述：《秋》是苏霍姆林斯基在《帕夫雷什中学》里自述的习作：他每逢春天清静的早晨到河边、森林和果园去细心观察，并把观察写成短文，用一个专门的习作本写一丛玫瑰、一只云雀、火红的天空、美丽的彩虹。这一篇从清晨的初霜写到傍晚的归巢乌鸦与夜色漫溢，是“到生动思想的源头去旅游”的成品。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》之“帮助教师完善教育技巧”《秋》

### sk-1091　日出

- 旧标签：aesthetic-nature-education, thinking-and-nature, teacher-growth
- 建议：**A14 美与艺术**（旧标签先验 + 文本证据（关键词 4.45 + 先验 2.5 = 6.95））
- 其他命中：自然与思维课（4.2）
- 转述：《日出》与《秋》是苏霍姆林斯基在《帕夫雷什中学》同一处并列援引的两篇习作。他写自己站在苜蓿草地旁看朝霞变色：天蓝、浅紫、粉红、橙黄、深红、金黄在颤动中依次变换；云雀从草地蹿起，在阳光里由灰色变成金黄；露珠闪光、蜜蜂嗡鸣，整片田野像在歌唱。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》之“帮助教师完善教育技巧”《日出》

### sk-1092　黄昏

- 旧标签：aesthetic-nature-education, thinking-and-nature, child-study
- 建议：**A12 自然与思维课**（旧标签先验 + 文本证据（关键词 4.16 + 先验 1.0 = 5.16））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：《黄昏》是《帕夫雷什中学》手抄杂志《我们的创作》上抄录的三年级学生习作，全文只有六句，把暮色拟人化成“拄拐杖的白发小老头”，悄悄走、向农舍探望、敲敲窗户——最后一句“孩子们正躺下睡觉”让整篇拟人落了地。同组还有四年级莉达的《夜》，用洋娃娃、小熊、小锡兵都睡了的细节写静，再以风中的路灯和雪面影子收尾。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》之“智育与教学法问题”《黄昏》（三年级，瓦利娅·马尔钦科）

### sk-1093　当太阳没入乌云的时候

- 旧标签：aesthetic-nature-education, thinking-and-nature, love-education
- 建议：**A12 自然与思维课**（旧标签先验 + 文本证据（关键词 4.16 + 先验 1.0 = 5.16））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：这是一年级学生麦娅·波斯托洛娃的习作，收在《帕夫雷什中学》抄录的手抄杂志作文里。她先写阳光下的金色田野、穗儿“在游戏”、花儿“朝蓝天微笑”，再写乌云遮住太阳后穗儿愁闷、花儿惊慌、草儿低头，最后一句把自己的盼望与穗儿、花儿的盼望合成一个：“我这样希望着，穗儿、花儿、草儿也都这样希望着。”
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》之“智育与教学法问题”《当太阳没入乌云的时候》（一年级，麦娅·波斯托洛娃）

### sk-1094　关于写教育日记的建议

- 旧标签：teacher-growth, child-study
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 6.67 + 先验 1.0 = 7.67））
- 其他命中：劳动与创造（5.3） · 教师（2.4）
- 转述：苏霍姆林斯基把教育日记看作教师专业成长的底层工具，而不是应付检查的正式文件：它是个人随笔和札记，是思考和创造的源泉。他自己坚持记了32年，并把一位医士27年记录儿童身高体重的做法接了过来，从教第一天起就记录儿童的身高、体重和智力发展资料。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 49“关于写教育日记的建议”

### sk-1095　怎样随着儿童的成长和发展而加深对家长的教育工作

- 旧标签：family-school, teacher-growth, labor-education
- 建议：**A8 家庭与母亲**（旧标签先验 + 文本证据（关键词 15.18 + 先验 2.5 = 17.68））
- 其他命中：阅读与书籍（11.7） · 幸福与精神生活（10.1）
- 转述：这一篇讲的是家校工作不能停在“开一次家长会”，而要随儿童年龄逐级加深。第一步是统一家庭与学校的精神生活：让家庭充满尊重科学、文化、书籍的精神，办图书日，推动家庭图书室，把傍晚一小时固定为读书时间；因为离开家庭和图书，自我教育就无从谈起。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 57“怎样随着儿童的成长和发展而加深对家长的教育工作”

### sk-1096　爱惜并发展青少年的记忆力：建立有意记忆和无意记忆的合理比例

- 旧标签：learning-difficulties, reading-and-books, child-study
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 10.81 + 先验 1.0 = 11.81））
- 其他命中：阅读与书籍（6.8）
- 转述：苏霍姆林斯基反对青少年用“分批背熟、再分批说给老师听”的儿童式方法学习。死记硬背会造成书呆子气，使知识脱离生活，甚至阻碍能力和爱好的形成。但中高年级教材又确实要求有意记忆，怎么办？他的答案不是取消背诵，而是调整比例：该记住的内容设为x，该理解和思考的内容就应是3x。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 42“爱惜并发展青少年的记忆力”

### sk-1097　怎样教人正确对待死

- 旧标签：love-education, family-school
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 6.65 + 先验 1.0 = 7.65））
- 其他命中：劳动与创造（4.6） · 道德判断与品德培养（3.0）
- 转述：苏霍姆林斯基把“如何面对死”当作道德教育不可回避的一课。他认为，人认识到时间与空间的无限之后，会格外痛苦地感到生命短暂；但人不能听命于死的摆布，而应去否定死、确立生。理解死不是让人在恐惧中消沉，而是为了更热爱、珍惜生命，并把这种理解变成真正的乐观主义。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》13“怎样教人正确对待死”

### sk-1098　少年的思维与言语活动

- 旧标签：child-study, thinking-and-nature
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 11.20 + 先验 2.5 = 13.70））
- 其他命中：了解儿童（7.2） · 评价与分数（4.8）
- 转述：这一节用一组对比实验说明少年思维的质变：低龄儿童看画注意武器、服装、马具等外部细节，少年则追问“这些东西怎么造出来的”“为什么停在这里”“国界在哪里”，关注潜在关系和因果联系。看机器模型时，低龄儿童要求把机器开动起来，少年却要求停下来、拆开来看构造；看金属零件时，低龄儿童评价“磨光的好看”，少年关心的是如何在旋床上加工
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《学生的精神世界》第5章“少年时期”之 (4)“少年的思维与言语活动”

### sk-1099　学龄初期儿童活动的特点

- 旧标签：child-study, labor-education, collective-education
- 建议：**A19 道德判断与品德培养**（文本证据推翻旧标签（关键词 2.99，压过旧标签项 2.50））
- 其他命中：教师（2.4）
- 转述：苏霍姆林斯基指出，低年级学生的年龄特点首先体现在活动上：他们无法对活动“漠不关心”，要么被吸引，要么觉得没意思，而且这种态度会直接写在脸上。孩子在游戏中最认真，有哭有笑、真动感情；但教师若想把这种认真劲儿直接搬到学习上，则注定失败，因为“掌握知识的重要性”不可能一下子被小孩子认识——他们更多是感觉，而不是理解。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《学生的精神世界》第4章“从幼年时期到少年时期”之 (6)“学龄初期儿童活动的特点”

### sk-1100　教师的人格在集体和学生个人精神生活中的作用

- 旧标签：teacher-growth, collective-education
- 建议：**A4 自我教育**（旧标签先验 + 文本证据（关键词 10.44 + 先验 1.0 = 11.44））
- 其他命中：幸福与精神生活（6.8） · 美与艺术（4.5）
- 转述：这一节把“教师人格”放在集体教育的根基位置。苏霍姆林斯基引用马克思关于人通过他人来反映自己的思想，指出：学生首先不是靠某种方法或手段受影响，而是靠教师本人的人格。没有教师真实思想和热情的鼓舞，再好的方法也会变成死板公式。孩子从学步起就同教育者比较、向教育者提要求、把教育者当榜样，所以不阐明教师个性的作用，谈培养集体就像
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《培养集体的方法》第4章“教师的人格、教师集体和学生集体”之 (1)“教师的人格在集体和学生个人精神生活中的作用”

### sk-1101　什么是小学？

- 旧标签：teacher-growth, child-study, reading-and-books
- 建议：**A6 了解儿童**（旧标签先验 + 文本证据（关键词 3.37 + 先验 2.5 = 5.87））
- 其他命中：检查知识与考查（5.1） · 思维与智力（4.0）
- 转述：苏霍姆林斯基在迎接自己第一批学生入学前夕追问：“什么是小学？”社会上常说“小学是基础的基础”，但指责也最多——说它没给儿童下一步学习所必需的知识和技能。他承认，小学确实要授予一定范围巩固的知识和技能；但更根本的是，小学首先应当教会学生怎样学习。
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《我把心给了孩子们》“儿童时代”之“什么是小学？”

### sk-1102　恋爱：尊重少年隐秘的内心世界

- 旧标签：love-education, family-school
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 4.26 + 先验 2.5 = 6.76））
- 其他命中：习惯与纪律（5.0） · 幸福与精神生活（3.3）
- 转述：苏霍姆林斯基先引用马卡连柯“任何时代任何民族的教育家都痛恨爱情”的戏谑之语，指出有些教师不懂得：年龄较大的少年已发育成男人或女人，两性之间的爱慕是规律性现象，而且少年爱慕的情感色彩与成年人的情欲完全不同，其客观基础是性本能，但直白说出会让他们大吃一惊。
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《公民的诞生》“道德的形成——公民的诞生”之“恋爱”

### sk-1103　道德习惯：确立道德观念和道德信念的基础

- 旧标签：love-education, collective-education, child-study
- 建议：**A4 自我教育**（文本证据推翻旧标签（关键词 14.09，压过旧标签项 9.57））
- 其他命中：评价与分数（9.6） · 习惯与纪律（4.8）
- 转述：苏霍姆林斯基把道德习惯看作道德观念与道德信念之间的桥梁。它源于高度自觉性与情感评价的统一：当一个人重视并习惯于高尚的道德真理时，意识中会像闪电般通过情感信号——“应当这样做，因为不这样做，自尊心是不允许的”。有了习惯，社会道德准则才真正成为个人的精神财富；没有习惯，就谈不上自我肯定、自我教育和自尊感。少年期正是形成这种
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《公民的诞生》“道德的形成——公民的诞生”之“道德习惯”

### sk-1112　青年人的道德信念和理想

- 旧标签：love-education, child-study
- 建议：**A4 自我教育**（文本证据推翻旧标签（关键词 15.59，压过旧标签项 8.85））
- 其他命中：思维与智力（7.8） · 劳动与创造（5.3）
- 转述：青年期是道德信念和理想真正开始形成的阶段。苏霍姆林斯基注意到，高中生不再满足于接受现成结论，而是要求独立表达自己的道德立场，并通过自己的行动让别人判断自己“站在哪一边”。他们强烈地想要认识自己、评价自己的内心世界，并据此选择未来的生活道路。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《学生的精神世界》第6章“青年早期”之“(3)青年人的道德信念和理想”

### sk-1113　集体和个人的精神生活

- 旧标签：collective-education, child-study, thinking-and-nature
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 6.67 + 先验 2.5 = 9.17））
- 其他命中：幸福与精神生活（7.1） · 道德判断与品德培养（6.2）
- 转述：在苏霍姆林斯基看来，真正的集体不是靠纪律和共同上课“捆”在一起的，而是由一个个精神生活丰富的个人组成的。如果每个学生的精神世界都空虚狭窄，集体就不可能真正形成；反过来，只有当集体拥有共同的智力兴趣、情感生活、世界观和信念时，个人才能在其中获得滋养。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《培养集体的方法》第3章“集体对个人教育影响的形成”之“(4)集体和个人的精神生活”

### sk-1114　教师的时间和各教学阶段的相互依存性

- 旧标签：teacher-growth, learning-difficulties
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 6.83 + 先验 1.0 = 7.83））
- 其他命中：学习困难学生（11.5） · 思维与智力（4.2）
- 转述：苏霍姆林斯基把教师的时间问题看作一个跨学段的系统问题。中高年级教师之所以被“赶尾巴”和补课耗尽时间，根源往往在小学：学生没有学会学习，尤其是没有形成边读边想、边想边读的阅读能力，以及半自动化的书写能力。于是，教师不得不一遍遍回头补旧知识，正常的教学进度被拖垮。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 7“教师的时间和各教学阶段的相互依存性”

### sk-1115　怎样引导学生从了解事实到认识抽象真理

- 旧标签：learning-difficulties, thinking-and-nature
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 7.46 + 先验 2.5 = 9.96））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：这一篇针对的是“会背不会用”的普遍弊病。苏霍姆林斯基指出，学生把规则、公式背得滚瓜烂熟，却不会在新情境中运用，原因在于记忆没有建立在理解之上。抽象真理必须从大量具体事实、事物和现象的分析中生长出来，并经过实践性作业，才真正成为可运用的知识。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 13“怎样引导学生从了解事实到认识抽象真理”

### sk-1116　培养情感的教育应当是怎样的

- 旧标签：love-education, family-school
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 10.26 + 先验 1.0 = 11.26））
- 其他命中：家庭与母亲（7.6） · 劳动与创造（5.3）
- 转述：情感教育不是讲一套“要爱别人”的道理，而是教孩子用心灵去观察、理解、感觉周围的人。苏霍姆林斯基强调，教师和家长要共同创造条件，让孩子在低年级就受到“热忱待人”的实际训练。最有价值的课程，是创造美并关心别人所享受的美：孩子为母亲、父亲、祖父母栽花、做事，在劳动和等待中体会到“我让别人快乐了”的欢乐。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 55“培养情感的教育应当是怎样的”

### sk-1117　活的习题集中的1000道题

- 旧标签：thinking-and-nature, learning-difficulties, child-study
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 7.04 + 先验 2.5 = 9.54））
- 其他命中：劳动与创造（5.3） · 全面发展与个性（5.2）
- 转述：苏霍姆林斯基用“活的习题集”来训练儿童的思维。这些题目不是机械计算，而是来自周围世界和民间谜语的问题，例如渡河、数数、分东西等，需要孩子在头脑中同时记住好几步“棋”。他认为，大脑像肌肉一样需要操练和克服困难；在物体和现象之间建立因果、时间、功能联系，正是智力发展的过程。
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《我把心给了孩子们》“儿童时代”之“活的习题集中的1000道题”

### sk-1118　思想变为信念

- 旧标签：love-education, child-study
- 建议：**A4 自我教育**（文本证据推翻旧标签（关键词 9.75，压过旧标签项 4.74））
- 其他命中：美与艺术（4.7） · 全面发展与个性（4.4）
- 转述：苏霍姆林斯基认为，道德教育的基础不是记住了多少道德条文，而是形成了真正的道德信念。思想要变成信念，教师首先必须了解少年的心灵，成为他们的知心人；同时，学生必须有丰富的“精神活动”，即把政治、道德、审美的思想变成自己内心的财富，并在行动中体现出来。
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《公民的诞生》“道德的形成——公民的诞生”之“思想变为信念”

### sk-1119　培养对自然财富的珍惜爱护态度

- 旧标签：aesthetic-nature-education, labor-education, health-first
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 17.20 + 先验 2.5 = 19.70））
- 其他命中：幸福与精神生活（7.1） · 习惯与纪律（4.8）
- 转述：苏霍姆林斯基把学校的物质基础和环境看作一种教育力量。校园里的树木、果园、花圃，以及学生亲手栽种和制作的东西，不只是“设施”，而是进入孩子精神生活、培养观点和信念的手段。当孩子为环境付出劳动，环境就带上了他的情感和记忆，他会真正珍惜它。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》第2章“学校的物质基础及学生周围的环境”之“培养对自然财富的珍惜爱护态度”

### sk-1120　体育与空余时间和休息问题

- 旧标签：health-first, child-study, aesthetic-nature-education
- 建议：**A14 美与艺术**（旧标签先验 + 文本证据（关键词 4.74 + 先验 2.5 = 7.24））
- 其他命中：劳动与创造（5.3） · 习惯与纪律（4.8）
- 转述：苏霍姆林斯基对“休息”的理解不是什么都不做，而是积极的活动和活动方式的恰当交替。休息既能恢复体力，也能促进精神力量。童年时期就培养积极休息的习惯，是教育的重要原则：劳动与脑力活动交替、带有审美满足的劳动、创造性地欣赏大自然，都可以成为真正的休息。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》第3章“关注健康与体育”之“体育与空余时间和休息问题”

### sk-1121　才能、爱好和志向的培养和发展

- 旧标签：labor-education, child-study, teacher-growth
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 5.31 + 先验 2.5 = 7.81））
- 其他命中：了解儿童（3.8）
- 转述：苏霍姆林斯基把“帮助每个孩子找到能发挥个人创造力和才能的生活道路”看作教育的重要使命。学校不应培养没有志向、对什么都不感兴趣的人；真正的个别教育，就是发现并发展每个孩子的爱好、才能和志向。每个孩子身上都蕴藏着才能的素质，但这些素质像火药，需要火花去点燃。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》第6章“劳动教育”之“才能、爱好和志向的培养和发展”

### sk-1132　怎样发展儿童的思维和智力

- 旧标签：learning-difficulties, thinking-and-nature, child-study
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 14.50 + 先验 2.5 = 17.00））
- 其他命中：学习困难学生（5.7） · 自然与思维课（4.1）
- 转述：苏霍姆林斯基把“发展思维和智力”看作与传授知识同等重要的智育任务，而不只是附带结果。对思维迟缓、所谓“头脑迟钝”的学生，不能靠反复补课和死记硬背，而要带他们回到“思维的源头”——大自然和周围世界的现象中去，通过连续观察发现因果关系，让思考的火花被点燃。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 40“怎样发展儿童的思维和智力”

### sk-1133　要保护青少年内心的纯洁激情

- 旧标签：love-education, child-study, collective-education
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 7.46 + 先验 1.0 = 8.46））
- 其他命中：道德判断与品德培养（5.4） · 劳动与创造（4.8）
- 转述：苏霍姆林斯基把“冷漠”视为青少年教育中最危险的毒素：它会把人变成只顾自己、对公共痛苦无动于衷的庸人。相反，青少年越是亲手为别人做好事，心灵就越纯洁高尚，也越会与邪恶和漠不关心势不两立。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 75“要保护青少年内心的纯洁激情”

### sk-1134　怎样启发学生在劳动和学习中进行自我教育

- 旧标签：labor-education, child-study, teacher-growth
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 5.31 + 先验 2.5 = 7.81））
- 其他命中：幸福与精神生活（7.6） · 全面发展与个性（4.4）
- 转述：苏霍姆林斯基强调，劳动中的自我教育不是靠讲道理讲出来的，而是靠真实的劳动氛围养出来的。学校和家庭如果让孩子闲散无事，再正确的教导都会变成空话；只有让劳动成为孩子能感受到快乐和创造的领域，自我教育才真正开始。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 85“怎样启发学生在劳动和学习中进行自我教育”

### sk-1135　要善于使美德具有吸引力

- 旧标签：love-education, collective-education
- 建议：**A19 道德判断与品德培养**（文本证据推翻旧标签（关键词 2.99，压过旧标签项 2.50））
- 其他命中：教师（2.4）
- 转述：苏霍姆林斯基指出，道德原则本身美好，并不等于它会自动吸引学生。越是崇高的原则，越需要以光彩、有表现力的活动去呈现；如果只是反复说“要正直、要诚实”，再正确的道理也会变成学生厌烦的说教。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 93“要善于使美德具有吸引力”

### sk-1136　情感教育和道德教育的统一

- 旧标签：love-education, aesthetic-nature-education, learning-difficulties
- 建议：**A1 全面发展与个性**（文本证据推翻旧标签（关键词 4.43，压过旧标签项 4.31））
- 其他命中：自我教育（3.8） · 幸福与精神生活（3.3）
- 转述：苏霍姆林斯基认为，认识世界从来不是纯粹理性、与情感无关的活动。如果一个人缺乏崇高的情感素养，就很难形成坚定的信念和道德立场；而情感上的冷漠会导向利己主义，成为漠视他人和社会利益的根源。
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《公民的诞生》“情感教育与美感教育”之“情感教育和道德教育的统一”

### sk-1138　我们怎样在校长和教导主任之间实行分工

- 旧标签：teacher-growth, collective-education
- 建议：**A17 习惯与纪律**（文本证据推翻旧标签（关键词 10.80，压过旧标签项 9.71））
- 其他命中：教师（7.2） · 健康与作息（5.3）
- 转述：苏霍姆林斯基把校长和教导主任的关系描述为“做同一项工作”的分工协作，而不是各管一摊。两人的共同目标只有一个：帮助教师提高教育技巧。具体做法是先共同商量、总结上一阶段工作的优缺点，再在学年、学季、教学周开始前把听课对象、指导教师、检查范围等分到人。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》第1章“全体教师团结一致是教育教学工作成功的保证”之“我们怎样在校长和教导主任之间实行分工”

### sk-1139　集体研究“思维与情感的统一”问题

- 旧标签：teacher-growth, thinking-and-nature, collective-education
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 11.05 + 先验 2.5 = 13.55））
- 其他命中：自然与思维课（4.1） · 幸福与精神生活（3.3）
- 转述：这一节讲的是帕夫雷什中学教师集体如何从一个真实的教学困惑出发，开展集体研究。苏霍姆林斯基在听课中发现学生回答贫乏、语言没有活生生的思想，于是记录、分析学生的词汇和言语，追问“词语怎样进入儿童意识、怎样成为思维工具”。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》第1章“全体教师团结一致是教育教学工作成功的保证”之“集体研究‘思维与情感的统一’问题”

### sk-1140　行为美的理想观念的培养

- 旧标签：collective-education, love-education, child-study
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 9.71 + 先验 1.0 = 10.71））
- 其他命中：学习困难学生（5.8） · 全面发展与个性（4.4）
- 转述：苏霍姆林斯基把“行为美”看作个人信念和公民精神的来源。要培养这种理想观念，关键是让每个学生都成为别人的教育者：高年级学生去带低年级的小组、辅导后进生，在关心、保护和帮助他人的过程中，自己也成长为有教养的人。
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《培养集体的方法》第3章“集体对个人教育影响的形成”之 (8)“行为美的理想观念的培养”

### sk-1152　青少年的思想是怎样成熟起来的

- 旧标签：love-education, collective-education, child-study
- 建议：**A2 公民与祖国**（旧标签先验 + 文本证据（关键词 7.98 + 先验 1.0 = 8.98））
- 其他命中：道德判断与品德培养（5.4） · 集体与同伴（3.2）
- 转述：苏霍姆林斯基认为，思想的成熟不是靠年龄增长或说教自然发生的，而是靠“操心”和“为别人做好事”一点点积累起来的。他特别警惕“无忧无虑的童年和少年时代”，认为那正是精神幼稚病的温床：一个孩子如果从小到大只被照顾、只被满足，心灵就会贫乏空虚，老师讲再崇高的道理也进不到他心里。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 73“青少年的思想是怎样成熟起来的”

### sk-1153　怎样做教育工作计划

- 旧标签：teacher-growth, family-school, reading-and-books
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 11.40 + 先验 2.5 = 13.90））
- 其他命中：思维与智力（13.7） · 家庭与母亲（3.5）
- 转述：苏霍姆林斯基反对把教育工作计划写成装潢门面的官样文章，但他坚持“没有计划就无法想象完全合格的教育工作”。做计划的第一步不是排活动表，而是先想清楚要把学生培养成什么样的人，并据此倒推十年、十五年：包括一份学生在校十年间要读完的世界文化书单，一份毕业后仍应继续阅读的“后备书单”，以及学生从入学到成年应为父母和他人做些什么、
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 97“怎样做教育工作计划”

### sk-1154　要教育学生不说空话

- 旧标签：love-education, teacher-growth, collective-education
- 建议：**A15 思维与智力**（文本证据推翻旧标签（关键词 8.20，压过旧标签项 6.88））
- 其他命中：尊严、爱与信任（4.4） · 集体与同伴（3.2）
- 转述：苏霍姆林斯基把“说空话”看作一种会同时腐蚀个人和集体的恶习：一旦空话流行，集体就不可能在思想上真正统一，因为语言与行动脱钩，人就等于在精神上被解除了武装。他给出的矫正方法非常具体——教学生说话算数，不给没有把握的承诺留余地：与其说“我保证完成”，不如说“我要尽力办成”；说了就要做，哪怕重做十次也不在众人面前失信。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 81“要教育学生不说空话”

### sk-1155　关于对自己子女的教育问题

- 旧标签：family-school, teacher-growth, love-education
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 7.10 + 先验 1.0 = 8.10））
- 其他命中：自然与思维课（4.1） · 教师（2.4）
- 转述：苏霍姆林斯基指出一个教师群体中普遍而自相矛盾的现象：最会教育别人孩子的人，往往没有时间教育自己的孩子。他的建议不是让教师把学校搬回家，恰恰相反——在家里，教师首先应当是父亲和母亲，而不是老师或班主任；不要把家庭变成“小型的学校”，不要把学校的气氛、教师“管人”的权力和情绪带回家。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 50“关于对自己子女的教育问题”

### sk-1156　手工劳动在全面发展中的作用

- 旧标签：labor-education, thinking-and-nature, child-study
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 16.38 + 先验 2.5 = 18.88））
- 其他命中：全面发展与个性（5.0） · 健康与作息（4.8）
- 转述：苏霍姆林斯基指出，手工劳动不等于简单的体力劳动；在高度素养的手工劳动中，创造思维会鲜明地显现出来。机器和工艺越复杂，在掌握技术之前需要具备的手工劳动基本技能就越多。他以帕夫雷什中学为例：低年级和中年级学生在学习操纵机器之前，先拆装机器的活动模型，理解零件和部件之间的相互作用，再过渡到真机器；这样培养出来的人会成为机器的
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》第6章“劳动教育”之“手工劳动在全面发展中的作用”

### sk-1158　青年的一般特点

- 旧标签：child-study, love-education, health-first
- 建议：**A7 健康与作息**（旧标签先验 + 文本证据（关键词 4.28 + 先验 2.5 = 6.78））
- 其他命中：劳动与创造（5.3） · 公民与祖国（3.9）
- 转述：苏霍姆林斯基把16—18岁青年身体进入成熟期看作精神生活的一个新因素：青年男女意识到自己身体已趋成熟，对自身力量有了信心，感到自己是“成年人”了。这种意识既可能促使他们努力学习，也可能带来一种不满足和不安——自己有充足的体力和精力，却还在学校学习，不能为祖国作出应有的贡献。因此，学习和生产劳动的正确结合，对青年期格外重
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《学生的精神世界》第6章“青年早期”之 (1)“青年的一般特点”

### sk-1159　科学世界观的形成过程与科学基础知识的掌握

- 旧标签：thinking-and-nature, labor-education, child-study
- 建议：**A3 幸福与精神生活**（文本证据推翻旧标签（关键词 11.27，压过旧标签项 8.17））
- 其他命中：思维与智力（5.7） · 全面发展与个性（5.1）
- 转述：苏霍姆林斯基区分了“掌握知识”和“形成世界观”：只有当人站在个人的生活立场上对待知识，让学到的知识在生活实践中得到反映并决定行为方向时，知识才转化为世界观因素；人对知识及其结论所采取的个人态度，就是信念。因此，教育性教学最重要的任务之一，是防止学生对知识采取冷漠态度，认为知识内容与己无关。
- 出处：《苏霍姆林斯基选集（五卷本）第4卷》（教育科学出版社），《帕夫雷什中学》第5章“智育”之“科学世界观的形成过程与科学基础知识的掌握”

### sk-1161　教师集体和学生集体

- 旧标签：collective-education, family-school, teacher-growth
- 建议：**A9 集体与同伴**（旧标签先验 + 文本证据（关键词 9.09 + 先验 2.5 = 11.59））
- 其他命中：幸福与精神生活（9.7） · 家庭与母亲（3.5）
- 转述：苏霍姆林斯基把学校与家庭不良影响的较量称为“争夺个别儿童灵魂的一种斗争”：有些孩子身心已受到家庭的摧残，教师集体必须考虑如何消除和制止家庭的不良影响，使学校和集体的影响占优势。正是“对这些儿童的命运负责”这种感情，把教师、学生特别是高年级学生团结在一起。教师集体和学生集体的这种责任感是巨大的精神财富，并且会随着一次次“
- 出处：《苏霍姆林斯基选集（五卷本）第1卷》（教育科学出版社），《培养集体的方法》第4章“教师的人格、教师集体和学生集体”之 (2)“教师集体和学生集体”

### sk-1162　关于学生的智力生活

- 旧标签：reading-and-books, thinking-and-nature, teacher-growth
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 15.50 + 先验 2.5 = 18.00））
- 其他命中：阅读与书籍（11.1） · 集体与同伴（5.2）
- 转述：这一条把“负担过重”的根源指向教师的关注点：只想着怎样迫使学生多啃教科书、把注意力从一切其他活动上拉回来，负担过重就不可避免。苏霍姆林斯基认为，学生的精神生活不能只剩上课、教科书、作业和分数；在此之外必须有丰富多彩的智力生活，首先是课外阅读，尤其是少年期的课外阅读。他建议班主任把“形成学生这种精神需要”当作主要任务，编
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 30. 关于学生的智力生活

### sk-1163　直观是认识的途径，是照亮认识途径的光辉

- 旧标签：thinking-and-nature, learning-difficulties, child-study
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 15.30 + 先验 2.5 = 17.80））
- 其他命中：幸福与精神生活（7.0） · 教师（2.4）
- 转述：苏霍姆林斯基反对把直观教具仅仅当作“吸引注意力”的手段，他认为那样做对智育有害。直观的价值在于促进思维过程：它的目的是让学生在认知的某个阶段能够脱离形象，进而领会概念、理解规律性。他还举了自己带水轮机活动模型上课的例子——水花在阳光下映出彩虹，学生的注意力全被这道偶然出现的彩虹吸走，而没有集中到他想要引导他们领会的概括
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 36. 直观是认识的途径，是照亮认识途径的光辉

### sk-1164　把每个学生引向兴趣的发源地

- 旧标签：reading-and-books, child-study, teacher-growth
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 17.51 + 先验 2.5 = 20.01））
- 其他命中：了解儿童（3.8） · 思维与智力（3.7）
- 转述：这一条把“兴趣”落到实处：先要区别“度过”和“利用”自由活动时间，再为每个学生找到属于他的兴趣发源地。第一位的发源地是书籍——读书应成为最重要的兴趣发源地，学校应成为书籍世界；即便学校地处偏远、设备匮乏，只要有充足的书籍，教育水平也能与文化中心相当。低年级要分年级建立图书角，并让教师亲自为每个学生挑选当时最需要、最适合
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 33. 把每个学生引向兴趣的发源地

### sk-1165　怎样训练儿童流利地书写

- 旧标签：learning-difficulties, child-study, labor-education
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 7.16 + 先验 2.5 = 9.66））
- 其他命中：思维与智力（7.5） · 阅读与书籍（6.8）
- 转述：苏霍姆林斯基把读和写称作“通向周围世界的两扇窗口”：不会流利、快速、有理解地阅读，不会流利、快速、半自动化地书写，儿童就像半盲人一样。他强调书写必须达到“半自动化”——学生不再需要分心去想某个字母怎么写、怎么连，才能腾出注意力去考虑语法规则和所写内容的意义。他的目标很具体：到三年级（四年级则更肯定）学生应能笔不离纸地写
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 44. 怎样训练儿童流利地书写

### sk-1166　怎样在脑力劳动中培养自觉的纪律

- 旧标签：reading-and-books, thinking-and-nature, health-first
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 11.06 + 先验 2.5 = 13.56））
- 其他命中：思维与智力（10.8） · 劳动与创造（5.3）
- 转述：这一条是对高年级学生讲的“脑力劳动自觉纪律”清单，前提是教师集体有浓厚的文化知识兴趣、课堂教学以多方面智力生活为基础、教师的知识远远超过教学需要、每个学生都有自己的智力爱好。苏霍姆林斯基认为，纪律不是外部约束，而是学生自己安排读书、思考、解决智力任务时形成的内在秩序。他给出的第一条就是每天读书：每天至少读两页所喜爱学科
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 86. 怎样在脑力劳动中培养自觉的纪律

### sk-1167　什么是课堂上的思想教育

- 旧标签：thinking-and-nature, teacher-growth, collective-education
- 建议：**A12 自然与思维课**（旧标签先验 + 文本证据（关键词 5.67 + 先验 1.0 = 6.67））
- 其他命中：评价与分数（4.7） · 自我教育（3.8）
- 转述：苏霍姆林斯基先破除一个流行观念：学生掌握知识的同时就自然受到了道德教育。他认为“通过教学的教育”“通过知识的道德教育”这类说法会让人产生无忧无虑的自我安慰心理——懂规律、会答题、拿高分，并不等于道德教育；只有当知识转变为信念、真理触及灵魂、激动人心，并促使学生用行动去捍卫时，教育才开始。因此，缺乏某项具体知识不说明道德
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 91. 什么是课堂上的思想教育

### sk-1168　怎样教会孩子善于理解人的悲痛

- 旧标签：love-education, family-school, child-study
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 4.38 + 先验 2.5 = 6.88））
- 其他命中：习惯与纪律（5.8） · 美与艺术（4.5）
- 转述：这一节教孩子如何面对亲人的死亡与悲痛：亲人去世意味着“你本身的一小部分死去”，要表示哀悼，要懂得在哀悼期不去娱乐场所、家里不放响亮的娱乐音乐，让良心悄悄提示自己。苏霍姆林斯基举了一个反面例子——九年级学生送葬后立刻去踢足球，还被朋友称赞“精神坚强”；他直言这不是坚强，而是道德上的无知：这种人在生活里没有任何神圣的东西。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》15. 怎样教会孩子善于理解人的悲痛

### sk-1169　如何成为谦虚的人，怎样培养谦虚

- 旧标签：love-education, collective-education, family-school
- 建议：**A19 道德判断与品德培养**（人工裁定（谦虚属于待人分寸/品德培养；纪律只是它的外壳（外部评审建议 A4，据内容改判 A19）））
- 其他命中：习惯与纪律（10.9） · 自我教育（8.8）
- 转述：苏霍姆林斯基把谦虚定义为“一门学问”：它涉及人与人之间的关系、行为举止、愿望、思想和感情、意志和性格。谦虚首先意味着不许有“我有特殊优点，因而该享有优待和宽容自己”的想法——社会纪律面前人人平等，要求别人做到的，也要要求自己做到。它还意味着正确地看待自己的优点和毛病：不管别人怎样夸奖，都要有自知之明，把夸奖当成鼓励自我
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》41. 如何成为谦虚的人，怎样培养谦虚

### sk-1170　我把心给了孩子们·前言

- 旧标签：love-education, teacher-growth, child-study
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 15.98 + 先验 2.5 = 18.48））
- 其他命中：幸福与精神生活（6.4） · 自我教育（3.8）
- 转述：这是《我把心给了孩子们》的自序。苏霍姆林斯基先说明这本书的性质：它是多年学校工作的总结，是沉思、关心、担忧和不安心情的总结；在一所农村学校身不离校地工作32年，对他而言是无与伦比的幸福。他坦言，考虑很久之后才给书取名《我把心给了孩子们》，因为把自己的一生都献给了孩子们，“我是有这个权利的”。谈到生活中什么最重要，他不假
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《我把心给了孩子们》前言

### sk-1171　怎样培养青年们正确对待爱

- 旧标签：love-education, family-school
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 9.07 + 先验 2.5 = 11.57））
- 其他命中：家庭与母亲（3.5） · 道德判断与品德培养（3.0）
- 转述：这一节直接对青年说话：人有性的本能，如果它不上升为高尚、美好的人类之爱，就可能使人回到动物状态；爱情方面的道德无知会给社会带来数不尽的不幸，把爱情当作玩乐的人必定给他人带来痛苦、不幸和悲伤。苏霍姆林斯基把尊重放在首位——要尊重姑娘，爱护她的名誉、人格、自尊和自主性，因为她可能成为妻子、孩子的母亲。他强调爱“是一种关系”
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》49. 怎样培养青年们正确对待爱

### sk-1172　请记住，没有也不可能有抽象的学生

- 旧标签：learning-difficulties, child-study, assessment-grading
- 建议：**A6 了解儿童**（旧标签先验 + 文本证据（关键词 13.98 + 先验 2.5 = 16.48））
- 其他命中：学习困难学生（4.9） · 评价与分数（4.2）
- 转述：这一节是苏霍姆林斯基因材施教思想的总纲。他用提水作比喻：有的孩子提5桶就精疲力尽，有的能提20桶，硬要弱小的孩子提20桶会把他压垮；脑力劳动同样如此，每个学生领会、记忆、保持知识的方式和速度都不同。因此不存在“抽象的学生”，任何教育规律都不能机械地搬用到大纲背后的每一个具体儿童身上。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 5. 请记住，没有也不可能有抽象的学生

### sk-1173　关于获取知识

- 旧标签：thinking-and-nature, teacher-growth, child-study
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 7.04 + 先验 2.5 = 9.54））
- 其他命中：阅读与书籍（2.9） · 教师（2.4）
- 转述：这一节区分了两种“积极性”：背熟书本、记住讲解、迅速回答是表面的积极性，未必促进智力发展；真正要发挥的是思维的积极性，使知识因被运用而生长。获取知识的本质不是接收结论，而是发现真理、回答问题——教师要让学生看出并感到自己有不理解的东西，让他们面临问题。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 12. 关于获取知识

### sk-1174　学生学习课程的积极活动内容

- 旧标签：labor-education, thinking-and-nature, child-study
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 14.40 + 先验 2.5 = 16.90））
- 其他命中：美与艺术（10.4） · 阅读与书籍（7.4）
- 转述：这一节讲的是“活动中学”的操作方法：教师要在开课之前，就为整个课程学习期间设计一套贯穿始终的积极活动，而不只是零散地做几次实验或练习。这种活动的目的不只是养成实际技能，更是让学生在课程体系内部持续地动手、观察、思考，从而发展思维和语言。苏霍姆林斯基把它称为联结语言和思维的桥梁。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 20. 学生学习课程的积极活动内容

### sk-1175　怎样按季节安排学生的学习

- 旧标签：health-first, child-study, teacher-growth
- 建议：**A7 健康与作息**（旧标签先验 + 文本证据（关键词 8.42 + 先验 2.5 = 10.92））
- 其他命中：自然与思维课（5.7） · 全面发展与个性（5.0）
- 转述：这一节把脑力劳动的节律与季节、学年节奏结合起来，是苏霍姆林斯基独有的“学习节奏学”。他从身体发育出发：春天机体防护力减弱、视力容易下降，而学校里面对的是正在成长的身体和形成中的大脑，所以春天的学习绝不能照搬秋天的安排。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 29. 怎样按季节安排学生的学习

### sk-1176　通过爱劳动促进学生智力发展

- 旧标签：labor-education, learning-difficulties, thinking-and-nature
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 14.50 + 先验 2.5 = 17.00））
- 其他命中：劳动与创造（10.1） · 阅读与书籍（7.1）
- 转述：这一节把劳动与智育直接连起来，提出“儿童的智慧出在他的手指头上”。苏霍姆林斯基强调的不是任何劳动，而是复杂的、创造性的、需要思考和精巧技能技艺的劳动：手越灵巧，头脑越明晰、越好钻研，分析事实、现象、因果关系和规律的能力也越突出。手与脑之间存在直接联系——思想检验、矫正和改善劳动过程，手则把详细情况报告给思想。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 34. 通过爱劳动促进学生智力发展

### sk-1177　怎样同集体进行有教育作用的谈话

- 旧标签：collective-education, teacher-growth
- 建议：**A15 思维与智力**（文本证据推翻旧标签（关键词 7.36，压过旧标签项 5.66））
- 其他命中：自我教育（4.3） · 美与艺术（4.2）
- 转述：这一节讲班主任和教师最常用的德育手段——集体谈话。苏霍姆林斯基首先强调语言的分量：教师通过语言打动学生的理智与心灵，而语言是否有力，取决于谈话有没有崇高的精神、能否鼓舞人；教师说出的不只是内容，也把自己的一部分心思交给学生。因此谈话的前提，是教师自己深信并用整个心灵捍卫所说的道理。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 98. 怎样同集体进行有教育作用的谈话

### sk-1178　在哪些条件下集体才能有效地发挥教育个人的作用

- 旧标签：collective-education, child-study, teacher-growth
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 9.07 + 先验 1.0 = 10.07））
- 其他命中：劳动与创造（5.3） · 全面发展与个性（4.4）
- 转述：这一节是对集体教育条件的系统总结，苏霍姆林斯基一口气列出十三条，核心是：集体之所以有教育力量，不靠外部管束和集体压力，而靠成员之间的相互理解、自我节制、精神成长和个性多样化。第一条要求每个人都能设身处地体会他人的精神世界与情绪；第二条要求学会把欲望同别人对比、衡量，懂得谦让；第三条强调集体只有在精神上不断成长时才是真正
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 88. 在哪些条件下集体才能有效地发挥教育个人的作用

### sk-1179　何谓珍惜生活的幸福

- 旧标签：aesthetic-nature-education, family-school, child-study
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 10.08 + 先验 1.0 = 11.08））
- 其他命中：自我教育（8.8） · 思维与智力（6.7）
- 转述：这一节把“珍惜生活的幸福”当作一项最重要的道德课题。苏霍姆林斯基说，生活的幸福像空气一样充盈，人却像在空气充足时感觉不到空气那样，很少去思索它；要真正珍惜它，需要高尚、细致、全面的精神修养，即智力、心灵和意志的修养。他把它比作“扬起自我教育风帆的风”——没有这股风，人就看不到生活目标，停止发展。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》3. 何谓珍惜生活的幸福

### sk-1180　理解亲人的痛苦能提高道德敏锐性

- 旧标签：family-school, love-education, child-study
- 建议：**A19 道德判断与品德培养**（文本证据推翻旧标签（关键词 9.15，压过旧标签项 7.65））
- 其他命中：幸福与精神生活（6.7） · 习惯与纪律（5.8）
- 转述：这一节讲道德敏锐性的培养机制：能感受和理解亲人的痛苦，会反过来提高一个人的道德敏锐性、品德和人性。苏霍姆林斯基要求孩子学会从别人的眼睛里、从细微到几乎察觉不到的举动中、从步履和呼吸里、从人观察世界的目光中看到痛苦；要知道自己的言行会直接影响他人的精神状态，不要以自己的举止使别人痛苦、受辱、不宁。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》12. 理解亲人的痛苦能提高道德敏锐性

### sk-1181　怎样培养个人对邪恶持毫不妥协的态度

- 旧标签：collective-education, labor-education, family-school
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 5.31 + 先验 2.5 = 7.81））
- 其他命中：全面发展与个性（4.4） · 道德判断与品德培养（3.0）
- 转述：这一节讨论道德教育中最难的范畴之一：个人对邪恶的态度。苏霍姆林斯基先指出恶的多种形式——利己主义、虚情假义、两面派、谄媚、随机应变、卑躬屈膝、懒惰、玩忽职守、追求轻松安逸，以及酗酒对人格的严重损害。然后给出核心要求：对丑恶的积极态度首先是憎恨它、不容忍它；看到恶不能置之不理，更不能保持平静。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》47. 怎样培养个人对邪恶持毫不妥协的态度

### sk-1182　最后一条建议——保密：把教育意图隐蔽起来

- 旧标签：teacher-growth, love-education
- 建议：**A4 自我教育**（旧标签先验 + 文本证据（关键词 10.28 + 先验 1.0 = 11.28））
- 其他命中：幸福与精神生活（6.8） · 尊严、爱与信任（4.3）
- 转述：苏霍姆林斯基把全书的最后一条建议留给“保密”：教育意图应当隐蔽，教师不必让学生时时感到自己正在被教育。理由不是欺骗，而是因为真正的教育最终要落成自我教育——只有当学生感到那些话是朋友之间的交流、是自己内心的活动，而不是一套专门针对他的“教育程序”，自我认识和自我完善的能力才不会被压抑。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 100. 最后一条建议——保密

### sk-1183　怎样在体育方面引导学生进行自我教育

- 旧标签：health-first, child-study, labor-education
- 建议：**A7 健康与作息**（旧标签先验 + 文本证据（关键词 8.94 + 先验 2.5 = 11.44））
- 其他命中：自然与思维课（9.8） · 幸福与精神生活（7.1）
- 转述：这一节把体育从“老师要求的锻炼”变成学生的自我教育。苏霍姆林斯基的出发点是：体格教育与自我教育是统一的，而这种统一从幼年就开始——当孩子刚学会拿汤匙时，就要让他劳动；只有从小劳动、边干边想的孩子，才会真正听懂关于体育的教导。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 87. 怎样在体育方面引导学生进行自我教育

### sk-1184　人生下来是为了在自己身后留下痕迹

- 旧标签：love-education, labor-education, family-school
- 建议：**A2 公民与祖国**（旧标签先验 + 文本证据（关键词 7.14 + 先验 1.0 = 8.14））
- 其他命中：劳动与创造（5.3） · 幸福与精神生活（3.4）
- 转述：这一节回答“人为什么活着”：人不是为了像尘埃一样无声无息地消失，而是要在身后留下永久的痕迹。苏霍姆林斯基把“留在人心中”看作人生最大的幸福与意义，而最基本的途径就是培养好自己的子女、并在劳动与创造中把自己的心血留在世界上。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》16. 人生下来是为了在自己身后留下痕迹

### sk-1185　怎样培养对亲人和亲近的人的忠诚感

- 旧标签：love-education, family-school, collective-education
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 9.53 + 先验 2.5 = 12.03））
- 其他命中：道德判断与品德培养（9.1） · 全面发展与个性（4.4）
- 转述：这一节把忠诚感的教育落在最具体的关系上：从种一棵“母亲苹果树”“父亲苹果树”开始，把第一次收获送给长辈；从对待父母的态度开始，学会奉献而不是隐藏。苏霍姆林斯基提出一个关键判断：忠实于崇高理想这种“道德发展的顶峰”，其根源恰恰是孩子对父母、对亲人的信任与忠诚。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》23. 怎样培养对亲人和亲近的人的忠诚感

### sk-1186　怎样教孩子理解道德上的自由感

- 旧标签：love-education, collective-education, child-study
- 建议：**A19 道德判断与品德培养**（文本证据推翻旧标签（关键词 8.39，压过旧标签项 6.76））
- 其他命中：公民与祖国（5.7） · 习惯与纪律（4.9）
- 转述：这一节处理德育中一个较难的命题：道德自由不是“想做什么就做什么”，而是人能自觉地把自己与集体、社会、人民的共同利益联系起来，听从义务感。苏霍姆林斯基指出，孩子长大后会不好意思再被大人牵着手，这种“想独立”的愿望恰恰是道德自由的萌芽，教育要尊重它、发展它，而不是压制它。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》34. 怎样教孩子理解道德上的自由感

### sk-1187　怎样教孩子明白和意识自己的过错

- 旧标签：love-education, child-study, family-school
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 9.12 + 先验 2.5 = 11.62））
- 其他命中：思维与智力（3.7）
- 转述：这一节把“认错”当作一种需要培养的能力：能感到自己有过错，是人的一大财富。苏霍姆林斯基提出一个关键机制——“良心的眼睛就是思维”，只有让孩子学会预想行为的后果、设身处地为他人着想，良心才会被唤醒；没有思索的地方，就没有良心的责备。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》38. 怎样教孩子明白和意识自己的过错

### sk-1188　培养尊敬爷爷奶奶的情感

- 旧标签：family-school, love-education, collective-education
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 11.83 + 先验 1.0 = 12.83））
- 其他命中：习惯与纪律（4.9） · 劳动与创造（4.6）
- 转述：这一节把“敬老”从道德口号变成家庭里可操作的制度：爷爷奶奶在家里要有受人尊敬的地位，家里遇到复杂难办的事先请他们发言；不住在一起就要写信，节日要祝贺；老人留下的心爱遗物要珍藏并传给子孙。苏霍姆林斯基的判断很直接——晚年只有安宁或不幸，而安宁来自“大家还尊敬他、没有忘记他”。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》19. 培养尊敬爷爷奶奶的情感

### sk-1189　人应当尊敬地纪念自己的先辈

- 旧标签：love-education, family-school, collective-education
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 4.38 + 先验 2.5 = 6.88））
- 其他命中：公民与祖国（4.0） · 幸福与精神生活（3.0）
- 转述：这一节把“纪念先辈”提到公民觉悟与良心的层面：心中没有过去的人，心中也不可能有未来；每一块墓碑下都是一部世界史，墓地是人类良心的卫兵，亲人的坟墓是心灵的一面镜子。忘记亲人的墓，意味着冷漠无情。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》14. 人应当尊敬地纪念自己的先辈

### sk-1190　怎样使学生们具有知识的欢乐

- 旧标签：learning-difficulties, reading-and-books, thinking-and-nature
- 建议：**A3 幸福与精神生活**（文本证据推翻旧标签（关键词 14.06，压过旧标签项 9.60））
- 其他命中：评价与分数（9.0） · 阅读与书籍（7.1）
- 转述：这一节回答“怎样让学生把学习体验为幸福”。苏霍姆林斯基指出：学习本应是最大的幸福，但在人人享有学习机会的社会里，它反而容易被看作负担甚至惩罚；一旦到了这一步，任何道德教育成绩都无从谈起。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》25. 怎样使学生们具有知识的欢乐

### sk-1191　怎样培养孩子自觉地去追求善良

- 旧标签：love-education, collective-education, labor-education
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 9.71 + 先验 1.0 = 10.71））
- 其他命中：自我教育（4.4） · 尊严、爱与信任（4.2）
- 转述：这一节的核心是把“善”从抽象说教变成带意志的积极行动：善不是别人灌输给孩子的抽象真理，也不是一朵只供欣赏的美丽小花，而是为正义思想而斗争的武器——是我们的活动、意志、劳动和对恶毫不妥协的斗争。用苏霍姆林斯基的话说，“善就是加上意志的一种思想”。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》46. 怎样培养孩子自觉地去追求善良

### sk-1192　教儿童利用自由活动时间

- 旧标签：child-study, health-first, thinking-and-nature
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 7.04 + 先验 2.5 = 9.54））
- 其他命中：劳动与创造（5.3） · 全面发展与个性（5.0）
- 转述：这一条接着上篇 31“必须有自由活动时间”回答“怎么用”。苏霍姆林斯基首先提醒教师：儿童对时间流逝的感觉与成人完全不同，一整个晴朗的夏日对他们可能像一整年，因此不能用硬性的分钟计划去束缚他们，也不该因为他们“忘了作业”而当众叱责。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 32. 教儿童利用自由活动时间

### sk-1193　青年对待爱情的精神准备应当包括些什么

- 旧标签：love-education, family-school
- 建议：**A15 思维与智力**（文本证据推翻旧标签（关键词 6.67，压过旧标签项 6.00））
- 其他命中：家庭与母亲（3.5） · 幸福与精神生活（3.3）
- 转述：苏霍姆林斯基把“爱情的精神准备”具体化为一份婚前自检清单：能否忠诚、有无懒惰自私冷酷、能否控制欲望、对家庭物质基础有无准备。他特别强调结婚前要征求父母意见，因为家庭生活的意义和目的就是教育子女；不思考未来子女就走进婚姻，好比要终生远行却既不知自己的力量，也不知要走的路。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》50. 青年对待爱情的精神准备应当包括些什么

### sk-1194　理解新教材是课堂教学的一个阶段

- 旧标签：learning-difficulties, thinking-and-nature
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 7.47 + 先验 2.5 = 9.97））
- 其他命中：劳动与创造（7.0） · 评价与分数（4.2）
- 转述：这一条把“理解”确立为课堂教学中一个独立而必要的阶段。苏霍姆林斯基区分了“了解”与“知道”：昨天全班似乎都懂了，今天却有一半人模糊甚至忘掉，原因就在于缺少理解。理解不是复述，而是学生自己思考所学内容、检验理解是否正确、尝试把知识运用于实践。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 15. 理解新教材是课堂教学的一个阶段

### sk-1195　不同年龄学生组成的集体不是凭空建立起来的

- 旧标签：collective-education, labor-education
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 5.31 + 先验 2.5 = 7.81））
- 其他命中：全面发展与个性（4.4） · 自我教育（4.3）
- 转述：这一条回答“混龄集体怎样才能真正建立起来”。苏霍姆林斯基认为，不同年龄学生之间的精神联系不是靠编班或口号产生的，而是靠有趣而复杂的共同劳动：当儿童和青少年在同一集体中驾驶机器、掌握复杂技能并相互传授经验时，劳动才真正有趣，集体才成为教育工具。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 78. 不同年龄学生组成的集体不是凭空建立起来的

### sk-1196　怎样使男女青年们具有人的欲望的素养

- 旧标签：love-education, family-school
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 4.90 + 先验 2.5 = 7.40））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：这一篇把“欲望的素养”作为爱情教育和人格教育的核心。苏霍姆林斯基指出，爱情只有在把“我想要”和“我应当”和谐融合时才是高尚的；在爱情中最能反映一个人的欲望素养，而人品也正表现在这里。能自觉控制欲望的人，大都能成为真正的人。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》48. 怎样使男女青年们具有人的欲望的素养

### sk-1197　怎样培养对妇女、姑娘、母亲的尊重

- 旧标签：love-education, collective-education
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 4.26 + 先验 2.5 = 6.76））
- 其他命中：公民与祖国（5.3） · 了解儿童（3.4）
- 转述：这一条把“尊重妇女、姑娘、母亲”与爱国主义、勇敢精神直接连在一起。苏霍姆林斯基先讲了一个真实场景：大雪封村，八年级学生想到独居老太太，冒着零下二十度严寒，用担架轮流抬着她走了五个小时送到医院。他说，正是在这一天，“男子汉诞生了”，14 岁的少年升到了勇敢的第一级。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 61. 怎样培养对妇女、姑娘、母亲的尊重

### sk-1198　教师应制订哪些计划

- 旧标签：teacher-growth, reading-and-books
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88））
- 其他命中：评价与分数（4.8） · 思维与智力（3.3）
- 转述：这一条先回应一个现实矛盾：教师常被没有必要的文牍压垮，但“官样文章”被批评后，又有人走向另一个极端，认为什么计划都不必订。苏霍姆林斯基的立场是：两种看法都不对，对工作有益的计划必须订。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 48. 教师应制订哪些计划

### sk-1199　忠诚感和对别人的忠诚意味着什么

- 旧标签：love-education, family-school
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 9.29 + 先验 2.5 = 11.79））
- 其他命中：全面发展与个性（4.4） · 公民与祖国（4.0）
- 转述：这一篇把“忠诚”从抽象的道德概念落到“留在人间”的生命意义上。苏霍姆林斯基说，人不同于动物之处，在于传宗接代的同时把自己的美、理想和对崇高事业的忠诚留在人间；一个人越善于在人间深刻反映自己，他的公民生活就越丰富，个人生活也越幸福。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》35. 忠诚感和对别人的忠诚意味着什么

### sk-1200　向初到学校工作的教师提一些建议

- 旧标签：teacher-growth, reading-and-books, child-study
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 7.44 + 先验 2.5 = 9.94））
- 其他命中：思维与智力（7.5） · 幸福与精神生活（7.0）
- 转述：这一条是给刚参加工作的教师的“长期投资”建议。苏霍姆林斯基从自己的体验出发：头十年过得很慢，后来时间飞驰，等到感到时间不够用时才后悔没有在青年时期就开始积累教育智慧。因此青年时期要一点一滴地积累教育者的智力财富。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 37. 向初到学校工作的教师提一些建议

### sk-1201　向准备担任一年级工作的教师提一些建议

- 旧标签：child-study, family-school, health-first
- 建议：**A7 健康与作息**（旧标签先验 + 文本证据（关键词 10.07 + 先验 2.5 = 12.57））
- 其他命中：家庭与母亲（7.6） · 阅读与书籍（7.4）
- 转述：这一条把“了解儿童”具体化为一年级教师入学前一年半就要开始的准备工作。苏霍姆林斯基说，他早在开始教儿童的一年半以前就有了未来学生的名单，并了解他们的父母、推测可能的遗传疾病，再由医生检验，掌握学生神经系统、呼吸、心脏、消化、视力和听力等状况。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 38. 向准备担任一年级工作的教师提一些建议

### sk-1202　第3封信：思想性就是真正的人性

- 旧标签：love-education, reading-and-books
- 建议：**A1 全面发展与个性**（文本证据推翻旧标签（关键词 8.81，压过旧标签项 7.40））
- 其他命中：尊严、爱与信任（4.9） · 道德判断与品德培养（3.0）
- 转述：儿子在大学来信中说，自己身边有人用讽刺的口吻谈论“思想性”，把为理想而生活说成是想捞道德资本，他因此感到沮丧，不知道该怎样理解为理想而生活。苏霍姆林斯基回信说：正因为这些问题让你焦虑不安，这才好；对周围人说什么、想什么毫不在乎，才是真正危险的。
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《给儿子的信》第3封信

### sk-1203　怎样同家庭一道指导儿童劳动

- 旧标签：labor-education, family-school
- 建议：**A8 家庭与母亲**（旧标签先验 + 文本证据（关键词 4.14 + 先验 2.5 = 6.64））
- 其他命中：幸福与精神生活（3.0） · 劳动与创造（2.3）
- 转述：这一条回答的是“学校怎样和家庭一道指导儿童劳动”。苏霍姆林斯基的判断很直接：劳动只有成为家庭经济生活不可缺少的一部分、成为子女对家庭的神圣义务，才具有教育力量；如果家庭不需要儿童劳动、家长只想让孩子轻松，那么学校安排的实习课在孩子眼里就只是游戏，而且是令人厌烦、想尽快摆脱的游戏。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 58. 怎样同家庭一道指导儿童劳动

### sk-1205　怎样教学生们成为好子女

- 旧标签：family-school, love-education
- 建议：**A7 健康与作息**（文本证据推翻旧标签（关键词 10.22，压过旧标签项 10.14））
- 其他命中：家庭与母亲（7.6） · 幸福与精神生活（7.1）
- 转述：这一篇既是苏霍姆林斯基对学生的直接教诲，也是对教师和家长的提醒。乌克兰民谚说人有三个不幸——“死亡、衰老、子女不好”，前两个无法避免，唯有“子女不好”可以像防火一样预防，而这不只取决于父母，也取决于子女自己。好子女的标准很具体：只给家里带来和睦、安宁、欢乐和幸福，不带来忧虑、烦恼、埋怨和耻辱。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》21. 怎样教学生们成为好子女

### sk-1206　怎样使思想和公民尊严感融为一体

- 旧标签：teacher-growth, collective-education, reading-and-books
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 12.94 + 先验 2.5 = 15.44））
- 其他命中：评价与分数（10.0） · 思维与智力（7.5）
- 转述：这一条讨论的是教学中一个“十分微妙”的问题：怎样让学生因为学习好、因为自己的知识和成绩而感到一种公民的尊严。苏霍姆林斯基认为，关键在于把知识和智力财富变成“个性的自我表现”，而不是只让集体知道某个学生怎样学功课、怎样回答问题。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 27. 怎样使思想和公民尊严感融为一体

### sk-1207　集体的自主活动重在什么

- 旧标签：collective-education, assessment-grading
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 9.60 + 先验 1.0 = 10.60））
- 其他命中：学习困难学生（5.7） · 评价与分数（4.7）
- 转述：这一条回答“集体的自主活动重在什么”。苏霍姆林斯基先纠正一个常见误解：不是丰富的精神生活取决于自主活动，恰恰相反，自主活动是充实而丰富的精神生活的结果；集体越是关心每个成员的命运、越能让每个人给同志带来精神财富，自主活动才越有内容。其基础是“集体对个人的每项要求同时又是集体对个人的关怀与爱护”。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 90. 集体的自主活动重在什么

### sk-1208　在校学习是正在成长一代的积极的公民生活

- 旧标签：teacher-growth, love-education
- 建议：**A2 公民与祖国**（旧标签先验 + 文本证据（关键词 7.98 + 先验 1.0 = 8.98））
- 其他命中：思维与智力（7.5） · 劳动与创造（5.3）
- 转述：这一篇把“在校学习”从一项个人任务重新定义为正在成长一代的积极的公民生活。苏霍姆林斯基说，知识是公民的精神力量和武器；在当代，如果公民知识水平不高、没有求知精神、没有丰富的智力生活，就不可能有强盛独立的国家。学数学、物理、化学、生物，就是准备用智慧和知识为祖国服务；学生的天职就是竭尽全力去学习。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》30. 在校学习是正在成长一代的积极的公民生活

### sk-1209　第17封信：尊重妇女与女性美

- 旧标签：love-education, family-school
- 建议：**A19 道德判断与品德培养**（文本证据推翻旧标签（关键词 9.44，压过旧标签项 6.76））
- 其他命中：尊严、爱与信任（4.3） · 幸福与精神生活（3.8）
- 转述：儿子在信中问父亲：怎样尊重姑娘的女性美，什么是女性美。苏霍姆林斯基说，这个问题让儿子不安，他很高兴，因为对待妇女的态度是衡量道德的一把尺子——马克思说过，从这种关系可以判断人的整个文化教养程度；对妇女蛮横无理的人，会对一切都蛮横无理。
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《给儿子的信》第17封信

### sk-1210　第13封信：从柏林谈对祖国的责任

- 旧标签：love-education, teacher-growth
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 6.73 + 先验 1.0 = 7.73））
- 其他命中：劳动与创造（4.7） · 自我教育（4.4）
- 转述：这封信写于柏林。苏霍姆林斯基告诉儿子，自己不是第一次出国，但每次远离祖国，都会有一种新的力量激起他热爱祖国的情感；在国外，他特别深切地感到自己对祖国担负的一切责任。他把祖国比作慈祥而又严格的母亲：如果儿子成了懒惰、冷酷、意志薄弱、假仁假义、不诚实的人，母亲会何等伤心。
- 出处：《苏霍姆林斯基选集（五卷本）第3卷》（教育科学出版社），《给儿子的信》第13封信

### sk-1211　结束语：共产主义信念是新人成长的合金

- 旧标签：love-education, teacher-growth
- 建议：**A7 健康与作息**（文本证据推翻旧标签（关键词 13.23，压过旧标签项 10.71））
- 其他命中：劳动与创造（10.7） · 思维与智力（10.4）
- 转述：这是《年轻一代共产主义信念的形成》的结束语，写于 1961 年加加林完成人类首次宇宙飞行之后。苏霍姆林斯基把这一事件看作人类思维、创造、劳动发展的新阶段，也是人类精神发展的新阶段；他用“合金”作比喻：强壮健康的身体、高度发达的智力、深湛的技术知识、高尚的道德品质，融合成新人的真正威严，而融合这一合金的强大力量就是共产主
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《年轻一代共产主义信念的形成》结束语

### sk-1212　传播知识与参加社会生活

- 旧标签：collective-education, teacher-growth
- 建议：**A15 思维与智力**（人工裁定（「传播知识」= 向他人讲解以加深理解，集体只是场景（外部评审意见）））
- 其他命中：（除建议条目外无其他关键词命中）
- 转述：苏霍姆林斯基把学校看作农村文化和知识的主要基地，主张把知识的加深过程纳入社会生活：高年级学生到村里的“文化基地”，为庄员和工人办报告会、自然科学晚会和文学晚会，用科学道理去说服人、消除迷信和反科学偏见。他指出，学生在向别人传授知识时，自己也会把问题想得更清楚，并发现新的疑问。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 28. 传播知识与参加社会生活

### sk-1213　怎样教孩子懂得奉献的思想

- 旧标签：love-education, child-study
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 10.08 + 先验 1.0 = 11.08））
- 其他命中：尊严、爱与信任（4.9） · 习惯与纪律（4.8）
- 转述：这一节把“奉献”放回义务的地基上：人活着就应当尽义务、应当奉献，否则生活无法维持。苏霍姆林斯基反过来说，一个人越是严格履行对他人的义务，就越能从自由这一真正幸福的源泉中汲取力量；若试图把自己从奉献中解脱出来，反而会成为放任自流的奴隶。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》6. 怎样教孩子懂得奉献的思想

### sk-1214　怎样在学校集体内建立劳动关系

- 旧标签：labor-education, collective-education
- 建议：**A9 集体与同伴**（旧标签先验 + 文本证据（关键词 9.09 + 先验 2.5 = 11.59））
- 其他命中：劳动与创造（2.3）
- 转述：苏霍姆林斯基把“物质关系”看作集体建设中特别重要的一环：责任感、领导、服从、互助合作和经验交流，都要有物质形式来承载。没有对物质财富的明确责任，谈论责任感就是空话；没有互助合作和同志式的经验交流，就不可能有真正的集体。帕夫雷什中学的做法是让少先队和共青团的作业队真正掌管机器、试验田、园地和自己的经济账目。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 77. 怎样在学校集体内建立劳动关系

### sk-1215　怎样祝贺亲人的生日

- 旧标签：family-school, love-education
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 11.50 + 先验 1.0 = 12.50））
- 其他命中：尊严、爱与信任（4.9） · 家庭与母亲（3.5）
- 转述：苏霍姆林斯基把“祝贺亲人生日”当作修养的标志来教：孩子应当终生记住父母、爷爷奶奶、兄弟姐妹的生日，因为家庭的幸福就在于彼此奉献心中的温暖，家里有多少个人就有多少个生日。他还给出很具体的分寸——生日那天要早起，当面说祝福；对姐姐、母亲等不要刻意提年龄；给孩子的祝词也不宜说“祝你长寿”，因为孩子还无法理解。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》22. 怎样祝贺亲人的生日

### sk-1216　在学校集体中什么可以讨论和什么不可以讨论

- 旧标签：collective-education, child-study
- 建议：**A9 集体与同伴**（旧标签先验 + 文本证据（关键词 8.56 + 先验 2.5 = 11.06））
- 其他命中：评价与分数（9.6） · 学习困难学生（4.9）
- 转述：这一篇划出了集体舆论的边界。苏霍姆林斯基列出多类不应拿到集体面前讨论的行为：因家庭不幸或父母反社会行为引起的不良行为、因生父生母问题造成的创伤、对成人粗暴专横的抗议、由教师错误或不公正评分引起的行为、因智力发展或力所不及而成绩落后、涉及私人友谊的行为等。理由不是学生没有分辨力，而是没有必要再次触动伤口。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 89. 在学校集体中什么可以讨论和什么不可以讨论

### sk-1217　怎样把教师劳动的意义传送到学生的意识中去

- 旧标签：teacher-growth, love-education
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88））
- 其他命中：道德判断与品德培养（3.0） · 幸福与精神生活（3.0）
- 转述：苏霍姆林斯基先说明教师劳动的特殊性：纺织工、炼钢工、庄稼人较快就能看到成果，而教师要年复一年、甚至十几年才看到自己造就的对象；任何劳动都不像教师劳动那样一有差错就可能造成严重后果。因此，学生理解教师劳动的复杂性，不是对教师的怜悯，而是成为教师志同道合者的前提。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》28. 怎样把教师劳动的意义传送到学生的意识中去

### sk-1218　向在规模大的学校里工作的教师提些建议

- 旧标签：teacher-growth
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 2.38 + 先验 2.5 = 4.88））
- 其他命中：思维与智力（3.7） · 集体与同伴（3.2） · 劳动与创造（3.0）
- 转述：这一篇是写给大规模学校里的年轻教师的。苏霍姆林斯基承认，在有许多同事的学校里更容易提高水平，但提醒借鉴经验是一件复杂而需要创造的工作：不要依次去听所有人的课，那样很难抓到要领。他给出一条省时的入口——先看学生练习本；如果某个班绝大多数学生的字写得漂亮、清秀、正确，这就是可以学习的直接标志，因为练习本是整个教育工作的一面
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 46. 向在规模大的学校里工作的教师提些建议

### sk-1220　给单班制学校教师的建议

- 旧标签：teacher-growth, reading-and-books
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 12.67 + 先验 2.5 = 15.17））
- 其他命中：学习困难学生（4.9） · 幸福与精神生活（3.8）
- 转述：这一篇专门写给单班制、双班制小型学校的教师。苏霍姆林斯基承认这类学校只有一两个教师，要维持丰富多彩的精神生活气氛很费力，但他强调责任恰恰在这里：如果教师自身没有一般文化和教育上的高度素养，偏远的居住点就可能继续落后，而改变这种状况只能依靠教师本人。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 47. 给单班制学校教师的建议

### sk-1221　怎样培养忠于社会主义祖国的情感

- 旧标签：love-education, aesthetic-nature-education
- 建议：**A2 公民与祖国**（旧标签先验 + 文本证据（关键词 13.32 + 先验 1.0 = 14.32））
- 其他命中：了解儿童（7.2） · 全面发展与个性（5.2）
- 转述：苏霍姆林斯基把祖国放在“不可度量”的财富序列里：祖国、儿子的忠诚、对生养自己的土地和人民的忠诚，任何别的东西都不能与之相比。他从词源上把“祖国”与“父母”联系起来，指出母亲只生下身体，祖国却产生一个人作为公民的灵魂，因此爱国情感天然带有对父母、对土地、对人民的依恋。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》56. 怎样培养忠于社会主义祖国的情感

### sk-1222　怎样和家长一道培养未来的母亲和父亲

- 旧标签：family-school, love-education
- 建议：**A8 家庭与母亲**（旧标签先验 + 文本证据（关键词 7.64 + 先验 2.5 = 10.14））
- 其他命中：幸福与精神生活（6.4） · 劳动与创造（5.3）
- 转述：这一条把培养未来的母亲和父亲作为学校与家庭共同的任务。学校培养的不只是公民和劳动者，还是未来的父母、自己子女的教育者；因此要防止对婚姻、爱情、生儿育女的轻率态度，并在家长教育学校中向父母讲清子女性成熟期面临的课题。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 60. 怎样和家长一道培养未来的母亲和父亲

### sk-1223　用追求理想的方法培养思想性

- 旧标签：love-education, collective-education, teacher-growth
- 建议：**A2 公民与祖国**（旧标签先验 + 文本证据（关键词 13.32 + 先验 1.0 = 14.32））
- 其他命中：全面发展与个性（9.5） · 检查知识与考查（5.1）
- 转述：这一条讲的是“用追求理想的方法培养思想性”。苏霍姆林斯基把祖国比作人的家和摇篮，强调要有道德权利谈祖国的不幸，就必须先为巩固祖国做具体的事，蔑视空话和蛊惑宣传。他认为正确的世界观不是凭空灌输的，而是在生活中观察并创造出对自己珍贵的东西时形成的；14 岁应当以公民身份回答“我活在这个世界上是为了什么”。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》57. 用追求理想的方法培养思想性

### sk-1224　不要害怕困难，有困难是好事，否则就谈不上对青少年进行思想教育

- 旧标签：health-first, love-education, labor-education
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 8.97 + 先验 2.5 = 11.47））
- 其他命中：幸福与精神生活（3.0） · 劳动与创造（2.3）
- 转述：这一条正面回答“为什么要让青少年吃苦”。苏霍姆林斯基说，克服困难的过程能培养英勇无畏的精神、陶冶高尚情操；而且困难不会让人变得冷酷，反而使人对善良和他人更温厚、更有同情心，对邪恶更不妥协。他向学生展示的生活不是坦途，青年尤其是男青年应准备经受最严峻的考验。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 74. 不要害怕困难，有困难是好事，否则就谈不上对青少年进行思想教育

### sk-1225　怎样教孩子们理解和运用苏维埃国家法律

- 旧标签：collective-education, love-education
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 10.40 + 先验 1.0 = 11.40））
- 其他命中：尊严、爱与信任（8.5） · 劳动与创造（4.6）
- 转述：这一条是五卷本中少见的“法治教育”专论。苏霍姆林斯基先确立前提：苏维埃法律是公正、人道的，它保护的是个人、家庭、幸福和未来的孩子；同时法律必须对邪恶有强大的威力和毫不妥协的制裁。遵纪守法不是压抑，而是“高度自由的表现”——自由是最巨大也最危险的力量，必须审慎、理智地使用；面对违法行为不能袖手旁观。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》59. 怎样教孩子们理解和运用苏维埃国家法律

### sk-1226　怎样教育共青团员关心公共利益

- 旧标签：labor-education, collective-education
- 建议：**A5 尊严、爱与信任**（文本证据推翻旧标签（关键词 9.01，压过旧标签项 5.66））
- 其他命中：教师（4.8） · 评价与分数（4.8）
- 转述：这一条从两个反面例子讲起：一位副校长把社会学研究室布置得很漂亮，却答不出怎样让马列主义真理深入青少年心灵——苏霍姆林斯基批评这种“只看得见上级命令，而看不见人的灵魂”的教育，说没有灵魂、没有心灵，教育就等于零。接着是一个正面案例：共青团员在为国家仓库选送谷米时，有人建议把差谷米垫在车厢底下、好谷米盖在上面以“完成计划”
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 76. 怎样教育共青团员关心公共利益

### sk-1227　代前言

- 旧标签：teacher-growth, child-study
- 建议：**A11 劳动与创造**（文本证据推翻旧标签（关键词 5.31，压过旧标签项 4.88））
- 其他命中：幸福与精神生活（4.0） · 阅读与书籍（2.9）
- 转述：《代前言》交代了《给教师的100条建议》的写作缘起：苏霍姆林斯基在帕夫雷什中学工作期间，同刚开始工作的年轻教师进行过数百次会见和谈话，收到成千上万封信，这些促使他写成此书。他深信，没有比教师更富有求知精神、不满足现状、更充满创造思想的人。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》代前言

### sk-1228　怎样激励人们经常不断地发展和完善道德

- 旧标签：collective-education, love-education
- 建议：**A9 集体与同伴**（旧标签先验 + 文本证据（关键词 6.84 + 先验 2.5 = 9.34））
- 其他命中：评价与分数（4.8） · 美与艺术（4.2）
- 转述：这一条回答“怎样激励人不断发展和完善道德”。苏霍姆林斯基首先给出一个原则：要使一个人力争自身达到道德的美好和完善，他必须在自己周围、在同学身上看到这种美和完善；人只有通过对待别人的态度和与人们相处，才能培养出自己独特的品格。他引用马克思的话说明，人起初是以别人来反映自己的，学会像对待别人一样对待自己，是集体教育艺术的秘
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 70. 怎样激励人们经常不断地发展和完善道德

### sk-1229　怎样使青年对我们的生活和斗争不要漠不关心

- 旧标签：love-education, family-school, collective-education
- 建议：**A2 公民与祖国**（旧标签先验 + 文本证据（关键词 13.32 + 先验 1.0 = 14.32））
- 其他命中：幸福与精神生活（10.6） · 尊严、爱与信任（4.7）
- 转述：这一条针对“青年对生活和斗争漠不关心”的问题，把培育爱国主义者和公民称为共青团教育最主要、最复杂的任务。苏霍姆林斯基认为，只有具有同情心和勇敢的人才能成为爱国主义者和公民；爱国主义是感情和思想结合的产物，它首先要求用心灵而不是仅用理智去理解祖国这一神圣事物。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 71. 怎样使青年对我们的生活和斗争不要漠不关心

### sk-1231　怎样培养少年列宁主义者，教师在少先队组织生活中的作用

- 旧标签：collective-education, love-education, teacher-growth
- 建议：**A2 公民与祖国**（旧标签先验 + 文本证据（关键词 13.32 + 先验 1.0 = 14.32））
- 其他命中：集体与同伴（9.1） · 习惯与纪律（4.9）
- 转述：这一条讲少先队组织在培养少年列宁主义者中的作用，以及教师、教育者应扮演什么角色。苏霍姆林斯基认为，儿童加入少先队就开始了社会政治生活的新阶段；基层集体的教师、教育者的主要任务，是用崇高的公民理想来激励少先队，让少先队集体生活用比个人志向、兴趣和才能更重要的东西把儿童和少年振奋起来、团结起来。他把少先队组织称为“学习文明
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 66. 怎样培养少年列宁主义者，教师在少先队组织生活中的作用

### sk-1232　怎样培养年轻一代在伟大卫国战争英雄面前的责任感

- 旧标签：love-education, teacher-growth, family-school
- 建议：**A2 公民与祖国**（旧标签先验 + 文本证据（关键词 7.98 + 先验 1.0 = 8.98））
- 其他命中：尊严、爱与信任（4.9） · 全面发展与个性（4.4）
- 转述：这一条讲的是如何让年轻一代在面对伟大卫国战争英雄时产生真正的责任感。苏霍姆林斯基先摆事实：法西斯德国入侵苏联，妄图消灭俄罗斯、白俄罗斯、乌克兰民族，在被占领土和德国本土建造“杀人工厂”，两千万苏联士兵和军官为祖国的自由与独立献出生命。他要孩子记住这些，不是要求他们背下数字，而是让他们明白自己今天能活着、能自由劳动，是别
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》54. 怎样培养年轻一代在伟大卫国战争英雄面前的责任感

### sk-1233　怎样使共青团员胸怀社会主义祖国

- 旧标签：love-education, collective-education, teacher-growth
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 11.40 + 先验 1.0 = 12.40））
- 其他命中：公民与祖国（9.3） · 思维与智力（7.4）
- 转述：这一条谈的是怎样让每个学生真正受到“为祖国服务”这种爱国主义精神的陶冶。苏霍姆林斯基把这件工作称为细致而复杂，并且描述得很具体：教师用火热的语言讲述之后，学生会深受鼓舞，各自去寻找并找到自己喜爱的书，在“祖国的天空发现自己的灿烂明星”。真正的标志是学生开始追问自己——我是什么样的人？我以前是怎样生活的？将来我要怎样生活
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 72. 怎样使共青团员胸怀社会主义祖国

### sk-1234　在当今做个革命者意味着什么

- 旧标签：love-education, teacher-growth, collective-education
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 13.51 + 先验 1.0 = 14.51））
- 其他命中：劳动与创造（9.9） · 公民与祖国（8.0）
- 转述：这一条回答的是一个价值定向问题：在今天，做“革命者”到底意味着什么。苏霍姆林斯基没有把它讲成政治表态，而是先让孩子懂得自己已经拥有的东西——公民身份、自由劳动的幸福、精神生活与成长的道路，然后把这些“拥有”放回历史里，指出它们是革命换来的。他要求孩子把吃穿住的关怀放在第二位，把智力和情感、创造和美、图书和音乐的关怀放在
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》53. 在当今做个革命者意味着什么

### sk-1235　怎样培养共青团员的上进心

- 旧标签：collective-education, love-education, teacher-growth
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 9.29 + 先验 2.5 = 11.79））
- 其他命中：劳动与创造（5.3） · 评价与分数（4.8）
- 转述：这一条讲怎样培养共青团员的上进心，苏霍姆林斯基是把它放在“道德美感”里谈的。他认为，伟大思想的鼓舞作用能让人创造出自身的美；要把青年培养得使他们感到自己是美好的，让道德的美感培育出崇高的自豪感和公民的尊严，使他们不仅能看到周围的事物，也能看到自己。他给出一个很强的判断：一个人若不能以自身的美引为自豪，就不可能懂得良心的
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 69. 怎样培养共青团员的上进心

### sk-1236　怎样培养学生在道德上准备当军人的天职

- 旧标签：love-education, teacher-growth, family-school
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 4.90 + 先验 2.5 = 7.40））
- 其他命中：幸福与精神生活（6.3） · 习惯与纪律（5.8） · 集体与同伴（5.4）
- 转述：这一条谈的是怎样让学生从童年起在道德上为承担保卫祖国的责任做好准备。苏霍姆林斯基把这件事理解为长期的品格养成，而不是临到服兵役时才开始的思想动员：能吃苦耐劳、不怕困难、信守诺言，这些品质都要从小培养，而信守诺言本身就是一种道德上的高尚品格。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》58. 怎样培养学生在道德上准备当军人的天职

### sk-1237　怎样向少年列宁主义者灌输共产主义思想

- 旧标签：collective-education, love-education, teacher-growth
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 11.06 + 先验 1.0 = 12.06））
- 其他命中：自我教育（8.2） · 幸福与精神生活（6.4）
- 转述：这一条讲的是思想信念怎样才能真正进入少年儿童的心灵。苏霍姆林斯基的出发点是那句拉丁谚语：“话语开导人，榜样吸引人。”他认为靠抽象宣讲和反复说教无法把思想交给孩子，只能通过体现人的最高美德的鲜明形象和榜样，把信念展示在儿童的意识和心灵面前；这些美德在他那里被概括为为人民的幸福而斗争、自我牺牲、对信仰忠贞不渝、百折不挠、对
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 67. 怎样向少年列宁主义者灌输共产主义思想

### sk-1238　怎样使青年在领到印有伟大列宁肖像的红色共青团证时激情满怀，怎样使他们珍惜共青团员的称号

- 旧标签：collective-education, love-education, teacher-growth
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 10.75 + 先验 1.0 = 11.75））
- 其他命中：劳动与创造（9.9） · 集体与同伴（9.1）
- 转述：这一条是写给即将做高年级学生工作的年轻教育者的，回答一个很具体的问题：怎样让青年在领到印有列宁肖像的红色共青团证时真的激情满怀，怎样让他们珍惜共青团员的称号。苏霍姆林斯基先给出前提性的建议——经常独自一人思考，并且要喜欢这种“为青年人的命运而思索的快乐时刻和不安时刻”。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 68. 怎样使青年在领到印有伟大列宁肖像的红色共青团证时激情满怀，怎样使他们珍惜共青团员的称号

### sk-1240　请记住，没有也不可能有抽象的学生

- 旧标签：learning-difficulties, child-study, assessment-grading
- 建议：**A6 了解儿童**（旧标签先验 + 文本证据（关键词 13.98 + 先验 2.5 = 16.48））
- 其他命中：教师（8.4） · 美与艺术（4.2）
- 转述：这一节的重点不是“因材施教”这个结论，而是它在一堂课里怎么落地：同一份大纲、同一个知识点，作业要在难度和数量上分档。苏霍姆林斯基举出的实例是帕夫雷什中学阿里申柯与雷萨克的数学课——解题占课堂90%的时间，班内分成若干组：成绩最好的学生除了大纲习题，还拿超出大纲的材料，作业要“经过努力才能完成”，偶尔甚至给一道不能独立解
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 5. 请记住，没有也不可能有抽象的学生

### sk-1241　评分应当有分量

- 旧标签：assessment-grading, teacher-growth, love-education
- 建议：**A16 评价与分数**（旧标签先验 + 文本证据（关键词 14.36 + 先验 2.5 = 16.86））
- 其他命中：尊严、爱与信任（9.6） · 幸福与精神生活（7.1）
- 转述：这一节最值得单独拎出来的是开头那句判断：**评分是师生关系的显影剂**。苏霍姆林斯基说，根据学生怎样看待教师所给的分数，可以“准确无误地推断出”他对待教师的态度、对教师信任和尊敬的程度。分数之所以能反照关系，是因为它只有在师生彼此信任和关怀的基础上，才会成为推动脑力劳动的力量；一旦这层关系不存在，同样的分数就退化成最微
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 17. 评分应当有分量

### sk-1242　怎样使家庭作业的检查成为有效的脑力劳动

- 旧标签：assessment-grading, learning-difficulties, teacher-growth
- 建议：**A16 评价与分数**（旧标签先验 + 文本证据（关键词 5.46 + 先验 2.5 = 7.96））
- 其他命中：检查知识与考查（6.8） · 习惯与纪律（4.8）
- 转述：这一节问的是：怎样让“检查家庭作业”不再等于“点名一个人复述，其余人走神”。苏霍姆林斯基给出的答案是把检查改成三种替代形态，各自适用不同场景。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 16. 怎样使家庭作业的检查成为有效的脑力劳动

### sk-1245　让学生记住基本知识

- 旧标签：learning-difficulties, reading-and-books, teacher-growth
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 18.62 + 先验 1.0 = 19.62））
- 其他命中：学习困难学生（4.9） · 评价与分数（4.2）
- 转述：这份“必须终生牢记”的清单不是凭经验随手列的，而是从高年级大纲倒推出来的。苏霍姆林斯基要求小学教师从一年级起就动手：把四年级的语文、数学教学大纲拿来，还要拿五年级的数学教学大纲，再加上历史、自然、地理的课外读物和这些课在四年级的大纲，把所有这些材料加以对照和比较，弄清一件事——为使学生能在四年级和五年级顺利学习，三年级
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 8. 让学生记住基本知识

### sk-1246　怎样在脑力劳动中培养自觉的纪律

- 旧标签：teacher-growth, learning-difficulties, collective-education
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 11.06 + 先验 1.0 = 12.06））
- 其他命中：思维与智力（10.8） · 全面发展与个性（5.2）
- 转述：自觉纪律是前提的产物，不是管制的产物。苏霍姆林斯基对七年级以上学生提出脑力劳动纪律的建议时，先交代清楚：这些建议的效果取决于许多条件和前提，其中最主要的是四项——学校里首先是教师集体要有浓厚的文化知识兴趣；课堂教学要以多方面的智力生活为基础；教师的知识要远远超过教学的需要；要使每个学生都有自己的智力爱好。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 86. 怎样在脑力劳动中培养自觉的纪律

### sk-1247　怎样教学生自己教育自己

- 旧标签：collective-education, love-education, teacher-growth
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 13.79 + 先验 2.5 = 16.29））
- 其他命中：集体与同伴（6.8） · 评价与分数（4.8）
- 转述：苏霍姆林斯基把自我教育放在个人教育的核心位置：集体教育的力量依赖于对个人的教育，而对个人的教育如果离开自我教育就不可思议。他明确说，在对个人的教育中，自我教育是起主导作用的方法之一——教师的任务不是替学生走路，而是让他独立行走、对自己负责。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 82. 怎样教学生自己教育自己

### sk-1248　怎样培养母亲和父亲做好学校和家庭的协同教育工作

- 旧标签：family-school, love-education, child-study
- 建议：**A7 健康与作息**（文本证据推翻旧标签（关键词 15.53，压过旧标签项 12.00））
- 其他命中：习惯与纪律（12.0） · 思维与智力（10.7）
- 转述：苏霍姆林斯基把家长教育学校当作一项常规课程来办，而不是零散的家长会：不关心家长的教育修养，任何教育和教学任务都不可能完成，家长教育学是整个教育理论和实践的基础。学校按学段分成学前部、一至三年级、四至八年级、九至十一年级四个部，父母在孩子入学前三年就开始学习。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 52. 怎样培养母亲和父亲做好学校和家庭的协同教育工作

### sk-1249　父母在孩子生活中的作用

- 旧标签：family-school, love-education, labor-education
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 5.31 + 先验 2.5 = 7.81））
- 其他命中：幸福与精神生活（6.4） · 自我教育（5.8）
- 转述：苏霍姆林斯基先把“尊重父母的劳动”说成一件具体的事：父母给予你的一切，都是用他们的劳动、血汗和劳累换来的；孩子能回报的方式不是空口的感谢，而是正直地生活、热爱劳动、在学习年代勤奋学习，并给家里带来平静和安宁。劳动在这里是父母与子女之间最实在的连接。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》20. 父母在孩子生活中的作用

### sk-1252　怎样减轻批改作业之苦

- 旧标签：assessment-grading, teacher-growth
- 建议：**A20 检查知识与考查**（文本证据推翻旧标签（关键词 12.48，压过旧标签项 7.83））
- 其他命中：阅读与书籍（6.8） · 劳动与创造（5.3）
- 转述：这一节的落点是可执行的三步流程，而不是号召教师忍耐。苏霍姆林斯基先诊断病灶：批改之苦的祸根不是批改本身，而是「技能与知识之间的比例失调」——在语法、规范阅读、数学这类课程里，技能长期落后于知识，学生因此大量出错，教师再用力批也批不完，所以单纯压缩批改时间的努力「什么结果也没有达到」。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 19. 怎样减轻批改作业之苦

### sk-1253　“两个教学大纲”，发展学生的思维

- 旧标签：reading-and-books, thinking-and-nature, learning-difficulties
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 11.40 + 先验 2.5 = 13.90））
- 其他命中：思维与智力（10.4） · 检查知识与考查（5.1）
- 转述：本卡只谈第二个教学大纲怎么排：书目清单怎么配、读物在时间上放在哪里。苏霍姆林斯基的排法有三条可操作规则。第一条是「按难点配量」：某个时候所学习的概念愈复杂，学生读的书就应当愈有趣、愈有吸引力——读物的难度要与概念的难度反向补偿，越难的概念配越好看的读物。第二条是「一套而不是一本」：教电流定律时，他凑集了一套专门的小丛书
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 9. “两个教学大纲”，发展学生的思维

### sk-1254　直观是认识的途径，是照亮认识途径的光辉

- 旧标签：thinking-and-nature, learning-difficulties, teacher-growth
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 11.16 + 先验 2.5 = 13.66））
- 其他命中：学习困难学生（12.2） · 美与艺术（4.2）
- 转述：这一节可以收束成三条检查红线。第一条，不抢注意力：直观只有在促进思维过程时才有助于发展和加深注意力，物体形象本身能长时间吸住学生，但那不是目的。他用自己的课做反例——水轮机活动模型转动时水花在阳光下映出一道彩虹，他没发现，学生却看见了，于是全部注意力离开了他想引导他们领会的概括性结论，落到这个偶然现象上，这节课效果不好
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 36. 直观是认识的途径，是照亮认识途径的光辉

### sk-1255　怎样教孩子正确对待脑力劳动

- 旧标签：learning-difficulties, teacher-growth, health-first
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 11.06 + 先验 1.0 = 12.06））
- 其他命中：劳动与创造（10.0） · 自我教育（8.8）
- 转述：这一篇的枢纽是：思维是最复杂的劳动，脑力劳动也是劳动。苏霍姆林斯基提醒，如果只把劳动理解成“手拿铲子或扫帚”，学生就会轻视劳动的多面性，也就不会把学习当成一件需要认真对待的劳动来干。因此他要求教师“确立对思考、对思维的态度，就像对劳动的态度那样”。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》29. 怎样教孩子正确对待脑力劳动

### sk-1256　培养对待学校的态度要像对待人民精神生活的最重要的发源地那样

- 旧标签：family-school, reading-and-books, love-education
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 8.71 + 先验 2.5 = 11.21））
- 其他命中：幸福与精神生活（7.5） · 公民与祖国（3.9）
- 转述：这一段把“尊敬学校”这件事从口号拉回到家庭的书架上。苏霍姆林斯基设想的“图书的节日”发生在学年开始之前，核心动作有两个，都发生在家庭一侧：父母给自己的孩子买一本有纪念意义的书，并且用这本书去充实**家庭图书馆**；随后，这个节日最有象征性的举动是把书捐进学校的永久性图书馆。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》27. 培养对待学校的态度要像对待人民精神生活的最重要的发源地那样

### sk-1257　在校学习是正在成长一代的积极的公民生活

- 旧标签：collective-education, love-education, teacher-growth
- 建议：**A2 公民与祖国**（旧标签先验 + 文本证据（关键词 13.32 + 先验 1.0 = 14.32））
- 其他命中：幸福与精神生活（10.3） · 自我教育（8.2）
- 转述：这一篇的要害是把“在校学习即公民生活”从一句命题变成日常可执行的东西。苏霍姆林斯基给了一个判断标准：教师只有在“每天都使孩子在学校里增添一点公民意识”的条件下，才真正成为教育者。也就是说，公民意识不是一次班会讲出来的，而是每天在具体岗位上被重复确认出来的。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》30. 在校学习是正在成长一代的积极的公民生活

### sk-1258　共产主义信念的形成是社会进步和道德进步的客观必然性

- 旧标签：collective-education, love-education, teacher-growth
- 建议：**A2 公民与祖国**（旧标签先验 + 文本证据（关键词 12.89 + 先验 1.0 = 13.89））
- 其他命中：劳动与创造（5.3） · 自我教育（3.8）
- 转述：这一章的核心机制是：信念不是被讲出来的，而是客观社会关系与教育的有意影响共同作用的产物。苏霍姆林斯基把影响人的意识的因素分成两个“紧密交织”的方面——一是社会关系的客观作用，二是教育者为确立一定观点和信念而开展的积极而有目的的活动；他称之为客观方面与主观方面。这一章要讲的“客观必然性”正落在这里：道德进步的客观规律与社
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《年轻一代共产主义信念的形成》第2章 共产主义信念的形成是社会进步和道德进步的客观必然性

### sk-1259　怎样才能做到使行为举止听从良心的最强有力的指挥

- 旧标签：love-education, child-study, teacher-growth
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 13.41 + 先验 2.5 = 15.91））
- 其他命中：幸福与精神生活（6.7） · 习惯与纪律（5.8）
- 转述：这一篇回答的是道德教育中最难的问题：怎么让孩子的行为不靠外人的目光和夸奖来支撑，而由自己的良心来指挥。苏霍姆林斯基把良心说成心灵里最细微、最娇嫩、最易感受的一角，是对自尊心的轻微触及；因此教育的第一要务不是训诫，而是保护儿童的心灵不受虚伪和可耻行为的侵扰，培养出一颗纯洁的良心。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》33. 怎样才能做到使行为举止听从良心的最强有力的指挥

### sk-1260　怎样培养自己的学生具有共同参与、共同感受的能力

- 旧标签：love-education, collective-education, family-school
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 12.88 + 先验 2.5 = 15.38））
- 其他命中：集体与同伴（12.3） · 幸福与精神生活（6.7）
- 转述：这一篇讲的是教师怎样把「共同参与、共同感受」变成学生真实的能力，而不是口头上的集体主义。起点是观察：孩子生活在人群之中，要细心看人们怎样干活、休息、生病、离别与重逢，看人们怎样达到目标又提出新目标。每个人都是一个复杂的世界，接触十个世界，自己的世界就每天出现在这十个人面前。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》36. 怎样培养自己的学生具有共同参与、共同感受的能力

### sk-1261　怎样培养孩子具有慷慨大方和大公无私的品格

- 旧标签：love-education, family-school, labor-education
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 13.95 + 先验 1.0 = 14.95））
- 其他命中：尊严、爱与信任（9.6） · 全面发展与个性（4.4）
- 转述：这一篇把「慷慨大方、大公无私」当作可以在童年、少年和青年早期培养起来的品格，而不是天生的好心肠。苏霍姆林斯基先给吝啬定性：吝啬使人贫乏，把人变得自私自利、视钱如命；它实质上是惟恐把自己心灵的一部分奉献给别人、让别人生活得更好的利己主义病态，并会逐渐变成贪婪，摧残个性、精神世界、需求和兴趣，最终导致无人性和仇视人类。预防
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》40. 怎样培养孩子具有慷慨大方和大公无私的品格

### sk-1262　美是培养善良、热爱劳动、热诚和爱情的重要手段

- 旧标签：aesthetic-nature-education, love-education, labor-education
- 建议：**A1 全面发展与个性**（文本证据推翻旧标签（关键词 9.44，压过旧标签项 7.81））
- 其他命中：劳动与创造（5.3） · 自我教育（4.4）
- 转述：这一篇是苏霍姆林斯基美育思想的纲领性表述：美不是生活的装饰，而是培养善良、热爱劳动、热诚和爱情的重要手段。他从人对花瓣与晚霞的注视讲起，说明美的存在不依我们的意识和意志为转移，但美需要被人发现、被人认识，才会存在于人的心灵之中；我们来到世界上就是为了认识美、确立美和创造美。人能看到天空的奥秘、群星的闪烁、晚霞的粉红、草
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》52. 美是培养善良、热爱劳动、热诚和爱情的重要手段

### sk-1264　班里的后进生

- 旧标签：learning-difficulties, child-study, teacher-growth
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 14.50 + 先验 1.0 = 15.50））
- 其他命中：劳动与创造（14.2） · 自然与思维课（10.7）
- 转述：这一篇最容易被读成一句“不放弃后进生”的口号，其实苏霍姆林斯基留下的是一套可以照着做的多通道方案。他的出发点是一个诊断：这些学生“不会在记忆的同时进行思考”，所以单纯“操练”记忆力、逼他们死记硬背是行不通的，那只会让神经系统和整个机体疲惫至极，记忆力反而更差。因此他没有把希望押在药物或记忆术上，而是把帮助拆成几条同时进
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 64 篇“班里的后进生”

### sk-1265　教会学生学习

- 旧标签：learning-difficulties, reading-and-books, teacher-growth
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 17.24 + 先验 2.5 = 19.74））
- 其他命中：学习困难学生（17.1） · 健康与作息（10.7）
- 转述：这一篇把给学习困难学生配读物的事，直接比作医生给虚弱病人配饮食：不能上大鱼大肉，也不能让他饿着，要讲配给与吸收。苏霍姆林斯基的判断是——学习能力越低、掌握基础知识越吃力，独立阅读就越重要，而且个别工作“应当从独立阅读开始”；如果教师培养不出学生认真思索书中内容的能力，任何逼他死记硬背的企图都不会有效果。配什么读物这件事
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 46 篇“教会学生学习”

### sk-1266　负担过重揭秘

- 旧标签：learning-difficulties, health-first, teacher-growth
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 10.81 + 先验 1.0 = 11.81））
- 其他命中：劳动与创造（5.3） · 全面发展与个性（5.2）
- 转述：这一篇给“减负”提供了一个可操作的判别标准：先把知识分成两类。第一类是对概括化真理（规则、定义、从属关系）的经常性记忆，需要专门下功夫；第二类是对“作为概括性真理之源的规律性”的认识，靠理解因果与关系获得。两类相互联系，但要求不同的智力活动——把第二类当第一类去背，就是负担过重的真正根源，而且会挤掉那些真正必须牢固记忆
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 20 篇“负担过重揭秘”

### sk-1267　公民的起点

- 旧标签：love-education, collective-education, teacher-growth
- 建议：**A2 公民与祖国**（旧标签先验 + 文本证据（关键词 9.39 + 先验 1.0 = 10.39））
- 其他命中：评价与分数（8.9） · 尊严、爱与信任（4.8）
- 转述：这一篇给出的是一条时机判断：当分数成了衡量人的标准和尺度，“人在分数后面消失了”，后果首先不是排名难看，而是成绩下降和对学习的冷淡。苏霍姆林斯基并不主张把成绩不好的学生当做好学生，也不赞赏懒汉，他要根除的是闲散和懒惰——但他指出的出路是：如果能唤醒沉睡的才能，让一个“自己对自己摆手”的学生哪怕在一门功课上成为优秀生，教
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 36 篇“公民的起点”

### sk-1268　行为训练是自觉纪律教育的一种方法

- 旧标签：collective-education, teacher-growth, love-education
- 建议：**A16 评价与分数**（文本证据推翻旧标签（关键词 16.10，压过旧标签项 9.34））
- 其他命中：自我教育（8.2） · 集体与同伴（6.8）
- 转述：本篇把“纪律要求”转写成一套可复制的操作：先由教师确定训练的任务与内容，再把任务提出来，使每个学生感到这不是强加给他的，而是集体自愿为整个集体接受的。任务必须触及全班利益、与学习活动直接相关（如“没有正当理由决不缺课”“课后无人监督自动留下补课”“不提示、不抄袭”），并且要用克服困难的过程本身去鼓舞集体——这个克服困难
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 2 篇“行为训练是自觉纪律教育的一种方法”

### sk-1269　怎样爱学生

- 旧标签：love-education, teacher-growth, child-study
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 11.39 + 先验 1.0 = 12.39））
- 其他命中：劳动与创造（5.4） · 尊严、爱与信任（4.9）
- 转述：本篇把“爱学生”从情感宣言落成一套可操作的技术。前提是区分两种爱：本能的爱缺乏生活哲理，有时会给儿童带来很大害处；保护性教育依靠的是理智的人道的爱——它因对人性的深刻认识和对个性一切长短的深刻理解而充满崇高精神，能防止非理性行为并激励诚实和高尚行为。它要求集中心灵的全副力量并始终不渝地奉献出来。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 27 篇“怎样爱学生”

### sk-1270　情感教育

- 旧标签：love-education, aesthetic-nature-education, child-study
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 22.47 + 先验 1.0 = 23.47））
- 其他命中：劳动与创造（5.3） · 健康与作息（4.3）
- 转述：本篇提供的是一条情感教育方法：被压抑的情感不能靠讲道理解除，必须靠通道把它重新引出来。萨穆伊尔式的冷漠不是性格，而是“以牺牲感情为代价”换来的——压抑自己的感情、扭曲自己的理智，最终会发展到对一切都漠不关心。因此工作目标不是纠正表面行为，而是恢复他被压住的乐观与顽皮。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 16 篇“情感教育”

### sk-1271　关于教育道德的一封信

- 旧标签：teacher-growth, love-education, child-study
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 8.71 + 先验 1.0 = 9.71））
- 其他命中：检查知识与考查（6.0） · 尊严、爱与信任（4.7）
- 转述：这封信把“教育道德”落成一份可以逐项自问的清单。阿纳托利的悲剧不是突然发生的：马刀折裂被女教师嘲笑、爷爷去世三天没来上学却被质问“你为什么不会”、总结性听写得 2 分后批语“不思努力”并要求拿回家给母亲签名、作业本被埋进菜园、节日朗诵被临时撤下、图书馆彩画丢失被指认为他撕的、被安排与爱嘲弄人的女生同桌。每一件单看都是“
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 65 篇“关于教育道德的一封信”

### sk-1272　德育中的教师语言

- 旧标签：teacher-growth, love-education, collective-education
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 14.09 + 先验 2.5 = 16.59））
- 其他命中：评价与分数（10.2） · 了解儿童（7.1）
- 转述：苏霍姆林斯基把教师语言当成可训练的能力，而不是天生口才。这段文字给出了三条训练路径。第一条是“目的扩容”：不文明的教师跟学生打交道只带两三种目的——禁止、允许、责备；教育行家则带着许多目的，最常见的一项是阐明道德真理、概念、规范。第二条是“词库换挡”：做道德评价时不靠特意挑选的尖刻“强硬”词语，而先用普通词语的情感色彩
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 30 篇“德育中的教师语言”

### sk-1273　开发出每个学生独特的人格之美

- 旧标签：child-study, love-education, labor-education
- 建议：**A12 自然与思维课**（文本证据推翻旧标签（关键词 11.01，压过旧标签项 9.67））
- 其他命中：思维与智力（7.8） · 了解儿童（7.2）
- 转述：观察什么：不看孩子在课堂上的读写反应，而看他在自然与劳动现场的行为。巴甫利克在教室里被判定“思维迟钝”“对自然景物和自然现象都无动于衷”，到了田野和树林里却完全变成另一个人——他讲自己观察到的动植物现象时，能“第一眼就发现事物与现象之间的无形联系”。另一类同等重要的信号是手：自然课老师说他的智慧“在手指尖上”，即动手的
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 8 篇“开发出每个学生独特的人格之美”

### sk-1274　发展学生的个人能力与爱好

- 旧标签：child-study, labor-education, collective-education
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 7.93 + 先验 2.5 = 10.43））
- 其他命中：了解儿童（3.8） · 集体与同伴（3.7）
- 转述：编组原则：劳动组织的形成基础是“对某项劳动的共同兴趣”，学生自愿结合，规模控制在 3~12 人，帕夫雷什学校每年不少于 70 个这样的组或队。最具教育效能的不是同水平分组，而是成员劳动技能水平参差不齐的混合组织——能力强的和能力弱的人在同一个组里，才既有带教也有追赶。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 11 篇“发展学生的个人能力与爱好”

### sk-1275　我们的职责是培养人

- 旧标签：child-study, health-first, family-school
- 建议：**A7 健康与作息**（旧标签先验 + 文本证据（关键词 8.42 + 先验 2.5 = 10.92））
- 其他命中：思维与智力（7.5） · 学习困难学生（5.7）
- 转述：阶段一，先解决身体。对沃洛佳这类被判定“最无望”的孩子，第一步不是补课，而是改善生活条件：吃好、多呼吸新鲜空气、多晒太阳、在大自然中积极活动。这一阶段的观察指标是外显且可记的——脸色红润、脸颊饱满，说明“脑细胞也开始变得更有生机了”。但作者立刻划出边界：这还远远不够，身体健康只是前提，不能停在“吃好睡好”上。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 18 篇“我们的职责是培养人”

### sk-1279　学校与大自然

- 旧标签：aesthetic-nature-education, thinking-and-nature, health-first
- 建议：**A12 自然与思维课**（旧标签先验 + 文本证据（关键词 30.29 + 先验 1.0 = 31.29））
- 其他命中：集体与同伴（6.8） · 健康与作息（6.4）
- 转述：这是一份可排进校历的全年自然观察与劳动安排。载体是“思维课”——在大自然中讲授的独特课程，每堂课只针对一个要观察的具体事物或现象定题目，目的是让儿童形成整体印象。题目清单本身就是任务表，且随季节分布：春有“大自然从睡梦中醒来”“田野和草原上迎春开放的第一批鲜花”“春天的森林在复苏”“云雀的鸣叫声”；夏有“清晨蜜蜂起床后
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 59 篇“学校与大自然”

### sk-1280　您家的氛围

- 旧标签：family-school, love-education, collective-education
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 13.63 + 先验 2.5 = 16.13））
- 其他命中：幸福与精神生活（10.1） · 美与艺术（4.7）
- 转述：苏霍姆林斯基把家庭称作社会的“基木细胞”，同时给出一个不靠物质条件的判断标准：家庭能不能成为教育力量，不取决于房子、园子、葡萄园，而取决于父母是否抱着崇高的目的、并且让孩子看到自己正是在为这个目的奋斗。孩子对“人的世界”的认识从父母开始，家里日常关系的样子，就是孩子最早接受的道德课。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 43 篇“您家的氛围”

### sk-1281　致年轻父亲的信

- 旧标签：family-school, love-education, child-study
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 10.40 + 先验 1.0 = 11.40））
- 其他命中：家庭与母亲（7.6） · 评价与分数（4.8）
- 转述：这封信从一位年轻父亲的具体困惑开始：孩子为一件缝制的夹克使性子、穿着泥靴子进房间，还对打扫的阿姨说“这种活是给您钱的”。苏霍姆林斯基没有先批评孩子，而是把问题定位在“愿望的管理”上——需要是生活的动力，从需要产生愿望；育人的全部实质，正在于使个人的愿望与集体、社会、人民的利益相协调，从孩子意识生活的最初时日起就进行“愿
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 48 篇“致年轻父亲的信”

### sk-1282　劳动·志向·幸福

- 旧标签：labor-education, child-study, love-education
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 15.39 + 先验 2.5 = 17.89））
- 其他命中：评价与分数（4.8） · 全面发展与个性（4.4）
- 转述：苏霍姆林斯基把“志向”当成可以操作的教育对象：志向不是天生的，天生只给出一个大致的活动范围；具体在哪个范围内找到位置、发展什么能力，取决于天赋与实际工作如何接上，中间要有一座“桥梁”。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 15 篇“劳动·志向·幸福”

### sk-1283　义务感的培养

- 旧标签：love-education, family-school, collective-education
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 8.65 + 先验 2.5 = 11.15））
- 其他命中：劳动与创造（10.0） · 幸福与精神生活（9.7）
- 转述：苏霍姆林斯基把“我应当”看作要建起来的东西，而不是要喊出来的东西。他强调“楼房”要坚实就得有牢固的基础：基础是人在义务中的表现，是在与他人和集体的关系中通过履行义务而得到的自我确认；对待“应当”，应当像对待自我要求和良心的嘱咐一样。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 50 篇“义务感的培养”

### sk-1284　学习兴趣是学生学习活动的重要动力

- 旧标签：learning-difficulties, teacher-growth, child-study
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 8.42 + 先验 2.5 = 10.92））
- 其他命中：学习困难学生（17.2） · 评价与分数（8.9）
- 转述：兴趣不是等来的，而是被“成功预感”点出来的。苏霍姆林斯基把培养学习愿望的位置定在“教师能否正确组织学生的学习活动”上，而不是谈话、开会之类的特别措施。于是第一件可操作的事发生在备课桌上：备课时就要深入思考学生克服学习困难的途径，任何情况下都不回避这些困难，而要引导学生想办法克服困难——“虽说有困难，但却有获胜的办法”。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 1 篇“学习兴趣是学生学习活动的重要动力”

### sk-1285　脑力劳动及学校与生活的联系

- 旧标签：labor-education, thinking-and-nature, teacher-growth
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 11.20 + 先验 2.5 = 13.70））
- 其他命中：自然与思维课（11.0） · 全面发展与个性（5.1）
- 转述：“动手”本身不产生智力，让动手包含思维的关键，是把注意力按到“并非第一眼就能看出来的关系”上。苏霍姆林斯基把这件事定为有经验教师的重要任务：孩子们对种子在干燥粮仓里放十年不发芽、一旦进了温暖潮湿的土壤就发芽结出数百粒新种子这类现象早已司空见惯，正是这些平凡问题的产生在促进他们发展智力。培养智力的艺术，恰恰在于让孩子认真
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 6 篇“脑力劳动及学校与生活的联系”

### sk-1286　社会与教师

- 旧标签：teacher-growth, collective-education, family-school
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 7.21 + 先验 2.5 = 9.71））
- 其他命中：习惯与纪律（4.9） · 评价与分数（4.8）
- 转述：教师专业成长在这篇里不是靠个人觉悟，而是靠几件可安排的制度性事情。第一件是校内研讨换内容。那位年轻数学教师带来变化之后，学校的新校长支持他的每个想法、经常找他征求意见；校务会议从此不再“耐着性了去听那些枯燥无味的报告”，改成具有创新色彩的学术讨论，讨论的是十分尖锐的实际问题——例如“怎样才能让学生在课堂上认真听讲”“学
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 10 篇“社会与教师”

### sk-1287　劳动是人全面发展的基础

- 旧标签：labor-education, child-study, love-education
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 9.90 + 先验 2.5 = 12.40））
- 其他命中：全面发展与个性（5.0） · 思维与智力（3.4）
- 转述：职业启蒙在这篇里的逻辑是“先广后深再扎根”，而不是先替孩子定职业。第一步是让孩子认识不同职业的实质：文中列举的劳动者包括钳工、安装工、车工、建筑工、饲养员、从事种植和园艺工作的人等，作者说他们“把劳动当成自己的本质需要，当成生活乐趣的重要源泉”，而根源是热爱、珍惜自己的事业、以自己的职业为荣，并且确信在自己的职业里既有
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 13 篇“劳动是人全面发展的基础”

### sk-1288　教师与孩子们

- 旧标签：teacher-growth, love-education, child-study
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 7.36 + 先验 1.0 = 8.36））
- 其他命中：幸福与精神生活（6.7） · 尊严、爱与信任（4.6）
- 转述：师德自省在这篇里由一次退休告别逼出来。一位教了35年数学的老教师，在同事们为他送行时哭着说出真话：“我从来也没有爱过孩子”，每次走向教室心情都很沉重，甚至想写调动申请；直到最后一个年头他才懂得“孩子们是最明智的哲学家和最敏锐的心理学家”，他们感到他走进教室就像掉进冰窟窿里。要自省的第一问就来自这里：把“学生为什么不喜欢
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 17 篇“教师与孩子们”

### sk-1289　教育与自我教育

- 旧标签：love-education, child-study, health-first
- 建议：**A4 自我教育**（文本证据推翻旧标签（关键词 40.23，压过旧标签项 4.99））
- 其他命中：评价与分数（4.8） · 全面发展与个性（4.4）
- 转述：自我教育不是一句态度，而是一条有次序的机制：自我认识—自我要求—自我控制，并且每一步都有明确的触发条件。起点是自我认识。作者引古语“战胜自己是最难的胜利”，说“认识自己便山此开始，自我教育也由此开始”。而自我认识不是凭空反省出来的，它来自“成功地克服自身弱点的欢悦”——一个人在童年体验过这种欢悦，才会开始以批判的目光看
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 21 篇“教育与自我教育”

### sk-1290　要善于表扬好人好事

- 旧标签：love-education, collective-education, teacher-growth
- 建议：**A16 评价与分数**（文本证据推翻旧标签（关键词 10.26，压过旧标签项 7.14））
- 其他命中：习惯与纪律（7.1） · 道德判断与品德培养（5.4）
- 转述：“怎样表扬才对”这篇给的第一条是看对象：被表扬的“好人好事”是孩子真做的事，还是孩子为了被表扬而做的事。文中那所学校里，有学生做好事只是希望得到表扬；作者判断，如果不是没完没了地在墙报上报道沃洛佳和他的“铁木儿小队”、不给他们颁发荣誉证书，要让沃洛佳帮助别人，“他兴许连一根小指头儿也不愿动弹”。表扬一旦变成常规化的公开
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 26 篇“要善于表扬好人好事”

### sk-1291　一块面包

- 旧标签：love-education, labor-education, family-school
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 9.90 + 先验 2.5 = 12.40））
- 其他命中：幸福与精神生活（11.1） · 尊严、爱与信任（8.5）
- 转述：《一块面包》从牧人伊万·斯捷潘诺维奇送来的一块干面包讲起：他的孙子用面包打梨，被揪住耳朵后流泪，却不是因为羞愧而是因为疼痛，跑开以后又笑了起来。老人追问：这样的孩子能成为真正的公民吗？苏霍姆林斯基由此把公民教育从宏大口号拉回到日常——对一块面包、对他人劳动的态度，就是公民感的起点。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 28 篇“一块面包”

### sk-1292　既要见树木，也要见森林

- 旧标签：reading-and-books, thinking-and-nature, teacher-growth
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 11.06 + 先验 2.5 = 13.56））
- 其他命中：思维与智力（7.5） · 自然与思维课（5.2）
- 转述：学生负担重的根源，苏霍姆林斯基不认为在大纲内容多，而在背记占比过高、课外阅读与思考太少。他给出一条可检验的规律：需要背记的信息在材料总量中占的比重越大、出于兴趣和认知需要所读的材料越小，学习就越艰难。要减轻八年级的负担，用于自我陶冶的读书时间应比背记功课的时间多两倍，九、十年级多3\~4倍；为此还要留出闲暇——学生每天
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 31 篇“既要见树木，也要见森林”

### sk-1293　没有信任便没有教育

- 旧标签：teacher-growth, love-education, child-study
- 建议：**A10 教师**（旧标签先验 + 文本证据（关键词 7.21 + 先验 2.5 = 9.71））
- 其他命中：幸福与精神生活（6.8） · 习惯与纪律（4.8）
- 转述：这篇文章回应一封学生来信：校长和班主任禁止16岁的男女学生去旅游，先允许后自食其言。苏霍姆林斯基指出这类“禁令”有三重后果——把16岁的人变成娃娃，让他们仍感到自己是软弱无力的孩子；把学生推向心灵锁闭、不说真话、不坦诚相见的境地；把纯属青少年个人生活的事情也纳入允许或禁止，使精神生活的范围缩小、变得贫乏。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 32 篇“没有信任便没有教育”

### sk-1295　我的教育信念

- 旧标签：love-education, collective-education, child-study
- 建议：**A9 集体与同伴**（旧标签先验 + 文本证据（关键词 6.84 + 先验 2.5 = 9.34））
- 其他命中：劳动与创造（7.8） · 幸福与精神生活（7.0）
- 转述：《我的教育信念》从“石头人”故事讲起：一位庄员为独子早早盖好石头房子、石头棚子、石头狗窝，孩子长大后对邻居的火灾、他人的苦难一概不问。作者由此提出，教育的实质是在每个人心灵里确立真正神圣的东西；而信念若不落成活动，就只是口号。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 40 篇“我的教育信念”

### sk-1296　父母教育学

- 旧标签：family-school, love-education, child-study
- 建议：**A8 家庭与母亲**（旧标签先验 + 文本证据（关键词 7.64 + 先验 2.5 = 10.14））
- 其他命中：劳动与创造（10.0） · 幸福与精神生活（6.7）
- 转述：《父母教育学》面对的是家长反复提出的问题：究竟该怎样教育孩子、怎样把父母的爱护和严格要求协调起来。苏霍姆林斯基先给出一个判断：人是世界一切财富中至尊至贵的财富；没有教养、没有道德、一无所能的人，如同驾驶着发动机损坏的飞机升空，既害自己也害别人。所以学校请家长来校，一定要请假来。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 42 篇“父母教育学”

### sk-1297　人是最巨大的财富

- 旧标签：love-education, child-study, collective-education
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 11.50 + 先验 1.0 = 12.50））
- 其他命中：尊严、爱与信任（9.7） · 习惯与纪律（5.8）
- 转述：全卷篇幅最大的这篇文章，用马林娜妈妈、科利亚、托利亚、米佳、费佳等一系列真实命运，回答一个问题：怎样把“人是世界上最巨大的财富”变成可操作的教育路径。第一条是给人指出通往幸福之路：幸福的反面是苦难，一个人的痛苦、悲哀、屈辱、不安和孤独若无人理睬、无人分担，教育就会化为乌有；而一旦他为自己获得了幸福、品尝到幸福的滋味，就
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 49 篇“人是最巨大的财富”

### sk-1298　强有力的教育手段

- 旧标签：reading-and-books, love-education, aesthetic-nature-education
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 15.63 + 先验 2.5 = 18.13））
- 其他命中：幸福与精神生活（10.1） · 美与艺术（8.7）
- 转述：苏霍姆林斯基把文学教育当作一套可操作的安排，而不是一句情感口号。他给出的前提很具体：能否让阅读成为教育的主导力量，取决于“如何学习文学读物”以及“课外阅读和课内阅读的关系处理得如何”。他还划出一条检测红线——文学知识不同于数学知识，检测方式也必须不同，否则就会出现文学课得 5 分、毕业后五年不读一本文艺作品的人。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 52 篇“强有力的教育手段”

### sk-1299　今日的小学生

- 旧标签：reading-and-books, child-study, family-school
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 20.17 + 先验 1.0 = 21.17））
- 其他命中：阅读与书籍（15.6） · 了解儿童（6.6）
- 转述：这一篇给出的不是“要多读书”的口号，而是一套让书在孩子心里压过屏幕的操作。第一条是教师自身的读书状态：教师要用童心未泯的好奇心、永不满足的求知欲和作为思想者的自豪感去感染学生——孩子是被一个正在读书、正在惊奇的大人带进书里的，不是被规定带进去的。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 54 篇“今日的小学生”

### sk-1300　大自然、劳动和世界观

- 旧标签：aesthetic-nature-education, labor-education, thinking-and-nature
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 16.99 + 先验 2.5 = 19.49））
- 其他命中：思维与智力（7.5） · 全面发展与个性（5.1）
- 转述：这一篇的可操作内核，是把“人与自然是一个整体”这样一个世界观，落成一年四季都能排进课表的自然劳动课。第一步是设置固定的自然观察场合：旅游、参观、麦田边的日常观察都算课，教师在这些场合里不讲抽象道理，而是用水塘淤塞、草场被“憋死”、沃土流失露出黏土这类真实案例，让学生自己生出公民的忧患感——“不应如此”这句话，就是儿童初
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 60 篇“大自然、劳动和世界观”

### sk-1301　“应该劳动”、“劳动艰苦”和“劳动美好”三个因素的和谐统一

- 旧标签：labor-education, love-education, child-study
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 11.99 + 先验 1.0 = 12.99））
- 其他命中：劳动与创造（7.8） · 阅读与书籍（6.8）
- 转述：这一篇把劳动教育的排课问题讲得最实：三因素的和谐统一不能靠“硬性规定的组织形式”实现，校办工厂、教学生产队只是劳动教育的一个方面，光把它们建起来并不等于劳动教育落地。真正的起点在课堂——学习本身才是学生头等的劳动，思维、认识世界、探求真理、获取知识并由此形成观点和信念，都是这种劳动的内容；最大的危险不是学生不打扫教室，
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 62 篇“‘应该劳动’、‘劳动艰苦’和‘劳动美好’ 三个因素的和谐统一”

### sk-1302　心灵的劳动

- 旧标签：teacher-growth, love-education, family-school
- 建议：**A4 自我教育**（旧标签先验 + 文本证据（关键词 10.58 + 先验 1.0 = 11.58））
- 其他命中：劳动与创造（7.0） · 健康与作息（4.8）
- 转述：“心灵的劳动”在这篇里不是比喻，而是一套可以布置的安排。第一层安排是环境：校门入口种玫瑰这样秀美娇嫩的东西，并且要关心让学生周围这类东西尽可能多一些。理由很直接——若学生四周全是钢筋水泥般坚不可摧的东西，根本用不着心灵的劳动；只有当每天多次从盛开的玫瑰前走过，需要克制“掐一朵、甚至只是摸一摸”的诱惑时，道德力量才有被锻
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 66 篇“心灵的劳动”

### sk-1303　别让心灵锈斑斑

- 旧标签：family-school, love-education, labor-education
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 12.47 + 先验 2.5 = 14.97））
- 其他命中：幸福与精神生活（6.4） · 家庭与母亲（4.1）
- 转述：这一篇回答的是“怎样让生活艰苦些而不流于说教”，答案是把艰苦做成孩子亲身参与、有起点也有节庆的长期工程。第一步是原则上的分寸：不必人为制造艰苦，只需善于看到生活中真实存在的艰苦、不绕道而过，并坚忍承受。苏霍姆林斯基反复强调“人珍重的只能是他注入自己心血的东西”，所以艰苦必须是孩子自己付出的心血，而不是家长口头宣布的规矩
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 12 篇“别让心灵锈斑斑”

### sk-1304　谈语言的教育作用

- 旧标签：teacher-growth, love-education, collective-education
- 建议：**A15 思维与智力**（文本证据推翻旧标签（关键词 11.50，压过旧标签项 10.92））
- 其他命中：教师（8.4） · 幸福与精神生活（6.3）
- 转述：这篇《谈语言的教育作用》针对的是一种流行的轻视：有人说教师的语言在教育手段中只占第二位，首位的应是活动与劳动，于是“语言教育”被当作收效不明显的事，谈话前的准备也就被省掉了。苏霍姆林斯基反驳说，行为与劳动固然重要，但决定它们的正是人的内心活动，而语言是影响内心活动的重要手段；因此谈话不是随便聊聊，而是要和学生的智慧与心
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 14 篇“谈语言的教育作用”

### sk-1305　人民教师

- 旧标签：teacher-growth, collective-education, love-education
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 15.63 + 先验 1.0 = 16.63））
- 其他命中：自我教育（6.4） · 幸福与精神生活（6.3）
- 转述：《人民教师》通篇讲的是教师这个身份到底意味着什么，但其中有一层很实在的日常操作含义：教师的自我要求不是抽象的道德口号，而是几件天天要做的事。苏霍姆林斯基把它概括为“两项重任”——一是给学生一定的知识储备，二是教学生终身自己补充和丰富知识、独立运用人类文化成果的本领。他直言第一项任务学校和社会都重视，第二项却很少有人认真
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 22 篇“人民教师”

### sk-1306　休怕成为慈爱的人

- 旧标签：love-education, teacher-growth, child-study
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 10.28 + 先验 1.0 = 11.28））
- 其他命中：美与艺术（4.5） · 思维与智力（4.0）
- 转述：这篇《休怕成为慈爱的人》以少年谢尔盖的自述开头，但真正给教师留下的是一套关于“慈爱语言分寸”的操作方法。苏霍姆林斯基先划清两头：慈爱不是娇纵，不是娃娃腔的咿呀之语，也不是轻率满足闲得难受的儿童随心所欲的要求——姑息任性同样会使心变得俗不可耐，因为被娇宠的孩子只看得见自己，成了以个人天地为宇宙中心的利己主义者。所以慈爱的
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 35 篇“休怕成为慈爱的人”

### sk-1307　致女儿的信

- 旧标签：family-school, child-study, love-education
- 建议：**A6 了解儿童**（旧标签先验 + 文本证据（关键词 3.37 + 先验 2.5 = 5.87））
- 其他命中：习惯与纪律（5.0） · 集体与同伴（3.7）
- 转述：这封信是写给即将实习的女儿的，但季姆科那一段本身是一份很具体的观察示范。前一位女教师知道季姆科在课间讲童话、把同学聚在身边，就向这份天赋“宣战”：禁止、停学、压制，结果孩子变得愁眉苦脸、怀恨在心，最后把两个小同学的芦笛扔进了火堆。苏霍姆林斯基接手后，观察的第一个动作不是处理纪律，而是走近看：他悄悄走到季姆科跟前，看到的
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 38 篇“致女儿的信”

### sk-1308　寄语后来人

- 旧标签：teacher-growth, love-education, child-study
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 14.68 + 先验 2.5 = 17.18））
- 其他命中：幸福与精神生活（10.2） · 评价与分数（8.9）
- 转述：《寄语后来人》是苏霍姆林斯基写给年轻教师的“教育遗嘱”。这一段把“保护儿童的信赖”从一句态度宣言落成可操作的要求：先承认儿童是脆弱、没有自卫力的，教师面对的是一碰就会受损的心灵，而不是等待灌输知识的容器；教学不是“把知识从一个头脑搬入另一个头脑”，而是每时每刻的心灵接触。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 41 篇“寄语后来人”

### sk-1309　致父亲们的话

- 旧标签：family-school, love-education, child-study
- 建议：**A2 公民与祖国**（旧标签先验 + 文本证据（关键词 7.14 + 先验 1.0 = 8.14））
- 其他命中：幸福与精神生活（6.4） · 劳动与创造（5.3）
- 转述：《致父亲们的话》把父亲的教育作用拆成两件可执行的事。第一件是让父辈的功劳与孩子自己的根分开：父辈的荣誉不能变成儿女坐享清福的资本，孩子必须有自己的发光点；而点燃这个发光点的办法，是父亲用自己的劳动与忠于理想的实际行动去示范，而不是拿功劳去要求孩子听话。具体的操作是让孩子“在自己的父辈身上发现和认清永不消逝的特点——为创
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 53 篇“致父亲们的话”

### sk-1310　我们在儿童身上延续自己

- 旧标签：family-school, love-education, labor-education
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 10.77 + 先验 2.5 = 13.27））
- 其他命中：家庭与母亲（9.4） · 检查知识与考查（5.1）
- 转述：《我们在儿童身上延续自己》把“家庭怎么安排”讲得很具体。第一件事是让孩子进入真实的共同劳动：小奥莉娅总说“我俩在干活呐”“我俩累了”，她在与奶奶一起做家务中认识世界、认识他人，并由此形成道德标准——自幼爱憎分明，对游手好闲、懒懒散散嫉恶如仇。所以家庭安排的要点不是给孩子安排课程，而是给他一个可以“我俩一起”的真实劳动位
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 63 篇“我们在儿童身上延续自己”

### sk-1311　纯洁与高尚

- 旧标签：teacher-growth, family-school, love-education
- 建议：**A2 公民与祖国**（旧标签先验 + 文本证据（关键词 9.39 + 先验 1.0 = 10.39））
- 其他命中：评价与分数（4.8） · 全面发展与个性（4.4）
- 转述：《纯洁与高尚》给家长和教师提供的是两条可操作的道德要求。第一条是：不能过双重生活。人的道德“自我”不可分割，一个人在私人小天地里阴暗肮脏，就不可能在公共生活中真正高尚；工程师安德烈在集会上慷慨陈词要远赴他国支援，却在女友怀孕时想逃避责任，公众由此看清他的“高昂激情”下藏着什么。因此评价一个人——也包括教师评价自己——不
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 67 篇“纯洁与高尚”

### sk-1313　怎样激发学生在道德方面进行自我教育

- 旧标签：love-education, collective-education, child-study
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 14.09 + 先验 2.5 = 16.59））
- 其他命中：自我教育（4.3） · 公民与祖国（3.9）
- 转述：这一篇给出的是道德自我教育可落地的一套安排，而不是一句号召。首先是要求本身要具体、可检查：要教导学生在道德问题上严格要求自己、做到一丝不苟，要教导他们约束自己；作者举的例子是学校教师集体经过多年努力制定的“道德修养的自我教育提纲”，用编号条目把学生在同他人道德关系中应当遵守的要求逐条写出来——祖国、独处时的良心、对人的
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 84. 怎样激发学生在道德方面进行自我教育

### sk-1315　青年对待爱情的精神准备应当包括些什么

- 旧标签：love-education, family-school, child-study
- 建议：**A11 劳动与创造**（文本证据推翻旧标签（关键词 7.57，压过旧标签项 6.76））
- 其他命中：自我教育（6.2） · 集体与同伴（5.4）
- 转述：苏霍姆林斯基给青年谈爱情，是从一张自查清单开始的，而不是从道德训诫开始：建立家庭之前，先问自己能不能成为忠诚的人、身上有没有懒惰自私冷酷无情、能不能控制自己的欲望、对家庭的物质保证有没有准备（因为妻子可能长期不工作、要教养孩子）。接着是征询父母意见——他们的生活智慧能帮助青年迈好这一步，而家庭生活的意义和目的就是教育子
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》50. 青年对待爱情的精神准备应当包括些什么

### sk-1316　怎样教学生们成为好子女

- 旧标签：family-school, love-education, child-study
- 建议：**A7 健康与作息**（文本证据推翻旧标签（关键词 10.22，压过旧标签项 10.14））
- 其他命中：家庭与母亲（7.6） · 阅读与书籍（7.4）
- 转述：这一篇把“教学生成为好子女”落到学校与家庭的具体安排上。第一条安排是改掉“叫家长”的默认做法：尽可能少请家长到学校来对孩子进行道德训斥、用父亲的“强硬手腕”吓唬儿子，而应尽可能多地让孩子同父母在精神上交往，这种交往能给母亲和父亲带来欢乐。第二条安排是把“给家庭带来欢乐”当成办学的支点——作者说初年级正是依靠这一点办学而
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》21. 怎样教学生们成为好子女

### sk-1317　教材的首次学习

- 旧标签：learning-difficulties, teacher-growth, assessment-grading
- 建议：**A16 评价与分数**（旧标签先验 + 文本证据（关键词 4.16 + 先验 2.5 = 6.66））
- 其他命中：学习困难学生（4.9） · 集体与同伴（3.7）
- 转述：苏霍姆林斯基把“教材的首次学习”当作可操作的一节课来设计：首次学习是从不知到知、从表面到实质的第一步，这一步走偏，后面再补也吃力。他的做法不是讲得更多，而是把首次学习课变成一节“能看见每个学生脑子在干什么”的课。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 14. 教材的首次学习

### sk-1318　技能和知识之间不可比例失调

- 旧标签：learning-difficulties, reading-and-books, teacher-growth
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 12.67 + 先验 2.5 = 15.17））
- 其他命中：思维与智力（3.3） · 教师（2.4）
- 转述：这一条把“技能”当成学习的工具来检查，而不是当成知识之外的附属品。苏霍姆林斯基提出三项必须达到自动化的工具性技能，并各给了一个可操作的检查或训练办法。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 24. 技能和知识之间不可比例失调

### sk-1321　学习之母不应变成后娘

- 旧标签：learning-difficulties, assessment-grading, teacher-growth
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 7.51 + 先验 1.0 = 8.51））
- 其他命中：劳动与创造（7.9） · 检查知识与考查（6.2）
- 转述：“复习是学习之母”在实际教学中常变成后娘：学生被迫在一两天内做完几个星期做过的事，事实与结论压顶而来，脑子里乱成一团，还要同时应付其他功课，结果精疲力竭、伤了身体。苏霍姆林斯基的对策不是少复习，而是按学科性质把复习改造成几种具体的作业形式——这就是综合复习法。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 18. 学习之母不应变成后娘

### sk-1323　怎样在日常活动过程中防止神经衰弱

- 旧标签：health-first, teacher-growth, child-study
- 建议：**A7 健康与作息**（旧标签先验 + 文本证据（关键词 14.36 + 先验 2.5 = 16.86））
- 其他命中：尊严、爱与信任（13.8） · 幸福与精神生活（10.0）
- 转述：这一条把教师的神经衰弱写成一条可以追踪的链条，而不是一句“工作压力大”。起点是只会从儿童交往中收获伤心、愤怒、生气，根源是不理解儿童世界——儿童首先是用情感认识周围世界的，教师若只听到不愉快的曲调，就会破坏自己内部器官的工作，出现神经失调，其中最可怕的一种是神经衰弱。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 3. 怎样在日常活动过程中防止神经衰弱

### sk-1327　要善意待人

- 旧标签：love-education, teacher-growth, child-study
- 建议：**A19 道德判断与品德培养**（文本证据推翻旧标签（关键词 9.44，压过旧标签项 8.90））
- 其他命中：评价与分数（8.9） · 集体与同伴（8.9）
- 转述：这一条讲的是善意的性质：它是相互的。苏霍姆林斯基先把善意从口号还原成一次自检——如果成绩不好、跟不上同班同学、甚至犯了流氓行为的是你自己的儿子，你会不会提出开除、减品行分数？理智或许会提醒你这些办法也是需要的，但心里首先冒出来的，一定是能挽救儿子、在他心里建立道德的纯洁和美的办法。这份心愿就是善意待人。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 4“要善意待人”

### sk-1328　作为教育者的教师应具备什么品质

- 旧标签：teacher-growth, reading-and-books, collective-education
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 6.83 + 先验 2.5 = 9.33））
- 其他命中：集体与同伴（5.2） · 全面发展与个性（4.4）
- 转述：这一条把“教师品质”落成一项可以自己动手做的工程：智力财富的自我建设。苏霍姆林斯基给出一个反直觉的标尺——只有把自己知识的1%用于课堂讲授就够了的教师，才是真正热爱自己学科的人。知识越丰富，教师对知识、科学、脑力劳动和智力生活的态度就表露得越鲜明，这种表露本身才是热爱。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 62“作为教育者的教师应具备什么品质”

### sk-1329　怎样培养孩子具有善意感

- 旧标签：love-education, family-school, child-study
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 17.18 + 先验 1.0 = 18.18））
- 其他命中：尊严、爱与信任（13.2） · 思维与智力（4.2）
- 转述：这一条把礼貌用语当作道德训练的具体内容，而不是礼仪表演。“您好”“祝您健康”里包含心与心沟通的最本质关系，见面不说就意味着严重的道德无知；“谢谢”意味着别人给你带来幸福、造就福利，问题不只是在该说的时候说出口，而在于心上感受、用心灵活动去报答人家的好意；“请”则包含对他人人格的尊敬，包括对其自主性、独立性和善良意愿的尊
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》37“怎样培养孩子具有善意感”

### sk-1330　怎样向青年们谈爱情

- 旧标签：love-education, family-school, child-study
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 4.26 + 先验 2.5 = 6.76））
- 其他命中：公民与祖国（4.0） · 家庭与母亲（3.5）
- 转述：这是一条关于“怎么谈”的方法建议。苏霍姆林斯基不从不许早恋谈起，而是从信箱谈起：许多姑娘和青年妇女的来信像被烧得通红的铁片，里面反复出现同一句话——“他爱我，但不尊重我……怎样做才能使他既爱我，又尊重我呢？”他从这个真实困境切入，因此谈话的对象不是抽象的“青少年”，而是具体的人正在经历的痛苦。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》51“怎样向青年们谈爱情”

### sk-1331　怎样才能使人成为有教养的人

- 旧标签：love-education, child-study, teacher-growth
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 13.97 + 先验 2.5 = 16.47））
- 其他命中：思维与智力（11.2） · 劳动与创造（9.9）
- 转述：这篇导言里，苏霍姆林斯基没有把“真正的人”写成一句口号，而是列出了一份可以逐条对照的理想形象清单。这份清单大致有六个方向：一是对生活的目的和意义有理解与感受，能向自己提出“我为什么而活着”并给出回答；二是精神世界、精神利益与精神需求丰富，是“具有和谐的、多方面精神生活的人”；三是肯定与否定和谐统一——既有深沉忠贞的爱，
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》导言 怎样才能使人成为有教养的人

### sk-1332　认识自己

- 旧标签：child-study, love-education, collective-education
- 建议：**A4 自我教育**（文本证据推翻旧标签（关键词 14.61，压过旧标签项 9.34））
- 其他命中：劳动与创造（7.0） · 集体与同伴（6.8）
- 转述：这一篇回答一位15岁读者的来信，但苏霍姆林斯基没有停在“自我教育靠意志力”这种空话上，而是给出了三个可以把“认识自己”设计成长期任务的实例。第一个是菲利普爷爷：92年、从没哪天不劳动，把一片蛮荒经营成“菲利普爷爷草地”。他的“认识自己”不是内省，而是在一块具体土地上几十年不间断的劳动中，一点点看清自己是谁。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 51 篇“认识自己”

### sk-1334　关于学校教育的思考

- 旧标签：family-school, love-education, teacher-growth
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 4.74 + 先验 2.5 = 7.24））
- 其他命中：幸福与精神生活（3.4） · 思维与智力（3.3）
- 转述：这一篇以一位年轻母亲的回访开篇：十年前她是班上抽签不准备也能考好历史的骄傲学生，如今带着小女儿来报名，却已经离婚。她说自己既不需要同情也不需要安慰，只对那些在青春时代教育过她的人“十分气恼”——“他们没有教会人怎样生活”。她明确否认原因是失望或性格不合，而是“我们简直不会生活，不会做妻子和丈夫”。
- 出处：《苏霍姆林斯基选集（五卷本）第5卷》（教育科学出版社），《论文集》第 39 篇“关于学校教育的思考”

### sk-1335　理解新教材是课堂教学的一个阶段

- 旧标签：learning-difficulties, teacher-growth, thinking-and-nature
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 7.47 + 先验 2.5 = 9.97））
- 其他命中：检查知识与考查（6.2） · 评价与分数（4.2）
- 转述：这条建议把“理解新教材”当成课堂上必须单独安排、有固定时长的操作阶段，而不是讲完就过的过渡。原文给出的操作要点有三组。第一是留出思考时间并让学生当场自我检查：讲完三角函数定义后，给时间让学生打开草稿本画直角三角形、记下讲解内容、复习定义、自己举例说明函数关系；随后做自我检查——能不能重讲一遍？很多人发现自己无法复述，于
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 15. 理解新教材是课堂教学的一个阶段

### sk-1336　怎样在体育方面引导学生进行自我教育

- 旧标签：health-first, child-study, love-education
- 建议：**A7 健康与作息**（旧标签先验 + 文本证据（关键词 20.68 + 先验 2.5 = 23.18））
- 其他命中：自然与思维课（14.0） · 劳动与创造（7.9）
- 转述：这一条把体育自我教育从“理念”变成一份可执行的日常安排，原文逐条列出了七项（本卡摘录第2～7项）。作息方面：要在日出之前起床，夏天比太阳起得更早，走到原野里去呼吸新鲜空气、用露水洗脸洗手；每天早晨一起来就做早操，夏天最好睡在院子里、睡在干草或刚脱粒的新鲜谷草上。锻炼方面：每天早晨用冷水擦身，尽量在池塘里洗澡直到秋天出现
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 87. 怎样在体育方面引导学生进行自我教育

### sk-1337　知识既是目的又是手段

- 旧标签：learning-difficulties, reading-and-books, teacher-growth
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 10.71 + 先验 1.0 = 11.71））
- 其他命中：幸福与精神生活（7.1） · 学习困难学生（5.7）
- 转述：苏霍姆林斯基把“知识不进入流通”看作学习困难的一个原因：知识被当成“为了储存”的货物，唯一的用途是回答教师的问题。要改变这一点，第一件事是改判“知道”的标准——知道就是会运用知识，而不是会复述。教师如果只以“能记住并按教师要求立即亮出来”作为有才能的标准，知识就必然与学生的精神生活和智力兴趣脱节，掌握知识反而变成希望尽
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 11. 知识既是目的又是手段

### sk-1338　教学生观察,教学生细看

- 旧标签：thinking-and-nature, learning-difficulties, child-study
- 建议：**A12 自然与思维课**（旧标签先验 + 文本证据（关键词 9.81 + 先验 1.0 = 10.81））
- 其他命中：美与艺术（10.4） · 思维与智力（7.5）
- 转述：训练观察的第一步是纠偏。有些学校只把观察当作“证实某些题材和章节的手段”，用完了就放下；而观察本身是积极的智力活动，是发展智力的途径，也是“知识的理解和记忆之母”。所以要真正教观察，先得把它从附属地位解放出来：给它独立的时间、独立的目的，而不是在需要举例时顺带看一眼。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 21. 教学生观察,教学生细看

### sk-1339　阅读是“困难”学生智力教育的重要手段

- 旧标签：reading-and-books, learning-difficulties, teacher-growth
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 6.83 + 先验 2.5 = 9.33））
- 其他命中：学习困难学生（12.2） · 思维与智力（7.5）
- 转述：这里说的“困难”学生，是领会、理解、记忆都慢的那一类：一项内容还没理解，下一项又该学了；一项背熟了，另一项又忘了。常见的应对办法是把他们的脑力劳动范围尽量缩小——教师对困难学生说“你只读教科书就行了，不要分散精力去读别的书”。苏霍姆林斯基判定这是完全错误的：学生的学习越困难，脑力劳动中遇到的困难越多，他就越需要多阅读；
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 23. 阅读是“困难”学生智力教育的重要手段

### sk-1341　关于学生的智力生活

- 旧标签：learning-difficulties, thinking-and-nature, teacher-growth
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 11.40 + 先验 1.0 = 12.40））
- 其他命中：评价与分数（8.9） · 集体与同伴（8.4）
- 转述：负担过重的根源被点得很清楚：如果教师考虑的只是怎样迫使学生更多地啃教科书、怎样把学生的注意力从其他一切活动上转移过来，那么负担过重就不可避免。也就是说，减负的第一个动作不是把作业量减几道题，而是改变教师的关注点——除上课、教科书、家庭作业、分数之外什么也不考虑的学校，其遭遇不会令人羡慕。学生除通常的学业、观念、兴趣之外
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 30. 关于学生的智力生活

### sk-1342　怎样研究学前儿童的思维

- 旧标签：child-study, thinking-and-nature, teacher-growth
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 14.52 + 先验 2.5 = 17.02））
- 其他命中：阅读与书籍（7.1） · 美与艺术（4.2）
- 转述：研究学前儿童思维的第一件事，是先承认两种思维类型客观存在：一种是逻辑分析思维（数学思维），一种是艺术思维（形象思维）。一年级教师的任务不是评判哪种更好，而是判断在每个儿童身上哪一种占优势，因为这对正确地指导学生的脑力劳动极为重要。教他们学会思考、发展思维意味着两件事同时做：一方面两种思维都要发展，不可有片面性；另一方面
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 39. 怎样研究学前儿童的思维

### sk-1343　关于对自己子女的教育问题

- 旧标签：family-school, teacher-growth, child-study
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 7.10 + 先验 1.0 = 8.10））
- 其他命中：尊严、爱与信任（4.3） · 自然与思维课（4.1）
- 转述：要避免“最会教育别人孩子的人却没时间教育自己孩子”这个矛盾，第一条是角色分离：在家里，对孩子的身份既不是老师，也不是班主任，而首先是父亲和母亲。所以不要把家庭变成小型的学校，尽可能别把学校的气氛带到家里去——这不过是为了让你们和孩子组成一个美满的家庭。教育不是某种特殊组织的、人为安排的“措施”，教育首先是一种生活方式。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 50. 关于对自己子女的教育问题

### sk-1344　谁在教育儿童，什么在教育儿童，在教育方面什么取决于教师，什么取决其他教育者

- 旧标签：family-school, teacher-growth, collective-education
- 建议：**A13 阅读与书籍**（旧标签先验 + 文本证据（关键词 7.44 + 先验 1.0 = 8.44））
- 其他命中：思维与智力（7.5） · 美与艺术（4.7）
- 转述：这一篇把参与教育的力量数清楚：家庭（其中最细致、最有才华的雕塑家是母亲）、教师、集体（儿童集体、少年集体、青年集体）、受教育者本人（自我教育）、书籍所构成的精神生活世界，以及完全意料之外的“雕塑家”（街上结交的少年、来做客一周的亲属或熟人）。儿童像一块大理石，同时有几把刀子在上面雕刻；教育之所以难，正因为在同一处地方会
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 51. 谁在教育儿童，什么在教育儿童，在教育方面什么取决于教师，什么取决其他教育者

### sk-1345　为使儿童愿意好好学习该做些什么

- 旧标签：assessment-grading, family-school, teacher-growth
- 建议：**A16 评价与分数**（旧标签先验 + 文本证据（关键词 14.36 + 先验 2.5 = 16.86））
- 其他命中：幸福与精神生活（11.3） · 学习困难学生（10.5）
- 转述：让孩子愿意学习的第一个做法，是把学习动机接到家庭情感上。儿童脑力劳动的人道化，在于他想给妈妈爸爸带来快乐；科利亚说“我应该好好学习，妈妈有心脏病”，他并不是被分数驱动，而是知道自己的劳动能让母亲安心。所以教师要珍惜、爱护和发展孩子作为劳动者的自豪感，让他看得见、体验得到自己的成绩，不能让他因为落后而陷入无穷的痛苦。孩子
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 56. 为使儿童愿意好好学习该做些什么

### sk-1347　怎样通过集体使个性全面发展

- 旧标签：collective-education, child-study, love-education
- 建议：**A14 美与艺术**（文本证据推翻旧标签（关键词 13.40，压过旧标签项 11.40））
- 其他命中：阅读与书籍（11.4） · 劳动与创造（10.7）
- 转述：这一篇的出发点是：人是一个不可分割的整体（道德的、智力的、情感的、审美的、创造的），而任何一个基层班集体在成员相互关系的组织上都有局限性，所以班集体不可能成为完成个性全面发展任务的唯一组织形式。要让每个人显出长处，就必须在班集体之外再搭出多种类型的集体。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 64. 怎样通过集体使个性全面发展

### sk-1348　青少年的思想是怎样成熟起来的

- 旧标签：collective-education, love-education, teacher-growth
- 建议：**A2 公民与祖国**（旧标签先验 + 文本证据（关键词 7.98 + 先验 1.0 = 8.98））
- 其他命中：思维与智力（8.2） · 幸福与精神生活（7.0）
- 转述：这一篇回答“怎样让青少年的思想成熟起来”，做法是让思想“操心”起来。前提判断是：童年和少年时代完全无忧无虑的生活，是产生精神幼稚病的根源；青少年在生活中应有所操心——为人民、社会和祖国操心和不安。让少年学会以一个公民的态度观察世界，是教育智慧的一个高峰，最主要的是让儿童关心社会，把社会的事情看成自己切身的事情。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 73. 青少年的思想是怎样成熟起来的

### sk-1349　在哪些条件下集体才能有效地发挥教育个人的作用

- 旧标签：collective-education, teacher-growth, child-study
- 建议：**A9 集体与同伴**（旧标签先验 + 文本证据（关键词 6.84 + 先验 2.5 = 9.34））
- 其他命中：劳动与创造（5.3） · 全面发展与个性（4.4）
- 转述：这一篇把前面许多建议汇总成“集体有效教育个人”的条件清单，共十三条。它的用法不是通读，而是逐条自查：哪些做到了、哪些没做到。清单前三条是基础——(1)每个人都应体会“人是在一起生活和劳动的”，以人道主义态度对待他，理解并体会他的精神世界和他此时此刻的情绪状态（苏霍姆林斯基称之为“对人的体会”）；(2)每个人要节制自己的
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 88. 在哪些条件下集体才能有效地发挥教育个人的作用

### sk-1350　在学校集体中什么可以讨论和什么不可以讨论

- 旧标签：collective-education, teacher-growth, love-education
- 建议：**A9 集体与同伴**（旧标签先验 + 文本证据（关键词 8.56 + 先验 2.5 = 11.06））
- 其他命中：家庭与母亲（7.6） · 习惯与纪律（5.0）
- 转述：这一篇给集体舆论划边界。结论很硬：并非与学生行为有关的一切都能提到学校集体中讨论。不可讨论的包括：因家庭中明显或隐蔽的不正常现象（家长的反社会行为、父母的口角、吵闹与不和）引起的不良行为；因生父或生母缺失而给孩子造成精神创伤后发生的行为——不管破坏纪律多严重，只要他没有父亲或母亲，就不应在集体中分析他的行为；因学生用行
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 89. 在学校集体中什么可以讨论和什么不可以讨论

### sk-1351　教师的权威是什么，应该表现在哪里

- 旧标签：teacher-growth, love-education, child-study
- 建议：**A4 自我教育**（旧标签先验 + 文本证据（关键词 10.58 + 先验 1.0 = 11.58））
- 其他命中：劳动与创造（10.0） · 尊严、爱与信任（4.6）
- 转述：这一节把教师权威定为一门可操作的技术活，而不是一种天赋或地位。苏霍姆林斯基用"手术刀"作比：它最要紧、最锐利，也最不安全——能做出最细致、几乎察觉不到的"手术"，也可能把伤口刺痛。同一把刀，用在什么地方、怀着什么动机，决定了它是在育人还是在伤人。因此他给出一句可当标准的判断：对学生的权威是对教师最困难的考验，是教育工作
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 94. 教师的权威是什么，应该表现在哪里

### sk-1352　理解亲人的痛苦能提高道德敏锐性

- 旧标签：love-education, family-school, child-study
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 6.65 + 先验 1.0 = 7.65））
- 其他命中：习惯与纪律（5.8） · 劳动与创造（4.6）
- 转述：苏霍姆林斯基把"理解亲人的痛苦"当成一门可以训练的技能，而不是天生的善心。训练入口是观察：从别人的眼睛里、从细微到几乎察觉不到的举动里、从步履和呼吸里、从人看世界的目光里读出痛苦。他记录的做法很具体——带孩子去田里、草地、牧场，不只是干活，更是"去观察人"，学会看人的心情，目的是"日后能帮助人"。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》12. 理解亲人的痛苦能提高道德敏锐性

### sk-1353　怎样教会孩子们热爱自己的父母

- 旧标签：family-school, love-education, child-study
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 14.62 + 先验 2.5 = 17.12））
- 其他命中：幸福与精神生活（6.7） · 习惯与纪律（4.8）
- 转述：这一节要解决的是"教会孩子爱父母"从哪一步下手。苏霍姆林斯基先立起责任的一端：子女的责任就是报答父母的关怀与忠诚，而且这种责任"决不能用任何尺子来衡量，也决不能用任何数字来计算"。关键机制是"相互的奉献"——爱既能把人身上最隐秘的源泉打开，源源涌出善来，也可能把儿女的心变成干涸的荒野，取决于奉献是否真的双向流动。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》17. 怎样教会孩子们热爱自己的父母

### sk-1354　怎样培养对亲人和亲近的人的忠诚感

- 旧标签：love-education, family-school, collective-education
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 8.08 + 先验 1.0 = 9.08））
- 其他命中：检查知识与考查（6.2） · 尊严、爱与信任（4.9）
- 转述：这一节把"忠诚感"从抽象的道德词变成一串可以照着做的动作。第一个动作是种树：在宅旁地栽下母亲苹果树、父亲苹果树、奶奶苹果树、爷爷苹果树、兄弟姐妹苹果树，让忠诚感有一个能看见、能浇灌的载体。第二个动作是分配果实：从这些树上收获的头一次果实，要送给母亲、奶奶、父亲和爷爷——背后是一句格言式的判断，"你奉献出来的东西，是属于
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》23. 怎样培养对亲人和亲近的人的忠诚感

### sk-1355　怎样把教师劳动的意义传送到学生的意识中去

- 旧标签：teacher-growth, love-education, child-study
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 6.41 + 先验 1.0 = 7.41））
- 其他命中：自我教育（6.2） · 全面发展与个性（4.4）
- 转述：这一节回答的是操作层面的问题：学生凭什么真正理解教师劳动，而不是被要求去"感恩"。苏霍姆林斯基的做法是先把教师的劳动放进可比的对象里——纺织工人一小时看到成果，炼钢工人几小时看到火焰般的铁水，庄稼人几个月看到谷穗，而教师要年复一年，甚至十几年，意图才勉强显现。差异一旦被讲清楚，"教师的劳动是无可比拟的"就不再是一句口号
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》28. 怎样把教师劳动的意义传送到学生的意识中去

### sk-1357　何谓珍惜生活的幸福

- 旧标签：love-education, child-study, family-school
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 10.08 + 先验 1.0 = 11.08））
- 其他命中：劳动与创造（6.9） · 思维与智力（6.7）
- 转述：这一节是本库中“珍惜生活的幸福”这一命题的原文出处，本卡只取其中的做法层面。苏霍姆林斯基不满足于让孩子承认“要珍惜幸福”这句话，而是给出一串可以照着做的动作：牵着手带孩子看、坐下来谈、提出问题、等孩子自己追问。教师与家长的角色被他写成“聪明地拉着孩子的手步入人的世界，不要蒙上他们的眼睛”——既不回避人世间的苦难，也不把
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》3. 何谓珍惜生活的幸福

### sk-1358　何种见解能够培养出成熟的思想

- 旧标签：child-study, thinking-and-nature, teacher-growth
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 10.81 + 先验 2.5 = 13.31））
- 其他命中：幸福与精神生活（10.9） · 阅读与书籍（8.7）
- 转述：本卡取这一节的落地做法：怎样让孩子真正意识到自己不会永远是孩子、长大成人后要在大地上留下痕迹。苏霍姆林斯基明确否掉了说教路线——要“委婉地、细致地、非强加地”启发，“尤为重要的是细致的提示，而不是喋喋不休的说教，老帅哪怕是个小小的提示都会唤起儿童意识中丰富的思想”。所以问题不是“讲什么道理”，而是“用什么场合让他自己想
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》4. 何种见解能够培养出成熟的思想

### sk-1359　怎样教孩子懂得奉献的思想

- 旧标签：love-education, labor-education, family-school
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 10.08 + 先验 1.0 = 11.08））
- 其他命中：尊严、爱与信任（4.9） · 习惯与纪律（4.8）
- 转述：本卡取这一节的操作面：教“奉献”不是讲一通道理，而是把它放回义务的地基上，再换成可反复练习的日常行为。苏霍姆林斯基的起点是硬话——人应当尽义务，“我们生活的全部意义，就在于我们全都应当尽义务，应当奉献”，因为你的每一个满足和欢乐都与他人为你付出的精神上和肉体上的力量分不开；把奉献从义务中抽掉，先是变成自私自利的人，然后
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》6. 怎样教孩子懂得奉献的思想

### sk-1360　在哪些行为之中应表现出义务感

- 旧标签：love-education, collective-education, family-school
- 建议：**A11 劳动与创造**（文本证据推翻旧标签（关键词 11.84，压过旧标签项 10.72））
- 其他命中：公民与祖国（9.7） · 幸福与精神生活（7.4）
- 转述：本卡把这一节整理成“义务感落在哪些具体行为上、怎样练”的清单。苏霍姆林斯基先立地基：权利若没有义务和具体责任（公民、劳动者、有文化素养的人、儿子或女儿、父亲或母亲的责任），就是不可思议的；“谁想不尽义务而享受幸福生活，最终将成为一个令人谴责或令人遗憾的人”。而精神高尚的根本，是“把应当付出个人幸福看做是一种信念”，首先
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》8. 在哪些行为之中应表现出义务感

### sk-1361　怎样教人正确对待死

- 旧标签：love-education, child-study, family-school
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 10.28 + 先验 1.0 = 11.28））
- 其他命中：劳动与创造（4.6） · 思维与智力（4.1）
- 转述：本卡取的是“怎样跟孩子谈死”的方法与分寸。苏霍姆林斯基先给出立场：死是人最大的不幸，人看见人死不能像看见干枯的橡树或一条老狗死去那样平静；但“不理解死，便难以理解生”，也难理解人在大地上每走一步应负的责任。因此把死当做最大的痛苦去理解，目的不是恐惧，而是为了热爱生命、珍惜生命；孩子若能同成年人一起把死当做一种不可避免的
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》13. 怎样教人正确对待死

### sk-1363　怎样教会孩子善于理解人的悲痛

- 旧标签：love-education, family-school, child-study
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 9.36 + 先验 2.5 = 11.86））
- 其他命中：幸福与精神生活（10.1） · 习惯与纪律（5.8）
- 转述：本卡收的是哀悼期可执行的言行规范：面对亲人去世，孩子该怎么做、家长和教师该说什么、不该做什么。苏霍姆林斯基写得非常具体——爷爷奶奶去世，孩子要知道“这也是你本身的一小部分死去”，应当表示哀悼；哀悼时期不应该去俱乐部、电影院和其他娱乐场所，家里不该放响亮的、供娱乐用的音乐，而“良心也会悄悄地向你提示”。这些要求不靠外部监
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》15. 怎样教会孩子善于理解人的悲痛

### sk-1364　怎样培养良心感

- 旧标签：love-education, child-study, teacher-growth
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 10.64 + 先验 1.0 = 11.64））
- 其他命中：道德判断与品德培养（9.4） · 思维与智力（7.5）
- 转述：这一篇通篇讲“怎样练”，与讲原理的卡片互补。核心机制是：良心只有建立在羞耻心之上才会在人的心灵中存在，而羞耻感是可以“加倍地去认识体验和感受”训练出来的——训练场就在活动、举止和对自己行为的思考之中。换句话说，良心感不是听来的，是练出来的，练得越细、越积极，羞耻感和良心感就越得到强化。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》32. 怎样培养良心感

### sk-1365　怎样才能做到使行为举止听从良心的最强有力的指挥

- 旧标签：love-education, child-study, teacher-growth
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 6.97 + 先验 1.0 = 7.97））
- 其他命中：习惯与纪律（5.8） · 尊严、爱与信任（4.4）
- 转述：这一篇回答的是“怎样让良心真的指挥行为”。作者把要点定得很集中：主要的一点是保护儿童的心灵不受虚伪和可耻行为的侵扰，培养出纯洁的良心。而良心本身是一种非常细嫩、而且任性的东西——如果由着它的性子为所欲为，它就会变成残酷的东西；所以要教孩子（尤其是少年）主宰自己的良心、管束住它，它才会成为一生行为举止的聪慧而卓越的卫士。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》33. 怎样才能做到使行为举止听从良心的最强有力的指挥

### sk-1366　怎样教孩子理解道德上的自由感

- 旧标签：love-education, collective-education, child-study
- 建议：**A19 道德判断与品德培养**（文本证据推翻旧标签（关键词 8.39，压过旧标签项 6.67））
- 其他命中：公民与祖国（5.7） · 全面发展与个性（5.0）
- 转述：这一篇讲“怎样教”，落脚点是把道德自由从抽象概念变成孩子能懂、能练的东西。道德自由不是想做什么就做什么，而是只有当人意识到自己是集体、社会、人民的一分子，懂得大家的共同利益和需求，听从自己的义务感，自由才成为真正的福利——为别人做好事应当成为个人的道德倾向、成为自己的需求与愿望，这样的人才既自由又幸福。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》34. 怎样教孩子理解道德上的自由感

### sk-1367　怎样教孩子懂得敏锐而有分寸的行为

- 旧标签：love-education, child-study, teacher-growth
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 6.41 + 先验 1.0 = 7.41））
- 其他命中：习惯与纪律（4.8） · 尊严、爱与信任（4.7）
- 转述：这是一张实践卡，处理日常里最难拿捏的一件事：怎样教孩子做到“敏锐而有分寸”。原文先给总原则——兼而有之：对别人的个别弱点容忍、心软、宽恕，对邪恶毫不妥协、毫不留情。作者说得很直白：你不去计较别人的弱点，同时站得高一点，但对待邪恶必须毫不留情。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》44. 怎样教孩子懂得敏锐而有分寸的行为

### sk-1368　怎样培养孩子自觉地去追求善良

- 旧标签：love-education, collective-education, teacher-growth
- 建议：**A4 自我教育**（旧标签先验 + 文本证据（关键词 12.59 + 先验 1.0 = 13.59））
- 其他命中：劳动与创造（12.5） · 幸福与精神生活（9.7）
- 转述：这一篇只讲“怎样培养”，核心是把善从外部要求变成孩子自愿的追求。原文给出的第一步是先立尺子：善的意念要成为孩子本身的一部分，与他的思想、观点、信念分不开，成为他用来解释和评价周围人际关系的尺子。这把尺子在他的意识、生活和实践中树立得越持久，道德教育和自我教育就越成功。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》46. 怎样培养孩子自觉地去追求善良

### sk-1369　怎样培养个人对邪恶持毫不妥协的态度

- 旧标签：love-education, collective-education, teacher-growth
- 建议：**A20 检查知识与考查**（文本证据推翻旧标签（关键词 5.10，压过旧标签项 5.05））
- 其他命中：评价与分数（4.8） · 公民与祖国（4.0）
- 转述：这是一张实践卡，回答“怎样安排”才能让孩子对邪恶不妥协。起点是态度：对待丑恶现象的积极态度首先是憎恨它，是不容忍、不妥协，是敢于勇敢、直率地批评身边的不公正；勇敢的人毋宁死，也不会背叛自己的信念。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》47. 怎样培养个人对邪恶持毫不妥协的态度

### sk-1370　什么是从事教师工作的才能，它是怎样形成的

- 旧标签：teacher-growth, child-study, reading-and-books
- 建议：**A6 了解儿童**（旧标签先验 + 文本证据（关键词 7.14 + 先验 2.5 = 9.64））
- 其他命中：尊严、爱与信任（5.0） · 健康与作息（4.8）
- 转述：这一篇回答的是“教师才能怎样形成”，即自我培养的路径。作者先设问：教育才能是什么、需要哪些客观条件、如何培养、确定、发展和磨炼。给出的第一条路径是自我检验——在九年级或十年级产生从教愿望时，就请求担任少先队辅导员或十月儿童小组教导员，真真切切地带起40个孩子。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》上篇 1. 什么是从事教师工作的才能，它是怎样形成的

### sk-1371　要教育学生对孤独者不要漠不关心

- 旧标签：love-education, collective-education, family-school
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 14.81 + 先验 1.0 = 15.81））
- 其他命中：思维与智力（8.2） · 尊严、爱与信任（4.7）
- 转述：这一篇给出同情教育的“组织方式”，而不只是同情教育的道理。苏霍姆林斯基的做法有三步：让学生真实地遇见不幸（路上遇见目光忧愁的老奶奶，随后了解她失去三个儿子、丈夫、两个兄弟和母亲的遭遇），让学生自发表达帮助的意愿（科斯佳说要把内心的全部温暖献给她），再把这股情感落成可持续的行动（栽下六窝葡萄和六株玫瑰作纪念，此后每天到她
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 80. 要教育学生对孤独者不要漠不关心

### sk-1372　最后一条建议—保密

- 旧标签：teacher-growth, love-education, child-study
- 建议：**A4 自我教育**（旧标签先验 + 文本证据（关键词 10.28 + 先验 1.0 = 11.28））
- 其他命中：幸福与精神生活（6.8） · 尊严、爱与信任（4.3）
- 转述：这一篇讲的是“隐蔽教育意图”的具体做法，而不只是它为什么成立。苏霍姆林斯基把全书建议都限定为“仅供教师知道”：学生不必在每个具体情况下知道教师正在教育他，因为影响生效的条件之一，是在自然而然的气氛中施加影响。他并不主张放弃目标，而是主张把目标藏进友好、无拘束的相互关系里。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 100. 最后一条建议—保密

### sk-1373　年轻一代共产主义信念的形成（绪论）

- 旧标签：collective-education, love-education, teacher-growth
- 建议：**A19 道德判断与品德培养**（文本证据推翻旧标签（关键词 9.15，压过旧标签项 7.04））
- 其他命中：公民与祖国（6.0） · 自我教育（3.8）
- 转述：这篇绪论把“道德教育不同于知识教育”从判断落成了方法问题。苏霍姆林斯基先立命题：共产主义道德的决定性力量是信念，形成信念是教育的主要任务之一；而许多学校最严重的缺点，恰恰是用“理解道德概念、真理、规范”取代信念的形成。原因就在于忽视了道德教育与知识教育的区别。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《年轻一代共产主义信念的形成》绪论

### sk-1374　孩子应该怎样理解自己对他人的义务

- 旧标签：love-education, family-school, child-study
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 12.51 + 先验 1.0 = 13.51））
- 其他命中：尊严、爱与信任（9.1） · 美与艺术（8.7）
- 转述：这一篇回答的是操作问题：怎样让孩子真的理解“对他人的义务”。苏霍姆林斯基先拆掉一个常见的借口——这些道理对孩子太难。他反过来说：10 岁的孩子能理解每句话、每个思想，7 岁的孩子也能明白个大概。但有一个前提条件：孩子必须在相互关系良好的环境里生活，并且在关系中亲身体验到“彼此都应当奉献”。他用了一个很准的类比——音乐不
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》7. 孩子应该怎样理解自己对他人的义务

### sk-1376　忠诚感和对别人的忠诚意味着什么

- 旧标签：love-education, collective-education, family-school
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 10.39 + 先验 1.0 = 11.39））
- 其他命中：劳动与创造（10.0） · 自然与思维课（9.3）
- 转述：这一篇的可操作部分，是一次具体安排的谈话：毕业晚会前，苏霍姆林斯基把即将领毕业证书的学生带到森林里，在鲜花盛开的大自然中做“最推心置腹的谈话”，他自己称其为“对未来的父母进行的最后一次告诫”。场景本身就是方法——离开教室、离开讲台，让忠诚的讨论发生在人愿意说真话的地方。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》35. 忠诚感和对别人的忠诚意味着什么

### sk-1377　怎样使学生们具有知识的欢乐

- 旧标签：learning-difficulties, thinking-and-nature, teacher-growth
- 建议：**A15 思维与智力**（旧标签先验 + 文本证据（关键词 16.85 + 先验 2.5 = 19.35））
- 其他命中：健康与作息（11.2） · 自然与思维课（9.6）
- 转述：这一篇把“让学生体验知识的欢乐”落成了几件可以在学校里排进课表的事。第一件是“到思维的园地去旅行”：老师带孩子到花园、老橡树跟前、灌木林、养蜂场、池塘边、深山谷，目的不是讲完自然知识，而是向孩子“揭开那些不懂的东西”，唤起求知欲；老师把不懂的东西展示得越出色，孩子的惊讶越深，求知欲越明显——连最胆小、最腼腆的学生也会变
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》25. 怎样使学生们具有知识的欢乐

### sk-1378　怎样使男女青年们具有人的欲望的素养

- 旧标签：love-education, family-school, child-study
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 15.18 + 先验 1.0 = 16.18））
- 其他命中：自然与思维课（5.2） · 评价与分数（4.8）
- 转述：这一篇的可操作部分，是把“我想要”与“我应当”的融合拆成具体的教育安排。第一层是认知：教师必须让孩子相信，良好的欲望能鼓舞人做出忘我行为、能拯救一个人，不好的欲望能毁掉一个人；没有这个前提，控制欲望就只剩压抑。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》48. 怎样使男女青年们具有人的欲望的素养

### sk-1379　怎样培养青年们正确对待爱

- 旧标签：love-education, family-school, child-study
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 13.97 + 先验 2.5 = 16.47））
- 其他命中：思维与智力（7.5） · 自我教育（3.8）
- 转述：这一篇的操作性集中在三个层次。第一层是青年对姑娘的态度规范：要尊重姑娘，爱护她的名誉、人格、自尊和自主性；理由不是礼貌，而是关系本身——引起你好感的姑娘可能成为你的妻子、你孩子的母亲，会在新一代人身上再现你和她自己。由此他划出一条界线：爱并不意味着只是性的关系，如果把婚姻和长年夫妻生活只理解为性的关系，那就是道德上的无
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》49. 怎样培养青年们正确对待爱

### sk-1380　美是培养善良、热爱劳动、热诚和爱情的重要手段

- 旧标签：aesthetic-nature-education, love-education, labor-education
- 建议：**A11 劳动与创造**（旧标签先验 + 文本证据（关键词 5.31 + 先验 2.5 = 7.81））
- 其他命中：幸福与精神生活（6.7） · 美与艺术（4.5）
- 转述：这一篇把“美作为教育手段”落成一串可以做的活动。第一件是固定地去“美的发源地”：低年级期间，老师经常带学生出去，把这种出行明确称为“观察美的课堂”，任务是学会观察、欣赏、聆听周围世界的音乐并理解它。关键不在于去了多美的地方，而在于孩子对具体的对象发生惊讶——长满红浆果、黄叶子的野蔷薇丛，小槭树，有几片黄叶的齐整小苹果树
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》52. 美是培养善良、热爱劳动、热诚和爱情的重要手段

### sk-1381　在当今做个革命者意味着什么

- 旧标签：love-education, collective-education, teacher-growth
- 建议：**A2 公民与祖国**（旧标签先验 + 文本证据（关键词 7.98 + 先验 1.0 = 8.98））
- 其他命中：幸福与精神生活（6.4） · 劳动与创造（5.3）
- 转述：这一篇的操作面，在于把“革命者的责任”从口号变成课堂上能做的具体事。第一件事是让孩子的思想生活有具体的“材料世界”：苏霍姆林斯基说这段道德教诲包括从古罗马斯巴达克率领的第一次奴隶起义、到十七岁的列宁说出“我们不能走那条路”、从阿芙乐尔巡洋舰的炮响、到少先队员从已收获的田里拣麦穗打成一小捧小麦——事件、事实、形象是给孩子
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》53. 在当今做个革命者意味着什么

### sk-1382　用追求理想的方法培养思想性

- 旧标签：love-education, collective-education, teacher-growth
- 建议：**A1 全面发展与个性**（文本证据推翻旧标签（关键词 9.49，压过旧标签项 7.46））
- 其他命中：思维与智力（7.5） · 公民与祖国（5.3）
- 转述：这一篇讲的是“用追求理想的方法培养思想性”，落点是**具体安排**——原文没有停在“要有理想”的口号上，而是写出了一套可操作的布置。第一步是把抽象问题变成少年自己必须回答的问题：他先问“究竟怎样去培养智慧、世界观、思想性和追求理想的志向”，再引用达·芬奇“智慧是经验之女”，说明智慧靠使用而非灌输；接着把“智慧的勇敢和诚
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》57. 用追求理想的方法培养思想性

### sk-1383　要保护青少年内心的纯洁激情

- 旧标签：love-education, child-study, collective-education
- 建议：**A5 尊严、爱与信任**（旧标签先验 + 文本证据（关键词 9.12 + 先验 2.5 = 11.62））
- 其他命中：思维与智力（7.5） · 幸福与精神生活（6.7）
- 转述：这一篇给的是**具体做法与禁区**，而不是关于“激情可贵”的一般主张。先立靶子：要像防火那样警惕冷漠无情，因为冷漠会把人变成只顾自己、对公共事情漠不关心的庸人和小市民，其信条就是“事不关己，高高挂起”。正面做法则是一句可操作的判据——年轻人用自己的双手为别人做的好事越多，心灵就越纯洁越高尚。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《给教师的100条建议》下篇 75. 要保护青少年内心的纯洁激情

### sk-1385　共产主义信念的形成是社会进步和道德进步的客观必然性

- 旧标签：collective-education, love-education, teacher-growth
- 建议：**A2 公民与祖国**（旧标签先验 + 文本证据（关键词 12.89 + 先验 1.0 = 13.89））
- 其他命中：劳动与创造（5.3） · 尊严、爱与信任（4.4）
- 转述：第 2 章讲的是信念形成的“客观必然性”，这一节则把它落成方法：教育者具体怎样利用生产关系与集体生活来形成信念。原文的第一步是选择揭示内容——不能把生产关系笼统地讲成“社会发展规律”，而要挑出其中最重要的一个方面，即**同志式合作与互助的关系**，让学生看得见、摸得着。
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《年轻一代共产主义信念的形成》第2章 共产主义信念的形成是社会进步和道德进步的客观必然性

### sk-1387　结束语：把信念的号召落成可做的具体事情

- 旧标签：collective-education, love-education, teacher-growth
- 建议：**A3 幸福与精神生活**（旧标签先验 + 文本证据（关键词 6.29 + 先验 1.0 = 7.29））
- 其他命中：劳动与创造（5.3） · 健康与作息（4.8）
- 转述：结束语在描述过加加林宇宙飞行之后，把话头转向了教育者手上的活。苏霍姆林斯基说，此刻真正让教育者操心的问题不是理想多么宏大，而是两个可操作的问题：怎样让受教育者的每一次内心激动都伴随思考、劳动、英勇行为的勃发；哪些精神力量应当在人身上确立和锻炼。目标也很具体——让孩子进入生活时成为“拥有充分权利、又对长辈创造的财富倍加爱
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《年轻一代共产主义信念的形成》结束语

### sk-1388　怎样培养父辈和孩子们之间的和谐关系

- 旧标签：family-school, love-education, child-study
- 建议：**A4 自我教育**（文本证据推翻旧标签（关键词 9.75，压过旧标签项 6.76））
- 其他命中：尊严、爱与信任（4.3） · 思维与智力（4.1）
- 转述：这一节回答的是和谐关系从哪儿来这个问题。苏霍姆林斯基先摆出代际结构：年老的一代、创造力旺盛的一代、刚开始意识到自己存在的新一代同时生活在一个世界里，一个人的父母也是别人的孩子，人类种族就这样代代相传。由此得出法则——敬重老一辈，因为他们比你聪明、精神上比你富有；与长辈交往的时刻都要善于向他们学习，不要自以为是、过于自信
- 出处：《苏霍姆林斯基选集（五卷本）第2卷》（教育科学出版社），《怎样培养真正的人》18. 怎样培养父辈和孩子们之间的和谐关系

