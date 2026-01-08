import streamlit as st
import google.generativeai as genai
from PIL import Image
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("GOOGLE_API_KEY")

if not key:
    st.error("GOOGLE_API_KEY not found")
    st.stop()

genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-2.5-flash-lite")

st.sidebar.title(":red[UPLOAD YOUR IMAGE HERE]")
uploaded_image = st.sidebar.file_uploader("Here", type=["jpeg", "jpg", "png"])

if uploaded_image:
    image = Image.open(uploaded_image)
    st.sidebar.subheader(":blue[UPLOADED IMAGE]")
    st.sidebar.image(image)

st.title(":orange[STRUCTURAL DEFECTS] : :green[AI assisted structural defect identifier in construction business]")

st.write("""
To use the application follow the steps below:
* Upload the image
* Select report language
* Click Generate Report
* Download the generated report
""")

language = st.radio(
    "Select Report Language",
    ["English", "Hindi", "Kannada", "Tamil", "Gujarati", "Marathi"],
    horizontal=True
)

rep_title = st.text_input("Report Title")
prep_by = st.text_input("Report Prepared By")
prep_for = st.text_input("Report Prepared For")

language_instruction = {
    "English": "Generate the entire report in English.",
    "Hindi": "पूरी रिपोर्ट हिंदी भाषा में तैयार करें।",
    "Kannada": "ಸಂಪೂರ್ಣ ವರದಿಯನ್ನು ಕನ್ನಡ ಭಾಷೆಯಲ್ಲಿ ರಚಿಸಿ.",
    "Tamil": "முழு அறிக்கையையும் தமிழ் மொழியில் உருவாக்கவும்.",
    "Gujarati": "સંપૂર્ણ અહેવાલ ગુજરાતી ભાષામાં તૈયાર કરો.",
    "Marathi": "संपूर्ण अहवाल मराठी भाषेत तयार करा."
}

prompt = f"""
Assume you are a senior structural engineer.

The user has provided an image of a construction structure.

{language_instruction[language]}

Use the following details exactly:
Title: {rep_title}
Prepared By: {prep_by}
Prepared For: {prep_for}
Report Date: {dt.datetime.now().date()}

Generate a professional structural inspection report with the following sections:

1. Introduction
2. Defect Identification and Classification
   - Identify all visible defects (cracks, spalling, corrosion, honeycombing, exposed reinforcement, etc.)
3. Defect Description and Structural Impact
4. Severity Assessment (Low / Medium / High)
   - Mention whether each defect is avoidable or inevitable
5. Estimated Time Before Permanent Structural Damage
6. Remediation Plan
   - Short-term solution (cost in INR + time)
   - Long-term solution (cost in INR + time)
7. Preventive Measures for Future Construction
8. Conclusion

Use bullet points and tables wherever suitable.
Keep the report concise and within 3 pages.
Make it readable and suitable for civil engineers, site supervisors, and construction teams.
"""

if st.button("Generate Report"):
    if uploaded_image is None:
        st.error("Please upload an image first.")
    else:
        with st.spinner("Generating Report..."):
            response = model.generate_content(
                [prompt, image],
                generation_config={"temperature": 0.2}
            )

        st.success("Report Generated Successfully")
        st.write(response.text)

        st.download_button(
            label="Download Report",
            data=response.text,
            file_name="structural_defect_report.txt",
            mime="text/plain"
        )
