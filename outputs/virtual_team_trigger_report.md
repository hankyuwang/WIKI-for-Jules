# 虛擬團隊觸發報告：修復失效連結

## 發現問題
維護員（Maintainer）在進行日常巡檢時，發現 `content/` 中的 markdown 檔案（包括 `NPU架構探索.md`、`模型量化技術.md`、`AI加速晶片全景探索.md`）存在指向 `[[深度學習運算原理]]` 的失效連結。這表示該核心基礎知識頁面遺失或未建立，破壞了知識庫的完整性與雙向連結機制。

## 虛擬團隊工作計畫

依照 `.jules/instructions.md` 定義的流程，啟動虛擬團隊協作修復此問題：

### 1. 接待員 (Receptionist)
- **Goal**: 建立缺失的 `深度學習運算原理.md` 頁面，修復現有的失效連結。
- **Scope**: 涵蓋深度學習運算的核心原理（如矩陣乘法、啟動函數等），並探討不同硬體加速的觀點。
- **Non-goal**: 不涉及特定框架（如 PyTorch/TensorFlow）的底層 C++ 實作細節，專注於運算與架構層面。
- **Assumptions**: 假設讀者具備基礎的計算機結構知識，並正準備深入了解 NPU 或 AI 晶片架構。
- **Expected Output**: 一份包含摘要、YAML frontmatter，並涵蓋 3 種以上解決方案/觀點（含優點、缺點、成本、維護性、風險）的 Markdown 檔案。
- **Learning Level**: Beginner

### 2. 知識架構師 (Knowledge Architect)
- **Metadata**: `title: 深度學習運算原理`, `level: beginner`
- **Tag**: `deep-learning`, `compute`, `architecture`
- **Folder**: `content/`
- **Naming Rule**: 檔名為 `深度學習運算原理.md`
- **雙向連結策略**: 必須被 `NPU架構探索.md`, `模型量化技術.md`, `AI加速晶片全景探索.md` 正確引用。未來可在 `INDEX.md` 中新增該連結。

### 3. 研究員 (Researcher)
- 探索與整理深度學習最核心的運算類型（MAC 運算、GEMM）。
- 提出 3 種不同硬體觀點/方案來處理這些運算（例如：CPU, GPU, 專用 NPU/ASIC）。
- 針對這 3 種觀點，詳細比較其優缺點、成本、維護性與風險。

### 4. 驗證員 (Validator)
- 確認所述之運算原理（如 MAC 的本質）準確無誤。
- 確認提出的方案比較具有真實參考價值，不含幻覺。

### 5. 教育員 (Educator)
- 撰寫首段摘要（符合系統規則）。
- 組織內文，確保從基礎概念循序漸進，並使用適當的標題結構，讓初學者能夠輕易理解為何需要專門的 AI 晶片。

### 6. 實驗員 (Experimenter)
- （此階段暫不需實驗，重點在於知識整理）

### 7. 維護員 (Maintainer)
- 在完成文件建立後，執行 Quartz 專案的 build 與 test，確保沒有 broken links。

---
**結論**: 同意執行計畫，開始建立 `content/深度學習運算原理.md`，並更新 `INDEX.md`。
