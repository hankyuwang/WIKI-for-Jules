---
title: SRAM與DRAM在AI硬體中的角色
level: beginner
tags:
  - hardware
  - memory
  - sram
  - dram
---

# SRAM與DRAM在AI硬體中的角色

## 摘要

在 AI 硬體架構中，記憶體系統 (Memory Hierarchy) 是決定效能與功耗的關鍵。SRAM (Static Random-Access Memory) 和 DRAM (Dynamic Random-Access Memory) 是最基礎且最重要的兩種記憶體技術。SRAM 速度極快但面積大、成本高，通常作為晶片內的快取 (On-chip Cache)；而 DRAM 容量大、成本低但速度較慢，通常作為主記憶體 (Off-chip Memory)。理解兩者在 AI 晶片中的分工，是優化模型推論與訓練效能的基礎。

## 方案與觀點探討

### 觀點一：巨量 SRAM (SRAM-Heavy) 架構設計 (例如 Cerebras Wafer-Scale Engine)
此類架構極大化晶片面積，並在晶片上配置了數百 MB 甚至數 GB 的超大容量 SRAM，將整個 AI 模型和資料都放置在晶片內的 SRAM 中進行運算。

- **優點 (Pros)**: 消除 DRAM 存取帶來的 Memory Wall 瓶頸，提供破紀錄的超高記憶體頻寬與極低延遲，能效比極佳。
- **缺點 (Cons)**: 受限於 SRAM cell 面積過大（通常是 6T 架構），無法儲存像 GPT-4 等動輒數百 GB 的超大模型；晶片面積巨大，良率控制極難。
- **成本 (Costs)**: 製造與封裝成本極端高昂，因為需要特殊的光罩與晶圓級封裝 (Wafer-Scale Packaging) 技術。
- **維護性 (Maintainability)**: 低。這類系統通常是高度客製化的超級電腦，硬體故障難以進行模組化替換，軟體生態圈也較為封閉。
- **風險 (Risks)**: 若未來 AI 模型體積持續以指數型增長，單一晶片的 SRAM 容量可能無法應付，需要依賴分散式架構。

### 觀點二：以 DRAM 為中心 (DRAM-Centric) 的傳統架構 (例如標準 CPU/GPU)
運算晶片上只保留少量的 SRAM (L1/L2/L3 Cache)，主要依賴外部龐大的 DRAM (如 DDR 或 GDDR/HBM) 來儲存模型權重與啟動值 (Activations)。

- **優點 (Pros)**: 能夠輕易支援極大容量的記憶體，是目前訓練大型語言模型 (LLMs) 的唯一實用選擇；硬體與軟體生態系最為成熟。
- **缺點 (Cons)**: 晶片內與晶片外之間的資料搬移消耗了系統中超過一半以上的功耗，且頻寬受限於 I/O 介面，嚴重限制了運算效能 (Memory Bound)。
- **成本 (Costs)**: 記憶體本身成本相對較低，這得益於 DRAM 產業巨大的規模經濟效益。
- **維護性 (Maintainability)**: 高。標準化的記憶體介面與模組使得升級與維護十分容易。
- **風險 (Risks)**: 隨著運算單元 (MAC) 效能提升速度遠超過 DRAM 頻寬提升速度，兩者的差距（Memory Wall）會越來越大，降低硬體的實際利用率 (Utilization)。

### 觀點三：3D SRAM over Logic (SRAM 垂直堆疊技術)
透過先進封裝技術（如 TSMC SoIC），將獨立的 SRAM 晶粒直接垂直堆疊在運算邏輯晶粒 (Logic Die) 之上（例如 AMD 3D V-Cache）。

- **優點 (Pros)**: 結合了 SRAM 的高速特性與 3D 封裝的高密度互連，大幅增加晶片內快取容量，有效減少存取外部 DRAM 的次數。
- **缺點 (Cons)**: 散熱是主要問題，運算邏輯發出的熱量會被上方的 SRAM 晶片覆蓋，可能導致降頻。
- **成本 (Costs)**: 較高。需要先進的混合鍵合 (Hybrid Bonding) 封裝技術。
- **維護性 (Maintainability)**: 低。封裝為一體後無法單獨維修。
- **風險 (Risks)**: 封裝良率直接影響整體晶片良率與成本，且對散熱解決方案提出了極高的要求。