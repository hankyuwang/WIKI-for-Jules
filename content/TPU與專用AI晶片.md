---
title: TPU與專用AI晶片
level: intermediate
tags:
  - TPU
  - ASIC
  - Google
---

# TPU與專用AI晶片

除了通用性較強的 GPU，為了追求極致的效能與能效比，許多科技巨頭與新創公司開發了專為 AI 演算法量身打造的專用晶片，其中最具代表性的便是 Google 的 TPU（Tensor Processing Unit）。

## Prerequisites
- [[AI加速晶片概述]]
- [[基礎計算機結構]]

## 什麼是 TPU？
TPU 是一種特殊應用積體電路（ASIC），專為加速機器學習的工作負載而設計，特別是針對 TensorFlow 框架進行了深度優化。TPU 的核心架構通常包含龐大的脈動陣列（Systolic Array），能夠極高效率地執行矩陣乘法。

## 脈動陣列 (Systolic Array) 架構
這是一種硬體架構設計，資料在處理單元陣列中像血液一樣同步流動（脈動）。這種設計減少了對記憶體的頻繁存取，大幅提升了矩陣運算的效率。

## 專用 ASIC 的優勢與限制
- **優勢**: 在特定任務（如神經網路推理與訓練）上，能提供比 GPU 更高的每瓦效能（Performance per Watt）。
- **限制**: 缺乏靈活性。如果演算法發生重大改變，硬體可能無法有效支援。

## 其他專用 AI 晶片
除了 TPU，還有如 AWS 的 Inferentia / Trainium、Intel 的 Gaudi 等，這些晶片都試圖在特定領域或雲端環境中提供最佳的 AI 運算成本效益。在架構設計上，也可參考 [[NPU架構探索]] 以了解不同設計哲學。