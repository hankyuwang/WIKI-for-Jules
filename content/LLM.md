---
title: 大型語言模型 (LLM)
level: beginner
tags:
  - architecture
  - llm
  - transformer
---

# 大型語言模型 (LLM, Large Language Model)

## 摘要
大型語言模型（Large Language Models，簡稱 LLMs）是近年來人工智慧領域最重大突破之一。這類模型通常基於 [[Transformer]] 架構，透過在海量文本數據上進行預訓練（Pre-training），學習到了豐富的語言結構與世界知識。LLM 的出現不僅改變了自然語言處理 (NLP) 的範式，也帶動了底層硬體如 [[GPU架構與AI計算]] 以及分散式系統的快速發展。

## 原理與特點

### 1. 規模效應 (Scaling Laws)
LLM 最顯著的特點在於其「規模」。研究表明，隨著模型參數（Parameters）、訓練數據量（Dataset Size）與運算量（Compute）的增加，模型的性能會呈現可預測的提升。這種現象被稱為 Scaling Laws。當模型規模突破某個臨界點時，還會產生所謂的「湧現能力 (Emergent Abilities)」，使得模型能夠解決在訓練階段未曾見過的複雜任務。

### 2. 基石架構：Transformer
絕大多數現代 LLM 都採用了 [[Transformer]] 架構，特別是 Decoder-only 的設計（如 GPT 系列）。Transformer 透過自注意力機制（Self-Attention）捕捉長距離的上下文依賴關係。然而，這也帶來了所謂的 [[Long Context]] 挑戰與記憶體牆問題，因為在推論的 [[Decode]] 階段，注意力機制的運算量會隨著上下文長度的平方成長，並需要維護龐大的 [[KV Cache]]。

### 3. 從預訓練到對齊 (Alignment)
LLM 的訓練通常分為幾個階段：
1.  **預訓練 (Pre-training)**：在大量未標記文本上進行自監督學習，目標是預測下一個詞。這個階段耗費大量算力，賦予模型基礎的語言能力。
2.  **指令微調 (Instruction Tuning)**：在人工編寫或高品質的指令數據集上進行微調，讓模型學會如何遵循人類指令。
3.  **人類回饋強化學習 (RLHF)**：透過強化學習，讓模型的輸出更加對齊人類的價值觀與偏好，減少有害或幻覺內容。

## 面臨的挑戰與解決方案

### 1. 推論效能瓶頸
在實際部署 LLM 時，推論階段（特別是自迴歸生成的 [[Decode]] 階段）常面臨嚴重的記憶體頻寬瓶頸（Memory Bound）。為了解決這個問題，業界提出了多種 [[LLM推理最佳實務]]：
-   **量化技術 (Quantization)**：將模型權重與啟動值從 FP16/BF16 壓縮至 INT8 甚至 INT4/FP4（參見 [[模型量化技術]]）。
-   **PagedAttention**：透過分頁管理記憶體，有效解決 [[KV Cache]] 記憶體碎片化的問題，這是 vLLM 等高效推論框架的核心。
-   **硬體協同**：針對 LLM 特性設計的硬體架構，如加入更多 SRAM、採用 [[HBM]] 提升記憶體頻寬，甚至探索 [[Processing-in-Memory]] (PIM) 技術。

### 2. 訓練成本
訓練千億參數級別的 LLM 需要龐大的 GPU 叢集（如 NVIDIA H100 叢集）與高速網路互連（如 [[InfiniBand]]）。這推動了分散式訓練技術的發展，包括資料平行（Data Parallelism）、張量平行（Tensor Parallelism）與管線平行（Pipeline Parallelism）。

## 💡 初學者比喻：什麼是 LLM？
你可以把 LLM 想像成一個「超級圖書館員」。
在過去（預訓練階段），這位圖書館員閱讀了全世界數以億計的書籍、網頁和文章，他沒有特別去死記硬背哪一句話在哪一頁，而是學會了「人類說話和思考的邏輯」。
當你問他問題時（推論階段），他會根據他讀過的龐大知識庫，綜合判斷出最可能、最合理的回答。
但因為他大腦裡裝了太多東西（參數龐大），當他要連續回答很長的問題時，他需要很大的「工作記憶」（KV Cache）來記住你前面說過的話，這也就是為什麼運行 LLM 需要這麼強大的電腦硬體。

## 相關連結
- 回到 [[INDEX]]
- 延伸向 [[Transformer]]
- 延伸向 [[LLM推理最佳實務]]
- 延伸向 [[KV Cache]]
