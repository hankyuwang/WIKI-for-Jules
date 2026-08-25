---
title: TPU與專用AI晶片
level: intermediate
tags:
  - TPU
  - ASIC
  - Google
---

# TPU與專用AI晶片

除了通用性較強的 [[GPU]]，為了追求極致的效能與能效比，許多科技巨頭與新創公司開發了專為 AI 演算法量身打造的專用晶片，其中最具代表性的便是 Google 的 TPU（Tensor Processing Unit）。

## Prerequisites
- [[AI加速晶片概述]]
- [[基礎計算機結構]]

## 什麼是 TPU？
TPU 是一種特殊應用積體電路（ASIC），專為加速機器學習的工作負載而設計，特別是針對 [[TensorFlow]] 框架進行了深度優化。TPU 的核心架構通常包含龐大的脈動陣列（Systolic Array），能夠極高效率地執行矩陣乘法。與通用 GPU 相比，TPU 移除了顯示輸出、通用計算單元等非 AI 必要的電路，將所有電晶體預算投入到張量運算中。

## 脈動陣列 (Systolic Array) 架構
這是一種硬體架構設計，資料在處理單元（Processing Elements, PEs）陣列中像血液一樣同步流動（脈動）。
- **運作原理**: 權重資料預先載入陣列中，輸入資料從一個方向流入，部分和（Partial Sums）向另一個方向流動。在每一個時鐘週期，每個 PE 執行一次乘加運算（MAC），並將結果傳遞給下一個 PE。
- **優勢**: 這種設計極大地減少了對外部記憶體（如 HBM/SRAM）的頻繁存取，實現了高度的資料重用，大幅提升了矩陣運算的效率與能效比。詳見 [[Systolic Array]]。

## 專用 ASIC 的優勢與限制
- **優勢**:
  - **極致能效 (Performance per Watt)**: 在特定任務（如神經網路推理與訓練）上，能提供遠超 GPU 的效能。
  - **確定性延遲**: 由於架構專一，延遲時間更容易預測，適合要求嚴格的即時推理場景。
- **限制**:
  - **缺乏靈活性**: 如果 AI 演算法發生重大改變（例如從 CNN 轉向 Transformer，或者引入新的非矩陣運算操作），硬體可能無法有效支援，甚至面臨淘汰。
  - **開發成本極高**: ASIC 的設計、驗證與流片（Tape-out）成本高達數千萬美元，且週期長。

## 其他專用 AI 晶片生態
除了 Google TPU，市場上還有許多針對不同場景的專用晶片：
- **雲端訓練/推理**: AWS 的 Inferentia / Trainium、Intel 的 Gaudi 系列。
- **邊緣運算 (Edge AI)**: 著重極低功耗，如 NPU（Neural Processing Unit）。
在架構設計上，也可參考 [[NPU架構探索]] 以了解不同設計哲學。
