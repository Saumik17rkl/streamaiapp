# StreamLit Ai App


Gemini AI
Gemini AI is an interactive platform that leverages cutting-edge machine learning models to provide various AI-powered features. The tool includes a chatbot, image captioning, text embedding, and a "Ask Me Anything" feature. With a clean and intuitive UI powered by Streamlit, Gemini AI is designed to handle text-based interactions, generate insightful captions for images, and provide detailed responses to user queries.

Features
1. Chatbot
A chatbot powered by the Gemini AI model, which can have conversations with users.
It uses a session-based approach to remember chat history and deliver accurate responses.
The model responds intelligently to user queries in real-time.
2. Image Captioning
Upload an image, and the model generates captions with varying degrees of detail.
You can choose from different styles, such as:
Short & Sweet
Slightly More Descriptive
More Evocative
Focus on the Visual
The captions are tailored based on the style you select.
3. Embed Text
Converts input text into embeddings that can be used for various tasks like document retrieval.
The feature leverages the latest text embedding models to provide high-quality vector representations of text.
4. Ask Me Anything
Allows you to ask Gemini AI any question, and it will generate an answer based on its trained model.
The text input triggers a response from the Gemini model when the user presses Enter.
Installation
Prerequisites
Python 3.x installed.
Install required Python libraries using pip:
bash
Copy
Edit
pip install streamlit streamlit-option-menu pillow gemini-utility
Setting Up
Clone this repository to your local machine.
Navigate to the project directory and install dependencies.
You need to create a config.json file with your API key for the Gemini model.
Running the App
Once the dependencies are installed, run the following command to start the Streamlit app:

bash
Copy
Edit
streamlit run app.py
Open your browser and visit the URL http://localhost:8501 to interact with the app.

How to Use
Chatbot: Start typing your questions in the chatbot interface. The model will remember the context and provide responses.
Image Captioning: Upload an image, select the caption style, and get the AI-generated caption.
Embed Text: Enter any text, and the model will return its embedding representation.
Ask Me Anything: Type your question, and Gemini AI will provide a detailed answer.
Example Screenshots
Chatbot Interaction

Image Captioning

Contributing
We welcome contributions to Gemini AI! If you find any bugs, issues, or want to add new features, please feel free to fork the repository and submit a pull request.
