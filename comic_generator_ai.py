import os
import requests
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
STABILITY_API_KEY = os.getenv("STABILITY_API_KEY")
LLM_MODEL = "gpt-4o"


client = OpenAI(api_key=OPENAI_API_KEY)


st.set_page_config(page_title="ComicCrafter AI", page_icon="🎭", layout="wide")
st.title("🎭 ComicCrafter AI")


prompt = st.text_area("Enter your comic idea:", placeholder="A robot exploring an abandoned city...")

# Function to generate image using Stability AI
def generate_image_stability(prompt):
    if not prompt.strip():
        st.error("Error: Prompt cannot be empty for image generation.")
        return None

    try:
        url = "https://api.stability.ai/v2beta/stable-image/generate/core"
        headers = {
            "Authorization": f"Bearer {STABILITY_API_KEY}",
            "Accept": "image/*"
        }
        files = {
            "prompt": (None, prompt),
            "output_format": (None, "png"),
            "aspect_ratio": (None, "1:1")
        }

        response = requests.post(url, headers=headers, files=files)  # Use multipart/form-data

        if response.status_code == 200:
            return response.content  # Return image content
        else:
            st.error(f"Stability AI Error: {response.status_code} - {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"Stability AI Error: {e}")
        return None

# Generate Comic on Button Click
if st.button("Generate Comic"):
    if not prompt.strip():
        st.error("Please enter a valid comic idea.")
    else:
        
        with st.spinner("Generating story..."):
            try:
                response = client.chat.completions.create(
                    model=LLM_MODEL,
                    messages=[{"role": "user", "content": prompt}]
                )
                story = response.choices[0].message.content.strip()
            except Exception as e:
                st.error(f"Error generating story: {e}")
                story = None

        
        if story:
            st.markdown("### Story")
            st.write(story)

            
            with st.spinner("Generating image..."):
                image_data = generate_image_stability(prompt)

        
            if image_data:
                st.image(image_data, caption="AI-Generated Comic Panel", use_container_width=True)
            else:
                st.error("Failed to generate image.")
