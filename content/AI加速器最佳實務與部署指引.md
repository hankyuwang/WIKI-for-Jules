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

## 虛擬團隊補充說明：初學者專區

> **教育員白話文解釋**：什麼是算子融合 (Operator Fusion)？
> 在深度學習中，模型會經歷許多數學步驟，例如先做矩陣乘法，再做啟動函數。如果硬體每做完一步就把資料存回記憶體，下一步再讀出來，這會極度浪費記憶體頻寬 (造成 Memory Wall 的主因)。
> 「算子融合」就像是把多個步驟寫在同一張黑板上一次算完，資料不需要來回搬運，大幅減少記憶體開銷。

> **教育員白話文解釋**：流水線平行 (Pipeline Parallelism) 與 張量平行 (Tensor Parallelism)
> 1. **流水線平行**：就像工廠生產線，GPU 1 負責前半段，算完交給 GPU 2 負責後半段。
> 2. **張量平行**：像是一群人共同拼一張大拼圖，矩陣計算被切分成多塊，由多張 GPU 「同時」計算自己的部分，最後再合併結果。

### 業界最佳實務：推論框架 (Inference Frameworks)
為了讓 LLM 在 GPU/AI 加速器上跑得更快，業界發展出了許多推論框架：
- **vLLM**: 核心技術是 `PagedAttention`，將記憶體像虛擬記憶體一樣分頁管理，解決 KV Cache 碎片問題。
- **TensorRT-LLM**: NVIDIA 官方框架，對底層架構做了極致優化，結合算子融合與先進量化技術。
