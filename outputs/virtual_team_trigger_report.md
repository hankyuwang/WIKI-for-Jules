# 虛擬團隊觸發報告 (Virtual Team Trigger Report)

根據 `outputs/inspection_report.md` 的巡檢結果，啟動虛擬團隊進行知識庫補充與優化：

## 1. 知識架構師 (Architect) 指示
- 確保新增或補充的內容與 `INDEX.md` 以及現有的知識節點（如 `HBM架構解析`, `GPU架構與演進`, `Compiler`, `SDK與軟體堆疊`）產生雙向連結。
- 針對補充的頁面，需維持原有的 Metadata 與 Tag，確保符合 Document Level Hierarchy 規範。

## 2. 研究員 (Researcher) 與教育員 (Educator) 執行任務
發現有部分頁面內容過於單薄 (少於 1200 字元)，可能導致初學者無法完全理解脈絡。請針對以下頁面進行深度擴充，並加入初學者導覽、底層原理解析、優缺點或延伸學習路徑：

- **`高頻寬記憶體_HBM.md` (擴充)**:
  - 任務：補充 HBM 1~3/3e 的演進過程、具體頻寬數據比較。
  - 任務：詳述 3D 堆疊中 Microbump 與矽穿孔 (TSV) 的作用，以更具體的比喻讓讀者了解其與傳統 GDDR 的成本和效能差異。

- **`GPU運算架構.md` (擴充)**:
  - 任務：補充 GPU 的記憶體階層 (Registers, Shared Memory, Global Memory/HBM)。
  - 任務：詳細說明為何 Transformer 這種巨型模型特別依賴 GPU 的 Tensor Core，並增加對 `Warp` / `Thread Block` 的初學者比喻。

- **`TVM.md` (擴充)**:
  - 任務：原內容過短。請詳細說明 TVM (Tensor Virtual Machine) 作為深度學習編譯器的角色。
  - 任務：解釋它如何橋接不同的前端框架 (PyTorch, TensorFlow) 與後端硬體 (CPU, GPU, TPU)。
  - 任務：提供 TVM 的三個核心優勢與其 AutoTVM / Ansor 的最佳化流程。

- **`CUDA.md` (擴充)**:
  - 任務：補充 CUDA 程式設計模型的核心概念，例如 Kernel Function 的呼叫。
  - 任務：解釋 GPU 記憶體管理的挑戰 (Host to Device 傳輸)。
  - 任務：對比 AMD 的 ROCm 或開源的 Triton，提供多個方案的優缺點分析。

- **`AI最佳實務與部署指引.md` (擴充)**:
  - 任務：針對企業與小型團隊的 AI 部署，提供具體的三個方案 (例如：雲端 GPU 實例、地端自建叢集、邊緣運算設備部署)。
  - 任務：針對各方案分析優缺點、成本考量與維護性。

## 3. 驗證員 (Validator) 檢核點
- 確認所有補充內容是否包含過時或幻覺資訊（如未標示的 Volta, TPU v1/v2）。
- 確認補充的頻寬數據、硬體術語 (TSV, Tensor Core) 符合業界真實規格。

---
**執行計畫**：我們將利用 Python 腳本，透過生成或直接補充上述 `.md` 檔案的內容，實踐上述指引，以豐富知識庫內容並提升易讀性。
# 虛擬團隊觸發報告與執行計畫

基於 Wiki 巡檢報告，以下為虛擬團隊的執行計畫：

## 1. 驗證員 (Validator)
- **任務**：修正失效連結。
- **行動**：將 `Processing-in-Memory.md` 中的 `[[LLM]]` 連結修正，或是建立 `LLM.md` 補充基礎知識，並確保能與 INDEX.md 正確連結。目前看來建立 `LLM.md` 是最好的做法，因為 LLM 是一個重要的概念。

## 2. 研究員與教育員 (Researcher & Educator)
- **任務 1**：處理過時架構。
- **行動**：將 `Tensor Core.md` 中的 `Volta` 確保標示為 `早期` 歷史架構，若有非歷史描述則替換為 `Hopper/Blackwell`。
- **任務 2**：豐富內容過少的頁面，補充詳細、初學者友善的解釋與比喻，並確保包含 `level` 與 `tags` 的 YAML frontmatter，以及正確的知識地圖延伸。
- **行動清單**：
  1. 擴充 `AI模型分類與硬體協同設計.md`
  2. 擴充 `AI加速晶片軟體堆疊與SDK設計.md`
  3. 擴充 `自研AI晶片策略與前沿挑戰.md`
  4. 擴充 `AI加速晶片全景探索.md`
  5. 擴充 `深度學習運算原理.md`
  6. 擴充 `商用AI加速晶片分析.md`
  7. 擴充 `主流AI加速晶片架構分析.md`
  8. 建立 `LLM.md` 並加入內容。

## 3. 知識架構師 (Architect)
- **任務**：確保上述所有修改都有透過 `[[WikiLink]]` 語法連結到現有的知識網路中，並且內容分類明確 (Beginner/Intermediate/Advanced)。
