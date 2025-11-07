import google.generativeai as genai
from schema import form_structure

genai.configure(api_key="AIzaSyBte64NJgcH-8prMF20_8avNtiPKaew1Vk")

def generate_query(user_prompt):
    model = genai.GenerativeModel("gemini-2.5-pro")  

    table_name = form_structure["formData"]["formName"]
    field_names = [f["data_name"] for f in form_structure["fieldsData"]]

    schema_context = f"""
    You are an SQL generator. 
    Based on this table:
    Table: {table_name}
    Columns: {', '.join(field_names)}

    Question: {user_prompt}

    Return ONLY the SQL query. 
    No explanations, no text, no formatting, only SQL syntax.
    """

    response = model.generate_content(schema_context)
    return response.text.strip()



