---
title: DeepSpeed
level: intermediate
tags:
  - AI
  - DeepSpeed
  - LLM
---

# DeepSpeed

摘要：DeepSpeed 是微軟開源的分散式訓練框架，其最著名的 ZeRO (Zero Redundancy Optimizer) 優化技術能大幅減少超大型語言模型訓練時的記憶體佔用，突破單一硬體的記憶體極限。

## Prerequisites (先備知識)
- [[GPU架構與AI計算]] : 了解單一 GPU 的記憶體限制。
- [[梯度下降]] : 了解模型訓練過程中的優化器 (Optimizer) 運作。

## 為什麼需要分散式訓練與 DeepSpeed？
在傳統的資料平行 (Data Parallelism) 訓練中，每一個 GPU 都會保留一份完整的：
1. **模型權重 (Weights)**
2. **梯度 (Gradients)**
3. **優化器狀態 (Optimizer States)** (例如 Adam 的動量參數)

對於百億或千億參數的巨型模型，光是儲存這些狀態就會撐爆單一 GPU 的高頻寬記憶體（如 80GB）。

## ZeRO (Zero Redundancy Optimizer) 原理
ZeRO 的核心概念是「消除冗餘」。與其讓每個 GPU 都複製一份完整的資料，ZeRO 透過在叢集內的 GPU 之間「切分」並「分散」這些資料。它分為三個漸進的階段：
- **ZeRO Stage 1**：僅切分並分散 **優化器狀態**。這可以在不增加額外網路通訊開銷的情況下，節省大量記憶體。
- **ZeRO Stage 2**：進一步切分 **梯度**。
- **ZeRO Stage 3**：進一步切分 **模型權重**。在需要進行前向 (Forward) 或反向 (Backward) 傳播時，GPU 才會透過網路通訊動態「抓取」需要的權重片段。這使得訓練極大模型成為可能，但對網路頻寬 (如 [[InfiniBand]]) 要求極高。

## 與 Megatron 的結合 (3D 平行化)
在實務上，業界普遍採用 **Megatron-DeepSpeed** 框架來實現 3D 平行化：
- [[Megatron]] 負責處理 **張量平行 (Tensor Parallelism)** (將單一矩陣運算切分到不同 GPU) 與 **管線平行 (Pipeline Parallelism)** (將模型不同層分配到不同 GPU)。
- DeepSpeed 負責 ZeRO 數據平行。
這兩者的結合，是目前訓練頂級 LLM 的最佳實務。
