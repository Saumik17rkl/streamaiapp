import os
import json
import google.generativeai as genai

# Setting up a working directory
working_directory = os.path.dirname(os.path.abspath(__file__))
config_file_path = f"{working_directory}/config.json"
config_data = json.load(open(config_file_path))

# Loading the API key
GOOGLE_API_KEY = config_data["GOOGLE_API_KEY"]

# Configure google generativeai with API key
genai.configure(api_key=GOOGLE_API_KEY)

# Function to load the newer Gemini model for chatbot (assuming 'gemini-1.5-flash' or equivalent)
def load_gemini_pro_model():
    # Use the updated model name here, like "gemini-1.5-flash"
    gemini_pro_model = genai.GenerativeModel("gemini-1.5-flash")
    return gemini_pro_model

# Function for image captioning (assuming the new version supports image captioning)
def geminiai_pro_vision_response(prompt, image):
    # Updated model name for image captioning task
    gemini_pro_vision_model = genai.GenerativeModel("gemini-1.5-flash")
    response = gemini_pro_vision_model.generate_content([prompt, image])
    result = response.text
    return result


#Function for embedding model
def embedding_model_response(input_text):
    # Use the correct model name format
    embedding_model = "models/embedding-001"

    # Generate embeddings for the input text
    embedding = genai.embed_content(model=embedding_model,
                                    content=input_text,
                                    task_type="retrieval_document")
    embedding_list =  embedding["embedding"]
    return embedding_list


#Function to get a response from gemini pro to LLM

def gemini_pro_response(user_prompt):
    gemini_pro_model=genai.GenerativeModel("gemini-pro")
    response = gemini_pro_model.generate_content(user_prompt)
    result = response.text
    return result

