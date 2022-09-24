import sqlite3
connect = sqlite3.connect(r'C:\Users\premd\OneDrive\Desktop\HHA_504_\flask-with-db\pt_table.db')
##connect = sqlite3.connect('\flask-with-db\pt_table.db')
db = connect.cursor()

db.execute("DROP TABLE IF EXISTS pt_table")  ##to delete table name "patient_table" from pt_table database if exist
connect.commit() # commit the changes

## create new tabler with new variables
table = """ CREATE TABLE pt_table (
            mrn VARCHAR(255) NOT NULL,
            firstname CHAR(25) NOT NULL,
            lastname CHAR(25) NOT NULL,
            dob CHAR(25) NOT NULL
        ); """

db.execute(table)
connect.commit() # commit the changes

db.execute("INSERT INTO pt_table(mrn, firstname, lastname, dob) values('12345', 'John', 'Smith', '01/01/2000')")
db.execute("INSERT INTO pt_table(mrn, firstname, lastname, dob) values('23456', 'Jane', 'Doe', '02/02/2001')")
db.execute("INSERT INTO pt_table(mrn, firstname, lastname, dob) values('34567', 'Mary', 'Smith', '03/03/2002')")
db.execute("INSERT INTO pt_table(mrn, firstname, lastname, dob) values('45678', 'Bob', 'Smith', '04/04/2003')")
db.execute("INSERT INTO pt_table(mrn, firstname, lastname, dob) values('56789', 'Jinsuk', 'Park', '05/05/2004')")
db.execute("INSERT INTO pt_table(mrn, firstname, lastname, dob) values('02045', 'Peter', 'Doe', '09/23/1979')")
db.execute("INSERT INTO pt_table(mrn, firstname, lastname, dob) values('67890', 'Jenny', 'Dolan', '04/25/1987')")
db.execute("INSERT INTO pt_table(mrn, firstname, lastname, dob) values('56849', 'Manny', 'Zausin', '07/12/1956')")
db.execute("INSERT INTO pt_table(mrn, firstname, lastname, dob) values('45678', 'Benny', 'Pedro', '08/24/1948')")


Dummyperson1= """ INSERT INTO pt_table(mrn, firstname, lastname, dob) values('45783', 'Vallarie', 'Goldstein', '05/31/1958') """
Dummyperson2= """ INSERT INTO pt_table(mrn, firstname, lastname, dob) values('45839', 'Wendy', 'Gottachetta', '01/05/1987') """
db.execute(Dummyperson1)
db.execute(Dummyperson2)
connect.commit()

#close the connection
##connect.close()