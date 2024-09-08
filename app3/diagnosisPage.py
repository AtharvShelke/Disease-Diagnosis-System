import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox

def ontype(i):
    if search_entry.get()=="Select Your Symptoms:":
        search_entry.delete(0, tk.END)
        tk.Frame(app, bg="#082b5b", width=350, height=1).place(x=530, y=142)


# Disease data dictionary
disease_data = {
    "Hypertension": "High blood pressure, headaches, dizziness",
    "Diabetes": "Increased thirst, frequent urination, fatigue",
    "Heart disease": "Chest pain, shortness of breath, fatigue",
    "Cancer": "Varies by type and stage, e.g., lumps, weight loss",
    "Stroke": "Numbness, confusion, severe headache, trouble walking",
    "Arthritis": "Joint pain, stiffness, swelling",
    "Alzheimer's disease": "Memory loss, disorientation, behavior changes",
    "Asthma": "Wheezing, shortness of breath, coughing",
    "COPD": "Chronic cough, shortness of breath, wheezing",
    "Influenza": "Fever, cough, sore throat, fatigue",
    "Pneumonia": "High fever, cough with mucus, shortness of breath",
    "Depression": "Persistent sadness, loss of interest, fatigue",
    "Anxiety disorders": "Excessive worry, restlessness, rapid heartbeat",
    "Osteoporosis": "Bone pain, loss of height, fractures",
    "Obesity": "Excessive body weight, increased risk of related conditions",
    "HIV/AIDS": "Fever, fatigue, swollen lymph nodes, opportunistic infections",
    "Hepatitis": "Jaundice, fatigue, abdominal pain, dark urine",
    "Malaria": "High fever with chills, headache, sweating",
    "Tuberculosis": "Cough (often with blood), fever, night sweats",
    "Cholera": "Profuse, watery diarrhea, vomiting, dehydration",
    "Measles": "High fever, cough, red, watery eyes, red rash",
    "Chickenpox": "Itchy rash, fever, fatigue, headache",
    "Dengue fever": "High fever, severe headache, joint and muscle pain",
    "Zika virus": "Mild fever, rash, joint pain, red eyes",
    "Ebola": "Fever, severe headache, muscle pain, vomiting, diarrhea",
    "Chlamydia": "Painful urination, unusual discharge, lower abdominal pain",
    "Gonorrhea": "Painful urination, unusual discharge, pelvic pain",
    "Syphilis": "Sores, rash, fever, fatigue",
    "Herpes": "Painful sores or blisters, itching and tingling",
    "Inflammatory bowel disease (IBD)": "Abdominal pain, diarrhea, weight loss",
    "Crohn's disease": "Diarrhea, abdominal pain, fatigue",
    "Ulcerative colitis": "Bloody diarrhea, abdominal pain, urgency to have a bowel movement",
    "Rheumatoid arthritis": "Joint pain, swelling, morning stiffness, fatigue",
    "Multiple sclerosis": "Fatigue, muscle weakness, numbness, coordination problems",
    "Parkinson's disease": "Tremors, muscle rigidity, slowness of movement",
    "Migraine": "Severe headaches, nausea, sensitivity to light and sound",
    "Chronic kidney disease": "Fatigue, swelling in legs/feet, changes in urination",
    "Cirrhosis": "Fatigue, jaundice, abdominal pain, confusion",
    "Irritable bowel syndrome (IBS)": "Abdominal pain, changes in bowel habits, bloating",
    "Psoriasis": "Red, scaly patches, itching, burning",
    "Eczema": "Dry, itchy skin, rash, inflammation",
    "Lupus": "Fatigue, joint pain, skin rashes, fever",
    "Fibromyalgia": "Widespread pain and tenderness, fatigue, sleep disturbances",
    "PCOS (Polycystic ovary syndrome)": "Irregular periods, excess hair growth, acne, weight gain",
    "Endometriosis": "Pelvic pain, painful periods, painful intercourse",
    "Menopause": "Hot flashes, night sweats, mood swings, vaginal dryness",
    "Erectile dysfunction": "Difficulty achieving/maintaining an erection",
    "Premature ejaculation": "Ejaculation occurring too quickly during sexual intercourse",
    "Infertility": "Difficulty conceiving after a year of trying",
    "Allergies": "Sneezing, runny/stuffy nose, itchy/watery eyes, skin rash",
    "Celiac disease": "Digestive problems, diarrhea, fatigue, skin rash",
    "Glaucoma": "Increased intraocular pressure, gradual loss of peripheral vision",
    "Macular degeneration": "Blurred/distorted central vision",
    "Osteoarthritis": "Joint pain, stiffness, reduced range of motion",
    "Gout": "Sudden, severe joint pain, swelling, redness",
    "Anemia": "Fatigue, weakness, pale skin, shortness of breath",
    "Leukemia": "Fatigue, frequent infections, easy bleeding/bruising, enlarged lymph nodes",
    "Lymphoma": "Swollen lymph nodes, fever, unexplained weight loss",
    "Pancreatitis": "Severe abdominal pain, nausea, vomiting",
    "Gastritis": "Stomach pain/discomfort, nausea, vomiting, bloating",
    "GERD (Gastroesophageal Reflux Disease)": "Heartburn, regurgitation of stomach acid, chest pain",
    "Peptic ulcer": "Burning or gnawing pain in the stomach, nausea, vomiting",
    "Autism": "Difficulty with social interaction, repetitive behaviors, communication challenges",
    "ADHD (Attention-Deficit/Hyperactivity Disorder)": "Inattention, hyperactivity, impulsivity",
    "Schizophrenia": "Delusions, hallucinations, disorganized thinking, social withdrawal",
    "Bipolar disorder": "Episodes of mania and depression, mood swings",
    "OCD (Obsessive-Compulsive Disorder)": "Obsessions, compulsions (repetitive behaviors)",
    "PTSD (Post-Traumatic Stress Disorder)": "Flashbacks, nightmares, anxiety, avoidance behaviors",
    "Anorexia nervosa": "Extreme weight loss, fear of gaining weight, distorted body image",
    "Bulimia nervosa": "Binge eating, followed by purging behaviors (vomiting, laxative use), guilt and shame",
    "Binge-eating disorder": "Recurrent episodes of overeating, feelings of guilt and loss of control",
    "Sickle cell anemia": "Fatigue, pain crises, jaundice, swelling of hands/feet",
    "Hemophilia": "Excessive bleeding, easy bruising, joint pain/swelling"
}

