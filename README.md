# 🏥 Predictive Health Insurance Premium Model  

A machine learning project to predict health insurance premiums based on factors like **age, BMI, smoking habits, and medical history**. 

🔗 **Live Demo**: [Health Insurance Premium Calculator](https://health-insurance-premium-calculation.streamlit.app/)  

---

## 📌 Project High level Overview  
This project was developed for **Shield Insurance** by **AtliQ AI** with the objective of building a predictive model that can accurately estimate health insurance premiums.  

The solution has two phases:  
- **Phase 1 (MVP)** – Build and deploy a predictive model with a Streamlit application.   

---

##**Before we go deep dive into ML model process, let's first discuss about some important aspects of Insurance Business.**

## 📌 Business Process Evolution  

### 🔹 As-Is Business Process (Before IT Systems – ~2008)  
1. Applicant fills out a **paper application**.  
2. Insurance agent submits the application & documents.  
3. Imaging team scans the paper form into the system.  
4. Data entry team manually creates an application in the internal system.  
5. Underwriter reviews the application → approves or rejects.  
6. Fulfillment team prints and mails the result to the applicant.  

💡 **How Premiums Were Calculated in this Era:**  
- Done manually by **actuaries** and underwriters.  
- Relied on **mortality/morbidity tables**, historical claims, and simple statistical methods.  
- Premiums were rule-of-thumb and based on experience, not automated models.  

---

### 🔹 To-Be Business Process (After IT Systems – ~2009 onwards)  
1. Applicant submits application via **website/online portal**.  
2. Underwriter reviews the application → approves or rejects.  
3. Results are **emailed** to the applicant.  

💡 **How Premiums Were Calculated in this Era:**  
- Early **rule-based systems** inside IT platforms.  
- Example rules: Smoker → +40%, High BMI → +25%.  
- Later, **Generalized Linear Models (GLMs)** were adopted for premium pricing.  
- GLMs were regulator-friendly, explainable, and widely used (SAS, R, Excel).  

Example:
Premium = Base Rate + β1(Age) + β2(Smoker) + β3(BMI) + β4(Pre-existing condition)
---

### 🔹 Current Approach (Machine Learning Era – 2015 onwards)  
Now with machine learning, insurers can:  
- Use **large datasets** (demographics, lifestyle, medical history, IoT, wearables).  
- Apply **non-linear algorithms** (XGBoost, Random Forest, Neural Nets).  
- Achieve **higher accuracy** and more personalized pricing.  

💡 **In this Project:**  
- Built a predictive model to estimate health insurance premiums.  
- Deployed as a **Streamlit application** for real-time usage by underwriters.  

---

## 🎯 Objectives  
- Achieve **>97% accuracy** in premium prediction.  
- Ensure **95% of predictions** are within **±10% error** of the actual value.  
- Provide an **interactive Streamlit app** for real-time predictions.  

---

## ⚙️ Key Features  
- Data preprocessing and EDA for insurance datasets.  
- Trained and optimized machine learning models.  
- Interactive **Streamlit web app** for premium calculation.  
- Cloud deployment – accessible from anywhere.  

---

## 🛠️ Tech Stack  
- **Python**  
- **Scikit-learn / XGBoost / RandomForest**  
- **Pandas, NumPy, Matplotlib, Seaborn**  
- **Streamlit** (deployment & UI)  

---

⚡ *Try out the model directly here →* [Health Insurance Premium Calculator](https://health-insurance-premium-calculation.streamlit.app/)  

