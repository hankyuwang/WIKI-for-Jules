---
title: MAC
level: beginner
tags:
  - AI
  - MAC
  - Hardware
  - Architecture
---

# MAC (Multiply-Accumulate)

摘要：MAC (Multiply-Accumulate，乘積累加運算) 是深度學習與神經網路底層硬體運算的最基本核心元件。它將乘法與加法結合在單一指令或硬體單元中，大幅提升了矩陣運算的效率。

## 已知事實與原理
在深度學習中，神經網路的前向傳播與反向傳播大量依賴於矩陣乘法 (Matrix Multiplication) 與卷積運算 (Convolution)。這些運算本質上都是由無數次的「將兩個數字相乘，然後加到一個累加器中」所構成。

一個標準的 MAC 運算公式為：
$$ a \leftarrow a + (b \times c) $$

在硬體層面，MAC 單元負責在單一時脈週期 (Clock Cycle) 內完成這兩個動作。現代的 AI 加速器（如 GPU、TPU 或 NPU）會將成千上萬個 MAC 單元平行排列，以達到極高的運算吞吐量 (Throughput)。例如，Google TPU 的核心脈動陣列 (Systolic Array) 就是由大量的 MAC 單元組成的二維陣列。

## 效能與限制
- **算力指標**：硬體的 AI 算力常以 TOPS (Tera Operations Per Second) 或 TFLOPS 來衡量。一個 MAC 運算通常包含兩次 Operation (一次乘法，一次加法)。
- **瓶頸 - 記憶體牆 (Memory Wall)**：MAC 單元雖然運算極快，但如果無法及時從記憶體 (如 SRAM 或 HBM) 讀取資料 $b$ 與 $c$，MAC 單元就會閒置。因此，如何提升資料重用率 (Data Reuse) 並降低資料搬移功耗，是硬體架構設計的核心難題。

## 延伸學習
- [[GPU架構與演進]]：了解現代 GPU 如何透過 Tensor Core 平行處理大量的 MAC 運算。
- [[TPU架構深度解析]]：探索 TPU 如何透過脈動陣列將 MAC 單元緊密結合，解決資料傳輸延遲。
- [[基礎計算機結構]]：回顧算術邏輯單元 (ALU) 的基本原理。
