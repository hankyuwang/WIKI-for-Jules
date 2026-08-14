---
title: ASIC 加速晶片設計
level: intermediate
tags:
  - asic
  - hardware
  - design
---

# ASIC 加速晶片設計

特殊應用積體電路 (Application-Specific Integrated Circuit, ASIC) 是為了單一特定用途所設計的晶片。在 AI 領域，ASIC 被設計來提供最佳的效能與最低的功耗。

## ASIC 在 AI 加速的定位

在開發 AI 硬體時，工程師通常在「通用性 (Generality)」與「效能 (Performance / Efficiency)」之間進行權衡。
CPU 和 [[GPU架構與發展|GPU]] 具有高通用性，但為此付出了較大矽面積與功耗的代價。
[[FPGA在AI加速的應用|FPGA]] 提供了硬體層級的彈性。
而 ASIC 則位於頻譜的極端，犧牲了通用性，將電路完全為特定的神經網路運算量身打造，因此能達到極致的效能功耗比。

## ASIC 設計的核心挑戰

開發一款成功的 AI ASIC 需要面對許多挑戰：

1. **高昂的 NRE 成本**
   晶片設計的非經常性工程支出 (Non-Recurring Engineering, NRE) 非常驚人，包含昂貴的 EDA 工具授權費、光罩製作費等。如果晶片的出貨量不夠大，難以攤平這些前期投資。

2. **漫長的開發週期 (Time-to-Market)**
   從架構設計、RTL 撰寫、驗證、實體設計到最終的流片 (Tape-out)，一個 ASIC 專案通常需要一到兩年甚至更久的時間。在 AI 演算法日新月異的今天，晶片在設計初期針對的模型可能在晶片上市時就已過時。這也就是為何 ASIC 通常需要保有一定程度的軟體可程式性。

3. **軟硬體協同設計 (SW/HW Co-design)**
   一個好的硬體如果沒有配套的編譯器將模型有效地映射到硬體資源上，其效能將大打折扣。這在 [[NPU架構探索]] 中有詳細探討，編譯器需要處理記憶體分配、運算排程與指令生成。

## 典型 AI ASIC 範例

- **Google TPU**：專為 TensorFlow 設計的大型加速器，詳見 [[TPU深度解析]]。
- **邊緣 NPU (Edge NPU)**：內建於手機 SoC（如 Apple A 系列, Qualcomm Snapdragon）或物聯網設備中，專注於低功耗的影像處理或語音辨識推論。

回顧整體 AI 晶片生態，可參考：[[AI加速晶片總覽]]。

## ASIC 過時風險與應對方案

針對演算法演進導致硬體過時的風險，現代 ASIC 設計中通常會加入一定比例的可程式化運算單元，以確保對未來神經網路模型的兼容性。
