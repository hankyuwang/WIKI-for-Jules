# Wiki 定期巡檢報告

- [x] 新最佳實務: 檔案 `HBM技術與AI硬體瓶頸.md` 提及 `FlashAttention`，應更新為最新的 `FlashAttention-2` 或 `FlashAttention-3` 以反映最新最佳實務。
- [x] 新最佳實務: 檔案 `cuDNN.md` 提及 `FlashAttention`，應更新為最新的 `FlashAttention-2` 或 `FlashAttention-3` 以反映最新最佳實務。
- [x] 新最佳實務: 檔案 `AI加速器晶片研究.md` 提及 `FlashAttention`，應更新為最新的 `FlashAttention-2` 或 `FlashAttention-3` 以反映最新最佳實務。
- [x] 新最佳實務: 檔案 `ROCm.md` 提及 `FlashAttention`，應更新為最新的 `FlashAttention-2` 或 `FlashAttention-3` 以反映最新最佳實務。
- [x] 新最佳實務: 檔案 `RNN.md` 提及 `FlashAttention`，應更新為最新的 `FlashAttention-2` 或 `FlashAttention-3` 以反映最新最佳實務。
- [x] 新最佳實務: 檔案 `AI晶片軟體堆疊與SDK設計.md` 提及 `FlashAttention`，應更新為最新的 `FlashAttention-2` 或 `FlashAttention-3` 以反映最新最佳實務。
- [x] 新最佳實務: 檔案 `AI模型分類與硬體協同設計.md` 提及 `FlashAttention`，應更新為最新的 `FlashAttention-2` 或 `FlashAttention-3` 以反映最新最佳實務。
- [x] 新最佳實務: 檔案 `Triton.md` 提及 `FlashAttention`，應更新為最新的 `FlashAttention-2` 或 `FlashAttention-3` 以反映最新最佳實務。
- [x] 新最佳實務: 檔案 `AI加速晶片全景探索.md` 提及 `FlashAttention`，應更新為最新的 `FlashAttention-2` 或 `FlashAttention-3` 以反映最新最佳實務。
## 1. 知識地圖架構整理
目前 `INDEX.md` 中有 56 個項目被放在 `## 其他知識節點` 底下，未被妥善分類到知識地圖。
建議將這些孤兒節點移至適當的分類：

**虛擬團隊與 AI Agent 相關 (移至「虛擬團隊」或「AI 軟體」):**
- [[AIAgent與硬體架構演進]]

**硬體架構與加速器相關 (移至「硬體架構 (中階)」):**
- [[AI加速晶片的記憶體架構]]
- [[AI加速晶片研究總覽]] 及底下延伸閱讀
- [[AI晶片方案評估與發展趨勢]]
- [[AI晶片未來發展趨勢]]
- [[AI晶片記憶體架構]]
- [[ASIC加速晶片設計]]
- [[ASIC與TPU架構分析]]
- [[FPGA在AI加速的應用]]
- [[FPGA在AI硬體的角色]]
- [[GPU在AI加速的應用]]
- [[GPU架構與AI計算]]
- [[GPU與NPU架構比較]]
- [[TPU技術解析]]
- [[TPU深度解析]]
- [[TPU與專用AI晶片]]
- [[邊緣AI晶片設計]]
- [[邊緣運算AI晶片]]
- [[新型態AI硬體架構]]
- [[前瞻技術挑戰]]

**記憶體與封裝 (移至「進階記憶體與封裝 (高階)」):**
- [[AI晶片的新型記憶體解決方案]]
- [[CoWoS]]
- [[GDDR]]
- [[LPDDR]]
- [[前沿技術挑戰與瓶頸]]

**模型架構與運算相關 (移至「基礎運算與模型架構」):**
- [[Decode]]
- [[KV Cache]]
- [[Long Context]]
- [[Mamba]]
- [[MoE]]
- [[Prefill]]
- [[SIMD]]
- [[模型與硬體適配性]]

**軟體與編譯器 (移至「AI 軟體與編譯器」):**
- [[AI最佳實務與部署指引]]
- [[CUDA逆向工程與算子實作分析]]
- [[DeepSpeed]]
- [[Megatron]]
- [[Optimizer]]
- [[SDK與軟體堆疊]]
- [[TVM]]
- [[TensorRT]]
- [[cuDNN]]

**網路與互連 (建議新增分類「網路與互連」):**
- [[InfiniBand]]
- [[NVLink]]
- [[NoC]]
- [[PCIe]]
- [[RDMA]]
- [[RoCE]]

*(已排除 `其他知識節點` 中重複的項目如 [[小型團隊策略]]、[[前瞻技術挑戰]] 等)*

## 2. 內容擴充與完善 (呼叫虛擬團隊)
下列專有名詞頁面內容過少或僅有標題，需要呼叫虛擬團隊（研究員 -> 驗證員 -> 教育員）進行內容擴充：
- [[Decode]]: 說明 LLM 推論中的 Decode 階段硬體需求。
- [[Prefill]]: 說明 LLM 推論中的 Prefill 階段硬體需求與效能瓶頸。
- [[KV Cache]]: 說明 LLM 推論中 KV Cache 對記憶體容量和頻寬的影響。
- [[Mamba]]: 介紹 SSM/Mamba 模型架構與傳統 Transformer 的差異及其在硬體上的優勢。

## 3. 執行計畫
- 由於使用者要求我「在產生巡檢報告後，直接觸發虛擬團隊執行報告中的內容」，我將直接扮演虛擬團隊的角色，對 `INDEX.md` 進行重構，將所有孤立節點整合回主架構，並擴充上述四個核心概念 (`Decode.md`, `Prefill.md`, `KV Cache.md`, `Mamba.md`) 的內容。


## 4. 額外巡檢結果與執行 (Trillium & SSM)
- [x] 孤立節點: 已將 `[[SSM]]` 整合至 `INDEX.md` 中合適的分類下。
- [x] 架構名稱更新: 已將指定四份核心文件 (`主流AI加速晶片架構分析.md`, `商用AI加速晶片架構研究.md`, `TPU.md`, `自研AI晶片發展策略.md`) 中的 `Trillium` 更新為 `TPU v6 (Trillium)` 或 `v6 (Trillium)`。
