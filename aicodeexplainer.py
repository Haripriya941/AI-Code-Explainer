import streamlit as st
import google.generativeai as genai
genai.configure(api_key="")
model = genai.GenerativeModel("gemini-2.5-flash")
st.title("AI Code Explainer")
prompt = st.text_input("Paste your code here")
if st.button("Submit"):
    res = model.generate_content(
        prompt + """
        Explain this code in simple terms.
        Explain like I am a beginner and add comments to the code.
        """
    )
    st.write(res.text)
