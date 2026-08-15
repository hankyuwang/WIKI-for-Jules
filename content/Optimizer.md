---
title: Optimizer
level: intermediate
tags:
  - AI
  - Optimizer
---

# Optimizer

摘要：Optimizer (最佳化器) 負責在模型訓練過程中，根據計算出的梯度來更新神經網路的權重。常見的 Optimizer 如 Adam、SGD 等，在分散式訓練中往往佔用大量記憶體。

## 已知事實
在大型語言模型 (LLM) 訓練中，Optimizer 狀態 (如 Adam 的 Momentum 和 Variance) 佔用的記憶體往往是模型參數本身的兩到三倍。這使得 Optimizer 成為記憶體瓶頸 (Memory-bound) 的核心問題之一。

## 原理
梯度下降演算法計算出損失函數對權重的梯度後，Optimizer 會決定如何更新這些權重。以 Adam 為例，它不僅需要儲存當前的權重，還需要為每個權重參數維護一階動量 (Momentum) 和二階動量 (Variance) 的狀態，這導致了巨大的記憶體開銷。

## 限制
標準的 Optimizer 在單一 GPU 上訓練巨大模型時會遇到 OOM (Out of Memory) 錯誤。即便使用混合精度 (Mixed Precision) 訓練，Optimizer 狀態仍需以 FP32 格式儲存以保持數值穩定性，進一步加劇了記憶體壓力。

## 未知問題
業界仍在積極探索如何設計出既能像 SGD 一樣節省記憶體，又能像 Adam 一樣快速收斂的全新 Optimizer 演算法。

## 最佳實務
在分散式訓練中，業界普遍採用 DeepSpeed 的 ZeRO (Zero Redundancy Optimizer) 技術，透過將 Optimizer 狀態切分並分散到叢集中的多個 GPU 上，大幅減少單一節點的記憶體負載。

## 方案與觀點分析

### 方案一：ZeRO-1 (Optimizer State Partitioning)
- 優點：只對 Optimizer 狀態進行切分，對通訊頻寬的要求相對較低，能立即釋放大量記憶體。
- 缺點：無法解決模型參數本身過大導致的記憶體瓶頸。
- 成本：低，現有框架 (如 DeepSpeed) 已高度整合。
- 維護性：高，為業界標準做法。
- 風險：在節點數量極多時，All-Gather 通訊可能成為瓶頸。

### 方案二：8-bit Optimizers (如 bitsandbytes)
- 優點：將 Optimizer 狀態量化為 8-bit，直接將記憶體佔用減少 75%，且幾乎不損失收斂速度。
- 缺點：需要特殊的 CUDA kernel 支援，可能在某些舊版硬體上效能不佳。
- 成本：低，可透過外掛套件快速導入。
- 維護性：中，依賴第三方開源庫的維護更新。
- 風險：量化帶來的些微數值誤差在極端情況下可能導致訓練不穩定。

### 方案三：CPU Offloading
- 優點：將 Optimizer 狀態和更新計算卸載到主機的 CPU 和 RAM 上，讓 GPU 專注於前向和反向傳播，適合硬體資源極度受限的情境。
- 缺點：PCIe 頻寬成為嚴重瓶頸，更新權重的速度極慢，大幅拖累整體訓練時間。
- 成本：極低，只需改變軟體設定。
- 維護性：高。
- 風險：訓練時間過長可能導致專案延宕。
