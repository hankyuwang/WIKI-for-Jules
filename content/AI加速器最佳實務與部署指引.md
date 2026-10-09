---
title: AI 加速器最佳實務與部署指引
level: intermediate
tags:
  - best-practices
  - deployment
  - hardware
---

# AI 加速器最佳實務與部署指引

## Prerequisites (先備知識)
- [[基礎計算機結構]]
- [[AI加速晶片概述]]
- [[模型與硬體適配性]]

## 1. 軟硬體協同開發最佳實務
為了發揮 AI 加速器的最大效能，軟體與硬體的協同設計至關重要。
- **算子融合 (Operator Fusion)**: 盡可能將多個小型算子合併，以減少記憶體頻寬的消耗與 Kernel 啟動的開銷。
- **混合精度訓練與推理 (Mixed Precision)**: 根據硬體支援 (如 Tensor Cores)，適當使用 FP8, BF16 或 INT8 來提升吞吐量。
- **記憶體階層管理**: 妥善利用快速但容量小的 SRAM (On-chip memory) 與容量大但較慢的 HBM/DDR，實作 Tiling 技術。

## 2. 部署策略
- **叢集拓樸感知**: 在分散式訓練時，分配任務應考慮網路拓樸 (如 NVLink, InfiniBand)，將通訊密集的任務放在同一個節點內。
- **負載平衡與流水線 (Pipeline)**: 針對 LLM 等大模型，使用 Pipeline Parallelism 與 Tensor Parallelism，並調整微批次大小 (Micro-batch size) 以最大化 GPU 使用率。
- **邊緣部署優化**: 對於資源受限的邊緣設備，善用量化 (Quantization, 如 PTQ/QAT) 與剪枝 (Pruning) 技術縮減模型大小。


## 詳細解說與專有名詞補充
- **微批次大小 (Micro-batch size)**：在訓練巨大的 AI 模型時，為了避免記憶體爆炸，我們會把一批資料切成更小的「微批次」，分批送進硬體運算。
- **管線平行化 (Pipeline Parallelism)**：想像一條生產線，把一個巨大的神經網路切成幾段，不同的硬體（如 GPU）負責不同的段落。資料就像在流水線上傳遞一樣，從第一個 GPU 算完傳給第二個。
- **張量平行化 (Tensor Parallelism)**：把神經網路中單一的一層（例如一個超大的矩陣）切開，分配給多個 GPU 同時計算，算完後再把結果拼起來。
- **剪枝 (Pruning)**：把神經網路中那些「不重要、對結果影響很小」的連接（權重）直接刪除，讓模型變小、變快。
- **Tensor Cores**：這是 NVIDIA GPU 裡面專門用來加速矩陣乘法（AI 運算核心）的特殊硬體單元。
- **Tiling 技術**：就像鋪磁磚一樣，因為晶片內部的超高速記憶體（SRAM）很小，無法一次裝下整個大矩陣，所以必須把大矩陣切成一小塊一小塊（Tiling），分批搬進 SRAM 裡面計算。