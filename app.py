from pathlib import Path
import base64

import streamlit as st
from PIL import Image


BASE_DIR = Path(__file__).parent
PROFILE_IMAGE = BASE_DIR / "assets" / "profile.jpg"


st.set_page_config(
    page_title="朱芷宜 | 航運管理學習歷程",
    page_icon="CY",
    layout="wide",
)


def load_css() -> None:
    st.markdown(
        """
        <style>
        :root {
            --ink: #17201c;
            --muted: #5f6b65;
            --line: #dfe5df;
            --paper: #f7f8f3;
            --white: #ffffff;
            --green: #1f4f45;
            --orange: #d56d2d;
            --sage: #d8e4d6;
        }

        .stApp {
            background: var(--paper);
            color: var(--ink);
        }

        [data-testid="stHeader"] {
            background: rgba(247, 248, 243, 0.88);
            backdrop-filter: blur(10px);
        }

        .block-container {
            max-width: 1180px;
            padding-top: 2.2rem;
            padding-bottom: 4rem;
        }

        h1, h2, h3, p, li, div {
            letter-spacing: 0;
        }

        h1 {
            font-size: clamp(2.7rem, 7vw, 5.8rem);
            line-height: 0.95;
            font-weight: 850;
            color: var(--ink);
            margin: 0 0 1rem 0;
        }

        h2 {
            font-size: clamp(1.65rem, 3vw, 2.55rem);
            color: var(--ink);
            margin-top: 0;
        }

        h3 {
            font-size: 1.05rem;
            color: var(--ink);
        }

        .hero {
            display: grid;
            grid-template-columns: minmax(0, 1.25fr) minmax(260px, 0.75fr);
            gap: 2.2rem;
            align-items: center;
            min-height: 78vh;
            padding: 2rem 0 3rem;
            border-bottom: 1px solid var(--line);
        }

        .eyebrow {
            color: var(--orange);
            font-weight: 800;
            text-transform: uppercase;
            font-size: 0.78rem;
            margin-bottom: 0.7rem;
        }

        .lead {
            color: var(--muted);
            font-size: clamp(1.02rem, 1.8vw, 1.25rem);
            line-height: 1.8;
            max-width: 700px;
        }

        .hero-panel {
            background: var(--green);
            color: var(--white);
            padding: 1rem;
            border-radius: 8px;
            box-shadow: 0 24px 50px rgba(23, 32, 28, 0.16);
        }

        .hero-panel img {
            width: 100%;
            aspect-ratio: 4 / 5;
            object-fit: cover;
            object-position: center 18%;
            border-radius: 6px;
            display: block;
            background: #fff;
        }

        .contact-strip {
            display: flex;
            flex-wrap: wrap;
            gap: 0.65rem;
            margin-top: 1.4rem;
        }

        .pill {
            display: inline-flex;
            align-items: center;
            min-height: 2.4rem;
            border: 1px solid var(--line);
            border-radius: 999px;
            padding: 0.45rem 0.85rem;
            color: var(--ink);
            background: rgba(255, 255, 255, 0.7);
            font-weight: 650;
            font-size: 0.94rem;
        }

        .section {
            padding: 3.7rem 0;
            border-bottom: 1px solid var(--line);
        }

        .section-grid {
            display: grid;
            grid-template-columns: minmax(190px, 0.34fr) minmax(0, 0.66fr);
            gap: 2rem;
            align-items: start;
        }

        .section-label {
            color: var(--orange);
            font-weight: 850;
            font-size: 0.85rem;
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 1rem;
        }

        .card {
            background: var(--white);
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: 1.25rem;
            min-height: 170px;
        }

        .card strong {
            color: var(--green);
        }

        .timeline {
            display: grid;
            gap: 0.75rem;
        }

        .event {
            display: grid;
            grid-template-columns: 118px minmax(0, 1fr);
            gap: 1rem;
            padding: 1rem;
            background: var(--white);
            border: 1px solid var(--line);
            border-radius: 8px;
        }

        .event-date {
            color: var(--green);
            font-weight: 850;
        }

        .knowledge-band {
            background: var(--green);
            color: var(--white);
            border-radius: 8px;
            padding: 1.4rem;
        }

        .knowledge-band h3,
        .knowledge-band p {
            color: var(--white);
        }

        .kb-flow {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 0.8rem;
            margin-top: 1rem;
        }

        .kb-step {
            background: rgba(255, 255, 255, 0.11);
            border: 1px solid rgba(255, 255, 255, 0.24);
            border-radius: 8px;
            padding: 1rem;
        }

        .footer {
            padding: 2rem 0 0;
            color: var(--muted);
            font-size: 0.95rem;
        }

        div[data-testid="stVerticalBlock"] {
            gap: 0;
        }

        @media (max-width: 760px) {
            .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
            }

            .hero,
            .section-grid,
            .cards,
            .kb-flow {
                grid-template-columns: 1fr;
            }

            .hero {
                min-height: auto;
                padding-top: 1rem;
            }

            .event {
                grid-template-columns: 1fr;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def section_start(label: str, title: str, body: str) -> None:
    st.markdown(
        f"""
        <div class="section">
          <div class="section-grid">
            <div class="section-label">{label}</div>
            <div>
              <h2>{title}</h2>
              <p class="lead">{body}</p>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


load_css()

image_html = ""
if PROFILE_IMAGE.exists():
    image = Image.open(PROFILE_IMAGE)
    st.session_state["_profile_size"] = image.size
    encoded_image = base64.b64encode(PROFILE_IMAGE.read_bytes()).decode("ascii")
    image_html = f'<img src="data:image/jpeg;base64,{encoded_image}" alt="朱芷宜 profile">'
else:
    image_html = '<div style="aspect-ratio:4/5;background:#fff;border-radius:6px;"></div>'

st.markdown(
    f"""
    <div class="hero">
      <div>
        <div class="eyebrow">Shipping Management Portfolio</div>
        <h1>朱芷宜<br>CHU, CHIH-YI</h1>
        <p class="lead">
          航運管理學系學生，正在累積港務、航運、職涯探索與校園實務經驗。
          這個網站整理我的學習歷程，也把 eportfolio 轉化成可持續更新的個人知識庫。
        </p>
        <div class="contact-strip">
          <span class="pill">航運管理學系</span>
          <span class="pill">111B09700</span>
          <span class="pill">jillju1768@gmail.com</span>
        </div>
      </div>
      <div class="hero-panel">
        {image_html}
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

section_start(
    "01 / ABOUT",
    "把航運管理的學習，整理成清楚可追蹤的歷程。",
    "我的背景來自航運管理學系，學習主軸包含海運、港務、物流職涯與實習準備。網站公開呈現適合被看見的內容，私人聯絡資料則保留在原始檔案中。",
)

st.markdown(
    """
    <div class="section">
      <div class="section-grid">
        <div class="section-label">02 / FOCUS</div>
        <div class="cards">
          <div class="card"><h3>航運與港務</h3><p>參與港勤徵才、海運貨物承攬、智慧港灣永續發展等主題活動，建立產業理解。</p></div>
          <div class="card"><h3>職涯與實習</h3><p>持續關注航管系實習報告、企業說明會、求職講座，把課堂和職場連起來。</p></div>
          <div class="card"><h3>執行與服務</h3><p>擔任總務股長、校安中心工讀與招生志工，累積流程協助與責任感。</p></div>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

events = [
    ("2026-06", "航管系就業實習報告大會暨業師職場心得分享會"),
    ("2026-05", "臺灣港務港勤股份有限公司徵才說明會"),
    ("2025-03", "海運界老兵的職涯分享：從船公司前進海運貨物承攬業"),
    ("2024-11", "管理學院大專生研究計畫申請與執行分享會"),
    ("2024-10", "超捷集團實習說明會"),
    ("2023-05", "智慧港灣永續發展新思維"),
]

timeline_html = "".join(
    f'<div class="event"><div class="event-date">{date}</div><div>{title}</div></div>'
    for date, title in events
)

st.markdown(
    f"""
    <div class="section">
      <div class="section-grid">
        <div class="section-label">03 / TIMELINE</div>
        <div>
          <h2>近期學習時間軸</h2>
          <div class="timeline">{timeline_html}</div>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section">
      <div class="section-grid">
        <div class="section-label">04 / EXPERIENCE</div>
        <div class="cards">
          <div class="card"><strong>班級幹部</strong><h3>總務股長</h3><p>112 學年度上下學期擔任總務股長，負責班級例行事務與協調。</p></div>
          <div class="card"><strong>校內工讀</strong><h3>校安中心</h3><p>2023 年 6 月於校安中心工讀，接觸校園行政與現場支援。</p></div>
          <div class="card"><strong>服務與嘉獎</strong><h3>志工與活動</h3><p>協助招生面試場地布置與引導，並有愛心捐血與幹部表現嘉獎紀錄。</p></div>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section">
      <div class="section-grid">
        <div class="section-label">05 / KNOWLEDGE BASE</div>
        <div class="knowledge-band">
          <h2 style="color:white;">我的個人知識庫</h2>
          <p>
            我把 eportfolio 當作原始資料，不直接覆寫；再整理成可閱讀、可更新、可互相連結的 wiki。
            這樣未來新增文章、講座心得或作品時，不會只是堆檔案，而是會累積成自己的學習地圖。
          </p>
          <div class="kb-flow">
            <div class="kb-step"><h3>Raw Sources</h3><p>PDF、文章、照片與原始紀錄，保存事實來源。</p></div>
            <div class="kb-step"><h3>Wiki Pages</h3><p>整理成 Profile、Learning Map、Experience 等主題頁。</p></div>
            <div class="kb-step"><h3>Outputs</h3><p>網站、履歷、簡報或作品集都能從知識庫生成。</p></div>
          </div>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="footer">
      © 2026 朱芷宜 · Built with Streamlit · Knowledge base first version
    </div>
    """,
    unsafe_allow_html=True,
)
