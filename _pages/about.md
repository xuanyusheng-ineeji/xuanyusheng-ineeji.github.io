---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I am a researcher with a background in Artificial Intelligence, Computer Vision, and Natural Language Processing. I received my M.S. degree from Dongguk University (Seoul, South Korea) in 2025, where I was a member of the Game Engine & Robot Intelligence Lab. My research focuses on AI-driven game commentary generation, conversational emotion recognition, and 3D scene reconstruction from monocular video. Prior to my graduate studies, I worked as a frontend developer at a mobile game company in China for nearly three years. I have published papers at journals including *IEEE Access* and *Mathematics* (MDPI), with total <a href='https://scholar.google.com/citations?user=ExfeJJwAAAAJ'>google scholar citations <strong><span id='total_cit'>0+</span></strong></a> <a href='https://scholar.google.com/citations?user=ExfeJJwAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>.


# 🔥 News
- *2025.11*: &nbsp;🎉🎉 Joined ineeji Co., Ltd. as a Researcher at the AI Research Lab (Team 2), working on AI-based energy management and time-series data analysis.
- *2025.08*: &nbsp;🎉🎉 Paper accepted at *Mathematics* (MDPI) — "Integrating Temporal Event Prediction and Large Language Models for Automatic Commentary Generation in Video Games".
- *2025.07*: &nbsp;🎉🎉 Paper accepted at *Mathematics* (MDPI) — "EmoBERTa-CNN: Hybrid Deep Learning Approach for Enhanced Emotion Recognition in Conversational Settings".
- *2024.10*: &nbsp;🎉🎉 Paper published in *IEEE Access* — "Indoor Scene Reconstruction From Monocular Video Combining Contextual and Geometric Priors".

# 📝 Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Mathematics 2025</div><img src='/images/mathematics-13-02738-g002.png' alt="commentary" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Integrating Temporal Event Prediction and Large Language Models for Automatic Commentary Generation in Video Games**

**Xuanyu Sheng**, A. Yu, M. Zhang, G. An, J. Park, K. Cho

*Mathematics*, Vol. 13, No. 17, p. 2738, MDPI, 2025. — **1st Author** <strong><span class='show_paper_citations' data='ExfeJJwAAAAJ:d1gkVwhDpl0C'></span></strong>

- Combined OS-CNN time-series prediction with LLaMA3.3 to generate real-time soccer game commentary within 3 seconds.
- Achieved F1-score 0.8503 on Google Research Football dataset using Focal Loss + SMOTE.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Mathematics 2025</div><img src='/images/mathematics-13-02438-g001.png' alt="emotion" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**EmoBERTa-CNN: Hybrid Deep Learning Approach Capturing Global Semantics and Local Features for Enhanced Emotion Recognition in Conversational Settings**

M. Zhang, A. Yu, **Xuanyu Sheng**, J. Park, J. Rhee, K. Cho

*Mathematics*, Vol. 13, No. 15, p. 2438, MDPI, 2025. — **3rd Author** <strong><span class='show_paper_citations' data='ExfeJJwAAAAJ:u-x6o8ySG0sC'></span></strong>

- Fused EmoBERTa with CNN and attention mechanism for conversational emotion recognition.
- Achieved F1-score 96.0% on SemEval-2019 Task 3 and 79.45% on MELD, outperforming DialogXL and EmotionFlow.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IEEE Access 2024</div><img src='/images/cho1-3481250-large.gif' alt="reconstruction" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Indoor Scene Reconstruction From Monocular Video Combining Contextual and Geometric Priors**

M. Wen, **Xuanyu Sheng**, K. Cho

*IEEE Access*, Vol. 12, pp. 153360–153369, 2024. — **2nd Author** <strong><span class='show_paper_citations' data='ExfeJJwAAAAJ:u5HHmVD_uO8C'></span></strong>

- Proposed a ViT-based scene reconstruction model with CGF cost estimation.
- Outperformed prior methods on ScanNet v2 in Chamfer Distance, Precision, and F-score.
</div>
</div>

# 🎖 Honors and Awards
- *2025.08* TOPIK (Test of Proficiency in Korean) — Level 6, National Institute for International Education.
- *2023.09* SRDⅡ International Full Scholarship, Dongguk University.

# 📖 Educations
- *2023.09 - 2025.08*, M.S., Dongguk University, Seoul, South Korea. GPA: 4.0/4.5.
- *2016.09 - 2020.06*, B.S., Bohai University, China. GPA: 80.57/100.

# 💻 Work Experience
- *2025.11 - present*, Researcher, AI Research Lab (Team 2), ineeji Co., Ltd., Seoul, South Korea.
- *2023.09 - 2025.08*, Researcher, Game Engine & Robot Intelligence Lab, Dongguk University, Seoul, South Korea.
- *2020.11 - 2023.08*, Frontend Developer, Hangzhou Langtu Technology Co., Ltd., China.
