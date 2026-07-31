---
title: AI模型分類與硬體架構關聯
level: intermediate
tags:
  - ai-model
  - hardware-architecture
  - bottleneck
---

# AI模型分類與硬體架構關聯

不同的 AI 模型結構對硬體資源的依賴截然不同。了解模型架構與硬體之間的對應關係，有助於設計或選擇合適的 [[NPU架構探索|AI加速晶片]]。

## 1. LLM Dense (大型語言模型 - 密集網路)
- **特徵**：由大量 Transformer Block 組成，每一層都包含巨大的權重矩陣（如 GPT-3/4）。
- **瓶頸分類**：**Memory Bound (記憶體受限)**
- **硬體需求分析**：
  - 在生成階段（Decoding / Token-by-Token），Batch Size 通常較小，運算量小但需要將龐大的權重從記憶體讀入運算單元。
  - 此時的瓶頸是記憶體頻寬 (Memory Bandwidth)。因此，硬體設計極度依賴 HBM (High Bandwidth Memory) 或 SRAM-centric 架構（如 Groq）來突破頻寬限制。

## 2. MoE (Mixture of Experts - 混合專家模型)
- **特徵**：每個 Token 只啟動網路中的部分子網路（Experts），整體模型參數極大，但每次推理的活躍參數較少。
- **瓶頸分類**：**Capacity Bound (容量受限) & Network Bound (網路/互連受限)**
- **硬體需求分析**：
  - 需要極大的記憶體容量來存放所有 Experts 的權重。
  - 在分散式運算時，Token 需要被發送到存放對應 Expert 的節點上處理（All-to-All 通訊），這對晶片間互連網路 (Interconnect, 如 NVLink/TPU ICI) 的頻寬和延遲提出了極高要求。

## 3. CNN / YOLO (卷積神經網路 / 電腦視覺)
- **特徵**：大量的卷積層 (Convolution)，具有極高的資料重複使用率 (Data Reuse)。
- **瓶頸分類**：**Compute Bound (算力受限) & SRAM Bound (晶片內存受限)**
- **硬體需求分析**：
  - 由於資料重複使用率高，這類模型非常適合使用 [[Systolic Array]] 來最大化乘加運算 (MAC) 的吞吐量。
  - 重點在於晶片內的 SRAM 容量與資料搬移排程 (Dataflow, 如 Weight Stationary 或 Output Stationary)，以減少對外部 DRAM 的存取。

## 4. Mamba / SSM (State Space Models)
- **特徵**：近期興起的架構，具有 RNN 的特性，推論時不需要像 Transformer 的 Attention 機制保留長長的 KV Cache。
- **瓶頸分類**：相對平衡，但偏向 **SRAM/Register Bound**
- **硬體需求分析**：
  - 狀態變數 (Hidden States) 會在時間步之間傳遞，需要快速的晶片內存 (SRAM) 來保存狀態。
  - 對外部記憶體頻寬的依賴（尤其在長文本推論時）大幅低於 Transformer，非常適合部署在記憶體受限的邊緣裝置上。
