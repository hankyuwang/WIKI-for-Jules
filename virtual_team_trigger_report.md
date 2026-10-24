# 虛擬團隊執行報告

## 接待員 (Receptionist)
- 任務：分析巡檢報告需求，分配給對應團隊成員。
- 指示：修復 `Processing-in-Memory.md` 的失效連結，並豐富 `Quantization.md` 與 `基礎計算機結構.md` 的內容。

## 知識架構師 (Architect)
- 任務：確保修改後的內容與知識地圖 (INDEX.md) 一致，不破壞既有連結結構。
- 指示：確認 `[[LLM]]` 應指向何處，建議改為 `[[Transformer]]` 或新增 `LLM.md`（目前選擇將其改為 `[[Transformer]]` 以利用現有節點）。

## 研究員 (Researcher)
- 任務：為 `Quantization.md` 和 `基礎計算機結構.md` 搜集並提供深度且正確的技術細節。
- 產出：提供量化 (Quantization) 的精度 (INT8, FP16) 比較與效能影響，以及基礎計算機結構 (CPU, GPU, 記憶體階層) 的運作原理。

## 驗證員 (Validator)
- 任務：驗證修改後的內容是否正確。
- 產出：確認量化與計算機結構的知識來源與準確性，確保無幻覺。

## 教育員 (Educator)
- 任務：將研究員的資料轉換為初學者友善、易讀的形式。
- 產出：為 `Quantization.md` 與 `基礎計算機結構.md` 加入生動的比喻（例如將量化比喻為解析度壓縮，將計算機結構比喻為廚房做菜），由淺入深說明。

## 實驗員 (Experimenter)
- 任務：本次任務無硬體或 PoC 實驗需求。
