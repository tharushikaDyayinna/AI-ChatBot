
import google.generativeai as genai
from schema import form_structure

genai.configure(api_key="AIzaSyBte64NJgcH-8prMF20_8avNtiPKaew1Vk")

def generate_query(user_prompt):
    model = genai.GenerativeModel("gemini-2.5-pro")

    # extract info from your JSON-based schema
    table_name = form_structure["formData"]["formName"]
    field_names = [f["data_name"] for f in form_structure["fieldsData"]]

    schema_context = f"""
    You are an SQL expert. Based on this table schema:
    Table: {table_name}
    Columns: {', '.join(field_names)}

    Generate a valid SQL query (MySQL syntax) for the following question:
    {user_prompt}
    """

    response = model.generate_content(schema_context)
    return response.text.strip()


