import mysql.connector
from tkinter import *

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Atharv.964',
    database='app'
)

cursorobj = db.cursor()


def symptoms():
    cursorobj.execute('SELECT symptoms FROM disease_info')
    symptoms_set = set(row[0] for row in cursorobj.fetchall())
    return symptoms_set

def diseases():
    cursorobj.execute('SELECT disease_name FROM disease_info')
    diseases_set = set(row[0] for row in cursorobj.fetchall())
    return diseases_set




def close_app(app):
    cursorobj.close()
    db.close()
    app.destroy()
    
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



def get_latest_inserted_disease():

    # Establish a connection to the MySQL database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Atharv.964",
        database="app"  # Replace with your database name
    )

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Retrieve the latest inserted disease
    select_query = "SELECT disease FROM history ORDER BY ID DESC LIMIT 1"
    cursor.execute(select_query)
    result = cursor.fetchone()

    if result:
        latest_disease = result[0]
        return latest_disease


def get_information(result):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Atharv.964",
        database="app"  # Replace with your database name
    )

    # Create a cursor object to interact with the database
    cursor = connection.cursor()
    query = "SELECT information FROM disease_info WHERE disease_name = %s;"
    disease_name = result
    cursor.execute(query, (disease_name, ))
    info = cursor.fetchone()
    return info
    
def get_remedy(result):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Atharv.964",
        database="app"  # Replace with your database name
    )

    # Create a cursor object to interact with the database
    cursor = connection.cursor()
    query = "SELECT remedies FROM disease_info WHERE disease_name = %s;"
    disease_name = result
    cursor.execute(query, (disease_name, ))
    info = cursor.fetchone()
    return info
    

