# 🤖 HR Assistant powered by GPT-4

An interactive Streamlit-based application designed to automate key HR tasks using OpenAI's GPT-4 API.

Built as part of a test assignment for MWS AI, this project showcases how Large Language Models (LLMs) can streamline the hiring process — from resume analysis to job post creation and interview preparation.

---

## 🧩 Features

| Function                | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| 📊 Resume Analysis       | Compares job descriptions with resumes and evaluates fit using GPT         |
| 📄 Job Post Generator    | Creates or improves job listings based on inputs and selected writing style|
| 🧠 Interview Questions   | Generates categorized interview questions based on a job description       |
| 🎨 Dark/Light Theme      | Custom CSS support for a pleasant UX in both dark and light modes          |

---

## ⚙️ Technologies Used

- **Python 3.13**
- **Streamlit** – front-end interface
- **OpenAI GPT-4** – language model via `openai` API
- **PyPDF2 & docx2txt** – for reading resume/job post files
- **.env** – for local API key management
- **Custom HTML + CSS** – for theming

---
## 🖼️ Screenshots

### 🌞 Light Mode
<img width="3370" height="808" alt="Снимок экрана 2025-07-31 164723" src="https://github.com/user-attachments/assets/6c483680-2482-4271-b801-47df837bcbe8" />

### 🌙 Dark Mode
<img width="3438" height="1203" alt="Снимок экрана 2025-08-01 012450" src="https://github.com/user-attachments/assets/bac10832-800b-4698-8f05-045d23213a5d" />


> Screenshots demonstrate the clean UI in both visual styles, showing how the app adapts for readability and user comfort.

---
## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/KalinNika/hr-assistant-gpt.git
   cd hr-assistant-gpt

2. Install the dependencies:
   pip install -r requirements.txt
   
3. Set your OpenAI API key:
Create a .env file with the following content:
OPENAI_API_KEY=your_openai_api_key_here

4. Run the app:
   streamlit run app.py

##  🧠 Prompt Engineering Logic
Each core feature uses a carefully crafted prompt with system role injection:

Resume Analysis: logical fit scoring based on experience, skills, education

Job Generation: GPT-4 acts as a copywriter or editor based on style

Interview Questions: questions categorized by soft/hard/behavioral skills

This structure demonstrates modular prompt design and real-world LLM usage in HR tasks.

## 📂 Project Structure
├── app.py           # Main Streamlit application

├── .env             # API key placeholder

## 📌 Use Case
This project is ideal for:

HR teams looking to prototype GPT integration

AI prompt engineers showcasing applied LLM usage

Recruiters streamlining manual processes

## 💡 Future Improvements (Planned)
Resume-to-vacancy match scoring with visualization

Database of candidate results

API-based integration with ATS systems

## 🧑‍💻 Author
Developed by @KalinNika

AI Developer & Prompt Engineer focused on applied automation with LLMs.


