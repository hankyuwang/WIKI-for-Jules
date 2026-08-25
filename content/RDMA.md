---
title: RDMA
level: intermediate
tags:
  - AI
  - RDMA
  - Networking
---

# RDMA (Remote Direct Memory Access)

摘要：RDMA（遠端直接記憶體存取）是一種允許網路卡直接讀寫另一台伺服器記憶體的技術，過程中完全繞過作業系統核心與 CPU，實現極高頻寬、極低延遲與零拷貝通訊，是構建現代 AI 超級電腦與分散式訓練叢集的網路基石。

## Prerequisites
- [[基礎計算機結構]]
- [[InfiniBand]], [[RoCE]]

## 傳統網路通訊的瓶頸
在傳統的 TCP/IP 網路通訊中，當伺服器 A 要發送資料給伺服器 B 時：
1. 資料必須從應用程式的 User Space 拷貝到作業系統的 Kernel Space 緩衝區。
2. CPU 需要介入處理複雜的網路協定堆疊（打包、驗證）。
3. 接收端同樣需要經歷 CPU 處理與多次記憶體拷貝。
在巨型 AI 模型（如 LLM）的分散式訓練中，節點間需要頻繁交換海量的梯度（Gradients）與權重。如果依賴傳統 TCP/IP，CPU 將會被網路通訊完全佔用，且延遲極高，導致 GPU 大量時間處於閒置等待狀態（IO-Bound）。

## RDMA 的運作原理與優勢
RDMA 解決了上述問題，其核心優勢包括：
- **Zero-Copy (零拷貝)**: 應用程式可以直接向網路卡（NIC）下達指令，NIC 透過 PCIe 直接從 GPU 的 HBM 讀取資料並發送至網路上，接收端 NIC 再直接將資料寫入目標 GPU 的 HBM。整個過程資料不經過系統主記憶體。
- **Kernel Bypass (繞過核心)**: 通訊過程完全不需要作業系統 Kernel 的介入，避免了 Context Switch 所帶來的延遲。
- **CPU Offload (釋放 CPU)**: 所有的通訊協定處理都在網路卡（SmartNIC/DPU）的硬體層面完成，CPU 的負載接近於零，可以專注於其他任務。

## RDMA 的主流實現標準
RDMA 是一種技術概念，在實際硬體部署中主要分為三大陣營：
1. **InfiniBand (IB)**: 最純粹、效能最高的 RDMA 實現。它擁有自己獨立的網路協定、交換器與網卡，支援硬體層面的無損網路（Lossless Network），由 NVIDIA（收購 Mellanox）主導。
2. **RoCE (RDMA over Converged Ethernet)**: 允許 RDMA 協定跑在標準的乙太網（Ethernet）上。這使得資料中心不需要建置兩套獨立網路，大幅降低了成本，是目前各家雲端大廠與開放運算計畫（OCP）最積極推動的方向。
3. **iWARP**: 運行在傳統 TCP/IP 上的 RDMA，雖然相容性極高，但因為保留了 TCP 的負擔，效能不如前兩者，在 AI 領域較少使用。
