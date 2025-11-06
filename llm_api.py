import google.generativeai as genai
import json
from schema import form_structure

# Configure Gemini API
genai.configure(api_key="AIzaSyBte64NJgcH-8prMF20_8avNtiPKaew1Vk")

# Initialize Gemini model
model = genai.GenerativeModel("gemini-2.5-flash-preview-09-2025")

def generate_query(user_question: str) -> str:
    json_schema = json.dumps(form_structure, indent=2)

    prompt = f"""
    You are an intelligent system that generates structured queries or expressions.
    Below is a JSON object that defines a form's data structure.

    JSON Schema:
    {json_schema}

    User question: "{user_question}"

    Generate a valid query, calculation expression, or formula
    using only the field names in the schema.
    Respond with the query only (no explanation).
    """

    response = model.generate_content(prompt)
    return response.text.strip()
