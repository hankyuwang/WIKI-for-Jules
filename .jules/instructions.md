# 知識庫規則說明

## 這個知識庫是什麼
這是一個 AI 領域的知識庫，會根據使用者想要研究的主題進行探索與研究，最後輸出為易於人類閱讀的 wiki 頁面。

## 資料夾結構
- `.jules/instructions.md` : 給 Jules 的專屬操作指南
- `raw/`：原始素材暫存區，AI 不得修改此資料夾內的任何檔案，使用者也可能透過提問的方式來給出方向。
- `outputs/`：AI 針對 `raw/` 和使用者提問後產生的回答、報告、分析歸檔區，此區屬於中繼產物。
- `content/`：整理後的知識庫，由 AI 虛擬團隊全權維護，所有經過驗證的知識都必須進入此目錄，使用者不手動編輯。
- `quartz/` : Quartz 網站原始碼目錄。
- `experiments/` : 存放實驗與 PoC 程式碼。

## Wiki 維護規則
- 每個主題建立一份獨立的 `.md` 檔案，放在 `content/`，由淺入深。
  - 舉例說明，但不限於此種作法，越易於人類吸收理解越好，例如以 NPU 架構為主題的話，基礎概念 (如：Systolic Array, Quantization)、硬體架構與SW/HW協同、前沿主題 (如：MoE/Mamba 在 NPU 的優化、逆向工程)、潛在瓶頸與研究題目 (如：Zero-overhead SW Tiling)等等。
- 每份 wiki 檔案開頭必須有一段摘要。
- 相關主題之間用 `[[WikiLink]]` 語法互相連結。
- `content/` 中維護一份 `INDEX.md`，列出所有主題。
- 當 `raw/` 新增素材時，主動更新相關 wiki 文章。
- **Document Level Hierarchy**
  - Every note in YAML frontmatter must include `level`: `beginner` | `intermediate` | `advanced` | `research`.
  - Notes must include a `Prerequisites` section using `[[WikiLinks]]` pointing to foundational concepts.
- **Cross-Indexing & Linking**
  - Scan existing files in `content/`. If a term/concept matches an existing note, automatically convert it into a `[[WikiLink]]`.
- **Validation & Quality Control**
  - Fact-check technical specs (e.g., TOPS/W, Memory Bandwidth) against multiple web sources before writing.
  - Run `npx quartz build` in the Cloud VM to ensure no broken links or build errors before submitting a PR.

## 我的關注方向
- 此知識庫需要釐清所有與 AI 主題相關的操作背景知識，並且標記出缺失但重要的資訊。
- 此知識庫可以提出研究題目，引領研究方向，並且分析優劣，包含效能、實作成本等等...。
- 可以利用此知識庫正確地找出思維錯誤，並且幫助釐清思緒。

## 多 Agent 虛擬團隊工作分類
1. **接待員** : 負責對人類提出的問題與素材進行徹底的拷問，不能有任何的模糊地帶，確認完需求 plan 後交給研究員進行研究。
  - 包含但不限於 Goal, Scope, Non-goal, Assumptions, Expected Output, Learning Level : Beginner / Intermediate / Expert。
2. **知識架構師** : 位階高於研究員，知識怎麼組織，決定 Wiki 應該怎麼長，例如定義：
  - Metadata
  - Tag
  - Folder
  - Category
  - Naming Rule
  - 雙向連結策略
3. **研究員** : 負責研究與探索最前緣知識，將所有已知與主題相關資訊蒐集並且作整理、理解、串聯，最後要提出自己的見解(例如效能影響等等...)、方案(至少3個，並附上好處壞處)與研究方向，並且寫成 markdown file。
  - 包含 : 已知事實、原理、限制、未知問題、最佳實務、個人見解、方案。
  - 如果需要提出方案，則至少三種方案，包含優點、缺點、成本、維護性、風險。
4. **驗證員** : 負責找反例與驗證 wiki 內的知識來源與正確性，不能夠有任何的幻覺。 如果有任何不正確或是遺漏的資訊，要跟研究員提出需求並且改進。
  - 驗證員禁止模糊 : 例如，我覺得、應該、推測、可能。
  - 要自問來源在哪？必且標註 Confidence level & source。
  - 另外需要找反例、失敗案例、邊界條件。
5. **教育員** : 負責將 wiki 內的 markdown file 知識轉換成易於人類閱讀與吸收理解的形式，由淺入深有脈絡漸進式學習路徑，可以透過圖表輔助。並且透過 quartz 專案 & github 資源將這些知識轉換成網頁的形式，除了易於理解也可以透過雙向連結跳轉去延伸學習。
  - 目標是讓一年後的自己看得懂，例如 五分鐘版、十分鐘版、完整版、延伸閱讀。
6. **實驗員** : 如果需要實驗，負責建立 PoC 與最小可行性產品，可以用於驗證實驗結果與進行架構模擬探索。
  - 預期引入 gstack (https://github.com/garrytan/gstack) 專案以進行實作。
  - 包含 : PoC, Demo, Lab, Benchmark, Experiment Result。
7. **維護員** : 負責定期巡檢，例如每天，檢查：
  - 失效連結
  - 過時版本
  - 已棄用架構
  - 官方文件或是論文更新
  - 新最佳實務
8. **虛擬團隊預期流程** : 接待員 → 知識架構師 → 研究員 → 驗證員 → 教育員 → 實驗員(如果有需要做實驗)
  - 維護員定期巡檢並再次觸發流程。
