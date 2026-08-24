---
title: DeepSpeed
level: intermediate
tags:
  - AI
  - DeepSpeed
  - LLM
---

# DeepSpeed

摘要：DeepSpeed 是微軟開源的分散式訓練框架，其最著名的 ZeRO (Zero Redundancy Optimizer) 優化技術能大幅減少超大型模型訓練時的記憶體佔用。

## ZeRO (Zero Redundancy Optimizer) 原理

在傳統的資料平行 (Data Parallelism) 訓練中，每一個 GPU 都會保留一份完整的模型權重 (Weights)、梯度 (Gradients) 以及優化器狀態 (Optimizer States, 例如 Adam 的 momentum 和 variance)。對於百億或千億參數的巨型模型，這些狀態會輕易撐爆單一 GPU 的 HBM (如 80GB 的 A100)。

ZeRO 透過在叢集內的 GPU 之間「切分」並「分散」這些資料來消除冗餘，主要分為三個階段：

- **ZeRO Stage 1**：僅切分並分散 **優化器狀態 (Optimizer States)**。這可以在不增加額外通訊開銷的情況下，節省大量記憶體。
- **ZeRO Stage 2**：除了優化器狀態，進一步切分 **梯度 (Gradients)**。
- **ZeRO Stage 3**：進一步切分 **模型權重 (Parameters)**。在需要進行前向 (Forward) 或反向 (Backward) 傳播時，才透過通訊動態抓取需要的權重片段。這使得訓練極大模型成為可能，但會增加網路通訊負擔。

## 與 Megatron 的結合

在實務上，為了訓練極巨量參數模型，業界普遍採用 **Megatron-DeepSpeed** 框架。[[Megatron]] 負責處理張量平行 (Tensor Parallelism) 與管線平行 (Pipeline Parallelism)，而 DeepSpeed 負責 ZeRO 數據平行，兩者結合以達到最佳的擴展性。

## 其他特性

除了 ZeRO，DeepSpeed 還包含其他優化技術，如 DeepSpeed-MoE (針對混合專家模型的優化)、Offloading (將部分狀態卸載到 CPU 記憶體或 NVMe SSD) 以突破 GPU 記憶體容量極限。
