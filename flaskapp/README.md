## 1 -> flaskapp
Contains the information from the backend of our product. There are two different programming languages in this file: python (.py) and SQL (.sql). In this folder you will find:

### app.py 
-> where the code for database connection with @routes is stored, as well as main portions of the structure of the database/application connection.


### migrations.json
_> migrations.json is a file indicating the destination ID of an application where one or multiple tables will be transferred. It facilitates users in relocating table and field data, like moving from a code customization within the primary application to an extension of the same application.

### models.py
-> this file contains the backbone of our database. all of the models are defined here and it is used by reset.from.peewee when creating the database.

### requirements.txt
-> description of all of the technologies and their versions used in this section of the project. 

### reset.from.peewee.sh
-> file that drops and creates tables based on the rest of the program. It initializes the database.

### tables.sql
-> file containing the code for creating the tables to UP database in SQL.
