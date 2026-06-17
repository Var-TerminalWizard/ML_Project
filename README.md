# 🎓 Student Performance Prediction System

An end-to-end Machine Learning project that predicts a student's **Mathematics Score** based on demographic, educational, and academic performance attributes.

The project demonstrates a complete ML workflow, including data ingestion, preprocessing, model training, hyperparameter tuning, model persistence, and deployment through a Flask web application.

---

## 🚀 Project Overview

Educational institutions often need insights into student performance to identify learning gaps and improve outcomes. This project leverages Machine Learning to predict student mathematics scores using factors such as:

* Gender
* Race/Ethnicity
* Parental Level of Education
* Lunch Type
* Test Preparation Course
* Reading Score
* Writing Score

The application enables users to input student information and receive a predicted mathematics score in real time.

---

## ✨ Features

* End-to-End Machine Learning Pipeline
* Automated Data Ingestion
* Data Preprocessing using Scikit-Learn Pipelines
* Feature Engineering with ColumnTransformer
* Multiple Regression Models Comparison
* Hyperparameter Tuning using GridSearchCV
* Model Persistence using Pickle
* Flask-Based Web Interface
* Docker Support
* GitHub Actions CI/CD Workflow

---

## 🛠️ Technology Stack

| Category             | Technologies                    |
| -------------------- | ------------------------------- |
| Programming Language | Python                          |
| Machine Learning     | Scikit-Learn, CatBoost, XGBoost |
| Data Processing      | Pandas, NumPy                   |
| Visualization        | Matplotlib, Seaborn             |
| Web Framework        | Flask                           |
| Version Control      | Git & GitHub                    |
| Containerization     | Docker                          |
| Automation           | GitHub Actions                  |

---

## 📂 Project Architecture

```text
Dataset
   │
   ▼
Data Ingestion
   │
   ▼
Data Transformation
   │
   ▼
Model Training
   │
   ▼
Best Model Selection
   │
   ▼
Model Persistence
   │
   ▼
Prediction Pipeline
   │
   ▼
Flask Web Application
   │
   ▼
Predicted Math Score
```

---

## 📁 Project Structure

```text
ML_Project/
│
├── .github/
├── artifacts/
├── docs/
├── notebook/
├── src/
│   ├── components/
│   ├── pipeline/
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── templates/
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 📊 Machine Learning Workflow

1. Data Collection
2. Data Ingestion
3. Data Transformation
4. Feature Engineering
5. Model Training
6. Hyperparameter Tuning
7. Model Evaluation
8. Best Model Selection
9. Model Serialization
10. Deployment using Flask

---

## 🧠 Models Evaluated

The following regression algorithms were evaluated:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting Regressor
* AdaBoost Regressor
* K-Nearest Neighbors Regressor
* XGBoost Regressor
* CatBoost Regressor

The best-performing model is automatically selected based on evaluation metrics.

---

## 📖 Documentation

Detailed project documentation, architecture explanations, implementation details, and deployment guides are available in the project documentation website.

👉 **Full Documentation:** [Documentation Link Here]

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Var-TerminalWizard/ML_Project.git
cd ML_Project
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

---

## 🐳 Docker

Build the Docker image:

```bash
docker build -t student-performance-predictor .
```

Run the container:

```bash
docker run -p 5000:5000 student-performance-predictor
```

---

## 🎯 Skills Demonstrated

* Machine Learning Engineering
* Data Preprocessing
* Model Selection & Evaluation
* Hyperparameter Optimization
* Pipeline Development
* Flask Deployment
* Docker Containerization
* CI/CD Automation
* Software Engineering Best Practices

---

## 🔮 Future Improvements

* Cloud Deployment (AWS / Azure / GCP)
* Experiment Tracking with MLflow
* Model Monitoring
* REST API Development
* Unit Testing
* Automated Retraining Pipelines
* Advanced MLOps Integration

---

## 👨‍💻 Author

**Var-TerminalWizard**