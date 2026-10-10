# 維護員巡檢報告

## 1. 失效連結 (Dead Links)
經巡檢所有 `content/` 目錄下的 Markdown 檔案與 `content/INDEX.md`，目前未發現任何失效的 `[[WikiLink]]` 連結。

## 2. 過時版本 (Outdated Versions)
經檢查文件中提到的框架或技術版本（如 PyTorch, CUDA 等），未發現明顯過時且需要更新的版本資訊。

## 3. 已棄用架構 (Deprecated Architectures)
雖然文件中提及了 Volta、TPU v1、TPU v2 等早期架構，但檢查其上下文後發現：
- 這些架構主要是作為「歷史沿革」或「早期架構」來介紹（例如：「早期的 TPU v1」、「早期的 Volta 架構」），用於說明硬體架構的演進脈絡。
- 在歷史背景介紹中，這些描述是正確且必要的，因此不需要將其替換為新架構或標記為已棄用。

## 4. 官方文件或是論文更新 (Official Documentation or Paper Updates)
目前的文件未見明顯與最新官方文件或指標性論文衝突的內容。然而，隨著 AI 領域快速發展，建議虛擬團隊可以主動針對最新硬體架構（如 NVIDIA Blackwell, Google Trillium）以及最新的模型優化技術（如 FlashAttention-3, Mamba 等）進行更深度的追蹤與研究，並更新現有文件。

## 5. 新最佳實務 (New Best Practices)
文件中已涵蓋了量化、算子融合、KV Cache 等實務，但建議：
- 虛擬團隊（研究員）可進一步擴充並統整「大型語言模型推理（LLM Inference）的最佳實踐」，包括 vLLM 等框架的最新優化。
- 探索更多關於極低精度量化（如 FP4, INT4）對最新硬體架構的影響與實作指引。

---

## 虛擬團隊觸發任務指引 (Virtual Team Trigger Instructions)
根據 `.jules/instructions.md`，請虛擬團隊執行以下行動：

1. **接待員 (Receptionist)**：
   - 接收上述第 4 點與第 5 點的建議。
   - 確認目標：擴展關於最新硬體（NVIDIA Blackwell, Google TPU v6/Trillium）以及 LLM 推理最佳實踐（vLLM, 極低精度量化）的內容。

2. **知識架構師 (Architect)**：
   - 決定如何將新內容整合進現有知識地圖（如 `INDEX.md`）。
   - 規劃是否需要建立新的主題（例如 `LLM推理最佳實踐.md`、`極低精度量化實務.md`），或是擴充現有文件。

3. **研究員 (Researcher)**：
   - 針對 Blackwell、Trillium、vLLM 優化、FP4/INT4 量化進行研究。
   - 產出詳細的 Markdown 文件，包含已知事實、原理、限制、最佳實務，並提出至少三種方案與優缺點分析（若適用）。

4. **驗證員 (Validator)**：
   - 驗證研究員產出的內容，確認硬體規格（如 TOPS/W, Memory Bandwidth）與軟體效能數據無誤，標註來源與信心水準。

5. **教育員 (Educator)**：
   - 確保新產出的文件具備良好的可讀性，由淺入深，並包含 `Prerequisites` 連結。
   - 確認 YAML frontmatter 包含 `level` 與正確的 `tags`。
