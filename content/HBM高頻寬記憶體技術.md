---
title: HBM 高頻寬記憶體技術
level: intermediate
tags:
  - HBM
  - memory
  - hardware
---

# HBM 高頻寬記憶體技術

**摘要：**
高頻寬記憶體（High Bandwidth Memory, HBM）是為解決 AI 運算中「記憶體牆（Memory Wall）」問題而發展出的關鍵技術。透過將多個 DRAM 晶片立體堆疊（3D Stacking），並使用矽穿孔（TSV）技術穿透晶片，HBM 能提供遠超傳統 GDDR 記憶體的頻寬與更低的功耗，是目前高階 AI GPU（如 NVIDIA H100、AMD MI300）的標準配備。本篇將探討提升 AI 系統記憶體頻寬的三種解決方案，並分析 HBM 的優劣。

## 觀點與解決方案

### 1. 使用傳統 GDDR (Graphics Double Data Rate) 記憶體
傳統 GPU 常見的記憶體方案，透過將多顆 GDDR 記憶體晶片平面排列在 PCB 板上（如 GDDR6/GDDR6X），並透過高速匯流排與 GPU 連接。

*   **優點 (Pros)：** 技術成熟，產能充足且成本相對低廉；不需要複雜的 2.5D/3D 封裝技術。
*   **缺點 (Cons)：** 頻寬受限於 PCB 佈線的物理極限（Pin Count 限制），無法滿足超大模型的訓練需求；平面排列佔用大量 PCB 面積；功耗較高。
*   **成本 (Costs)：** 記憶體晶片與封裝成本低，適合消費級顯示卡或邊緣 AI 設備。
*   **維護性 (Maintainability)：** 散熱設計相對簡單，維護性好。
*   **風險 (Risks)：** 隨著模型增大，記憶體頻寬將成為嚴重的系統瓶頸（Memory-Bound）。

### 2. HBM (High Bandwidth Memory) 2.5D 先進封裝
將運算晶片（GPU/ASIC）與多顆 HBM 記憶體堆疊（Cube）並排放置在矽中介層（Silicon Interposer）上（即 2.5D 封裝，如台積電 CoWoS），透過 Interposer 上密集的微佈線實現超高頻寬連接。

*   **優點 (Pros)：** 記憶體頻寬極高（達數 TB/s 等級），徹底打破記憶體牆；大幅節省 PCB 面積；相較於 GDDR，提供更高的能效比（Bandwidth-per-Watt）。
*   **缺點 (Cons)：** 高度依賴先進封裝產能；TSV 與中介層製造過程複雜，良率控制挑戰大；散熱極為困難（熱量集中在極小體積內）。
*   **成本 (Costs)：** HBM 晶片本身極其昂貴，且 2.5D 封裝成本高昂，僅適用於高利潤的資料中心 AI 加速器。
*   **維護性 (Maintainability)：** 由於晶片與記憶體封裝在一起，若其中一顆 HBM 損壞，整個封裝體可能都需要報廢。
*   **風險 (Risks)：** 嚴重受制於少數記憶體供應商（如 SK Hynix、Samsung）的 HBM 產能與晶圓代工廠的先進封裝產能（Capacity constraint）。

### 3. 基於 CXL 擴展的記憶體池化 (Memory Pooling)
透過 [[CXL互連技術標準]]（Compute Express Link），將大量的傳統記憶體模組（甚至未來的 NVM）組成獨立的記憶體池，讓多個 CPU/GPU 動態共享記憶體資源，實現 Scale-Out 的記憶體擴充。

*   **優點 (Pros)：** 打破了單一伺服器節點的記憶體容量限制，可配置 TB 級別的系統記憶體；提高記憶體利用率，降低閒置資源浪費。
*   **缺點 (Cons)：** 存取延遲（Latency）顯著高於直接連接的 HBM 或 GDDR；雖然容量大，但頻寬仍受限於 PCIe/CXL 介面頻寬。
*   **成本 (Costs)：** 需要額外的 CXL 控制器與 Switch 硬體，初期建置成本較高，但長期可能透過資源共享降低 TCO（總擁有成本）。
*   **維護性 (Maintainability)：** 資源動態分配需要強大的軟體與作業系統支援，增加系統管理複雜度。
*   **風險 (Risks)：** CXL 生態系與標準（如 CXL 2.0/3.0）仍在發展初期，不同廠商間的硬體相容性與軟體支援度仍有待驗證。

## 相關主題
* [[GPU架構與發展]]
* [[CXL互連技術標準]]
* [[PIM記憶體內運算]]