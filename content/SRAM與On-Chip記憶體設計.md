---
title: SRAM 與 On-Chip 記憶體設計
level: intermediate
tags:
  - hardware
  - memory
  - SRAM
---

# SRAM 與 On-Chip 記憶體設計

## 摘要
靜態隨機存取記憶體（SRAM）由於其極低的存取延遲與高頻寬特性，廣泛作為現代處理器（CPU, GPU, NPU）的晶片內（On-Chip）快取（Cache）與暫存器（Scratchpad Memory）。在 AI 推理與訓練硬體架構中，如何最大化利用有限的 SRAM 資源，減少對外部 DRAM 的存取，是克服「記憶體牆（Memory Wall）」與降低系統功耗的關鍵設計挑戰。

## 設計觀點與分析

### 觀點一：增加 SRAM 容量以容納整個 AI 模型 (SRAM-only 系統)
極端設計是將處理器內部的 SRAM 容量擴增至數十甚至數百 MB，嘗試將整個神經網路模型（如 Transformer 的 KV Cache 或權重）完全保留在晶片內。

*   **優點 (Pros)**：消除對外部 DRAM 的存取需求，提供最極致的低延遲與高頻寬，且大幅降低整機功耗。
*   **缺點 (Cons)**：SRAM 電路結構由 6 顆電晶體（6T）組成，密度遠低於 DRAM（1T1C），佔用極大的晶片面積。
*   **成本 (Costs)**：直接導致晶片尺寸（Die Size）變大，嚴重降低晶圓良率（Yield），使單顆晶片製造成本呈指數上升。
*   **維護性 (Maintainability)**：超大面積的 SRAM 陣列容易受到製程變異（Process Variation）與軟錯誤（Soft Errors, 如宇宙射線）的影響，需要設計複雜的除錯與備援機制。
*   **風險 (Risks)**：隨著 AI 模型參數規模不斷膨脹，依賴純 SRAM 的設計難以跟上模型成長的速度，極易遭遇容量天花板。

### 觀點二：硬體管理的 Cache vs. 軟體管理的 Scratchpad Memory
在 AI 加速器設計中，對於晶片內建 SRAM，可以設計成由硬體自動管理的傳統快取（Cache），或是由編譯器與軟體顯式控制的暫存區記憶體（Scratchpad Memory, SPM）。

*   **優點 (Pros)**：
    *   **Cache**：對程式設計師透明，相容現有軟體生態系。
    *   **SPM**：提供完全可預測的存取延遲（Deterministic Latency），適合即時（Real-time）與高效能的張量運算排程。
*   **缺點 (Cons)**：
    *   **Cache**：硬體複雜度高，替換策略（Replacement Policy）在規律的 AI 矩陣運算中往往效率不佳（Thrashing）。
    *   **SPM**：程式設計極度困難，編譯器必須精確掌握資料的生命週期，並生成複雜的資料搬移指令。
*   **成本 (Costs)**：Cache 增加了硬體驗證與設計成本；SPM 則將負擔轉嫁給軟體編譯器開發團隊。
*   **維護性 (Maintainability)**：SPM 的軟體維護成本高，當硬體規格改變（如 SRAM 容量變動）時，可能需要重新調整編譯最佳化策略。
*   **風險 (Risks)**：若 SPM 編譯器未臻完善，開發者難以發揮硬體的理論效能上限，導致硬體雖然強大但「不好用」。

### 觀點三：3D SRAM 堆疊 (SRAM on Logic)
透過晶圓級封裝（Wafer-Level Packaging）或混合鍵合（Hybrid Bonding）技術，將獨立生產的高密度 SRAM 晶粒直接堆疊在運算邏輯晶粒之上（如 AMD 的 3D V-Cache 技術）。

*   **優點 (Pros)**：允許使用針對記憶體最佳化的製程節點來製造 SRAM，同時大幅擴增晶片內的快速記憶體容量，且不佔用原本運算邏輯層的寶貴面積。
*   **缺點 (Cons)**：散熱挑戰加劇。邏輯層產生的熱量必須穿透上方的 SRAM 晶粒才能散出，可能導致熱點（Hotspot）問題。
*   **成本 (Costs)**：雖然提高了良率（因為分成兩顆較小的晶片），但增加了先進封裝的成本，整體造價仍屬高昂。
*   **維護性 (Maintainability)**：封裝後的晶片不可維修，封裝良率直接影響最終產品成本。
*   **風險 (Risks)**：熱機械應力（Thermomechanical Stress）可能導致鍵合層（Bonding Layer）在長期熱循環下出現微裂紋，影響晶片壽命與可靠度。
