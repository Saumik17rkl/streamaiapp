import os
import streamlit as st
from streamlit_option_menu import option_menu
from gemini_utility import (load_gemini_pro_model,
                            geminiai_pro_vision_response,
                            embedding_model_response,
                            gemini_pro_response)
from PIL import Image
# Setting up a working directory
working_directory = os.path.dirname(os.path.abspath(__file__))

# Setting up page configuration
st.set_page_config(
    page_title="Gemini AI",
    page_icon="🧠",
    layout="centered"
)

# Sidebar navigation menu
with st.sidebar:
    selected = option_menu("Gemini AI",
                           ["Chatbot", "Image Captioning", "Embed Text", "Ask Me Anything"],
                           menu_icon="robot",
                           icons=['chat-dots-fill', 'image-fill', 'textarea-t', 'patch-question-fill'],
                           default_index=0)


# Function to translate role between gemini_pro_model and streamlit
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role


# If the "Chatbot" option is selected
if selected == "Chatbot":
    model = load_gemini_pro_model()

    # Initialize chat session if not already present
    if "chat_session" not in st.session_state:
        st.session_state.chat_session = model.start_chat(history=[])

    # Streamlit page title
    st.title("🤖 Chatbot")

    # Display the chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["text"])

    # Input fields for user's message
    user_prompt = st.chat_input("Ask Gemini Pro...")

    if user_prompt:
        st.session_state.chat_history.append({"role": "user", "text": user_prompt})
        gemini_response = st.session_state.chat_session.send_message(user_prompt)

        # Display Gemini Pro response
        st.session_state.chat_history.append({"role": "assistant", "text": gemini_response.text})
        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)

elif selected == "Image Captioning":
    st.title("📸 Snap Narate")  # Added a camera emoji beside the title

    # Initialize history if not present
    if "history" not in st.session_state:
        st.session_state.history = []

    # File uploader for image
    uploaded_image = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png", "gif", "bmp", "tiff", "webp"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)

        # Ask the user for the type of caption they want
        st.subheader("Choose the type of caption you want:")
        caption_type = st.radio(
            "Select the caption style:",
            ("Short & Sweet", "Slightly More Descriptive", "More Evocative", "Focus on the Visual")
        )

        # Define prompts for each type
        prompt_map = {
            "Short & Sweet": "Write a short and simple caption for this image.",
            "Slightly More Descriptive": "Write a slightly more descriptive caption for this image.",
            "More Evocative": "Write an emotionally engaging and evocative caption for this image.",
            "Focus on the Visual": "Write a caption that focuses on the visual details of the image."
        }
        selected_prompt = prompt_map[caption_type]

        # Generate the caption
        caption = geminiai_pro_vision_response(selected_prompt, image)

        # Display the image and caption
        col1, col2 = st.columns(2)
        with col1:
            resized_image = image.resize((800, 500))
            st.image(resized_image, caption="Uploaded Image")
        with col2:
            st.success(f"Generated Caption ({caption_type}):\n\n{caption}")

        # Store the image and the caption in session state
        st.session_state.history.append({"image": uploaded_image, "caption": caption, "type": caption_type})

    # Show previously uploaded images and their captions
    if len(st.session_state.history) > 0:
        st.write("### History of Previous Captions:")
        for idx, entry in enumerate(st.session_state.history):
            st.write(f"#### Entry {idx + 1}")
            col1, col2 = st.columns(2)
            with col1:
                image = Image.open(entry["image"])
                resized_image = image.resize((800, 500))
                st.image(resized_image, caption="Uploaded Image")
            with col2:
                st.info(f"Caption Type: {entry['type']}\n\nCaption: {entry['caption']}")

#Text Embedding page
elif selected == "Embed Text":
    st.title("📖 Embed Text")

    # Input text box
    input_text = st.text_area(label="", placeholder="Enter the text to get the embeddings", key="embed_input")

    # Check if input_text has been entered
    if input_text:
        response = embedding_model_response(input_text)
        st.markdown(response)
#Ask me anything
elif selected == "Ask Me Anything":
    st.title("❔ Ask Me Anything")

    # Input box that triggers on pressing Enter
    user_prompt = st.text_input(label=" ", placeholder="Type your question and press Enter")

    # Check if user has entered a prompt and if they pressed Enter
    if user_prompt:
        response = gemini_pro_response(user_prompt)  # Call your Gemini-Pro response function
        st.markdown(response)  # Display the result
