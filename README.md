# StudyMate AI

StudyMate AI is an AI-powered student study assistant built using Flask and the Google Gemini API.

It helps students with common study tasks such as understanding concepts, summarizing notes, improving written answers, and practicing topics through automatically generated quizzes.

This project was developed as part of the ShadowFox AI Engineer Internship Beginner Level task.

## Features

### 1. Explain Concept
Enter a concept or question and StudyMate AI provides a beginner-friendly explanation with:

- Simple Explanation
- How It Works
- Example
- Key Points

### 2. Summarize Notes
Enter study notes and the application generates a structured summary containing:

- Main Topic
- Important Points
- Key Terms
- Quick Revision

### 3. Improve Answer
Enter an existing answer and the AI improves its clarity and organization while keeping the original meaning.

The output includes:

- Improved Answer
- What Was Improved
- Key Points

### 4. Generate Quiz
Enter a topic or study content and the application generates 5 beginner-friendly questions with answers.

## Technologies Used

- Python
- Flask
- Google Gemini API
- HTML
- CSS
- Jinja2

## Project Structure

```text
StudyMate-AI/
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── gemini_service.py
├── test_gemini.py
├── requirements.txt
└── .gitignore
