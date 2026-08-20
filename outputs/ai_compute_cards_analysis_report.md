# AI 算力卡規格分析報告

## 1. 他們通常顯示甚麼規格
根據市面上的 AI 算力卡（如 MirrorFrog 上所列資料），通常顯示的核心規格包含：
- **Chip / Architecture (架構)**：如 GPU, NPU, ASIC, TPU, LPU 等，或具體的微架構代號（如 NVIDIA Blackwell, AMD CDNA）。
- **Memory (記憶體容量與類型)**：例如 HBM3e, HBM3, GDDR6X 等。
- **Bandwidth (記憶體頻寬)**：例如 8 TB/s, 3.35 TB/s, 1.6 TB/s。
- **FP16 / BF16 Performance (半精度浮點運算效能)**：例如 2,700 TFLOPS, 1,000 TFLOPS 等，代表算力。
- **TDP (熱設計功耗)**：例如 1000W, 700W, 350W，代表功耗。
- **Category (分類定位)**：如 Training (訓練), Inference (推理), Workstation/Consumer, Edge 等。

*(註：對於未公開之次世代硬體規格如 TPU v7，需聲明其詳細規格尚未公開。)*

## 2. 這些規格為什麼重要? 原因是?
- **Memory (容量)**：決定了能夠載入多大的 AI 模型參數與 Context Window。若容量不足，則需跨多張卡切割模型，增加通訊延遲。
- **Bandwidth (頻寬)**：決定了資料餵給運算核心的速度，直接影響推理生成階段的極限速度，解決所謂的「記憶體牆」問題。
- **FP16 / TFLOPS (算力)**：代表硬體在單位時間內能處理多少次矩陣乘加運算，直接影響訓練時間與模型推理的預填充 (Prefill) 速度。
- **TDP (功耗)**：資料中心供電與散熱有極限，功耗決定了能密集部署多少張卡，同時影響營運成本 (TCO)。

## 3. 甚麼樣的規格代表優劣?
優劣的衡量通常不僅看絕對值，還看性價比與能效比：
- **容量與頻寬越高越好**：如 HBM3e 優於 HBM3，讓模型不會卡在等資料。
- **FLOPS/W (能效比) 越高越優**：在同等功耗下榨出更多算力。
- **適用場景對應**：
  - 訓練端 (Training)：極度需要高 FP16/BF16 算力與高速互連網絡。
  - 推理端 (Inference)：極度依賴極高的記憶體頻寬與低延遲架構。

## 4. 這些規格與 AI model 間的關係是?
- **參數規模 (Parameters) ↔ Memory 容量**：千億參數模型需要大量 HBM 存放權重與推理時產生的 Context (如 KV Cache)。
- **運算階段 (Prefill vs Decode)**：
  - **Prefill (理解 Prompt)**：屬於 Compute-bound，吃重 FLOPS 算力 (如 FP16/BF16)。
  - **Decode (生成 Token)**：屬於 Memory-bound，吃重 Memory Bandwidth (頻寬)，算力往往不是瓶頸。
- **資料精度 (Precision) ↔ 演算法優化**：AI 模型逐漸採用低精度量化技術 (Quantization)，硬體若原生支援更低精度 (如 FP8/INT4)，能在不增加硬體成本下，成倍擴大模型吞吐量。
