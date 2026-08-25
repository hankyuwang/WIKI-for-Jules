---
title: Mamba
level: intermediate
tags:
  - AI
  - Mamba
---

# Mamba

## Prerequisites
- [[Transformer]]
- [[RNN]]

摘要：Mamba 是 基於狀態空間模型(SSM)的新架構，具備線性時間複雜度，有望解決長文本瓶頸。



## 虛擬團隊補充說明：Mamba 的線性時間複雜度優勢

> **教育員白話文解釋**：在傳統的 Transformer 中，要回顧過去的記憶就像是每次都要把所有讀過的書重新翻一遍（運算量呈平方級增長）。而 Mamba 就像是學會了「做筆記」和「動態忘記不重要資訊」的技術，它把所有重要的歷史資訊壓縮成一個固定大小的筆記本（Hidden State）。不管讀了多少書，它都只需要看這本筆記本就好，這大大減少了運算和記憶體的負擔。

**Mamba 在硬體上的優勢：**

1. **解決長文本的 O(N^2) 瓶頸**：傳統 Attention 機制在處理長度為 $N$ 的文本時，運算量與記憶體需求會隨著 $N^2$ 暴增。Mamba 基於選擇性狀態空間模型 (Selective SSM)，將時間複雜度降為 $O(N)$（線性時間複雜度）。這意味著它可以輕鬆處理數十萬甚至百萬級別長度的 Context。
2. **免除龐大的 KV Cache**：Transformer 在推論時需要儲存每一層、每一個 Token 的 KV Cache，這會佔用驚人的記憶體容量，並導致嚴重的 Memory-bound 問題。Mamba 不需要完整的 KV Cache，只需維護固定大小的狀態向量（State Vector），極大地減輕了記憶體容量與頻寬的壓力。
3. **SRAM 感知運算 (Hardware-aware Algorithm)**：Mamba 演算法在設計時就考慮了底層硬體的特性。它透過在快速的 SRAM 中完成核心的狀態掃描與更新運算，避免了頻繁向較慢的 HBM 讀寫資料，從而實現了極高的推論吞吐量。

## 已知事實
隨著 LLM 推理序列長度增加，Transformer 架構的 Attention 機制呈現平方複雜度，KV Cache 佔用龐大記憶體。Mamba 透過選擇性狀態空間模型 (Selective SSM)，在保持高效能的同時實現了線性複雜度，成為當前備受矚目的 Transformer 替代或互補方案。

## 原理
Mamba 架構的核心在於透過硬體感知的平行掃描 (Hardware-aware Parallel Scan) 演算法。它將狀態更新過程進行高度平行化，並且在 SRAM 中完成運算，避免頻繁與 HBM 進行資料讀寫（減少 Memory-bound 的影響）。它不再需要像 Transformer 那樣儲存所有的歷史 KV Cache，而是將歷史資訊壓縮在一個固定大小的隱藏狀態 (Hidden State) 中。

## 限制
雖然 Mamba 在推理階段非常高效，但在某些需要精確回憶特定歷史細節的任務（如資訊抽取、in-context learning）上，由於歷史資訊被壓縮，其表現可能略遜於 Attention 機制。

## 未知問題
目前業界仍在探索如何將 Mamba 與現有的 MoE (Mixture of Experts) 架構無縫整合，以及在大規模叢集訓練時的擴展性極限。

## 最佳實務
針對長文本應用場景，目前建議可以探索混合架構（Hybrid Architecture），例如在底層使用 Mamba 處理長序列以降低複雜度，並在頂層使用少量的 Attention 層以維持精準的上下文關聯能力。

## 方案與觀點分析

### 方案一：混合 Mamba-Transformer 架構
- 優點：兼顧 Mamba 在處理長序列時的線性時間複雜度優勢與 Transformer 的精確回憶能力。
- 缺點：模型架構複雜，訓練難度與超參數調校困難。
- 成本：中高，需要重新設計模型架構並進行訓練。
- 維護性：中，依賴開源社群對混合架構軟體堆疊的支援度。
- 風險：可能無法充分發揮單一架構的硬體極致最佳化潛力。

### 方案二：全 Mamba 架構與硬體加速器協同設計
- 優點：透過專注於 SSM 操作的客製化硬體（如專用 SRAM 掃描單元），可大幅突破記憶體牆限制，推論速度極快。
- 缺點：放棄了成熟的 Attention 硬體生態（如 Tensor Core 等）。
- 成本：極高，需開發全新的硬體與對應的編譯器。
- 維護性：低，專用硬體不易應對未來演算法的快速演進。
- 風險：如果演算法主流不轉向 Mamba，專用硬體將成為沉沒成本。

### 方案三：軟體層面的編譯器最佳化 (Triton/CUDA)
- 優點：無需硬體更動，直接在現有 GPU 架構上利用 Triton 等工具編寫 Hardware-aware 的 Kernel，達成 SRAM 感知的最佳化。
- 缺點：受限於現有硬體架構的物理限制。
- 成本：低，純軟體開發。
- 維護性：高，演算法更新時只需修改軟體 Kernel。
- 風險：在某些非 GPU 架構上可能難以直接移植，降低跨平台相容性。