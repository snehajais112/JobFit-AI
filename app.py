import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader

genai.configure(api_key="enter your api key")

model = genai.GenerativeModel("gemini-3.6-flash")


st.set_page_config(
    page_title="AI Recruitment Agent",
    page_icon="🤖",
    layout="wide"
)

st.title(" AI Recruitment Agent")
st.write("Upload Resume + Paste Job Description")


uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)


job_description = st.text_area(
    "Paste Job Description",
    height=250
)


if uploaded_file:

    pdf = PdfReader(uploaded_file)

    resume_text = ""

    for page in pdf.pages:
        text = page.extract_text()
        if text:
            resume_text += text

    st.success("Resume Uploaded Successfully ✅")

    with st.expander("View Resume Text"):
        st.write(resume_text)

    if st.button("Analyze Candidate"):

        if not job_description.strip():
            st.warning("Please paste Job Description.")
            st.stop()

        with st.spinner("Analyzing Candidate..."):

            prompt = f"""
You are an Expert Technical Recruiter and ATS System.

Compare the Resume with the Job Description.

JOB DESCRIPTION:
{job_description}

RESUME:
{resume_text}

Return output in the following format:

# ATS SCORE
Give ATS score out of 100.

# MATCH PERCENTAGE
Give job match percentage.

# SKILLS MATCHED
List matching skills.

# MISSING SKILLS
List missing skills.

# CANDIDATE STRENGTHS
Bullet points.

# CANDIDATE WEAKNESSES
Bullet points.

# INTERVIEW READINESS
Beginner / Intermediate / Strong

# TOP 10 INTERVIEW QUESTIONS
Generate questions based on JD.

# HIRING RECOMMENDATION
Short recommendation:
Hire / Consider / Reject

# RESUME IMPROVEMENT SUGGESTIONS
Actionable suggestions.
"""

            response = model.generate_content(prompt)

            st.subheader("📊 Recruitment Analysis")
            st.markdown(response.text)
