---
title: 大語言模型 (LLM) 基礎
level: beginner
tags:
  - llm
  - transformer
  - concepts
---

# 大語言模型 (Large Language Model, LLM)

大語言模型 (LLM) 是基於龐大文本資料訓練的深度學習模型，能夠理解並生成人類語言。它們通常基於 [[Transformer]] 架構，具有數十億甚至數千億個參數。

## 基礎運作原理
LLM 透過預測「下一個單字」(Next-token prediction) 來生成文本。在推論階段，分為兩個主要步驟：
1. **[[Prefill]] (預填充)**：模型讀取使用者的提示詞 (Prompt)，並計算初始狀態與 [[KV Cache]]。
2. **[[Decode]] (解碼)**：模型根據先前的狀態，一個接一個地生成後續的 Token。

## 為什麼 LLM 需要強大的硬體？
因為 LLM 包含極大量的參數，導致其推論階段遇到了嚴重的記憶體牆問題，這也是為什麼我們需要探討 [[AI記憶體瓶頸與解決方案]] 以及 [[高效能LLM推理框架最佳實務]]。
在硬體層面，LLM 依賴強大的 [[GPU架構與AI運算]]，並逐漸在 [[商用AI加速晶片分析]] 中成為主要的考量指標。
