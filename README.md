# Engineering-test

1st question
Steps to do the task: [Engineering_test.ipynb]

1. Execute first block of notebook and mention the name of zip folder(Having diffrent csv files)
2. Then Run another Blocks and We can see the "Combined.csv" file

2nd question
Steps to do the task: [api_to_db]

1. First I make a virtual environment to run flask with any compatible version (venv folder)
   . Commands
   1. create virtual env : py -3 -m venv venv
   2. activate virtual env : venv\Scripts\activate
2. Then install flask and flask_sqlalchemy
   . commands
   1. pip install flask
   2. pip install flask_sqlalchemy
3. Make app.py and create table by python shell
   .commands
   1. from app import db
   2. db.create_all()
4. Make template to show table
5. Run app.py and go to "/" on server, We see the table has all the data from API
6. https://prnt.sc/1tb3niw

Note : All the Used libraries are shown in requirement.txt
