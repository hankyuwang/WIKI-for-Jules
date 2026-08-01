---
title: 非揮發性記憶體在AI的應用
level: research
tags:
  - hardware
  - memory
  - nvm
---

# 非揮發性記憶體在AI的應用

## 摘要

非揮發性記憶體 (Non-Volatile Memory, NVM)，如 NAND Flash、ReRAM (電阻式記憶體)、MRAM (磁阻式記憶體) 和 PCM (相變化記憶體)，能在斷電後保持資料不遺失。傳統上，NAND Flash 用作大容量儲存裝置 (SSD)，速度遠不及 DRAM。然而，隨著 AI 模型（尤其是 LLMs）暴增至數千億參數，單靠昂貴的 DRAM 儲存模型權重變得不切實際。同時，新興的 Storage-Class Memory (SCM) 和新興 NVM 提供了介於 DRAM 與 NAND 之間的效能與成本平衡，並開啟了類比運算 (Analog Computing) 的新契機。

## 方案與觀點探討

### 觀點一：使用 NAND Flash (SSD) 作為虛擬記憶體擴展儲存大模型權重
透過優化作業系統的分頁 (Paging) 機制，或在應用程式層面實現智慧載入 (Smart Loading)，將不常使用的模型層 (Layers) 或權重暫存在高速 NVMe SSD 中，只在需要計算時才載入 DRAM/GPU 記憶體中。

- **優點 (Pros)**: 極大地降低了硬體成本，允許在記憶體容量有限的消費級硬體 (如 Mac 或 PC) 上執行超大型 AI 模型 (如 Llama 3 70B)。
- **缺點 (Cons)**: 推論速度 (Tokens/sec) 會大幅下降，因為 PCIe 與 SSD 的頻寬遠低於 DRAM，且延遲極高 (微秒等級)。
- **成本 (Costs)**: 極低。NAND Flash 的每 GB 成本遠低於 DRAM。
- **維護性 (Maintainability)**: 高。純軟體層面的優化，硬體皆為標準現成產品 (COTS)。
- **風險 (Risks)**: 頻繁的讀寫可能加速 SSD 磨損 (Wear-out)，縮短儲存裝置壽命；使用者體驗可能因為過高的延遲而無法接受。

### 觀點二：Storage-Class Memory (SCM) 的應用 (例如 Intel Optane, 雖然已停產但概念延續)
使用具備位元組尋址 (Byte-addressable) 能力、延遲接近 DRAM 但容量更大的 SCM 作為 DRAM 和 NAND 之間的新階層。未來的 CXL 介面結合新興記憶體有望延續此概念。

- **優點 (Pros)**: 填補了 DRAM (快但容量小) 與 NAND (慢但容量大) 之間的鴻溝，非常適合圖神經網路 (GNN) 或擁有龐大 embedding table 的推薦系統。
- **缺點 (Cons)**: 寫入速度通常不佳，且存在寫入次數限制 (Endurance limit)；軟體生態系統尚未完全適應這類記憶體。
- **成本 (Costs)**: 介於 DRAM 與 NAND 之間，但需要特殊的記憶體控制器與介面。
- **維護性 (Maintainability)**: 中等。硬體本身可抽換，但軟體架構需要針對非揮發性質與不對稱讀寫效能進行重新設計。
- **風險 (Risks)**: SCM 市場目前缺乏強而有力的商業推手，新興技術 (如 CXL 擴展 DRAM) 可能會取代 SCM 在資料中心的定位。

### 觀點三：利用新興 NVM (ReRAM, MRAM) 進行類比記憶體內運算 (Analog In-Memory Computing)
不僅僅是儲存，而是利用 ReRAM 電阻矩陣或 MRAM 的物理特性，直接使用克希荷夫電路定律 (Kirchhoff's circuit laws) 在記憶體陣列中執行矩陣乘法加法運算 (MAC)。

- **優點 (Pros)**: 實現真正的 "Zero Memory Wall"，能效比 (TOPS/W) 是傳統數位架構的數十倍甚至百倍，是邊緣 AI (Edge AI) 與物聯網設備的完美解決方案。
- **缺點 (Cons)**: 受限於類比雜訊 (Analog Noise)、裝置變異性 (Device Variability) 以及低精確度，目前僅能用於小規模或容忍低精度的 AI 任務。
- **成本 (Costs)**: 需要全新的製造流程與製程整合，初期良率低，客製化成本高。
- **維護性 (Maintainability)**: 極低。電阻值的漂移 (Drift) 問題嚴重，需要複雜的線上校正與補償機制。
- **風險 (Risks)**: 半導體製程穩定性挑戰極大，且難以與主流基於數位邏輯的強大生態圈 (如 CUDA) 競爭。