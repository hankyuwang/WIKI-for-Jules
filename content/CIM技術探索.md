---
title: CIM (Computing-In-Memory) 技術探索
level: advanced
tags:
  - hardware
  - cim
  - architecture
---

# CIM (Computing-In-Memory) 技術探索

## 摘要

CIM (Computing-In-Memory，記憶體內運算) 是一種顛覆馮·紐曼架構 (Von Neumann Architecture) 的新興計算典範。傳統架構下，資料儲存 (Memory) 與運算 (CPU/GPU) 是分離的，導致大量的資料搬移產生極高的能耗並形成延遲瓶頸 (Memory Wall)。CIM 技術藉由在記憶體陣列內部或緊鄰記憶體單元處直接執行類比或數位運算（如矩陣乘法 MAC 操作），從根本上減少資料搬移，極大地提升了 AI 推理，特別是邊緣 AI 的能效比 (TOPS/W)。

## CIM 的技術實現方案與觀點

### 方案一：Analog CIM (類比記憶體內運算，基於 SRAM 或 Non-Volatile Memory)

利用記憶體單元的物理特性（如電流與電導的歐姆定律，以及基爾霍夫電流定律）直接在交叉點陣列 (Crossbar Array) 中完成乘加運算。常使用的媒介包含 SRAM 或是新興的非揮發性記憶體 (如 RRAM, PCM, MRAM)。

*   **優點 (Pros)：** 理論上能效比 (Energy Efficiency) 極高，可達數十甚至上百 TOPS/W；運算密度極高，一次能完成大規模平行運算。
*   **缺點 (Cons)：** 運算精度受限於類比電路的雜訊、製程變異與溫度漂移，通常只能支援低精度 (如 INT8 甚至 INT4/INT1)；需要 ADC/DAC 轉換器，這部分會佔用大量面積和功耗。
*   **成本 (Costs)：** 研發與製程成本高，特別是整合新興非揮發性記憶體 (NVM) 需要特殊製程。
*   **維護性 (Maintainability)：** 由於類比特性的不穩定性，模型部署前可能需要針對硬體特性進行重新訓練或校準 (Hardware-Aware Training)，軟硬體耦合度高。
*   **風險 (Risks)：** 若製程漂移過大，可能導致推理準確率明顯下降；ADC/DAC 成為新的功耗瓶頸。

### 方案二：Digital CIM (數位記憶體內運算，基於 SRAM)

在靠近 SRAM 位元儲存單元 (Bitcell) 旁邊，或在外圍電路中，加入微型的數位邏輯閘 (如 Full Adder, Multiplier)，維持資料以數位形式進行運算。

*   **優點 (Pros)：** 運算精度完全可控且不受雜訊干擾，易於支援高精度浮點運算 (如 FP8/BF16/FP16)；相容於現有的數位 CMOS 製程與 EDA 設計流程。
*   **缺點 (Cons)：** 相較於 Analog CIM，能效比和運算密度較低；在 SRAM 陣列中加入邏輯閘會增加記憶體面積。
*   **成本 (Costs)：** 由於相容標準 CMOS 製程，製造成本相對可控，但面積增加會抵銷部分成本優勢。
*   **維護性 (Maintainability)：** 軟體編譯器開發相對容易，行為模式與傳統數位電路一致，較易整合到現有的 AI 框架中。
*   **風險 (Risks)：** 可能落入「只是一個擁有極大頻寬的傳統加速器」的窠臼，未能發揮 CIM 最大的能效潛力。

### 方案三：Near-Memory Computing (近記憶體運算，基於 3D 封裝)

嚴格來說這不完全是 "In-Memory"，而是將運算單元 (Logic Die) 與記憶體單元 (Memory Die) 透過 3D 堆疊 (如 TSV) 緊密結合，使兩者間的通訊距離縮短至微米等級。例如 HBM-PIM 概念。

*   **優點 (Pros)：** 避開了修改底層記憶體陣列設計的風險，DRAM/SRAM 與 Logic 可分別使用最適合的製程 (Memory Node vs. Logic Node) 製造。能大幅提升頻寬。
*   **缺點 (Cons)：** 仍存在一定程度的資料搬移，能效提升不如真正的 In-Memory 架構顯著。散熱是最大的挑戰。
*   **成本 (Costs)：** 高階 3D 封裝技術 (如 TSV, Hybrid Bonding) 成本極高，主要應用於雲端或高效能運算 (HPC)。
*   **維護性 (Maintainability)：** 軟體生態系統的調整相對於 Analog CIM 較為明確，但仍需要作業系統與編譯器支援。
*   **風險 (Risks)：** 複雜的散熱問題可能限制了運算單元能維持的最高時脈，導致整體效能受限。
