import streamlit as st
import openai

# Use API key from secrets.toml
openai.api_key = st.secrets["openai"]["api_key"]

# Streamlit UI setup
st.set_page_config(page_title="Daily Motivation Generator", page_icon="💡")
st.title("💡 Daily Motivation Generator")
st.markdown("Select your current mood to receive a motivational quote powered by Generative AI.")

# Mood selection
mood = st.selectbox("How are you feeling today?", [
    "Anxious", "Unmotivated", "Tired", "Happy", "Stressed", "Lost", "Confused"
])

# Button to trigger quote generation
if st.button("Generate Quote"):
    prompt = f"Give a short motivational quote for someone who is feeling {mood.lower()}."
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        quote = response["choices"][0]["message"]["content"]
        st.success(quote.strip())
    except Exception as e:
        st.error("❌ Something went wrong. Please check your OpenAI API key or try again later.")
