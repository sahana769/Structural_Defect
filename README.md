# 🏗️ Structural Defects — AI-Assisted Structural Defect Identification System (GenAI)

An **AI-powered structural inspection system** that analyzes construction site images to **detect, classify, and assess structural defects**, and generates a **professional, engineer-style inspection report** in **multiple Indian languages**.

Built using **Google Gemini (Vision + Prompt Engineering)** and **Streamlit**, this project focuses on **real-world construction and infrastructure use cases**.

---

## 🌍 Multilingual Report Generation (Key Feature)

The system can generate inspection reports in the following languages, so **any stakeholder can understand the output**:

- English  
- Hindi  
- Kannada  
- Tamil  
- Gujarati  
- Marathi  

👉 Language is selected directly from the UI, and the report is **generated natively in that language using prompt engineering** (not post-translation).

---

## 🔍 What This System Does

Upload an image of a structure (wall, beam, column, slab, etc.) and the system generates a **complete structural inspection report**, including:

- Identification of structural defects  
  - Cracks  
  - Spalling  
  - Corrosion  
  - Honeycombing  
  - Exposed reinforcement  
- Defect classification and description  
- Severity assessment (Low / Medium / High)  
- Structural and safety impact analysis  
- Estimated time before permanent damage  
- Short-term and long-term repair solutions  
- Approximate repair cost (INR) and implementation time  
- Preventive measures for future construction  
- Engineer-style report format (bullets + tables)

---

## 🧠 AI & Prompt Engineering Highlights

- Multimodal **vision-based defect understanding**
- **Prompt engineering to simulate a structural engineer**
- Multi-defect detection from a single image
- Severity, risk, and urgency assessment
- Cost and remediation reasoning
- Language-aware professional report generation

---

## 🛠️ Tech Stack

| Component | Technology |
|--------|-----------|
| Programming Language | Python |
| GenAI Model | Google Gemini (Vision + Text) |
| UI Framework | Streamlit |
| Image Processing | PIL |
| Prompt Engineering | Structured engineering prompts |
| Environment | python-dotenv |
| Deployment | Streamlit-compatible |

---

## ⚠️ Important Note (API Usage)

This project uses the **Google Gemini Free API**.

- The live app **may or may not respond** depending on available API quota.
- For uninterrupted usage:
  1. Clone the repository
  2. Add your own `GOOGLE_API_KEY` in a `.env` file
  3. Run the app locally or deploy it

---

## 🚀 Why This Project Matters

- Real **civil & construction engineering use case**
- Designed for **engineers, site supervisors, and field teams**
- Supports **regional languages** for wider accessibility
- Demonstrates strong **GenAI + prompt engineering skills**
- End-to-end system: Image → Analysis → Decision → Report

---

## 📌 Resume / LinkedIn One-Liner

Built an AI-assisted, multilingual structural defect detection system using Gemini Vision and prompt engineering to analyze construction images and generate professional inspection reports with severity, cost, and remediation insights.

---

## 📂 Repository

https://github.com/sahana769/Structural_Defect.git
