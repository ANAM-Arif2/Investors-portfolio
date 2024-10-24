import os
import yaml

UPLOAD_DIR = os.path.join( "public")

os.makedirs(UPLOAD_DIR, exist_ok=True)

async def file_uploader(rail_type, file):
    pdf_path = os.path.join("public", rail_type, "pdfs")
    os.makedirs(pdf_path, exist_ok=True)

    file_info = []

    # Check if the uploaded file is a PDF
    if file.content_type != 'application/pdf':
        return 0

    # Construct the file path
    file_location = os.path.join(pdf_path, file.filename)

    # Save the uploaded file to the specified directory
    with open(file_location, "wb") as f:
        contents = await file.read()
        f.write(contents)

    file_info.append({
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(contents)  # Get size in bytes
    })
    return file_location


async def create_yaml_file(user_input, policies, output_file, rail_type):
    """
    Creates a YAML file with the specified instruction content, incorporating user input and company policies.

    Parameters:
    - user_input (str): The content to be inserted into the instructions section.
    - policies (list of str): List of company policy statements to be inserted.
    - output_file (str): The name of the output YAML file. Defaults to 'config.yml'.
    """
    rail_path = os.path.join("public", rail_type, "ymls")
    os.makedirs(rail_path, exist_ok=True)
    # Convert the list of policies into a formatted string with bullet points
    formatted_policies = "\n".join([f"- {policy}" for policy in policies])

    # Define the YAML structure using LiteralString for 'content' fields
    yaml_structure = {
        'models': [
            {
                'type': 'main',
                'engine': 'openai',
                'model': 'gpt-3.5-turbo-instruct'
            }
        ],
        'instructions': [
            {
                'type': 'general',
                'content': LiteralString(f"""you are a classifier who classifies the prompt for the bot of a company named cybergen. You respond either 0 or 1
if the prompts are related to {user_input} then you respond as 1 otherwise you should respond 0.you will also entertain user with greetings.if user say hi you will response with hey there how are you.
.if the user say i m fine, how are you. you will say i am good thank you. .
Your response will be used in python code, so be strict in your response.""")
            }
        ],
        'rails': {
            'input': {
                'flows': [
                    'self check input'
                ]
            }
        },
        'prompts': [
            {
                'task': 'self_check_input',
                'content': LiteralString(f"""Your task is to check if the user message below complies with the company policy for talking with the company bot.

Company policy for the user messages:

{formatted_policies}


User message: "{{{{ user_input }}}}"


Question: Should the user message be blocked (Yes or No)?

Answer:""")
            }
        ]
    }

    # Write the YAML structure to the file
    try:
        with open(f"{rail_path}/test.yml", 'w') as file:
            yaml.dump(yaml_structure, file, sort_keys=False, default_flow_style=False, allow_unicode=True)
        print(f"YAML file '{output_file}' has been created successfully.")
        return rail_path
    except Exception as e:
        print(f"An error occurred while creating the YAML file: {e}")


# Step 1: Define a custom string class to handle multi-line strings with block scalars
class LiteralString(str):
    pass

# Step 2: Add a representer to PyYAML for the LiteralString class
def literal_str_representer(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')

# Register the representer with PyYAML
yaml.add_representer(LiteralString, literal_str_representer)