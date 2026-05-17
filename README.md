# Serene AI: Your Personal Study Companion

## Why I Built This

Being a university student is overwhelming. Even if you are organized, 
even if you show up to every lecture and take notes on everything, it 
still gets chaotic. There are slides, readings, assignment PDFs, practice 
problems, and recorded lectures all piling up at once. And when exam 
season hits, you are left staring at a mountain of material with no clear 
idea of where to start or what you actually understand versus what you 
just think you understand.

I felt this myself as a Data Science student at SFU. I would spend hours 
going through materials and still feel lost. The resources were there. 
I just could not connect them in a way that actually helped me study.

So I built Serene AI.

Serene AI is a personal AI study companion that actually knows your course 
material. You upload your notes, slides, and practice problems, and then 
you just talk to it. Ask it to explain a concept. Ask it where to find 
something in your notes. Ask it to quiz you. It answers based on what is 
actually in your materials, not just generic internet knowledge.

But here is what makes it different from just asking ChatGPT. Serene AI 
remembers you. Every session, it tracks what you are asking about, notices 
where you keep getting stuck, and builds a picture of your weak spots over 
time. So instead of you guessing what to study, it tells you.

I built this because I wanted to use it myself. And I think every 
university student would too.

---

## What Serene AI Can Do Right Now

### Phase 1 (Completed)
- Upload any course PDF including lecture notes, practice problems, 
  and assignments
- Ask any question about your uploaded material in plain English
- Get detailed, clear explanations based on what is actually in your 
  document, not generic internet answers
- Tested with real Statistics course material from SFU STAT 302

---

## What Is Coming Next

### Phase 2 (In Progress)
- Chat history so you can ask follow-up questions naturally
- Session memory that remembers what you have asked before
- Weak topic detection that notices where you keep getting stuck
- A personal progress dashboard showing your study patterns over time

### Phase 3 (Planned)
- Practice problem generator that creates new questions in your 
  professor's style based on your weak topics
- Answers and explanations for every generated problem

### Phase 4 (Vision)
- Named projects for each course, for example STAT 302 or CMPT 353
- Organized folders inside each project for lecture notes, practice 
  problems, and assignments
- Custom instructions for each folder so the AI knows exactly how 
  to help depending on what you are studying
- Full structured study agent experience built for university students

---

## Tech Stack

- Python 3.13
- Streamlit for the web interface
- OpenAI GPT API for AI powered answers
- PyPDF for reading and extracting text from PDF files
- Python dotenv for keeping API keys safe

---

## How To Run Serene AI Locally

Make sure you have Python installed. Then follow these steps:

**Step 1: Clone the repository**
```bash
git clone https://github.com/AlizadaMadina/serene-ai.git
cd serene-ai
```

**Step 2: Create and activate a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Step 3: Install the required libraries**
```bash
pip install -r requirements.txt
```

**Step 4: Add your OpenAI API key**

Create a file called .env in the project folder and add this line:

OPENAI_API_KEY=your_key_here

**Step 5: Run the app**
```bash
streamlit run app.py
```

Then open your browser and go to localhost:8501. That is it. 
Serene AI is running.

---

## Who This Is For

This is for any university student who has ever felt overwhelmed by 
the amount of course material they need to study. It is especially 
useful for Data Science and STEM students who deal with dense lecture 
notes, complex practice problems, and multiple courses at once.

It was built by a Data Science student at Simon Fraser University 
in Vancouver, Canada, for students exactly like her.

---

## Project Status

Phase 1 is complete and working. Phase 2 is actively in development.

Built with purpose by Madina Alizada