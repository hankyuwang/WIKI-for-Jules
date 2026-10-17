# Wiki 定期巡檢報告

## 1. 失效連結 (Dead Links)
- 發現並修復了 1 個失效連結：
  - `GPU運算架構.md` 中的 `[[Tensor Core]]` 修改為一般文字 `Tensor Core`。

## 2. 過時版本 (Outdated Versions)
- 未發現 CUDA 10 或 TensorFlow 1.x 等明顯過時的版本資訊。

## 3. 已棄用架構 (Deprecated Architectures)
- 已將多份文件中的過時架構更新為具有歷史準確性的描述：
  - `Volta` 更新為 `早期 Volta`
  - `TPU v1` 更新為 `早期 TPU v1`
  - `TPU v2` 更新為 `早期 TPU v2`
- 更新涵蓋的文件包含 `GPU 架構與演進.md`, `GPU架構與AI計算.md`, `NVLink.md`, `TPU與專用AI晶片.md`, `Systolic Array.md`, `TPU深度解析.md` 等。

## 4. 官方文件或是論文更新 (Official Document / Paper Updates)
- 文件庫已廣泛涵蓋最新的重點論文與技術：
  - **FlashAttention/FlashAttention-3**: 頻繁出現於多份文件 (如 `cuDNN.md`, `Triton.md`, `LLM推理最佳實務.md`)。
  - **LLaMA 3**: 已被包含於 `知名大廠AI加速晶片研究.md` 等。
  - **推理框架**: `vLLM`, `TensorRT-LLM`, `SGLang`, `PagedAttention` 已在最新推論實務文件內。

## 5. 新最佳實務 (New Best Practices)
- 文件庫已跟上當前最佳實務：
  - **低精度量化**: `FP4`, `FP8`, `INT4`, `INT8` 已大量涵蓋。
  - **新架構**: `MoE`, `Mamba`, `SSM` 已詳細探討。
  - **軟體開銷**: `Zero-overhead` 技術已在多份硬體分析文件中涵蓋。
