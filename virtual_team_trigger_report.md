# 虛擬團隊觸發報告 (基於巡檢報告)

## 觸發背景
維護員已完成定期巡檢，發現以下問題需要虛擬團隊介入處理：
1. 存在失效連結 `[[LLM]]` 於 `content/Processing-in-Memory.md` 中。
2. 孤立頁面 `Tensor Core` 尚未加入 `INDEX.md`。
3. 需要在 `LLM推理最佳實務.md` 補充 FlashAttention-3 與 FP4 極低精度量化。

## 角色分配與行動計畫

### 接待員 (Receptionist)
- **目標**: 釐清需要修復的失效連結與新內容補充。
- **行動**: 確認 `LLM` 詞彙在當前知識庫中是否應連結至其他現有頁面 (例如 `[[LLM推理最佳實務]]`)，或是應新增基礎介紹頁面。

### 知識架構師 (Architect)
- **目標**: 確保新內容的層級與連結正確。
- **行動**: 將 `Tensor Core` 加入 `INDEX.md` 中的適當分類 (例如 `硬體架構 (中階)` 或 `基礎運算與模型架構`)。規劃 `LLM推理最佳實務.md` 的結構以容納 FlashAttention-3。

### 研究員 (Researcher)
- **目標**: 研究 FlashAttention-3 的新特性。
- **行動**: 整理 FlashAttention-3 在硬體 (特別是 Hopper 架構) 上的優化，以及 FP4 極低精度量化對記憶體頻寬與算力的影響。

### 驗證員 (Validator)
- **目標**: 驗證新增內容的正確性。
- **行動**: 確認 FlashAttention-3 的硬體需求是否正確，避免幻覺。

### 教育員 (Educator)
- **目標**: 將研究結果轉化為易懂的 Wiki 內容。
- **行動**: 修改 `content/Processing-in-Memory.md` 修復失效連結。更新 `content/LLM推理最佳實務.md`。修改 `content/INDEX.md` 處理孤立頁面。
