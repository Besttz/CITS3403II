# CITS3403 GUILD Voting System
author:Haoran Zhang(22289211)
# Introduction of the application
The application provides five main functions to the users, which are Registration, Log in, Candidate info, Account, Admin. You can check all the information about the candidates in **candidate info** page. And also, you can see the votes of each candidates. I made a bar chart in **candidate info** page to let users have intuitive feelings for the votes of each candidates. If users want to vote the candidate they like, they are required to register. I put voting part into the **register page**. It means that when you register, you would vote at the same time(you must select one candidate). The username and email are unique in the sqlite database. If your email has been used by other, you will be required to use a different email. After you finish the register, the app would redirect you to **login page**. You voting result would appear in **account page**. In **account page**, you can change your email and username. For **admin page**, only you are login in as a administator can you access this page. In this page, you can see all the infromation about candidate and user, and also, you create or delete any candidate or user.
# Launching The Application
**Install Python:** `python3` `exit()`

**Set Up Virtual Environment:** `python3 -m venv venv`  `source venv/bin/activate`

**Change Directory To Project Folder:** `cd (INSERT PROJECT FOLDER PATH LOCATION)`

**Set Up Flask:** `pip install flask` `export FLASK_APP=run.py`

**Install Relevant Modules:** 

`pip install flask_sqlalchemy`

`pip install flask_bcrypt`

`pip install flask_login` 

`pip install flask_wtf` 

`pip install flask_admin`

**Run The App:** `flask run`

The app should now be running on [http://localhost:5000](http://localhost:5000), entered into any browser

**Additional Controls: Stop App:** ^C Exit Environment: deactivate

# Dependencies (i.e. required modules)
`Flask`
`Flask-Admin`
`Flask-Bcrypt`
`Flask-Login`
`Flask-SQLAlchemy`
`Flask-WTF`
`email-validator`

# Admin
You can create an admin directly by **admin page** or uses:

`python`

`from package import db`

`from package.models import User, Candidate`

`admin=User(username='',email='',password='',is_admin=True)`

`db.session.add(admin)`

`db.session.commit()`

# Testing
`python test.db -v`
