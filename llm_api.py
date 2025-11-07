import google.generativeai as genai
from schema import form_structure

# Configure Gemini API
genai.configure(api_key="AIzaSyBte64NJgcH-8prMF20_8avNtiPKaew1Vk")

def generate_query(user_prompt):
    model = genai.GenerativeModel("gemini-2.5-pro")  # ✅ valid model name

    # ✅ Dynamically extract table name and field names from JSON
    table_name = form_structure["formData"]["formName"]
    field_names = [f["data_name"] for f in form_structure["fieldsData"]]

    # ✅ Create structured prompt for Gemini
    schema_context = f"""
    You are an SQL generator bot. 
    Based on this database structure:
    Table: {table_name}
    Columns: {', '.join(field_names)}

    User Question: {user_prompt}

    Return only the SQL query.
    Do not include any explanations, comments, or formatting.
    """

    # ✅ Get Gemini response
    response = model.generate_content(schema_context)

    # ✅ Return only the text content
    return response.text.strip()