# List of symptoms
symptoms_list = [
    "High blood pressure", "Headaches", "Dizziness", "Increased thirst", "Frequent urination", "Fatigue", "Chest pain",
    "Shortness of breath", "Lumps", "Weight loss", "Numbness", "Confusion", "Severe headache", "Trouble walking", "Joint pain",
    "Stiffness", "Swelling", "Memory loss", "Disorientation", "Behavior changes", "Wheezing", "Coughing", "Chronic cough",
    "Fever", "Sore throat", "High fever", "Cough with mucus", "Jaundice", "Abdominal pain", "Dark urine", "Vomiting",
    "Dehydration", "Itchy rash", "Sweating", "Dry skin", "Inflammation", "Hot flashes", "Night sweats", "Mood swings",
    "Difficulty achieving/maintaining an erection", "Premature ejaculation", "Difficulty conceiving", "Sneezing",
    "Runny/stuffy nose", "Itchy/watery eyes", "Skin rash", "Digestive problems", "Diarrhea", "Increased intraocular pressure",
    "Gradual loss of peripheral vision", "Blurred/distorted central vision", "Reduced range of motion", "Sudden, severe joint pain",
    "Swelling", "Redness", "Weakness", "Pale skin", "Shortness of breath", "Frequent infections", "Enlarged lymph nodes",
    "Swollen lymph nodes", "Unexplained weight loss", "Severe abdominal pain", "Nausea", "Regurgitation of stomach acid",
    "Burning or gnawing pain in the stomach", "Delusions", "Hallucinations", "Disorganized thinking", "Social withdrawal",
    "Episodes of mania and depression", "Mood swings", "Obsessions", "Compulsions", "Flashbacks", "Nightmares", "Anxiety",
    "Avoidance behaviors", "Extreme weight loss", "Fear of gaining weight", "Distorted body image", "Binge eating", "Purging behaviors",
    "Guilt and shame", "Recurrent episodes of overeating", "Loss of control", "Pain crises", "Jaundice", "Swelling of hands/feet",
    "Excessive bleeding", "Easy bruising", "Joint pain/swelling"
]

