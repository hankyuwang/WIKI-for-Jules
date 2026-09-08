# Wiki 維護巡檢報告 (Inspection Report)

## 1. 失效連結 (Dead Links)
發現 0 個失效連結：
無失效連結。

## 2. 孤兒檔案 (Orphaned Files)
發現 0 個未在 INDEX.md 中引用的檔案：
無孤兒檔案。

## 3. 過時版本與官方文件更新 (Outdated Versions & Official Docs Updates)
- [x] `TPU與專用AI加速器.md`：需確認是否已納入 Google TPU v6 (Trillium) 的最新架構資訊。
- [x] `主要商用AI加速晶片架構分析.md`：需更新最新一代晶片（如 Blackwell, MI300X, Trillium）的具體規格比較，並確認有無棄用之舊架構。
- [x] `FlashAttention3與極低精度量化硬體需求.md`: 確認是否有更新的最佳實務。

## 4. 新最佳實務與已棄用架構 (New Best Practices & Deprecated Architectures)
- [x] 定期檢查 AI 推理框架 (如 vLLM, TensorRT-LLM) 是否有新的效能優化 (e.g. Speculative Decoding, FP8 KV Cache) 需新增至 `高效能LLM推理框架最佳實務.md`。

## 5. 待辦事項清單 (Action Items)
- [x] 執行虛擬團隊工作流程，針對上述項目進行研究與更新 (接待員 -> 知識架構師 -> 研究員 -> 驗證員 -> 教育員)。
- [x] 確保修改後的內容通過 `npx quartz build` 驗證。
