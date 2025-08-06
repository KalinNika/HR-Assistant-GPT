import streamlit as st
from PyPDF2 import PdfReader
import docx2txt

st.set_page_config(page_title="HR-помощник на GPT", layout="wide")

# ==================== 🌗 Тема ====================
theme = st.selectbox("🎨 Выберите тему интерфейса:", ["🌙 Тёмная", "🌞 Светлая"])
dark_mode = theme == "🌙 Тёмная"

# Цвета
background_color = "#0e1117" if dark_mode else "#ffffff"
text_color = "#ffffff" if dark_mode else "#000000"
button_bg = "#e0e0e0"
button_text_color ="#000000"

# ==================== 💄 Стили ====================
if dark_mode:
    custom_css = f"""
        <style>
            html, body, .stApp {{
                background-color: {background_color} !important;
                color: {text_color} !important;
            }}

            h1, h2, h3, h4, h5, h6, p, span, label, div, section, .stMarkdown, .stText, .stRadio, .stSelectbox, .stFileUploader {{
                color: {text_color} !important;
            }}

            .stButton > button {{
                background-color: {button_bg} !important;
                color: {button_text_color} !important;
                border: 1px solid #ccc;
                border-radius: 0.5rem;
                padding: 0.4em 1em;
            }}

            .stTextInput > div > div > input,
            .stTextArea > div > textarea {{
                background-color: #262730 !important;
                color: #ffffff !important;
            }}

            div[role="listbox"] > div {{
                color: #ffffff !important;
                background-color: #262730 !important;
            }}
        </style>
    """
else:
    custom_css = f"""
    <style>
        html, body, .stApp {{
            background-color: {background_color} !important;
            color: {text_color} !important;
        }}

        h1, h2, h3, h4, h5, h6, p, span, label, div, section, .stMarkdown, .stText, .stRadio, .stSelectbox, .stFileUploader {{
            color: {text_color} !important;
        }}

        .stButton > button {{
            background-color: {button_bg} !important;
            color: {button_text_color} !important;
            border: 1px solid #ccc;
            border-radius: 0.5rem;
            padding: 0.4em 1em;
        }}

        input, textarea, .stTextInput input, .stTextArea textarea {{
            background-color: #ffffff !important;
            color: #000000 !important;
            border: 1px solid #cccccc !important;
            border-radius: 5px !important;
            box-shadow: none !important;
        }}

        div[data-baseweb="select"] > div,
        div[data-baseweb="select"] input {{
            background-color: #ffffff !important;
            color: #000000 !important;
        }}

        div[data-baseweb="select"] div[role="listbox"],
        div[data-baseweb="select"] div[role="option"] {{
            background-color: #ffffff !important;
            color: #000000 !important;
        }}

        div[data-baseweb="select"] div[role="option"]:hover,
        div[data-baseweb="select"] div[aria-selected="true"] {{
            background-color: #f0f0f0 !important;
            color: #000000 !important;
        }}

        .stRadio > div {{
            background-color: #ffffff !important;
            color: #000000 !important;
        }}

        /* 💡 Для белого выпадающего списка selectbox в светлой теме — React Portal */
        div[role="presentation"] > div {{
            background-color: #ffffff !important;
            color: #000000 !important;
            border-radius: 0 0 6px 6px !important;
        }}

        div[role="presentation"] [role="option"] {{
            background-color: #ffffff !important;
            color: #000000 !important;
        }}

        div[role="presentation"] [role="option"]:hover,
        div[role="presentation"] [aria-selected="true"] {{
            background-color: #f0f0f0 !important;
            color: #000000 !important;
        }}
    </style>
    """



st.markdown(custom_css, unsafe_allow_html=True)

# ==================== 🧠 Заголовок ====================
st.markdown(f"<h1 style='color:{text_color};'>😀 HR-помощник на базе GPT</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='color:{text_color};'>Автоматизируйте рутину: анализируйте резюме, создавайте вакансии, готовьте вопросы к интервью.</p>", unsafe_allow_html=True)

# ==================== 🔘 Меню ====================
page = st.radio("Выберите режим:", ["📊 Анализ резюме", "📄 Генерация вакансии", "🧠 Генерация вопросов"], horizontal=True)

# ==================== 📊 Анализ резюме ====================
if page == "📊 Анализ резюме":
    st.markdown(f"<h2 style='color:{text_color};'>📈 Анализ соответствия резюме вакансии</h2>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📄 Вакансия")
        vacancy_text = st.text_area("Введите текст вакансии вручную:", key="vacancy_text")
        vacancy_file = st.file_uploader("📎 Или загрузите файл вакансии (PDF/DOCX):", type=["pdf", "docx"], key="vacancy_file")
    with col2:
        st.subheader("🧑‍💼 Резюме")
        resume_text = st.text_area("Введите текст резюме вручную:", key="resume_text")
        resume_file = st.file_uploader("📎 Или загрузите файл резюме (PDF/DOCX):", type=["pdf", "docx"], key="resume_file")

    if st.button("🔍 Анализировать соответствие", key="analyze_btn"):
        st.write("⚙️ Здесь будет вывод анализа соответствия...")