# Create the main application window
app = tk.Tk()
app.title("Disease Diagnosis Application")
app.geometry("1366x768")

bg_img = ImageTk.PhotoImage(Image.open("Your paragraph text/2.png"))
bg = tk.Label(image=bg_img)
bg.place(x=-1, y=0)


search_var = tk.StringVar()
search_entry = tk.Entry(app, textvariable=search_var, width=18, font=('arial', 16), background='#fcffdb', bd=0)
search_entry.insert(0, 'Select Your Symptoms:')
search_entry.bind('<FocusIn>', ontype)
search_entry.place(x=530, y=117)

def nextWin():
    pass

# Function to update the symptoms list based on the search query
def update_symptoms_list(event):
    search_query = search_var.get().lower()
    symptom_listbox.delete(0, tk.END)  # Clear the current listbox items
    for symptom in symptoms_list:
        if search_query in symptom.lower():
            symptom_listbox.insert(tk.END, symptom)

# Load the image for the Clear button
clear_button_image = ImageTk.PhotoImage(Image.open("Your paragraph text\clear button text.png"))

# Function to clear symptom selections and diagnosis text
def clear_selections():
    selected_symptoms.clear()
    symptom_listbox.selection_clear(0, tk.END)
    result_text.config(state="normal")
    result_text.delete(1.0, tk.END)
    result_text.config(state="disabled")

# Create a Clear button with the loaded image
clear_button = tk.Button(app, image=clear_button_image, command=clear_selections, bd=0)
clear_button.place(x=879, y=109)

# Create a listbox to select symptoms
selected_symptoms = []

def update_symptoms(event):
    selected_symptoms.clear()
    for item in symptom_listbox.curselection():
        selected_symptoms.append(symptom_listbox.get(item))

symptom_listbox = tk.Listbox(app, selectmode=tk.MULTIPLE, height=13, width=50, background='#fcffdb', font=('arial', 16), bd=0)
for symptom in symptoms_list:
    symptom_listbox.insert(tk.END, symptom)

search_entry.bind("<KeyRelease>", update_symptoms_list)
symptom_listbox.place(x=400, y=200)
symptom_listbox.bind("<<ListboxSelect>>", update_symptoms)



# Create a text widget for the diagnosis result
result_text = tk.Text(app, height=4, width=50, background="#fcffdb", bd=1, font=('arial', 16))
result_text.place(x=400, y=578)
result_text.config(state="disabled")

# Create a function to diagnose the disease
def diagnose_disease():
    if not selected_symptoms:
        result_text.config(state="normal")
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Please select one or more symptoms.")
        result_text.config(state="disabled")
    else:
        matched_diseases = {}
        for key, value in disease_data.items():
            matched_count = sum(1 for symptom in selected_symptoms if symptom.lower() in value.lower())
            matched_diseases[key] = matched_count

        nearest_disease = max(matched_diseases, key=matched_diseases.get)
        result_text.config(state="normal")
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Nearest Diagnosis: {nearest_disease}\n\n{disease_data.get(nearest_disease, 'No information available')}")
        result_text.config(state="disabled")

# Create a diagnose button
diagnose_button_image = ImageTk.PhotoImage(Image.open("Your paragraph text\diagnoseButton.png"))
diagnose_button = tk.Button(app, image=diagnose_button_image ,command=diagnose_disease, bd=0)
diagnose_button.place(x=650,y=527)


next_button_image = ImageTk.PhotoImage(Image.open("Your paragraph text/next.png"))
next_button = tk.Button(app, image=next_button_image ,command=nextWin, bd=0)
next_button.place(x=660,y=700)

# Run the tkinter main loop
app.mainloop()
