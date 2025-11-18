⭐ 𝑯𝒆𝒂𝒍𝒕𝒉𝒄𝒂𝒓𝒆 𝑫𝒂𝒕𝒂 𝑨𝒏𝒂𝒍𝒚𝒕𝒊𝒄𝒔 & 𝑨𝑰 𝑹𝒆𝒄𝒐𝒎𝒎𝒆𝒏𝒅𝒂𝒕𝒊𝒐𝒏 𝑺𝒚𝒔𝒕𝒆𝒎

A complete end-to-end analysis on healthcare data including EDA, Machine Learning, Anomaly Detection, and an AI-powered medical recommendation generator.

📌 𝑷𝒓𝒐𝒋𝒆𝒄𝒕 𝑶𝒗𝒆𝒓𝒗𝒊𝒆𝒘

This project aims to derive meaningful healthcare insights using data analysis and predictive modeling.
The system predicts Test Results, identifies unusual billing anomalies, and generates doctor-style recommendations using AI.

📂 𝑫𝒂𝒕𝒂𝒔𝒆𝒕 𝑺𝒕𝒓𝒖𝒄𝒕𝒖𝒓𝒆

The dataset includes:

Feature	Description
Name	Patient name
Age	Patient age
Gender	Male/Female
Blood Type	A+, O−, etc.
Medical Condition	Diagnosis category
Medication	Current prescribed drug
Billing Amount	Total amount billed
Admission/Discharge Dates	Hospital stay duration
Room Number	Assigned room
Test Results	Target variable
Insurance Provider	Health insurance

⚠️ Dataset is excluded from the repo using .gitignore as part of best practices.

📊 𝑻𝒂𝒔𝒌 𝟏 — 𝑬𝒙𝒑𝒍𝒐𝒓𝒂𝒕𝒐𝒓𝒚 𝑫𝒂𝒕𝒂 𝑨𝒏𝒂𝒍𝒚𝒔𝒊𝒔
✔ 𝐃𝐢𝐬𝐭𝐫𝐢𝐛𝐮𝐭𝐢𝐨𝐧 𝐀𝐧𝐚𝐥𝐲𝐬𝐢𝐬

Age Distribution

Billing Amount Distribution

Room Number Spread

✔ 𝐂𝐚𝐭𝐞𝐠𝐨𝐫𝐢𝐜𝐚𝐥 𝐅𝐫𝐞𝐪𝐮𝐞𝐧𝐜𝐲

Medical Condition

Admission Type

Medication

✔ 𝐈𝐧𝐬𝐢𝐠𝐡𝐭𝐬

Most patients fall under Diabetes, Cancer, or Obesity

Billing shows large variation with several expensive outliers

Emergency admissions dominate the dataset

🤖 𝑻𝒂𝒔𝒌 𝟐 — 𝑻𝒆𝒔𝒕 𝑹𝒆𝒔𝒖𝒍𝒕 𝑷𝒓𝒆𝒅𝒊𝒄𝒕𝒊𝒐𝒏 (𝑺𝒖𝒑𝒆𝒓𝒗𝒊𝒔𝒆𝒅 𝑳𝒆𝒂𝒓𝒏𝒊𝒏𝒈)
✔ 𝐖𝐨𝐫𝐤𝐟𝐥𝐨𝐰

Missing value handling

One-hot encoding

Train-test split (80/20)

Model trained using Random Forest Regressor

Metrics used:

𝑴𝑺𝑬

𝑹² 𝐬𝐜𝐨𝐫𝐞

Predicted vs actual plotted for comparison

⚠️ 𝑻𝒂𝒔𝒌 𝟑 — 𝑨𝒏𝒐𝒎𝒂𝒍𝒚 𝑫𝒆𝒕𝒆𝒄𝒕𝒊𝒐𝒏 𝒊𝒏 𝑩𝒊𝒍𝒍𝒊𝒏𝒈 𝑨𝒎𝒐𝒖𝒏𝒕𝒔
✔ 𝐌𝐞𝐭𝐡𝐨𝐝: Isolation Forest

Flags both extremely high and extremely low billings

Useful for fraud detection, extreme medical cases, or billing errors

✔ 𝐕𝐢𝐬𝐮𝐚𝐥𝐢𝐳𝐚𝐭𝐢𝐨𝐧

Scatterplot shows:
🟦 Normal points
🔴 Anomalies

🩺 𝑻𝒂𝒔𝒌 𝟒 — 𝑨𝑰 𝑫𝒐𝒄𝒕𝒐𝒓 𝑹𝒆𝒄𝒐𝒎𝒎𝒆𝒏𝒅𝒂𝒕𝒊𝒐𝒏 𝑮𝒆𝒏𝒆𝒓𝒂𝒕𝒐𝒓

A custom AI function produces medical advice based on:

Age

Medical Condition

Medication

Predicted Test Result

✔ 𝐒𝐚𝐦𝐩𝐥𝐞 𝐎𝐮𝐭𝐩𝐮𝐭
🩺 AI Doctor Recommendation

Based on the predicted test result, your current health condition appears to be in the serious concern range.

Patient Summary:
- Age: 30
- Medical Condition: Cancer
- Current Medication: Paracetamol

Recommended Advice:
- Seek immediate medical attention, adjust medication as needed, and avoid strenuous activities until your next evaluation.

📁 𝑷𝒓𝒐𝒋𝒆𝒄𝒕 𝑺𝒕𝒓𝒖𝒄𝒕𝒖𝒓𝒆
📦 healthcare_project
│
├── 📓 healthcare_analysis.ipynb
├── 🗂️ venv/
├── 📄 README.md
├── 📄 .gitignore
└── 📄 requirements.txt

▶️ 𝑯𝒐𝒘 𝒕𝒐 𝑹𝒖𝒏 𝒕𝒉𝒊𝒔 𝑷𝒓𝒐𝒋𝒆𝒄𝒕
1️⃣ Clone Repo
git clone https://github.com/dhanushkar006/healthcare.git
cd healthcare

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate  # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Launch Jupyter Notebook
jupyter notebook

📦 𝑹𝒆𝒒𝒖𝒊𝒓𝒆𝒎𝒆𝒏𝒕𝒔
pandas
numpy
matplotlib
seaborn
scikit-learn
jupyter

🚀 𝑭𝒖𝒕𝒖𝒓𝒆 𝑰𝒎𝒑𝒓𝒐𝒗𝒆𝒎𝒆𝒏𝒕𝒔

Add SHAP explainability

Deploy using FastAPI

Build a Streamlit dashboard

Add grid/random search for hyperparameters

Introduce time-series analysis on hospital stays

🙌 𝑨𝒄𝒌𝒏𝒐𝒘𝒍𝒆𝒅𝒈𝒎𝒆𝒏𝒕𝒔

Dataset by Prasad22 on Kaggle

Python ecosystem: scikit-learn, Jupyter, VS Code
