import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt

# Predefined normal DNA sequence
normal_sequence = "ATGCGTACGTAGCTAGCTAGCTAGCTA"

# Diseases and their mutation sequences and risk involvement
disease_data = {
    "Marfan Syndrome": {"mutated": "ATGCGTACGTAGCTAGATAGCTAGCTA", "mutation": True},
    "Familial Hypercholesterolemia": {"mutated": "ATGCGTACGTAGCTAGCTAGATAGCTA", "mutation": True},
    "Hypertrophic Cardiomyopathy": {"mutated": "ATGCGTACGTAGATAGCTAGCTAGCTA", "mutation": True},
    "Long QT Syndrome": {"mutated": "ATGCGTACGTAGCTAGCTAGCTAGAAA", "mutation": True},
    "Noonan Syndrome": {"mutated": "ATGCGTACGTAGCTAGTTAGCTAGCTA", "mutation": True},
    "Ehlers-Danlos Syndrome": {"mutated": "ATGCGTACGTAGCTAGCTAGCGAGCTA", "mutation": True},
    "Diabetes Type II": {"mutated": "ATGCGTACGTAGCTAGCTAGCTTGCTA", "mutation": False},
    "Asthma": {"mutated": "ATGCGTACGTAGCTAGCTAGCTAGTTA", "mutation": False},
    "Arthritis": {"mutated": "ATGCGTACGTAGCTAGCTAGCTAGCTT", "mutation": False},
    "Hypothyroidism": {"mutated": "ATGCGTACGTAGCTAGCTAGCTAGGTA", "mutation": False}
}

def calculate_risk():
    try:
        name = name_entry.get().strip()
        age = int(age_entry.get())
        cholesterol = int(chol_entry.get())
        smoke = smoke_var.get()
        alcohol = alcohol_var.get()
        selected_diseases = [disease_listbox.get(i) for i in disease_listbox.curselection()]

        if not name:
            messagebox.showwarning("Input Error", "Please enter the patient's name.")
            return

        if not selected_diseases:
            messagebox.showwarning("Input Error", "Please select at least one disease.")
            return

        # Mutation score
        mutation_score = sum([1 for d in selected_diseases if disease_data[d]["mutation"]])

        # Age risk
        age_risk = 0
        if age >= 60:
            age_risk = 3
        elif age >= 45:
            age_risk = 2
        elif age >= 30:
            age_risk = 1

        # Cholesterol risk
        chol_risk = 0
        if cholesterol > 240:
            chol_risk = 3
        elif cholesterol > 200:
            chol_risk = 2
        elif cholesterol > 180:
            chol_risk = 1

        # Smoking & alcohol risk
        smoke_risk = 2 if smoke else 0
        alcohol_risk = 1 if alcohol else 0

        # Final calculation
        total_risk = smoke_risk + alcohol_risk + chol_risk + mutation_score + age_risk
        risk_percent = (total_risk / 10) * 100

        # Update result display
        risk_result_label.config(
            text=f"Patient: {name}\n"
                 f"Total Risk Score: {total_risk}/10\n"
                 f"Estimated Cardiovascular Risk: {risk_percent:.2f}%"
        )

        # Mutation bar color logic
        mutation_related = any(disease_data[d]['mutation'] for d in selected_diseases)

        # Bar chart
        risks = [smoke_risk, alcohol_risk, chol_risk, mutation_score, age_risk]
        labels = ['Smoking', 'Alcohol', 'Cholesterol', 'Mutation', 'Age']
        colors = [
            'orangered',
            'crimson',
            'purple',
            'red' if mutation_related else 'lightgreen',
            'lightgreen'
        ]

        plt.figure(figsize=(8, 5))
        plt.bar(labels, risks, color=colors)
        plt.title(f'Risk Factor Contribution for {name}')
        plt.ylabel('Risk Score')
        plt.ylim(0, 4)
        plt.tight_layout()
        plt.show()

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for age and cholesterol.")

# GUI Setup
root = tk.Tk()
root.title("Cardiovascular Risk Calculator")

# Patient Name
tk.Label(root, text="Patient Name:").grid(row=0, column=0, sticky="e")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

# Age
tk.Label(root, text="Age:").grid(row=1, column=0, sticky="e")
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1)

# Cholesterol
tk.Label(root, text="Cholesterol Level:").grid(row=2, column=0, sticky="e")
chol_entry = tk.Entry(root)
chol_entry.grid(row=2, column=1)

# Lifestyle risks
smoke_var = tk.BooleanVar()
tk.Checkbutton(root, text="Smoker", variable=smoke_var).grid(row=3, column=0, columnspan=2)

alcohol_var = tk.BooleanVar()
tk.Checkbutton(root, text="Alcohol Use", variable=alcohol_var).grid(row=4, column=0, columnspan=2)

# Disease list
tk.Label(root, text="Select Diseases:").grid(row=5, column=0, sticky="ne")
disease_listbox = tk.Listbox(root, selectmode="multiple", height=10, exportselection=0)
disease_listbox.grid(row=5, column=1)

for disease in disease_data:
    disease_listbox.insert(tk.END, disease)

# Button to calculate
tk.Button(root, text="Calculate Risk", command=calculate_risk).grid(row=6, column=0, columnspan=2, pady=10)

# Output label
risk_result_label = tk.Label(root, text="", justify="left")
risk_result_label.grid(row=7, column=0, columnspan=2)

root.mainloop()

    