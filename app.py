import streamlit as st
from groq import Groq

# Connect to Groq AI
import os
from dotenv import load_dotenv
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# App title and design
st.set_page_config(page_title="Student Career Guidance Bot", page_icon="🎓")
st.title("🎓 Student Career Guidance Bot")
st.subheader("Your personal AI career advisor")
st.markdown("Tell me about yourself and I'll guide you toward the right career path!")

# Input fields
name = st.text_input("Your Name")
degree = st.text_input("Your Degree & Branch (e.g. B.Tech,B.com,MBA..etc)")
skills = st.text_area("Your Skills (e.g. Python, CAD, Excel, Communication, Product design)")
interests = st.text_area("Your Interests & Passions (e.g. Data, Design, Teaching)")
experience = st.text_area("Any Work Experience or Projects? (write 'None' if fresher)")

# Button
if st.button("Get Career Guidance 🚀"):
    if name and degree and skills and interests:
        with st.spinner("Analyzing your profile..."):

            # Message to AI
            prompt = f"""
You are an expert career counselor helping students in India find the right career path.

Student Profile:
- Name: {name}
- Degree: {degree}
- Skills: {skills}
- Interests: {interests}
- Experience: {experience}

Please provide:
1. Top 3 recommended career paths that suit this student
2. Why each career fits their profile
3. Skills they should develop for each path
4. First 3 practical steps to get started
5. Encouraging closing message

Be specific, practical and motivating. Format your response clearly with sections.
"""

            # Call Groq AI
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[  
                    {"role": "system", "content": "You are a helpful and experienced career counselor for students in India."},
                    {"role": "user", "content": prompt}
                ]
            )

            # Show result
            result = response.choices[0].message.content
            st.success("Here's your personalized career guidance!")
            st.markdown(result)
    else:
        st.warning("Please fill in all fields before getting guidance!")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ by Gopi Krishna | Powered by AI")