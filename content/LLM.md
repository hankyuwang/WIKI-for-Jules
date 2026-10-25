---
title: LLM (Large Language Model)
level: beginner
tags:
  - llm
  - ai-model
---

# LLM (大型語言模型)

## 摘要
LLM (Large Language Model，大型語言模型) 是基於 [[Transformer]] 架構發展出來的超大規模人工智慧模型。透過大量的文本數據訓練，LLM 能夠理解、生成和與人類進行自然語言互動。

## 💡 初學者比喻
想像 LLM 是一個讀遍了世界上所有圖書館書籍的超級學者。當你問他問題時，他並不是「搜尋」答案，而是根據他讀過的龐大知識，用他的話「接續」寫出最合理的回覆 (也就是所謂的 [[Decode]] 過程)。

## 核心概念與技術原理
LLM 的核心運作機制是**自迴歸 (Autoregressive)** 生成。給定一段前綴文本（Prompt），模型會計算出下一個最可能出現的詞（Token）。
1. **預訓練 (Pre-training)**：在海量未標註數據上學習語言的統計規律與知識。
2. **微調 (Fine-tuning)**：例如 SFT (Supervised Fine-Tuning) 和 RLHF (基於人類回饋的強化學習)，讓模型學會聽從指令並符合人類價值觀。

## 硬體挑戰：記憶體牆
LLM 最大的挑戰在於推論 (Inference) 階段的記憶體頻寬需求。由於每次生成一個 Token 都需要將數十到數百 GB 的模型權重從記憶體搬運到運算單元，這導致了嚴重的「記憶體牆」效應，也是為何我們需要如 [[HBM]]、[[KV Cache]] 優化，甚至探索 [[Processing-in-Memory]] 的原因。

## 延伸閱讀
- [[LLM推理最佳實務]]
- [[LLM推理擴展與效能瓶頸分析]]
- [[Transformer]]
