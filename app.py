import streamlit as st
from google import genai
from google.genai import types
import logging
from adk_agent.agent import ZindukaAgent

# --- ZINDUKA CHATBOT CONFIG ---
REGION = "global"
PROJECT_ID = "zinduka-chatbot"  # Replace with your actual GCP project ID
GEMINI_MODEL_NAME = "gemini-2.5-flash"

temperature = 0.3
top_p = 0.95

system_instructions = (
    "You are Zinduka, a compassionate mental health and gender-based violence support assistant. "
    "Offer empathetic, respectful, and confidential guidance. "
    "Avoid giving medical diagnoses; instead, encourage professional or community support where needed."
)

# --- Initialize Vertex AI Client ---
try:
    client = genai.Client(
        vertexai=True, 
        project=PROJECT_ID, 
        location=REGION)
    print(f"Vertex AI Client initialized successfully with model {GEMINI_MODEL_NAME}")
except Exception as e:
    st.error(f"Error initializing VertexAI client: {e}")
    st.stop()


# --- Core Chat Function ---
def call_model(prompt: str, model_name: str) -> str:
    """
    Calls the Gemini model with the user's prompt and system instructions.
    """
    try:
        
        content = [
            types.Content(role="user", #this indicates that the content is from the user
            parts=[types.Part.from_text(prompt)]) #allows multiple types of content from the user
        ]
            
        response = client.models.generate_content(
            model=model_name,
            contents=content,
            #config=types.GenerateContentConfig(
                #system_instruction=types.Content(
                    #role="system", parts=[types.Part.from_text(system_instructions)]
                #),
                #temperature=temperature,
                #top_p=top_p,
            ),
        #)project 

        logging.info(f"[call_model_response] LLM Response: \"{response.text}\"")
        return response.text

    except Exception as e:
        return f"Error: {e}"


# --- Streamlit Interface ---
st.set_page_config(page_title="Zinduka-bot", page_icon="💬")
st.title("💬 Zinduka-bot")
st.caption("Your safe space for mental health and GBV support 💛")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hello! I’m Zinduka-bot. How are you feeling today?"}
    ]

# Display previous chat messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
if prompt := st.chat_input("Type your message here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    with st.spinner("Thinking..."):
        model_response = call_model(prompt, GEMINI_MODEL_NAME)

    st.session_state.messages.append({"role": "assistant", "content": model_response})
    st.chat_message("assistant").write(model_response)