# ==================== 📄 Генерация вакансии ====================
elif page == "📄 Генерация вакансии":
    st.markdown(f"<h2 style='color:{text_color};'>📝 Генерация или улучшение описания вакансии</h2>", unsafe_allow_html=True)

    mode = st.radio("🎯 Режим:", ["Создать с нуля", "Улучшить существующее описание"], horizontal=True)
    style = st.selectbox("🎨 Стиль оформления:", ["Деловой", "Творческий", "Минималистичный"], key="style_select")

    if mode == "Создать с нуля":
        title = st.text_input("📌 Название должности:", key="job_title")
        duties = st.text_area("📋 Обязанности:", key="duties")
        requirements = st.text_area("🎯 Требования:", key="requirements")
        benefits = st.text_area("🎁 Преимущества:", key="benefits")

        if st.button("🧾 Сгенерировать описание вакансии", key="generate_vacancy"):
            st.write("📝 Здесь появится сгенерированное описание вакансии...")

    else:
        existing_text = st.text_area("✏️ Вставьте текст вакансии для улучшения:", key="improve_text")
        improve_file = st.file_uploader("📎 Или загрузите файл (PDF/DOCX):", type=["pdf", "docx"], key="improve_file")

        if st.button("🔁 Улучшить описание", key="improve_vacancy"):
            st.write("🧠 Обработка... Улучшенное описание будет здесь.")

# ==================== 🧠 Генерация вопросов ====================
elif page == "🧠 Генерация вопросов":
    st.markdown(f"<h2 style='color:{text_color};'>🧠 Генерация вопросов для интервью</h2>", unsafe_allow_html=True)

    question_text = st.text_area("📝 Вставьте описание вакансии или требования:", key="question_input")
    question_file = st.file_uploader("📎 Или загрузите файл (PDF/DOCX):", type=["pdf", "docx"], key="question_file")

    if st.button("🎤 Сгенерировать вопросы", key="generate_questions"):
        st.write("🤖 GPT сгенерирует вопросы для интервью на основе описания...")

# ==================== 🤖 PROMPT ENGINEERING ====================
import openai

openai.api_key = "your API"


# ========== Общая функция запроса к ChatGPT ==========
def get_chatgpt_response(messages, model="gpt-4"):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0.3
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ Ошибка: {e}"

# ========== Промпт 1: Анализ соответствия резюме ==========
def analyze_resume_prompt(vacancy_text, resume_text):
    return [
        {"role": "system", "content": (
            "Ты — эксперт по найму в международной компании. "
            "Твоя задача — строго и логично оценить, насколько кандидат соответствует вакансии по опыту, навыкам и образованию. "
            "Ты формируешь профессиональный, краткий и обоснованный вывод."
        )},
        {"role": "user", "content": (
            f"Вакансия:\n{vacancy_text}\n\n"
            f"Резюме:\n{resume_text}\n\n"
            "Оцени кандидата по:\n"
            "1. Ключевым совпадениям\n"
            "2. Недостаткам\n"
            "3. Заключению (Подходит / Частично / Не подходит)\n"
            "4. Краткому обоснованию"
        )}
    ]

if page == "📊 Анализ резюме" and st.session_state.get("analyze_btn"):
    if vacancy_text and resume_text:
        with st.spinner("🤖 GPT анализирует..."):
            messages = analyze_resume_prompt(vacancy_text, resume_text)
            result = get_chatgpt_response(messages)
        st.markdown("### 🧾 Результат анализа:")
        st.write(result)

# ========== Промпт 2: Генерация вакансии ==========
def generate_vacancy_prompt(title, duties, requirements, benefits, style):
    return [
        {"role": "system", "content": (
            f"Ты — HR-копирайтер. Генерируешь текст вакансии в стиле: {style}. "
            f"Ты структурируешь информацию, делаешь описание понятным и привлекательным."
        )},
        {"role": "user", "content": (
            f"Название: {title}\n\n"
            f"Обязанности:\n{duties}\n\n"
            f"Требования:\n{requirements}\n\n"
            f"Преимущества:\n{benefits}\n\n"
            "Сформируй качественное описание вакансии."
        )}
    ]

if page == "📄 Генерация вакансии" and st.session_state.get("generate_vacancy"):
    if title and duties and requirements:
        with st.spinner("🤖 Генерация описания..."):
            messages = generate_vacancy_prompt(title, duties, requirements, benefits, style)
            result = get_chatgpt_response(messages)
        st.markdown("### 📄 Сгенерированное описание вакансии:")
        st.write(result)

# ========== Промпт 3: Улучшение описания ==========
def improve_vacancy_prompt(existing_text, style):
    return [
        {"role": "system", "content": (
            f"Ты — опытный HR-редактор. Улучши описание вакансии в стиле: {style}. "
            "Сделай его структурированным, грамотным, привлекательным. Не теряй ключевые требования."
        )},
        {"role": "user", "content": f"{existing_text}"}
    ]

if page == "📄 Генерация вакансии" and st.session_state.get("improve_vacancy"):
    if existing_text:
        with st.spinner("🧠 Улучшаем описание..."):
            messages = improve_vacancy_prompt(existing_text, style)
            result = get_chatgpt_response(messages)
        st.markdown("### ✨ Улучшенное описание:")
        st.write(result)

# ========== Промпт 4: Генерация вопросов ==========
def generate_questions_prompt(description_text):
    return [
        {"role": "system", "content": (
            "Ты — технический рекрутер. Генерируешь вопросы по описанию вакансии. "
            "Группируешь их по категориям: hard skills, soft skills, поведенческие, мотивация."
        )},
        {"role": "user", "content": (
            f"{description_text}\n\nСоставь вопросы по категориям."
        )}
    ]

if page == "🧠 Генерация вопросов" and st.session_state.get("generate_questions"):
    if question_text:
        with st.spinner("🎤 Генерация вопросов..."):
            messages = generate_questions_prompt(question_text)
            result = get_chatgpt_response(messages)
        st.markdown("### 🎯 Вопросы для интервью:")
        st.write(result)