---
title: AI 模型分類與硬體協同設計
level: advanced
tags:
  - model
  - hardware
  - co-design
  - llm
  - cnn
---

# AI 模型分類與硬體協同設計

不同的 AI 模型架構具備截然不同的記憶體存取模式與運算強度 (Arithmetic Intensity)。理解這些模型分類，是設計 NPU 與 AI 加速硬體的關鍵。

## Prerequisites
- [[主流AI加速晶片架構分析]]

## 常見 AI 模型分類與特性

### 1. 卷積神經網路 (CNN) - e.g. YOLO, ResNet
- **運算特性**: 空間局部性 (Spatial Locality) 極高，大量重複使用相同的卷積核 (Weights) 在不同的圖像區塊上滑動。
- **Arithmetic Intensity (運算強度)**: 高。因為權重可以高度重用，對記憶體頻寬的需求相對可控。
- **硬體關聯與需求**:
  - 非常適合傳統的 Systolic Array，或是針對 2D 空間優化的運算單元。
  - 需要良好的 Line Buffer 設計或軟體的 Tiling 技術，將特徵圖 (Feature Maps) 留在 SRAM 中以降低對外部 DRAM 的存取。
  - **應用情境**: 大量應用於 Edge 端，如手機相機、安防攝影機的即時物件偵測，硬體設計重點在於極致的功耗效能比 (TOPS/W)。

### 2. 大型語言模型 (Dense LLM) - e.g. GPT-3, LLaMA
- **運算特性**: 核心為 Transformer 架構中的 Self-Attention 與 MLP (多層感知器)。推論過程通常分為兩個階段：
  - **Prefill (Prompt 處理階段)**: 平行度高，偏向 Compute-bound (算力受限)，矩陣相乘 (GEMM) 主導。
  - **Decode (生成 Token 階段)**: 逐字生成，矩陣-向量相乘 (GEMV) 主導，記憶體頻寬需求極高，偏向 Memory-bound。
- **Arithmetic Intensity**: 在 Decode 階段非常低。每次生成一個 Token 都需要將所有權重從 HBM 搬進 SRAM 算一次。
- **硬體關聯與需求**:
  - **極高的記憶體頻寬**: 這是為什麼 H100 必須搭載 HBM3/HBM3e 的原因。
  - **KV Cache 管理**: 為了避免重複計算歷史 context，硬體與軟體需有效管理 KV Cache 存在 SRAM/HBM 中的位置。
  - **應用情境**: 主要在雲端伺服器運行，依賴強大的 Scale-up 晶片。

### 3. 混合專家模型 (LLM MoE - Mixture of Experts) - e.g. Mixtral, GPT-4
- **運算特性**: 在前向傳播過程中，只有部分的「專家 (Experts)」神經網路被啟動。
- **Arithmetic Intensity**: 運算量比同等規模的 Dense 模型少很多，但「記憶體容量」需求依舊龐大 (所有專家的權重都需要存起來)。存取模式變得稀疏且難以預測。
- **硬體關聯與需求**:
  - **動態記憶體存取 (Gather/Scatter)**: 對於 GPU 來說，MoE 容易造成記憶體存取的不連續。硬體需要強大的跨節點 (Inter-node) 頻寬，因為不同 Token 挑選的 Expert 可能存放在不同 GPU 的 HBM 裡 (如 NVLink 扮演關鍵角色)。
  - **應用情境**: 雲端大規模叢集。MoE 對網路頻寬的要求有時甚至高於單卡算力。

### 4. 擴散模型 (Diffusion Models) - e.g. Stable Diffusion
- **運算特性**: 反覆迭代去噪 (Denoising)，通常結合了 CNN (U-Net) 與 Transformer (Cross-Attention)。
- **硬體關聯與需求**:
  - 記憶體消耗極大，特別是在高解析度圖片生成時的 Activation 尺寸會暴增。
  - 推論時間長，硬體設計若能加速 Attention 運算 (如 [[FlashAttention3與極低精度量化硬體需求|FlashAttention]] 的硬體化支援) 將大幅受益。

## 軟硬體協同設計的核心思維

現代 AI 晶片的設計已不再是單純疊加硬體規格，而是 **Software/Hardware Co-design**:

1. **Memory Wall 的突破**: 運算速度 (TOPS) 的增長遠快於記憶體頻寬 (GB/s) 的增長。硬體架構設計必須圍繞著「如何減少從 DRAM 讀取資料」，例如 Groq 的超大 SRAM 設計。
2. **算子融合 (Operator Fusion)**: 將多個小算子 (如 Conv -> BatchNorm -> ReLU) 融合在一起，資料留在暫存器或 SRAM 中直接接續計算，這需要編譯器 (Software) 與彈性的硬體管線 (Hardware) 互相配合。
3. **資料格式創新**: 從 FP32 到 FP16，再到目前的 FP8、INT4 甚至 1-bit LLM (如 BitNet)。硬體必須提早預判軟體演算法的趨勢，加入對低精度資料格式的原生支援，以節省記憶體與算力。

---
*相關閱讀*：
- [[AI加速晶片軟體堆疊與SDK設計]]
- [[自研AI晶片策略與前沿挑戰]]