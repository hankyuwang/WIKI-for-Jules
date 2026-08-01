---
title: 新型態AI硬體架構
level: advanced
tags:
  - Emerging Architecture
  - Neuromorphic
  - CIM
---

# 新型態AI硬體架構

為了突破傳統馮·諾伊曼架構（Von Neumann Architecture）中的「記憶體牆（Memory Wall）」瓶頸，學術界與產業界正在積極探索各種新型態的 AI 硬體架構。

## Prerequisites
- [[AI加速晶片概述]]
- [[基礎計算機結構]]

## 記憶體內運算 (Compute-in-Memory, CIM)
傳統架構中，資料必須從記憶體移動到運算單元才能處理，這消耗了大量的能量與時間。CIM 架構直接在記憶體陣列（如 SRAM, RRAM, MRAM）內部進行運算（主要是乘加運算 MAC），大幅減少了數據搬移。

## 神經形態計算 (Neuromorphic Computing)
受到生物大腦的啟發，神經形態晶片（如 Intel Loihi）採用脈衝神經網路（Spiking Neural Networks, SNN）。這種架構採用非同步處理，並且只有在接收到脈衝時才消耗能量，因此具有極高的能效潛力。

## 光學 AI 晶片 (Photonic AI Accelerators)
光學晶片利用光子而非電子來進行資料傳輸和運算。光子具有高頻寬、低延遲和低能耗的特性，特別適合處理大規模的線性運算（如矩陣乘法）。

## 挑戰與展望
這些新型態架構目前多處於研究或早期商業化階段。它們面臨著製程成熟度、軟體生態系（編譯器支持）以及精度控制等挑戰。針對各種架構的全面評估，請參考 [[AI晶片方案評估與發展趨勢]]。