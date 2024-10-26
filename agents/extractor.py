import os
import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content

def extractor(prompt):
    """
    Extracts structured information from resume text using Gemini
    """
    genai.configure(api_key=os.environ["key"])
    
    # Define the schema for structured output
    schema = {
        "type": content.Type.OBJECT,
        "properties": {
            "personal_info": {
                "name": content.Schema(type=content.Type.STRING),
                "phone_no": content.Schema(type=content.Type.NUMBER),
                "email": content.Schema(type=content.Type.STRING),
            },
            "education": {
                "degree": content.Schema(type=content.Type.STRING),
                "university": content.Schema(type=content.Type.STRING),
            },
            "work_experience": {
                "company": content.Schema(type=content.Type.STRING),
                "role": content.Schema(type=content.Type.STRING),
                "description": content.Schema(type=content.Type.STRING),
            }
        }
    }
    
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config={"response_schema": schema}
    )
    
    return model.generate_content(prompt).text