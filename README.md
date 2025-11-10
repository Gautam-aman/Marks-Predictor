# 🎓 Study Hours vs Marks Prediction (Machine Learning Project)

This project demonstrates a simple **Linear Regression** model that predicts a student’s marks based on the number of study hours per week.  
It uses **synthetic (dummy)** data to simulate realistic scenarios and helps beginners understand the end-to-end process of data generation, model training, evaluation, and prediction.

---

## 📊 Project Overview
The goal of this project is to:
- Analyze the relationship between study hours and marks.
- Build a predictive model using **Linear Regression**.
- Evaluate model performance using **MSE**, **MAE**, and **RMSE**.
- Visualize the correlation between study hours and marks scored.

---

## 🧠 Features
✅ Automatically generates dummy training data (`study_hours_vs_marks.csv`)  
✅ Implements model training and evaluation using `scikit-learn`  
✅ Allows user input for predictions  
✅ Uses key performance metrics  
✅ Beginner-friendly, easy-to-understand code  

---

## 🧩 Tech Stack
- **Language:** Python 🐍  
- **Libraries Used:**
  - `pandas` → Data handling  
  - `numpy` → Numerical computations  
  - `scikit-learn` → Machine Learning model  
  - `matplotlib` (optional) → Visualization  

---

## 📁 Dataset
**File:** [`study_hours_vs_marks.csv`](./study_hours_vs_marks.csv)

| Feature | Description |
|----------|--------------|
| `Study_Hours_Per_Week` | Number of study hours in a week (0–50) |
| `Marks_Scored` | Marks scored by the student (0–100) |

The dataset is **synthetic**, generated using a linear relationship with added Gaussian noise to simulate real-world variation.

