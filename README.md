# my-website

朱芷宜的 Streamlit 個人網站與個人知識庫。

## 本機執行

```powershell
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## 交作業部署方式

建議部署到 Streamlit Community Cloud，老師才可以從外部網路打開。

1. 把這個資料夾上傳到 GitHub repository。
2. 到 Streamlit Community Cloud 建立新 app。
3. 選擇 GitHub repository。
4. Main file path 填入 `app.py`。
5. Deploy 後取得公開網址，例如 `https://my-website.streamlit.app`。

## 注意隱私

`knowledge/raw/` 裡的原始 eportfolio PDF 含有電話、地址、生日等個人資料，已加入 `.gitignore`，不建議上傳到公開 GitHub。

網站只呈現適合公開的內容：姓名、科系、信箱、學習歷程、活動紀錄與知識庫架構。

## Knowledge Base

- `knowledge/raw/`: 原始資料，保持不修改。
- `knowledge/wiki/`: 由原始資料整理出的 Markdown 知識頁。
- `knowledge/AGENTS.md`: 知識庫維護規則。
- `knowledge/index.md`: 內容索引。
- `knowledge/log.md`: 處理紀錄。
