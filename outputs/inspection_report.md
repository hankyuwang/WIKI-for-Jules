# Wiki 巡檢報告 (2026-09-21)

## 1. 失效連結 (Dead Links)
- `XLA.md` 中的 `[[Compiler]]` 為失效連結。
  - **修復方式**：已將其修改為指向現有頁面 `[[MLIR|Compiler]]`。

## 2. 過時版本 (Outdated Versions) & 3. 已棄用架構 (Deprecated Architectures)
在以下檔案中發現了過時的硬體架構描述，包含 Volta 與 TPU v1/v2/v3。
- `TPU與專用AI晶片.md`: 更新 TPU v1/v2/v3 為早期架構，並指出現行為 Trillium (TPU v6)。
- `Systolic Array.md`: 更新 TPU v1 描述為早期 TPU v1。
- `GPU 架構與演進.md`: 更新 Volta 為早期 Volta。
- `TPU深度解析.md`: 更新 TPU v1/v2/v3 描述為早期架構。
- `GPU架構與AI計算.md`: 更新 Volta 描述。
- `CUDA逆向工程與算子實作分析.md`: 更新 Volta 描述。
- `NVLink.md`: 更新 Volta 描述。
- `TPU架構深度解析.md`: 更新 TPU v1/v2/v3 描述為早期架構。
  - **修復方式**：已將這些架構統一標註為「早期」架構，並根據脈絡補充現行主流架構 (例如 Hopper/Blackwell, Trillium)。

## 4. 官方文件或是論文更新 (Official Docs / Paper Updates) & 5. 新最佳實務 (New Best Practices)
經巡檢確認，當前知識庫已充分反映最新最佳實務與論文更新，包含：
- **Trillium (TPU v6)**：在多個 TPU 相關頁面中已作為最新架構被提及並有專門頁面 (`Trillium架構與演進.md`)。
- **FlashAttention (-3)**：已被提及於多個優化與長文本處理相關頁面中 (`FlashAttention3與極低精度量化硬體需求.md`, `Long Context.md`, `算子融合.md` 等)。
- **vLLM / TensorRT**：作為高效能 LLM 推理框架，在 `高效能LLM推理框架最佳實務.md`, `KV Cache.md` 等頁面已有充分的實務討論與整合。
  - **狀態**：皆為最新狀態，無需額外補充。

## 執行動作總結
- [x] 修復所有失效連結
- [x] 更新所有過時與已棄用架構的歷史描述
- [x] 驗證新技術與最佳實務是否已涵蓋
