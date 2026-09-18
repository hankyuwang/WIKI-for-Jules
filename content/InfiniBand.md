---
title: InfiniBand
level: advanced
tags:
  - AI
  - InfiniBand
  - RDMA
  - Networking
---

# InfiniBand

摘要：InfiniBand 是一種專為高效能運算 (HPC) 與大型 AI 訓練叢集設計的超高速、低延遲電腦網路互連標準，具備硬體級的無損傳輸與極高的頻寬。

## 核心架構與優勢
在大型分散式 AI 訓練（如千卡或萬卡 GPU 叢集）中，節點間同步梯度與傳遞張量的網路延遲會直接成為效能瓶頸。傳統基於乙太網路與 TCP/IP 的架構會消耗大量 CPU 資源並產生不可控的延遲。
InfiniBand 的設計從底層解決了這些問題：
- **原生支援 RDMA**：InfiniBand 從設計之初就是為了支援 RDMA (Remote Direct Memory Access)，允許硬體直接存取遠端記憶體，完全繞過作業系統與 CPU，實現微秒級甚至奈秒級的延遲。
- **基於信用的流量控制 (Credit-based Flow Control)**：不同於乙太網路在丟包後才重傳，InfiniBand 發送端必須在確認接收端有足夠的緩衝區「信用」(Credits) 時才會發送資料。這從根本上保證了網路是無損的 (Lossless)，避免了丟包重傳帶來的延遲抖動。
- **硬體卸載 (Hardware Offloading)**：許多通訊協議的處理都由 InfiniBand 網路卡（如 Nvidia ConnectX 系列）的硬體負責，釋放了寶貴的 CPU 算力。

## 在 AI 基礎設施中的角色
目前的旗艦級 AI 訓練基礎設施（例如 Nvidia 的 DGX SuperPOD）幾乎清一色採用 InfiniBand 架構，透過其特有的交換機（如 Quantum 系列）連接成千上萬顆 GPU。相較於伺服器內部的互連（如 PCIe 或 NVLink），InfiniBand 主要負責跨機架、跨伺服器節點 (Node-to-Node) 的高速通訊。

## 與乙太網路 / RoCE 的比較
雖然 InfiniBand 提供了最頂尖的效能，但其供應鏈封閉（主要由 Nvidia 主導）、硬體成本高昂，且與傳統資料中心的乙太網路不相容。這促使了雲端供應商積極發展替代方案，如 [[RoCE]] (RDMA over Converged Ethernet)，試圖在標準乙太網路上重現 InfiniBand 的效能。



## 虛擬團隊補充說明：InfiniBand 的實務挑戰與未來趨勢

雖然 InfiniBand (IB) 在效能上無可挑剔，但在大規模部署時，基礎設施團隊往往面臨以下挑戰：

1. **網路拓撲的複雜性**：為了達成無阻塞 (Non-blocking) 的通訊，大型 IB 網路常採用胖樹 (Fat-Tree) 或 Dragonfly 等複雜的拓撲結構。這需要大量的交換機與光纜，網路佈線與維護成本極高。
2. **廠商鎖定 (Vendor Lock-in)**：目前高效能 IB 市場幾乎由 Nvidia (收購 Mellanox 後) 獨佔。這種單一供應商的局面會導致議價空間小，且硬體交期難以控制。
3. **維運學習曲線**：IB 的網路管理協議與傳統乙太網路完全不同 (如 Subnet Manager 的設定)，IT 團隊需要重新培訓。

**未來趨勢：Ultra Ethernet 聯盟 (UEC) 的崛起**
由於 IB 的封閉性，包含 AMD, Intel, Microsoft, Meta 等科技巨頭聯合成立了 Ultra Ethernet Consortium (UEC)。他們的目標是改良傳統乙太網路，解決 RoCEv2 在擁塞控制與擴展性上的缺點，試圖打造出一個在效能上能媲美 IB，且具備開放標準的「AI 專用乙太網路」。
對於未來 AI 基礎設施的發展，IB 與進化版乙太網路的競爭將是觀察重點。
