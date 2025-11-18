**🏥 Healthcare Data Analysis & AI Recommendation System**

A complete end-to-end data analytics and machine learning project using a healthcare dataset.
This project includes EDA, Supervised Learning, Unsupervised Anomaly Detection, and an AI Doctor Recommendation Generator.

**📌 Project Overview**

This project analyzes a healthcare dataset to understand patient demographics, medical conditions, billing patterns, and test results.
It uses machine learning to predict Test Results and employs Isolation Forest to detect anomalies in billing amounts.
An AI-powered function generates a doctor-style medical recommendation based on model predictions.

**📂 Dataset**

Source: Kaggle
Dataset columns include:

Feature	Description
Name	Patient name
Age	Age of patient
Gender	Male/Female
Blood Type	e.g., A+, O−
Medical Condition	Diabetes, Cancer, etc.
Date of Admission	Admission date
Doctor	Assigned doctor
Hospital	Hospital name
Insurance Provider	Insurance company
Billing Amount	Total bill amount
Room Number	Assigned room number
Admission Type	Emergency / Urgent / Elective
Discharge Date	Date discharged
Medication	Drugs provided
Test Results	Continuous numerical value

⚠️ Dataset not included in this repository (ignored intentionally using .gitignore).

**🧪 Task Breakdown**
**🧹 Task 1 — Exploratory Data Analysis (EDA)**

Performed detailed analysis using pandas, matplotlib, and seaborn.

✔ Numerical Distributions

Age Distribution

Billing Amount Distribution

Room Number Distribution

✔ Categorical Frequencies

Medical Condition

Admission Type

Medication

✔ Insights

Most patients fall into common medical categories such as Diabetes, Cancer, Obesity.

Billing Amounts show a wide range with few very high outliers.

Admission types are mostly Emergency or Urgent.

**🤖 Task 2 — Supervised Learning: Predict Test Results**
✔ Steps Performed

Cleaned and pre-processed data

Encoded categorical variables using one-hot encoding

Split into Training (80%) and Testing (20%)

Trained a Random Forest Regressor

Evaluated model with:

Mean Squared Error (MSE)

R² Score

Displayed Predicted vs Actual results

✔ Key Outcome

The model successfully learned patterns from patient data and produced reasonably accurate predictions.

**⚠️ Task 3 — Unsupervised Learning: Anomaly Detection (Billing Amount)**

Using Isolation Forest, detected unusually high or low billing amounts.

✔ Findings

Most billing values fall within normal limits.

Some entries flagged as anomalies, possibly due to:

Rare expensive procedures

Incorrect billing

Data entry errors

✔ Visualization

A scatter plot showing normal vs anomalous points.

**🩺 Task 4 — AI Doctor Recommendation Generator**

An AI-powered function generates a doctor-like recommendation using:

Patient Age

Medical Condition

Current Medication

Predicted Test Result

**✔ Example Output**
🩺 AI Doctor Recommendation

Based on the predicted test result, your current health condition appears to be in the serious concern range.

Patient Summary:
- Age: 30
- Medical Condition: Cancer
- Current Medication: Paracetamol

Recommended Advice:
- Seek immediate medical attention, adjust medication as needed, and avoid strenuous activities until your next evaluation.

Please consult your healthcare provider for a detailed diagnosis and personalized treatment plan.

**📁 Project Structure**
healthcare_project/
│
├── healthcare_analysis.ipynb     # Main notebook (EDA + ML + Anomaly Detection + AI)
├── venv/                          # Virtual environment (ignored in git)
├── .gitignore                     # Ignore unnecessary files
├── README.md                      # Project documentation
└── requirements.txt               # Python dependencies (optional)

▶️ How to Run the Project
1️⃣ Clone the repository
git clone https://github.com/dhanushkar006/healthcare.git
cd healthcare

2️⃣ Create a virtual environment
python -m venv venv
source venv/Scripts/activate  # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Open the notebook
jupyter notebook

**📦 Recommended requirements.txt**

Add this file if not present:

pandas
numpy
matplotlib
seaborn
scikit-learn
jupyter

**🚀 Future Improvements**

Deploy model using FastAPI

Add SHAP interpretability

Build a Streamlit web UI

Add better hyperparameter tuning (RandomizedSearchCV / GridSearchCV)

**🙌 Acknowledgements**

Dataset by Prasad22 on Kaggle

Tools: Python, scikit-learn, Jupyter, Matplotlib, VS Code
