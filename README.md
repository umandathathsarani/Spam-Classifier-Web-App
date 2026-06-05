# 📩 Spam Email Classifier - Web Application

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.58.0-FF4B4B.svg?logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.9.0-F7931E.svg?logo=scikit-learn&logoColor=white)
![Status](https://img.shields.io/badge/Status-Production-success.svg)
![License](https://img.shields.io/badge/License-Proprietary-red.svg)

An end-to-end Machine Learning web application engineered to autonomously detect and filter spam in text messages and emails using Natural Language Processing (NLP).

🌍 **Live Application:** [Spam Email Classifier App](https://spam-classifier-web-app-umanda-binuri.streamlit.app)

**Engineered by:** Mummullage Binuri Umanda Thathsarani  
**Academic Context:** BSc (Hons) Information Technology Specializing in Artificial Intelligence, SLIIT

---

## 🧠 System Architecture Flow

The pipeline transforms unstructured human language into mathematical vectors for probabilistic classification.

`Raw Data` ➔ `NLTK Preprocessing` (Tokenization & Stop-words) ➔ `CountVectorizer` (Bag-of-Words Matrix) ➔ `Multinomial Naive Bayes` (Statistical Inference) ➔ `Streamlit UI` (Real-time Prediction)

---

## 📊 The Dataset
This repository includes the raw data folder (`data/`) for transparency and academic review. 
* **Source:** The open-source SMS Spam Collection dataset.
* **Volume:** 5,572 labeled records.
* **Structure:** Tab-separated values (`.tsv`) containing binary classifications (`ham` or `spam`) and raw text features.

---

## 🚀 Key Features
* **Zero-Latency Inference:** The pre-trained `.pkl` models load into cache upon server boot, allowing for instantaneous classification of user input.
* **Mathematical Feature Extraction:** Converts linguistic patterns into weighted probability matrices.
* **Cloud-Native Deployment:** Fully hosted on Streamlit Community Cloud with continuous integration linked directly to the `main` branch.

---

## 💻 Local Development Setup

To initialize this environment locally for testing or contribution:

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

---

## ⚙️ Technical Stack
| Domain | Technology | Purpose |
| :--- | :--- | :--- |
| **Frontend/UI** | `Streamlit` | Interactive web server and user interface rendering. |
| **Core ML Engine** | `Scikit-learn` | Algorithm training, mathematical vectorization, and prediction logic. |
| **Data Processing** | `Pandas`, `NLTK` | Dataset parsing, linguistic cleaning, and stop-word removal. |
| **Model Serialization** | `Joblib` | Exporting and compressing trained model states to `.pkl` files. |

---
*Copyright © 2026 Mummullage Binuri Umanda Thathsarani. All Rights Reserved.*