# Website Plan

## 1. Recommended Sections

建議網站分為 5 個區塊：

1. Hero / 首頁介紹：照片、姓名、英文名、航運管理學系、信箱、簡短定位。
2. About / 關於我：求學背景、個人特質、航運與職涯探索方向。
3. Learning Timeline / 學習歷程：用時間軸整理講座、說明會、研究與實習準備活動。
4. Experience / 經驗與能力：總務股長、校安中心工讀、志工、嘉獎紀錄。
5. Knowledge Base / 我的知識庫：說明 raw -> wiki -> schema 架構，展示目前已整理的主題頁。

## 2. Visual Direction

整體視覺建議走「清楚、可信任、專業但不冷淡」：白色與淺灰作為底色，深墨綠或深海軍藍作為文字與重點色，搭配暖橘色作為行動按鈕與標籤。版面保持大留白、強烈標題、清楚卡片與橫向資訊列，呼應服務型網站的直接感。

## 3. Three Reference Details From the Wix Template

- Bold first screen: 首屏要有大字標題和明確自我定位，不要只放履歷清單。
- Practical sectioning: 每個區塊都要有清楚任務，例如介紹、服務/能力、作品/歷程、聯絡。
- High-contrast action details: 用醒目的按鈕、分隔線或色塊標示重點，讓訪客能快速掃描。

## Knowledge Management Explanation

Karpathy 的原則可以用三句話理解：

- 原始資料不要改，放在 `raw/`，它是事實來源。
- AI 幫你把資料整理成 `wiki/`，每次加入新資料都更新既有頁面，而不是每次重新搜尋。
- 用 `AGENTS.md`、`index.md`、`log.md` 規定整理規則、導航與歷史紀錄，讓知識會累積。

套用到這個網站，eportfolio PDF 是 raw source；整理後的個人介紹、學習地圖、經驗頁是 wiki；網站首頁則是 output，把知識庫中適合公開的內容呈現給訪客。
