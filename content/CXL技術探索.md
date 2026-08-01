---
title: CXL (Compute Express Link) 技術探索
level: intermediate
tags:
  - hardware
  - cxl
  - interconnect
---

# CXL (Compute Express Link) 技術探索

## 摘要

CXL (Compute Express Link) 是一種建立在 PCIe 實體層之上、具備快取一致性 (Cache Coherency) 的高速互連標準。其核心目標是打破 CPU、GPU、加速器 (Accelerators) 以及記憶體之間的隔閡，實現資源池化 (Resource Pooling) 與記憶體擴展 (Memory Expansion)。隨著資料中心 AI 模型的參數量呈指數級增長，單一伺服器的記憶體容量已不敷使用，CXL 成為了克服此限制的關鍵技術。

## CXL 在資料中心與 AI 應用中的技術方案

### 方案一：Type 1 設備 (純加速器，無本地記憶體)

這類設備主要是網卡 (SmartNIC) 或特定演算法加速器。它們不自帶記憶體，而是透過 CXL.cache 協議直接且低延遲地存取主機 CPU 的記憶體資源，並保持快取一致性。

*   **優點 (Pros)：** 極低的存取延遲；硬體架構相對簡單。
*   **缺點 (Cons)：** 必須依賴主機 CPU 的記憶體容量與頻寬。
*   **成本 (Costs)：** 硬體製造成本較低。
*   **維護性 (Maintainability)：** 軟體端需要支援 CXL.cache，但由於硬體狀態較少，驅動程式開發相對單純。
*   **風險 (Risks)：** 若 CPU 記憶體頻寬成為瓶頸，加速器效能將受限。

### 方案二：Type 2 設備 (附帶本地記憶體的加速器，如 GPU/NPU)

這類設備（如現代 AI 加速卡）同時具備運算單元與大量的本地記憶體 (如 HBM)。透過 CXL.cache 和 CXL.mem 協議，CPU 可以存取加速器的記憶體，加速器也可以存取 CPU 的記憶體，兩者處於同一個一致性記憶體空間。

*   **優點 (Pros)：** 最大化記憶體利用率；簡化了 CPU 與 GPU 之間的資料搬移與同步模型 (Programming Model)。
*   **缺點 (Cons)：** 快取一致性的硬體實作極為複雜；異質記憶體 (HBM vs. DDR) 導致效能不一致 (NUMA 效應)。
*   **成本 (Costs)：** 晶片設計成本極高，IP 授權費昂貴。
*   **維護性 (Maintainability)：** 作業系統與應用程式需具備 NUMA 感知能力，否則可能因錯誤的資料放置策略導致效能下降。
*   **風險 (Risks)：** 一致性協議造成的額外延遲可能抵銷了部分頻寬優勢。

### 方案三：Type 3 設備 (記憶體擴充器/池化設備)

這類設備不包含運算單元，僅提供龐大的記憶體容量（通常是 DRAM，甚至未來的 NVM）。它們透過 CXL.mem 協議連接，將記憶體從特定的 CPU 中抽離出來，形成跨伺服器共享的記憶體池 (Memory Pooling)。

*   **優點 (Pros)：** 解決了「記憶體擱淺」(Memory Stranding) 問題，大幅提升資料中心整體的記憶體利用率；允許獨立升級運算或記憶體資源。
*   **缺點 (Cons)：** 存取跨節點記憶體的延遲 (Latency) 顯著高於本地記憶體。
*   **成本 (Costs)：** 系統層級的基礎設施建置成本較高（需 CXL Switch 等設備）。
*   **維護性 (Maintainability)：** 系統管理複雜，需要強大的記憶體配置與排程軟體 (Orchestrator) 進行動態資源分配。
*   **風險 (Risks)：** 延遲敏感型應用可能無法適應 CXL 記憶體池；Switch 硬體的成熟度與互通性 (Interoperability) 仍有挑戰。
