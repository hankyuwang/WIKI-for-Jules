---
title: 邊緣運算AI晶片
level: intermediate
tags:
  - Edge Computing
  - Edge AI
  - IoT
---

# 邊緣運算AI晶片

隨著物聯網 (IoT) 設備的普及和即時處理需求的增加，AI 計算正逐漸從雲端向邊緣（Edge）轉移。邊緣運算 AI 晶片專注於在資源受限的環境中執行高效的 AI 推理。

## Prerequisites
- [[AI加速晶片概述]]
- [[基礎計算機結構]]

## 為什麼需要在邊緣運算？
1. **降低延遲 (Latency)**: 數據無需傳回雲端，適合自駕車或工業自動化等要求即時反應的場景。
2. **保護隱私 (Privacy)**: 敏感數據可以留在本地設備處理。
3. **節省頻寬 (Bandwidth)**: 減少需要傳輸到雲端的數據量。

## 邊緣 AI 晶片的設計挑戰
- **功耗限制 (Power Constraint)**: 行動裝置和電池供電設備的功耗預算極低。
- **記憶體容量 (Memory Constraint)**: 邊緣設備無法配備大量的 DRAM，因此 [[模型量化技術]] 和權重複用設計至關重要。

## 常見的邊緣 AI 架構
邊緣運算通常採用 NPU（Neural Processing Unit）或是 DSP（Digital Signal Processor）結合微控制器（MCU）的架構。詳細設計探討請參考 [[NPU架構探索]]。此外，未來的低功耗架構創新可見 [[新型態AI硬體架構]]。
