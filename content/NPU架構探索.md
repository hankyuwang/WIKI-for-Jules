---
title: 類神經網絡處理器 (NPU) 架構探索
level: intermediate
tags:
  - npu
  - hardware
  - architecture
---

# NPU 架構探索

這篇筆記專注於 NPU (Neural Processing Unit) 的基礎與前沿架構探討。

## Prerequisites
- [[基礎計算機結構]]
- [[深度學習運算原理]]

## 基礎概念
NPU 的核心目的在於加速矩陣乘法與卷積運算，常見的基礎結構是 Systolic Array (脈動陣列)。藉由將資料流在運算單元之間傳遞，可以極大化地減少對主記憶體 (DRAM) 的存取。

## 軟硬體協同設計 (SW/HW Co-design)
要讓 NPU 發揮最大效能，編譯器扮演了至關重要的角色。例如透過 Zero-overhead SW Tiling 來將大矩陣切割，以符合 NPU 的 SRAM 限制，同時隱藏資料搬運的延遲。

## 延伸閱讀
- [[模型量化技術]]：量化技術與 NPU 的整數運算單元息息相關。
- [[AI加速晶片與邊緣運算部署策略]]：探討 AI 加速晶片在邊緣運算環境下的部署與應用策略。
