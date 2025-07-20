# Cardiovascular Risk Predictor 🫀🧬

A Python GUI application that predicts **cardiovascular risk** using patient lifestyle data (age, cholesterol, smoking, alcohol) and potential DNA mutation markers associated with cardiovascular-related diseases.

---



## 👩‍💻 Developed By
   
      Alishba Waheed


## 📌 Features

- ✅ **User-friendly Tkinter GUI**
- 🧬 **DNA mutation-based disease analysis**
- 📈 **Dynamic bar chart visualization of risk factors**
- 💡 Calculates total risk score and estimated cardiovascular risk (%)
- 🧾 Supports multiple disease selections with known mutation data

---

## Screenshots
GUI Interface

Bar Chart Output

## 🚀 Getting Started
Prerequisites

. Python  (Download Python)
.  Visual Studio Code (Recommended)

How to Run
🔹 Clone this Repository
``bash
git clone https://github.com/alishbawaheed/cardiovascular-riskpredictor.git
cd cardiovascular-riskpredictor
Launch Visual Studio Code

Go to File > Open Folder...

Select the cardiovascular-riskpredictor folder

🔹 Set Up Virtual Environment (Recommended)

In VS Code terminal:

python -m venv .venv
.\.venv\Scripts\activate       # For Windows PowerShell

🔹 Install Required Libraries
pip install matplotlib
🔹 Run the App
In the VS Code terminal:

python cardiovascular risk predictor.py

---

## 📁 Project Structure

📁 cardiovascular-riskpredictor  
├── 📄 cardiovascular risk predictor.py  – Main GUI application  
├── 📄 README.md – Project documentation  
└── 📁 .venv – Virtual environment (optional)  


## 💡 Usage
Enter Patient Info: Input age, cholesterol level, and lifestyle habits (smoking, alcohol).
Select Disease(s): Choose one or more cardiovascular-related diseases with known DNA mutation data.
Input DNA Mutations: Paste DNA sequences to check for mutation presence.
Calculate Risk: Click the Calculate Risk button to compute a risk score (out of 10).
View Results: A bar chart will show the contribution of each risk factor, and the app will display the estimated cardiovascular risk percentage


## Technologies Used
Python 3.x
Tkinter – for GUI development
Matplotlib – for visualizing risk contributions
VS Code – Recommended IDE