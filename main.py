import os
from dotenv import load_dotenv
from agents.graph import create_workflow

def main():
    # Load environment variables
    load_dotenv()

    # Initialize the workflow
    chain = create_workflow()

    # Specify the resume file to process
    file_path = r"C:\Projects\project\resume.pdf"  # Use a raw string to avoid issues with backslashes

    try:
        # Process the resume
        result = chain.invoke(file_path)  # Ensure that your chain can handle this invocation
        print(f"Processing complete: {result}")

    except Exception as e:
        print(f"Processing failed: {str(e)}")

if __name__ == "__main__":
    main()