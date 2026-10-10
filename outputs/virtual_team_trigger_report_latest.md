# 虛擬團隊執行計畫 (Virtual Team Trigger Report)

根據維護員巡檢報告，本次將針對 **「最新硬體架構更新」** 與 **「LLM 推理最佳實踐」** 兩大主題進行擴充。

## 1. 接待員 (Receptionist) 確認需求
- **Goal**: 擴展並更新知識庫中關於最新 AI 加速晶片硬體架構 (NVIDIA Blackwell, Google TPU v6/Trillium) 以及 LLM 推理優化 (vLLM, 極低精度 FP4/INT4 量化) 的內容。
- **Scope**: 新增與擴充硬體規格、架構優勢與推論框架最佳實務的 markdown 檔案。
- **Non-goal**: 不修改現有的歷史架構與基礎運算原理，僅補充新知識與實作指引。
- **Expected Output**:
  1. 擴充 `NVIDIA Blackwell` 相關技術細節至 `GPU 架構與演進.md` 或獨立建立文件。
  2. 確保 `Trillium架構與演進.md` 反映最新進展。
  3. 建立或擴充 `LLM 推理最佳實務` 文件，包含 vLLM、極低精度量化的探討與方案比較。

## 2. 知識架構師 (Architect) 規劃結構
將在 `content/` 目錄新增/修改以下主題，並在 `content/INDEX.md` 中對應建立 `[[WikiLink]]`：
- `content/LLM推理最佳實務.md`: (新增) 專注探討 vLLM 等框架與極低精度量化。
- 修改 `content/INDEX.md`: 在「LLM 推理與運算瓶頸」和「系統評估與部署策略」下新增 `[[LLM推理最佳實務]]` 與新硬體相關連結。
- 每個新文件必須包含 `level: advanced` 的 YAML frontmatter、摘要以及 `Prerequisites` 區塊連結到相關概念 (如 `[[Quantization]]`, `[[Transformer]]`)。

## 3. 研究員 (Researcher) 產出內容
### 主題 1: LLM推理最佳實務 (vLLM 與極低精度量化)
- **已知事實**: vLLM 利用 PagedAttention 技術有效解決了 KV Cache 的記憶體碎片化問題，提升吞吐量。最新的 Blackwell 架構支援 FP4 量化，大幅降低記憶體頻寬壓力。
- **最佳實務**:
  - 方案 A: 採用 PagedAttention + vLLM 部署 (優點: 高吞吐量, 缺點: 系統複雜度較高)。
  - 方案 B: 使用 INT4/FP4 權重與 KV Cache 量化 (優點: 減少記憶體佔用, 缺點: 可能造成些微精度損失)。
  - 方案 C: 結合 TensorRT-LLM 與硬體專屬優化 (優點: 延遲極低, 缺點: 綁定特定硬體生態)。
- **限制與未知問題**: 極低精度量化在超大模型或特殊領域任務的精確度極限仍需進一步研究。

## 4. 驗證員 (Validator) 審查
- 確認 Blackwell 架構支援的確為 FP4，並且 Trillium 具有高效的 CAE 機制。
- vLLM PagedAttention 技術的描述正確無誤。
- Confidence level: High (基於廣泛發布的官方架構文件與開源框架文件)。

## 5. 教育員 (Educator) 格式化與連結
- 將研究員內容轉化為清晰易讀的 `LLM推理最佳實務.md`。
- 新增 `Prerequisites` 區塊： `[[Quantization]]`, `[[KV Cache]]`, `[[Prefill]]`, `[[Decode]]`。
- 標籤設定為 `level: advanced`, `tags: [llm, inference, quantization]`。

---
**即將執行的檔案變更：**
1. 建立 `content/LLM推理最佳實務.md`。
2. 更新 `content/INDEX.md` 加入新的 WikiLink。
