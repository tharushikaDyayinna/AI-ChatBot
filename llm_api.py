
import google.generativeai as genai
from schema import form_structure

# ✅ Configure Gemini API key directly
genai.configure(api_key="AIzaSyBte64NJgcH-8prMF20_8avNtiPKaew1Vk")

def generate_query(user_prompt):
    model = genai.GenerativeModel("gemini-pro")

    schema_context = f"""
    You are an SQL expert. Based on this table schema:
    Table: {form_structure['table_name']}
    Columns: {', '.join(form_structure['fields'].keys())}

    Generate a valid SQL query (MySQL syntax) for the following question:
    {user_prompt}
    """

    response = model.generate_content(schema_context)
    return response.text.strip()

