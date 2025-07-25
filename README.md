# 🩺 Medical Insurance Cost Predictor

This project is a machine learning-powered web app that predicts the **medical insurance cost** of an individual based on key personal attributes. It uses a **Linear Regression model**, and the interface is built using **Streamlit** for easy interaction.

## 🚀 Demo
You can run the app locally using:

```bash
streamlit run app.py

📌 Features
Predicts medical insurance charges using user input

User-friendly web interface built with Streamlit

Trained on real insurance dataset

Includes preprocessing and model training pipeline

Fully open-source and ready for deployment

📁 Project Structure
bash
Copy
Edit
medical_insurance_cost/
│
├── app.py                  # Streamlit frontend
├── model.pkl               # Trained Linear Regression model
├── insurance.csv           # Dataset used
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation

📊 Input Parameters
Age
Gender
BMI
Number of Children
Smoking Status
Region

⚙️ Tech Stack
Python
Pandas, NumPy
Scikit-learn
Streamlit
Matplotlib / Seaborn (optional for EDA)

✅ How to Run
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/medical_insurance_cost.git
cd medical_insurance_cost
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the Streamlit app:

bash
streamlit run app.py

📚 Dataset
This project uses the Medical Cost Personal Dataset from Kaggle.

🧠 Model
The model is a Linear Regression model trained on a cleaned and preprocessed dataset. Key steps:
Categorical Encoding
Normalization
Model training and evaluation (R² score)

🙋‍♀️ Author
Bhagyashri Sonar
Data Science Enthusiast | B.Tech IT Final Year Student

🌐 License
This project is open-source and available under the MIT License.

Let me know if you want a shorter version or want to include images, deployment links, or Streamlit Cloud badges.


