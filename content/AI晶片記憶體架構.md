---
title: AI晶片記憶體架構
level: advanced
tags:
  - memory
  - architecture
  - hardware
---

# AI 晶片記憶體架構

在探討 [[AI加速晶片概覽]] 時，我們常說「記憶體牆 (Memory Wall)」是目前 AI 晶片設計面臨的最大挑戰之一。強大的運算核心需要有足夠快、足夠大的記憶體來餵養資料。

## 記憶體階層 (Memory Hierarchy)
AI 晶片通常具備多層次的記憶體結構：
1. **暫存器 (Registers)**: 速度最快，容量最小。
2. **晶片內建 SRAM (On-chip SRAM)**: 例如 TPU 中的 Unified Buffer，提供高頻寬的資料存取，減少對 DRAM 的依賴。
3. **高頻寬記憶體 (HBM)**: 透過 2.5D/3D 封裝技術，將多個 DRAM 晶粒堆疊並與運算晶片連接，大幅提升記憶體頻寬。

## 突破記憶體瓶頸的技術
為了減少資料搬運，除了增加快取，業界也積極發展：
- **存算一體 (Processing in Memory, PIM)**: 嘗試將部分運算單元直接整合到記憶體晶片中，這也是 [[AI晶片未來發展趨勢]] 的重點方向。
- **資料流架構優化**: 如 [[TPU技術解析]] 中提到的脈動陣列，最大化資料在晶片內部的重複利用率。
