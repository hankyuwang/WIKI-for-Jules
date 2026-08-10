---
title: AI模型分類與硬體架構關聯
level: intermediate
tags:
  - ai-model
  - hardware-architecture
  - llm
  - moe
  - yolo
---

# AI 模型分類與硬體架構關聯

不同的 AI 模型在運算 (Compute) 與記憶體存取 (Memory Access) 上的行為有著根本的差異。這決定了它們在不同硬體架構上運行時，會面臨不同的瓶頸。本篇分析目前主流 AI 模型分類，並探討它們與硬體架構間的關聯。

## 1. LLM Dense (大型語言模型 - 密集架構)
**代表模型**: Llama-3.1, GPT-4, BERT

*   **模型特徵**:
    *   **龐大的參數與矩陣**: 模型完全由巨大的 Dense Matrix (如 $W_Q, W_K, W_V$ 等 Attention 權重，以及 FFN 權重) 構成。
    *   **每次 Inference 需讀取所有權重**: 無論輸入什麼，每次生成一個 Token，幾乎所有的模型權重都要從記憶體讀取一次。
    *   **Compute to Memory Access Ratio (Arithmetic Intensity)**: 在 Inference 時 (Batch Size = 1)，Arithmetic Intensity 極低。
*   **硬體瓶頸**: **Memory Bound (受限於記憶體頻寬)**。算力再高也沒有用，因為資料餵不進運算單元。
*   **理想的硬體架構**:
    *   **極高的記憶體頻寬**: 必須採用 HBM3/HBM3e (如 NVIDIA H100, AMD MI300X)。
    *   **大容量 On-chip Cache/SRAM**: 盡可能將 KV Cache 留在晶片內 (如 AMD 的大 Infinity Cache 或 Groq 的全 SRAM 架構)。
    *   **架構關聯**: 這解釋了為什麼 Groq 放棄 HBM 改用全 SRAM，就是為了打破 LLM 生成時的 Memory Wall；也解釋了為何 AMD MI300X 的 192GB HBM 這麼受歡迎。

## 2. LLM MoE (Mixture of Experts - 混合專家模型)
**代表模型**: Mixtral 8x7B, GPT-4 (傳聞)

*   **模型特徵**:
    *   **稀疏啟動 (Sparse Activation)**: 模型包含多個 Expert (子網路)，但每次輸入只有少數 (例如 2 個) Expert 會被啟動。
    *   **總參數量大，但活躍參數量小**: 參數總量極大，但單次 Inference 的運算量(FLOPs)與活躍參數卻只有 Dense 模型的數分之一。
    *   **All-to-All 通訊**: 在分散式叢集中，Token 需要被路由(Routing)到不同的 GPU/節點上對應的 Expert。
*   **硬體瓶頸**: **Memory Capacity Bound (受限於記憶體容量) & Network Bound (受限於網路通訊)**。
*   **理想的硬體架構**:
    *   **極大的記憶體容量**: 需要把所有 Expert 的權重都載入，因此單卡/單節點的 HBM 容量必須極大 (AMD MI300X 再次佔優)。
    *   **超高速的晶片間互連網路**: NVLink (NVIDIA) 或是 OCS (Google TPU) 在處理 MoE 的 Expert Routing 時至關重要。缺乏高速互連的架構在跑 MoE 時效能會暴跌。

## 3. CNN / Vision (卷積神經網路 / 電腦視覺)
**代表模型**: YOLO, ResNet, MobileNet

*   **模型特徵**:
    *   **局部性 (Locality) 極高**: 卷積核 (Convolution Kernel) 重複掃描輸入影像，同一筆資料被多次重複使用。
    *   **High Arithmetic Intensity**: 運算量大，但記憶體存取相對較小 (Weight Reuse)。
    *   **Feature Map 記憶體消耗**: 訓練時需要儲存每一層的 Feature map 供 Backpropagation 使用，Inference 時只需存留相鄰層。
*   **硬體瓶頸**: 通常是 **Compute Bound (受限於算力)** 或 **SRAM Capacity Bound**。
*   **理想的硬體架構**:
    *   **Systolic Array**: 最適合跑卷積運算，Google TPU 或各種 Edge NPU 內建的 MAC Array 效率極高。
    *   **Software-managed SRAM**: 將 Feature map 放在 SRAM 中，透過軟體(或編譯器)排程 Tiling (分塊運算)，可以做到幾乎不需要存取外部 DRAM (Zero-overhead Tiling)。
    *   **架構關聯**: Edge 端晶片 (如 Apple ANE, 樹莓派上的 Hailo) 只要配置適當的 SRAM 和高效率的 MAC Array，即使沒有 HBM，也能以極低功耗將 YOLO 跑得非常快。

## 4. SSM (State Space Models) / Mamba
**代表模型**: Mamba, Jamba

*   **模型特徵**:
    *   **RNN 的變體**: 捨棄了 Transformer 的 Attention 機制，不需要儲存龐大的 KV Cache。狀態 (State) 被壓縮在固定大小的 Hidden State 中。
    *   **Hardware-aware Algorithm**: Mamba 的核心算子 (Selective Scan) 被設計為必須在 SRAM 中完成所有掃描操作，再寫回 HBM。
*   **硬體瓶頸**: **SRAM 頻寬與容量，以及算子融合 (Kernel Fusion) 的能力**。
*   **理想的硬體架構**:
    *   **大型 SRAM (Shared Memory)**: GPU 的 Shared Memory (如 H100) 或 TPU 的 Vector Memory 是關鍵。如果晶片的 SRAM 太小，無法將 State 留在內部進行掃描，Mamba 的效能優勢就會消失。
    *   **靈活的編程介面**: 需要能高度客製化 Kernel (如使用 CUDA/Triton) 以實現 SRAM 層級的融合。

## 總結
*   **買算力不等於買效能**：硬體架構必須與模型特性匹配。
*   **LLM 時代是記憶體的戰爭**：HBM 的容量與頻寬決定了 Dense 與 MoE 模型的極限。
*   **SRAM 是隱藏的王者**：無論是 Edge 端的 CNN (YOLO)，還是雲端的 Mamba，或是 Groq 的極端路線，如何有效利用 On-chip SRAM 避免存取 DRAM，是 AI 加速晶片架構設計的終極課題。
