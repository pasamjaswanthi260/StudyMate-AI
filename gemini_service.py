from google import genai
import os


api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def generate_study_response(feature, question):

    if feature == "explain":

        prompt = f"""
You are StudyMate AI, a helpful study assistant for college students.

The student wants to understand a concept.

Concept or question:
{question}

Explain it in a simple and beginner-friendly way.

Use exactly these section headings:

1. Simple Explanation
2. How It Works
3. Example
4. Key Points

Use plain text only.
Do not use Markdown.
Do not use backslashes.
Do not use asterisks.
Do not use hashtags.
Do not put a backslash before periods.
Keep each heading on its own line.
Leave one blank line between sections.
"""

    elif feature == "summarize":

        prompt = f"""
You are StudyMate AI, a helpful study assistant for college students.

The student wants to summarize their study notes.

Study notes:
{question}

Create a clear and easy-to-study summary.

Use exactly these section headings:

1. Main Topic
2. Important Points
3. Key Terms
4. Quick Revision

Use plain text only.
Do not use Markdown.
Do not use backslashes.
Do not use asterisks.
Do not use hashtags.
Do not put a backslash before periods.
Keep each heading on its own line.
Leave one blank line between sections.
"""

    elif feature == "improve":

        prompt = f"""
You are StudyMate AI, a helpful study assistant for college students.

The student has written an answer and wants to improve it.

Original answer:
{question}

Improve the answer while keeping its original meaning.

Use exactly these section headings:

1. Improved Answer
2. What Was Improved
3. Key Points

Use simple student-friendly language.
Make the answer clearer and more organized.
Do not change the original meaning.

Use plain text only.
Do not use Markdown.
Do not use backslashes.
Do not use asterisks.
Do not use hashtags.
Do not put a backslash before periods.
Keep each heading on its own line.
Leave one blank line between sections.
"""

    elif feature == "quiz":

        prompt = f"""
You are StudyMate AI, a helpful study assistant for college students.

The student wants to practice a topic using a quiz.

Topic or study content:
{question}

Generate exactly 5 beginner-friendly questions based only on the provided content.

Use this format:

Question 1:
Answer:

Question 2:
Answer:

Question 3:
Answer:

Question 4:
Answer:

Question 5:
Answer:

Use plain text only.
Do not use Markdown.
Do not use backslashes.
Do not use asterisks.
Do not use hashtags.
Do not put a backslash before periods.
Put each question and answer on separate lines.
Leave one blank line between questions.
Keep answers short and accurate.
"""

    else:

        return "Please select a valid study feature."


    try:

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        if not response.text:

            return "The AI did not return a response. Please try again."


        # Get the AI response
        cleaned_response = response.text

        # Remove unwanted Markdown formatting
        cleaned_response = cleaned_response.replace("\\.", ".")
        cleaned_response = cleaned_response.replace("**", "")
        cleaned_response = cleaned_response.replace("###", "")

        # Remove extra spaces at the beginning/end of lines
        lines = cleaned_response.splitlines()

        cleaned_lines = []

        for line in lines:

            line = line.strip()

            if line:
                cleaned_lines.append(line)
            else:
                # Keep only one blank line
                if cleaned_lines and cleaned_lines[-1] != "":
                    cleaned_lines.append("")

        cleaned_response = "\n".join(cleaned_lines).strip()

        return cleaned_response


    except Exception as e:

        print("Gemini API Error:", e)

        return (
            "Sorry, the AI service is currently unavailable. "
            "Please check your internet connection or try again later."
        )