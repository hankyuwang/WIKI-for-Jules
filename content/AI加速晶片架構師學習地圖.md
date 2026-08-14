---
title: AI加速晶片架構師學習地圖
level: intermediate
tags:
  - learning-map
  - architect
  - ai-hardware
---

# AI加速晶片架構師學習地圖

摘要：本學習地圖旨在提供一個由淺入深的 Top-Down 學習框架，幫助有志成為 AI 加速晶片架構師的學習者，系統性地掌握模型訓練與推論基礎、AI SDK 與軟體堆疊、編譯器優化、以及底層硬體架構設計等關鍵知識。這份地圖不僅列出必備關鍵字，也探討了模型演進如何影響硬體設計，以及常見的設計挑戰。

## 1. 如何成為一個 AI 加速晶片架構師

要成為一名稱職的 AI 加速晶片架構師，必須具備「全端（Full-Stack）」的思維，也就是不僅要懂硬體設計（如 PPA：Power, Performance, Area），更要深刻理解軟體行為與 AI 模型特性。晶片架構的設計往往是為了解決特定軟體與模型的痛點（例如記憶體牆、通訊瓶頸）。因此，學習路徑必須從最上層的應用與模型，向下貫穿軟體編譯，最終抵達底層硬體架構。

## 2. 學習知識樹狀圖 (Top-Down 框架)

**AI加速晶片架構師核心知識體系**
- 1. AI 演算法與模型行為 (Algorithm & Model Behavior)
  - 模型基礎知識
    - 訓練 (Training)：[[反向傳播]]、[[梯度下降]]、[[Optimizer]] 狀態
    - 推論 (Inference)：[[Prefill]] vs. [[Decode]] (Memory-bound vs Compute-bound)
  - 關鍵神經網路架構
    - [[Transformer]] ([[FlashAttention3與極低精度量化硬體需求|Attention]] 機制、[[KV Cache]])
    - [[CNN]], [[RNN]] (歷史背景與邊緣應用)
    - [[MoE]] (Mixture of Experts)、[[Mamba]]/[[SSM]] (最新演進)
  - 模型演進對硬體的影響
    - 參數規模爆炸 ([[LLM推理擴展與效能瓶頸分析|LLM]]) -> 記憶體容量與頻寬需求急劇上升
    - 長文本 ([[Long Context]]) -> [[KV Cache]] 瓶頸、分散式通訊需求

- 2. 軟體堆疊與 SDK (Software Stack & SDK)
  - 主流生態系
    - NVIDIA [[CUDA]] / [[cuDNN]] / [[TensorRT]]
    - AMD [[ROCm]], Intel [[OneAPI]]
  - 深度學習框架
    - [[PyTorch]], [[TensorFlow]], [[JAX]]
  - 分散式訓練框架
    - [[Megatron]]-LM, [[DeepSpeed]] (資料平行、張量平行、管線平行)

- 3. 編譯器與軟硬體協同優化 (Compiler & Co-design)
  - 圖級優化 (Graph-level Optimization)
    - [[算子融合]] ([[Operator Fusion]])、記憶體配置優化
  - 核心編譯器與 IR (Intermediate Representation)
    - [[MLIR]], [[XLA]], [[TVM]], [[Triton]]
  - 低精度量化技術 ([[Quantization]])
    - [[FP16]], [[BF16]], [[INT8]], [[FP8]], [[INT4]]
    - 量化感知訓練 ([[QAT]]) vs. 訓練後量化 ([[PTQ]])

- 4. 硬體架構設計 (Hardware Architecture)
  - 核心運算單元
    - [[MAC]] (Multiply-Accumulate)
    - [[TPU與脈動陣列|脈動陣列]] ([[Systolic Array]]) - Google [[TPU]] 經典設計
    - [[SIMD]] / [[SIMT]] - [[GPU]] 核心架構
  - 記憶體階層 (Memory Hierarchy)
    - On-chip [[SRAM]] (Global Buffer, Scratchpad)
    - Off-chip Memory ([[HBM]], [[GDDR]], [[LPDDR]])
  - 晶片間互連與通訊 (Interconnect & Communication)
    - 晶片內：[[NoC]] (Network on Chip)
    - 晶片間：[[NVLink]], [[PCIe]], [[CXL]]
    - 網路層：[[InfiniBand]], [[RDMA]], [[RoCE]] v2
  - 先進封裝與異質整合
    - 2.5D/3D 封裝 ([[CoWoS]])
    - [[小晶片]] ([[Chiplet]])
    - [[矽光子]]/光電共封裝 ([[CPO]])



