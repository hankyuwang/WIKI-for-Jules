---
title: AI 加速晶片全景探索
level: advanced
tags:
  - ai-chips
  - hardware
  - architecture
  - strategy
---

# AI 加速晶片全景探索

這篇筆記探討目前主流 AI 加速晶片的架構、使用場景與生態系，並分析邊緣運算的挑戰與新創團隊的硬體策略。

## Prerequisites
- [[NPU架構探索]]
- [[基礎計算機結構]]

## 主流 AI 晶片分析

### NVIDIA H100
- **使用場景**: 雲端資料中心、大型語言模型 (LLM) 訓練與推理。
- **硬體特點**: Hopper 架構，支援 FP8 運算，擁有 Transformer Engine，搭配高頻寬記憶體 (HBM3)。
- **關聯模型**: GPT-4, Llama 3 等超大型模型。
- **SDK 生態系**: CUDA, cuDNN, TensorRT。擁有最龐大且成熟的開發者社群，近乎是目前的產業標準。

### Google TPU v5p
- **使用場景**: Google Cloud 上的大規模 AI 訓練與推理。
- **硬體特點**: 專為機器學習矩陣運算高度最佳化，支援 OCI (Optical Circuit Switches) 以極高頻寬連結超級電腦叢集。
- **關聯模型**: Gemini 家族模型, PaLM。
- **SDK 生態系**: TensorFlow, JAX (XLA Compiler)。與 Google 基礎設施深度整合，效能極高但與硬體綁定較深。

### Apple ANE (Apple Neural Engine)
- **使用場景**: 行動裝置與邊緣運算 (iPhone, iPad, Mac)。
- **硬體特點**: 整合於 Apple Silicon SoC 中，專注於低功耗的即時推理，適合處理相機影像與語音識別。
- **關聯模型**: Core ML 支援的各類行動端模型、On-device LLMs。
- **SDK 生態系**: Core ML。開發體驗高度封閉且最佳化，適合 Apple 生態圈的應用開發。

### Groq LPU (Language Processing Unit)
- **使用場景**: 超低延遲的 LLM 推理。
- **硬體特點**: 採用 Deterministic (確定性) 架構，屏除傳統 GPU 複雜的排程器，確保極低的 P99 延遲。
- **關聯模型**: Llama 3, Mixtral 等開源模型。
- **SDK 生態系**: GroqCompiler。主打不需 CUDA 就能將 PyTorch 模型編譯執行，以提供極速的推理 API 為賣點。

## 邊緣運算面臨的挑戰
在邊緣端 (Edge) 執行 AI 模型常遭遇以下挑戰：
1. **功耗限制 (Power Budget)**: 邊緣裝置電池容量與散熱能力有限。
2. **記憶體頻寬 (Memory Bandwidth)**: LLM 推理往往是 Memory-bound，邊緣裝置的 LPDDR 頻寬難以滿足。
3. **軟硬體破碎化**: 不同廠商的 NPU 架構與工具鏈 (Toolchain) 差異巨大，難以做到 Write once, run everywhere。

## 新創團隊硬體策略 (Strategy for small startups)

對於資源有限的新創團隊，在選擇 AI 運算方案時可以考慮以下三種策略：

### 方案一：依賴公有雲 API (如 OpenAI, Anthropic, Groq)
- **優點**: 初期無須購買昂貴硬體，開發速度最快，可隨插即用。
- **缺點**: 依賴外部服務，資料有隱私疑慮，且長期大規模使用成本高昂。
- **成本**: 初期極低 (Pay-as-you-go)，後期規模擴大後邊際成本較高。
- **維護性**: 極高，無須維護硬體或叢集。
- **風險**: 第三方服務不穩定或 API 政策改變。

### 方案二：租用雲端 GPU / TPU 部署開源模型 (如 AWS, GCP, 算力池)
- **優點**: 對模型與資料擁有完全控制權，可自訂微調 (Fine-tuning)。
- **缺點**: 需要 DevOps 技能來維護基礎架構與模型部署，遇到流量突發時擴充 (Auto-scaling) 難度較高。
- **成本**: 中等，需支付固定的 Instance 費用或搶佔式實例 (Spot Instances)。
- **維護性**: 中等，需要有專職工程師維護部署架構。
- **風險**: 算力供應短缺時可能租不到機器。

### 方案三：自建邊緣運算裝置 / 購買消費級 GPU 叢集
- **優點**: 網路延遲最低 (若為邊緣裝置)，資料完全落地，長期來看運算成本可能較低。
- **缺點**: 初期資本支出 (CAPEX) 龐大，硬體維護成本高。
- **成本**: 初期極高 (購買硬體)，後續為電費與維護費。
- **維護性**: 差，硬體故障、散熱與網路架構都需要自行解決。
- **風險**: 硬體汰舊換新速度快，投資可能迅速貶值。
