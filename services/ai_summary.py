import os
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")


def generate_summary(article_text):

    prompt = f"""
You are an expert Telecom Industry Analyst.

Analyze the following telecom news article and generate:

1. Executive Summary (4-5 lines)

2. Key Highlights
- Bullet 1
- Bullet 2
- Bullet 3

3. Important Numbers

4. Companies Mentioned

5. Technology Mentioned

6. Benchmark Impact
(High / Medium / Low)

Article:

{article_text}
"""

    response = model.generate_content(prompt)

    return response.text
