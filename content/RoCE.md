---
title: RoCE (RDMA over Converged Ethernet)
level: intermediate
tags:
  - AI
  - RoCE
  - RDMA
  - Networking
---

# RoCE (RDMA over Converged Ethernet)

摘要：RoCE (RDMA over Converged Ethernet) 是一種允許在乙太網路上運行 RDMA（遠端直接記憶體存取）的網路協議。它結合了 RDMA 的低延遲、高頻寬優勢與乙太網路的廣泛普及性及低成本。

## 技術背景與演進
在傳統網路架構中，資料傳輸需要經過 CPU 及作業系統核心的 TCP/IP 網路堆疊，這會產生顯著的延遲與 CPU 資源消耗。RDMA 技術允許網路卡 (NIC) 直接讀寫應用程式的記憶體，繞過 CPU，從而大幅降低延遲。最初，RDMA 主要是基於 [[InfiniBand]] 網路實現的，但 InfiniBand 成本高昂且不相容於一般資料中心的乙太網路架構。
為了解決這個問題，RoCE 應運而生：
- **RoCE v1**：基於乙太網路鏈路層運作，但無法跨越多個子網路由，限制了其在大規模資料中心的應用。
- **RoCE v2**：基於 UDP/IP 協議運行，具備完整的路由能力，成為現代 AI 雲端資料中心與大型叢集的主流標準。

## 擁塞控制 (Congestion Control) 挑戰
與無損的 [[InfiniBand]] 不同，傳統乙太網路是會丟包的（Best-Effort）。為了在乙太網路上完美運行 RDMA，必須確保網路是「無損的」(Lossless)。這依賴於先進的擁塞控制機制：
- **PFC (Priority-based Flow Control)**：防止交換機緩衝區溢出，當壅塞發生時，通知發送端暫停發送特定優先級的封包。
- **ECN (Explicit Congestion Notification)**：在封包中標記擁塞狀態，讓接收端通知發送端降低發送速率。

## 業界應用現況
雖然大型的 AI 訓練叢集（如 Nvidia SuperPOD）歷史上傾向使用 [[InfiniBand]]，但隨著雲端服務商（如 AWS, Azure, GCP）的大規模採用，基於 RoCE v2 的乙太網路架構正在迅速普及。其優勢在於能利用現有的乙太網路交換機硬體，大幅降低基礎設施的建置與維護成本，並達到與 InfiniBand 相當的效能水準。



## 虛擬團隊補充說明：RoCEv2 的實務痛點與優化策略

對於預算有限或希望統一網路架構 (單一乙太網路) 的團隊來說，RoCEv2 是一個非常吸引人的方案。但實務上，要讓 RoCEv2 發揮出接近 InfiniBand 的效能，必須解決以下痛點：

1. **PFC (Priority-based Flow Control) 的死鎖問題**：
   RoCEv2 依賴 PFC 來實現無損網路。當接收端緩衝區滿時，會發送暫停訊號 (Pause Frame) 給發送端。在複雜拓撲中，這可能導致環狀的暫停，造成網路死鎖 (PFC Deadlock)，甚至引發 PFC 風暴癱瘓整個網路。
2. **ECN (Explicit Congestion Notification) 的調優難度**：
   為了在封包丟失前減緩發送速度，必須精細調校交換機的 ECN 閾值。這個調校過程非常複雜，且對於不同特性的 AI 訓練流量 (如 All-Reduce vs All-to-All) 的最佳參數可能完全不同。

**優化策略與最佳實務**：
- **實體隔離**：強烈建議將 AI 訓練的 RoCEv2 流量與一般儲存或管理網路 (TCP/IP) 進行實體隔離，使用專屬的交換機與網卡。
- **智慧網卡 (SmartNIC/DPU)**：利用現代 DPU (如 Nvidia BlueField 或 AMD Pensando) 將擁塞控制與 RDMA 處理邏輯卸載到網卡上的硬體加速器，減輕 CPU 負擔並提升網路穩定性。
- **監控與可見度**：部署細粒度的網路遙測 (Telemetry) 系統，即時監控 PFC 暫停幀的數量與佇列深度，才能在效能崩潰前找到瓶頸點。
