import tkinter as tk
from PIL import Image, ImageTk
import PIL.Image

from trial import *


    
def ontype(i):
    if search_entry.get()=="Select Your Symptoms:":
        search_entry.delete(0, tk.END)
        tk.Frame(app, bg="#082b5b", width=350, height=1).place(x=530, y=72)

disease_data=dict(zip(diseases(), symptoms()))

# Create the main application window
app = tk.Tk()
app.title("Disease Diagnosis Application")
app.geometry("1366x768")

bg_img = ImageTk.PhotoImage(PIL.Image.open("Your paragraph text/2.png"))
bg = tk.Label(image=bg_img)
bg.place(x=-1, y=0)


search_var = tk.StringVar()
search_entry = tk.Entry(app, textvariable=search_var, width=18, font=('arial', 16), background='#fcffdb', bd=0)
search_entry.insert(0, 'Select Your Symptoms:')
search_entry.bind('<FocusIn>', ontype)
search_entry.place(x=530, y=45)



# Function to update the symptoms list based on the search query
def update_symptoms_list(event):
    search_query = search_var.get().lower()
    symptom_listbox.delete(0, tk.END)  # Clear the current listbox items
    for symptom in symptoms_list:
        if search_query in symptom.lower():
            symptom_listbox.insert(tk.END, symptom)

# Load the image for the Clear button
clear_button_image = ImageTk.PhotoImage(PIL.Image.open("Your paragraph text\clear button text.png"))

# Function to clear symptom selections and diagnosis text
def clear_selections():
    search_entry.delete(0, tk.END)
    selected_symptoms.clear()
    symptom_listbox.selection_clear(0, tk.END)
    result_text.config(state="normal")
    result_text.delete(1.0, tk.END)
    result_text.config(state="disabled")

# Create a Clear button with the loaded image
clear_button = tk.Button(app, image=clear_button_image, command=clear_selections, bd=0)
clear_button.place(x=879, y=35)

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
symptom_listbox.place(x=400, y=128)
symptom_listbox.bind("<<ListboxSelect>>", update_symptoms)


# Create a text widget for the diagnosis result
result_text = tk.Text(app, height=4, width=50, background="#fcffdb", bd=1, font=('arial', 16))
result_text.place(x=400, y=555)
result_text.config(state="disabled")
var = ""
# Create a function to diagnose the disease
def diagnose_disease():
    global var
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
        var = nearest_disease
        insert_disease(var)


# Create a diagnose button
diagnose_button_image = ImageTk.PhotoImage(PIL.Image.open("Your paragraph text\diagnoseButton.png"))
diagnose_button = tk.Button(app, image=diagnose_button_image ,command=diagnose_disease, bd=0)
diagnose_button.place(x=650,y=478)

def insert_disease(disease_name):
    # Establish a connection to the MySQL database
    connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Atharv.964",
            database="app"  # Replace with your database name
        )

        # Create a cursor object to interact with the database
    cursor = connection.cursor()

        # Insert the disease name into the 'history' table
    insert_query = "INSERT INTO history (disease) VALUES (%s)"
    cursor.execute(insert_query, (disease_name,))
    connection.commit()

next_button_image = ImageTk.PhotoImage(PIL.Image.open("Your paragraph text/next.png"))
next_button = tk.Button(app, image=next_button_image ,command=lambda:nextWin(app), bd=0)
next_button.place(x=660,y=680)

def nextWin(app):

    app.destroy()
    import thirdpage



# Run the tkinter main loop
app.mainloop()
