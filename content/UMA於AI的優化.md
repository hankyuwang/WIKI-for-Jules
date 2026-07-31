---
title: UMA於AI的優化
level: beginner
tags:
  - UMA
  - memory
  - architecture
  - optimization
---

# UMA於AI的優化

## 摘要
統一記憶體架構（Unified Memory Architecture, UMA）允許 CPU 與 GPU（或 NPU）共享同一塊系統記憶體。在 AI 應用中，這意味著不需再將巨量的訓練資料或模型權重於 CPU 記憶體與 GPU 顯存間來回複製。蘋果的 Apple Silicon 是近期最成功應用 UMA 的範例之一，這種設計極大地簡化了程式設計模型，並在受限硬體內提供了運行龐大 AI 模型的可能性。

## 優化與實踐觀點

### 方案一：硬體層級的完全一致性 (Hardware Cache Coherency)
系統硬體自動維護 CPU 與 GPU 之間的快取一致性，確保兩者看到的記憶體狀態完全同步。
- **優點 (Pros):** 對軟體開發者極為友善，不需手動管理記憶體同步與資料拷貝。
- **缺點 (Cons):** 維護一致性會消耗大量的系統匯流排頻寬與硬體資源，在大量資料並發寫入時可能成為效能瓶頸。
- **成本 (Costs):** 需要極為複雜的系統單晶片（SoC）設計與昂貴的高頻寬記憶體（如 LPDDR5/HBM）來支撐龐大的頻寬需求。
- **維護性 (Maintainability):** 硬體自動處理複雜性，系統軟體與驅動程式的維護相對單純。
- **風險 (Risks):** 當 GPU 處理高解析度影像與推論大模型時，可能會吃光頻寬，導致 CPU 餓死（Starvation）。

### 方案二：軟體控制的零拷貝 (Software-Managed Zero-Copy)
硬體提供共享記憶體空間，但不保證強一致性，交由作業系統或驅動程式的 API（如 CUDA Unified Memory）來管理分頁遷移（Page Migration）。
- **優點 (Pros):** 降低了硬體設計的複雜度，且能針對特定 AI 工作負載進行記憶體遷移的客製化最佳化。
- **缺點 (Cons):** 若軟體預取（Prefetching）或分頁失效（Page Fault）處理不佳，會引發嚴重的延遲抖動（Jitter）。
- **成本 (Costs):** 硬體實作成本較低，但轉移了複雜度至軟體層。
- **維護性 (Maintainability):** 開發者需要深入理解底層驅動運作機制來進行效能調校，增加應用程式維護的難度。
- **風險 (Risks):** 在不同作業系統版本或不同驅動程式下，效能表現可能存在巨大差異，難以保證穩定的執行效能。

### 方案三：運算卸載與混合記憶體架構 (Offloading with Hybrid Memory)
在 UMA 的基礎上，為 GPU 或 NPU 保留少量的高速專用記憶體（如 SRAM 或 eDRAM），將大部分資料放在系統 DRAM，並透過智能排程決定資料存放位置。
- **優點 (Pros):** 兼顧了高頻寬與大容量，能最優化關鍵神經網路層（如 Attention 機制）的執行效能。
- **缺點 (Cons):** 需要高度智能化的編譯器與排程器來分析計算圖（Compute Graph），以決定哪些張量（Tensor）該放在哪裡。
- **成本 (Costs):** 需同時投入先進封裝與高階編譯器的研發。
- **維護性 (Maintainability):** 排程演算法需隨著新 AI 模型的出現不斷更新，維護成本極高。
- **風險 (Risks):** 若排程器判斷錯誤，會導致比純粹 UMA 更嚴重的資料搬移懲罰。
