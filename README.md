# JobFit AI 

## AI-Powered Resume Screening & Job Matching System

JobFit AI is an intelligent recruitment assistant built using Python, Streamlit, and Gemini AI. The application helps recruiters and hiring teams evaluate candidate resumes against job descriptions by providing ATS insights, skill-gap analysis, candidate evaluation, interview questions, and hiring recommendations.

---

##  Features

### Resume Analysis
- Upload resumes in PDF format
- Extract and process resume content automatically
- Generate professional candidate summaries

### Job Description Matching
- Compare candidate profiles with job requirements
- Identify matching skills and competencies
- Highlight missing skills and qualification gaps

### ATS Evaluation
- Generate ATS-style compatibility scores
- Measure candidate-job fit percentage
- Provide actionable improvement suggestions

### AI-Powered Insights
- Candidate strengths and weaknesses analysis
- Interview readiness assessment
- Personalized resume improvement recommendations
- Top interview questions based on the target role

### Hiring Support
- Automated candidate evaluation
- Data-driven hiring recommendations
- Faster initial screening process

---

##  Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Core Application Logic |
| Streamlit | User Interface |
| Gemini AI | Resume Analysis & Recommendations |
| PyPDF | PDF Text Extraction |
| Git & GitHub | Version Control |

---

##  Project Structure

```text
JobFit-AI/
│
├── app.py
├── requirements.txt
├── README.md
└── screenshots/
```

---

##  Installation

Clone the repository:

```bash
git clone https://github.com/your-username/JobFit-AI.git
cd JobFit-AI
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Setup

Add your Gemini API Key:

```python
genai.configure(api_key="YOUR_API_KEY")
```

---

##  Run Application

```bash
streamlit run app.py
```

##  Business Use Case

Recruiters often spend significant time manually reviewing resumes. JobFit AI automates the initial screening process by:

- Evaluating candidate-job fit
- Identifying skill gaps
- Generating interview questions
- Providing hiring recommendations

This reduces manual effort and improves recruitment efficiency.

---

##  Future Enhancements

- Real ATS scoring engine
- Multi-resume comparison
- Resume ranking system
- Candidate shortlisting dashboard
- ChromaDB-based candidate search
- RAG-powered recruitment assistant
- WhatsApp & Email integration

---

##  Author

Sneha Jaiswal

B.Tech (Computer Science and Engineering)

Passionate about Generative AI, AI Agents, Automation, and Intelligent Applications.

---

##  Project Highlights

- Built using Generative AI
- Practical HR Tech Use case
- End-to-End AI Application
- Resume Intelligence & Recruitment Automation.
