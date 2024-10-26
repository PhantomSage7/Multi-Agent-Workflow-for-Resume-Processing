import os
import PyPDF2
import docx

def reader(file_path):
    """
    Reads and extracts text from PDF or DOCX files
    """
    _, file_extension = os.path.splitext(file_path)
    text = ""
    try:
        if file_extension.lower() == '.pdf':
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                for page in reader.pages:
                    text += page.extract_text() or ''
        
        elif file_extension.lower() == '.docx':
            doc = docx.Document(file_path)
            for paragraph in doc.paragraphs:
                text += paragraph.text + '\n'
        
        return text.strip() if text else "No text found"
    except Exception as e:
        return f"An error occurred: {str(e)}"