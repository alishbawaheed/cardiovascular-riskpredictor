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
1. Enter Patient Info:
   - Input age
   - Cholesterol level
   - Lifestyle habits (e.g., smoking, alcohol consumption)

2. Select Disease(s):
   - Choose one or more cardiovascular-related diseases
   - Uses known DNA mutation data

3. Input DNA Mutations:
   - Paste DNA sequences to check for mutation presence

4. Calculate Risk:
   - Click the “Calculate Risk” button
   - App computes a risk score (out of 10)

5. View Results:
   - A bar chart displays the contribution of each risk factor
   - Final cardiovascular risk percentage is shown



## Technologies Used
🐍 Python 3.x – Core language  
🖼️ Tkinter – For GUI development  
📊 Matplotlib – For visualizing risk contributions  
🧠 VS Code – Recommended IDE for development  
