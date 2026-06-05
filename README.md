# 📩 Spam Email Classifier - Web Application

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.58.0-FF4B4B.svg)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.9.0-orange.svg)
![License](https://img.shields.io/badge/License-Proprietary-red.svg)

A production-ready web application that leverages Natural Language Processing (NLP) to autonomously classify text messages and emails as either "Spam" or "Ham" (legitimate) in real-time.

🌍 **Live Demo:** [Spam Email Classifier App](https://spam-classifier-web-app-umanda-binuri.streamlit.app)

**Developed by:** Mummullage Binuri Umanda Thathsarani  
**Academic Affiliation:** BSc (Hons) in Information Technology Specializing in Artificial Intelligence, SLIIT

---

## 🚀 Application Overview

This repository houses the frontend UI and deployment configuration for the Spam Classifier engine. It transitions the core Machine Learning pipeline from a local command-line interface into an accessible, interactive web product hosted on Streamlit Community Cloud.

**Key Features:**
* **Real-Time Inference:** Instantly processes user input through a pre-trained Multinomial Naive Bayes model.
* **Interactive UI:** Built with Streamlit for a responsive, user-friendly experience.
* **Cloud Deployed:** Fully hosted with automated continuous integration directly from the `main` branch.

---

## 🛠️ Local Development Setup

If you wish to run this web application locally on your machine:

**1. Clone the repository**
```bash
git clone [https://github.com/umandathathsarani/Spam-Classifier-Web-App.git](https://github.com/umandathathsarani/Spam-Classifier-Web-App.git)
cd Spam-Classifier-Web-App
```

**2. Isolate the environment**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
python -c "import nltk; nltk.download('stopwords')"
```

**4. Launch the Web Server**
```bash
streamlit run app.py
```
*The application will automatically open in your default web browser at `http://localhost:8501`.*

---

## ⚙️ Technology Stack
* **Frontend Framework:** Streamlit
* **Machine Learning:** Scikit-learn (Multinomial Naive Bayes, CountVectorizer)
* **Data Processing:** Pandas, NLTK (Natural Language Toolkit)
* **Model Serialization:** Joblib
* **Hosting:** Streamlit Community Cloud