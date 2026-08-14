---
title: Systolic Array
level: intermediate
tags:
  - AI
  - Systolic-Array
  - TPU
  - Architecture
  - Hardware
---

# Systolic Array (脈動陣列)

摘要：Systolic Array (脈動陣列) 是 Google TPU 的核心架構設計。它讓資料在互相連接的運算單元 (MAC) 之間像血液般有節奏地流動，極大地減少了存取外部記憶體的次數，實現了極高效率的矩陣乘法運算。

## 已知事實與原理
在傳統的馮·紐曼架構中，每次運算都需要從記憶體讀取資料，運算完成後再寫回記憶體。對於深度學習中龐大的矩陣相乘運算，這會造成嚴重的「記憶體牆 (Memory Wall)」瓶頸。

Systolic Array 透過一種特殊的硬體拓撲結構解決了這個問題。其運作原理如下：
1. **網格狀排列**：陣列由成千上萬個處理單元 (Processing Elements, PE) 組成二維網格，每個 PE 本質上就是一個 [[MAC]] (Multiply-Accumulate) 單元。
2. **資料流動**：資料（如神經網路的輸入特徵與權重）從陣列的邊緣輸入。在每一個時脈週期中，PE 計算完乘積累加後，並不會把結果寫回主記憶體，而是直接將結果或資料傳遞給相鄰的下一個 PE。
3. **資料重用 (Data Reuse)**：透過這種資料在陣列中「脈動 (Systolic)」流動的機制，一筆資料被讀出後，可以參與多次運算。這大幅降低了對 SRAM 或 HBM 的頻寬需求。

## 效能與優勢
Google 的 TPU (Tensor Processing Unit) 正是依靠 Systolic Array 取得了巨大的成功。例如 TPU v1 內部配置了 256x256 的矩陣相乘單元，單一時脈週期就能完成 65,536 次的 MAC 運算。
相較於早期 GPU 依賴大量的暫存器與 L1/L2 快取來隱藏延遲，Systolic Array 的設計更為緊湊，控制邏輯極簡，將晶片面積最大程度地讓給了運算單元。

## 限制與挑戰
- **缺乏通用性**：Systolic Array 是高度特化的硬體，專為 Dense Matrix Multiplication (稠密矩陣相乘) 設計。如果遇到需要分支預測、複雜控制流，或是稀疏矩陣 (Sparse Matrix) 的演算法，其效能會大幅下降。
- **陣列填不滿**：如果計算的模型矩陣尺寸較小，無法填滿巨大的 PE 網格，會造成大量運算單元閒置，導致實際利用率 (Utilization) 低落。

## 延伸學習
- [[MAC]]：Systolic Array 中最基本的運算節點。
- [[TPU架構深度解析]]：深入探討 Google TPU 是如何利用 Systolic Array 顛覆 AI 訓練與推論硬體的設計。
- [[NPU架構探索]]：了解其他神經網絡處理器如何借鑑並改良資料流架構。