## 3. 學習與職涯發展方案觀點分析

### 方案一：硬體底層出發 (Hardware-First Approach)
- **優點 (Pros):** 擁有扎實的數位邏輯、RTL 設計與計算機結構基礎，對 PPA (Power, Performance, Area) 有極高的敏銳度，適合開發極致效能的底層 IP。
- **缺點 (Cons):** 容易陷入「為設計而設計」的盲點，缺乏對 AI 模型實際行為與痛點的理解，設計出來的架構可能難以被編譯器有效利用。
- **成本 (Costs):** 需要長期的硬體設計經驗累積與 EDA 工具學習。
- **維護性 (Maintainability):** 所設計的硬體若不具備通用性，當 AI 模型快速演進時（如從 [[CNN]] 轉向 [[Transformer]]），硬體架構容易被淘汰。
- **風險 (Risks):** 可能設計出「算力極高但利用率極低」的晶片。

### 方案二：軟體/編譯器出發 (Software-First Approach)
- **優點 (Pros):** 深刻理解 AI 模型的發展趨勢（如 [[MoE]]、長文本）以及編譯器優化的極限。能夠從演算法的角度定義硬體規格，提出能被軟體高效利用的指令集或加速單元。
- **缺點 (Cons):** 可能對底層硬體物理限制（如佈線延遲、功耗牆、面積限制）理解不夠深刻，導致提出的架構在實體合成 (Physical Synthesis) 時難以實現。
- **成本 (Costs):** 需要精通複雜的編譯器架構（如 [[MLIR]], [[Triton]]）與底層驅動程式開發。
- **維護性 (Maintainability):** 軟體定義硬體的思維有助於開發高度靈活且可編程的架構，能較好地應對未來的演算法變更。
- **風險 (Risks):** 規格定義可能過於理想化，導致晶片 PPA 表現不佳。

### 方案三：軟硬體協同設計 (Hardware-Software Co-Design Approach) - 推薦路徑
- **優點 (Pros):** 結合軟硬體雙方的視角，在晶片定義初期就讓編譯器團隊與硬體團隊共同參與。能精準打擊系統瓶頸（如設計專屬的 [[KV Cache]] 管理單元或非同步通訊引擎）。
- **缺點 (Cons):** 學習曲線極為陡峭，要求架構師成為跨領域的通才（Generalist），溝通成本極高。
- **成本 (Costs):** 培養此類人才需要大量的跨部門專案實戰經驗，時間成本最高。
- **維護性 (Maintainability):** 開發出的架構通常能在效能與泛用性之間取得最佳平衡，生命週期最長。
- **風險 (Risks):** 要求個人極高的學習能力與持續追蹤前沿論文的毅力，容易因技術迭代過快而面臨知識焦慮。

## 4. 延伸閱讀與全景探索 (Extended Reading & Landscape Exploration)
- [[AI加速晶片全景探索]] : 涵蓋各廠 AI 加速晶片架構比較、應用與自研策略。
- [[主流AI加速晶片架構分析]] : 各大廠晶片硬體架構、應用情境與市場定位。
- [[自研AI晶片發展策略]] : 探討開發自研 AI 晶片的主要策略。
- [[邊緣運算AI晶片]] : 邊緣運算場景下的 AI 加速硬體方案。
- [[AI效能分析相關議題與最新進展]] : 廣度優先探索 AI 效能分析的最新進展與解決方案。
- [[AI晶片未來發展趨勢]] : AI 晶片架構發展趨勢與挑戰。

### 新增知識節點 (New Topics)
- [[Optimizer]] : 優化器在訓練時的記憶體瓶頸與解決方案 (如 ZeRO)。
- [[cuDNN]] : 深度學習框架底層依賴的 GPU 基礎運算加速庫。
- [[反向傳播]] : 梯度計算機制、記憶體限制與分散式訓練優化。
- [[梯度下降]] : 模型優化演算法原理及進階自適應調整策略。
