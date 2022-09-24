# flask-with-db

IP address via GCP ====>  34.70.61.86/patients
IP address local machine ====> 192.168.1.26/patients

#########PLEASE FIND SCREENSHOTS OF OUTPUT IN SCREENSHOT FOLDER############

Part 1 – Connecting Flask to SQlite:
Slides to follow: presentation wk4c
Create a new github repo called ‘flask-with-db’ in your
github account
Setup a local DBs on your machine(s) using SQLITE
Create an SQLite DB that contains a patient table and a
minimum of 4 additional columns for patient details beyond what I provided (MRN, first and last name, DOB)
Create these new fake patients/table using SQLalchemy;
create a file called creatDB.py in your repo that contains the source code for
how these patients were created
Connect your flask app to a local SQLite DB that is
within your repo folder
Inside your flask app, create a new route called ‘/patients’
Within the patient-patients route, display the list of
patients retrieve from the SQlite DB
Deploy to Azure or GCP, insert in IP of machines in
readme.md file in repo
Share github URL with me in classroom
