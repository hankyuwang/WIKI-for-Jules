# 虛擬團隊執行計畫 (Virtual Team Trigger Report)

根據維護員巡檢報告，虛擬團隊已啟動並指派任務，目標是針對內容稀少的頁面進行補充、解釋專有名詞、增加最佳實務，並確保所有頁面皆與知識地圖有良好的連結。

## 角色分工與計畫

### 1. 知識架構師 (Architect)
- 規劃文件更新策略：
  - 確保新增內容保留原有的 `Prerequisites (先備知識)`，或在沒有時自動補上。
  - 將艱澀名詞轉化為白話文，並透過 `[[WikiLink]]` 連結回基礎概念。
  - 確認 `AI加速器最佳實務與部署指引.md`, `ASIC與TPU架構分析.md`, `FPGA在AI硬體的角色.md` 等檔案能與 `INDEX.md` 知識地圖深度結合。

### 2. 研究員 (Researcher) & 驗證員 (Validator)
- **AI加速器最佳實務與部署指引.md**:
  - 蒐集並驗證 Pipeline Parallelism (流水線平行) 與 Tensor Parallelism (張量平行) 的原理。
  - 驗證 Operator Fusion (算子融合) 如何減少記憶體頻寬開銷 (Memory Bandwidth Overhead)。
  - 收集 vLLM, TensorRT-LLM 最佳實務。
- **ASIC與TPU架構分析.md**:
  - 探討 MAC (Multiply-Accumulate) 運算單元的微觀機制。
  - 研究 TPU 的記憶體瓶頸 (Memory Wall) 與 Roofline Model (屋頂模型)。
- **FPGA與GPU相關文件**:
  - 研究 FPGA 的 HLS (High-Level Synthesis) 技術。
  - 研究 GPU 的 Tensor Core 加速原理。

### 3. 教育員 (Educator)
- 將研究員與驗證員的內容轉化為易懂的 Markdown 格式。
- 針對 `AI加速器最佳實務與部署指引.md` 進行篇幅擴充，加入直觀解說。
- 針對 `ASIC與TPU架構分析.md` 補充「初學者專區」，用生活化的比喻解釋 Systolic Array 與 MAC。
- 更新文件並確保存檔。

---
## 執行任務列表

- [ ] 更新 `content/AI加速器最佳實務與部署指引.md`
- [ ] 更新 `content/ASIC與TPU架構分析.md`
- [ ] 更新 `content/FPGA在AI硬體的角色.md`
- [ ] 更新 `content/GPU在AI加速的應用.md`
- [ ] 確認 `outputs/inspection_report.md` 任務打勾

## 執行結果
- [x] 更新 content/AI加速器最佳實務與部署指引.md
- [x] 更新 content/ASIC與TPU架構分析.md
- [x] 更新 content/FPGA在AI硬體的角色.md
- [x] 更新 content/GPU在AI加速的應用.md
- [x] 確認 outputs/inspection_report.md 任務打勾
