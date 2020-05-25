# CITS3403 GUILD Voting System
author: Haoran, Tommy, Zhenyu & Sabrina

# Introduction of the application
The application mainly provides 6 functions to the users -- Registration, Log in, Candidate info, Vote, Account and Admin.
If users want to vote for the candidate they like, they are required to register in **register page** first. The username and email are unique in the sqlite database, thus when registering, if your username or email has been used by others, you need to use a new one.
After you finish the registeration, the app would redirect you to the **login page**. 
Now, you can vote for your favorite candidate in **vote page**! In this page, you can see the candidate informations, and make your voting choice.
You voting result would appear in **myvote page**. If you change your mind, you can go to the **vote page** and vote again. The final result depends on your last choice. If you go back to **candidate info page**, you can see the votes of each candidates. There is a bar chart in this page to let users have an intuitive feeling for the votes of each candidates. 
In **account page**, you can change your email and username and see your vote history.
And also, for the **admin page**, only when you are logged in as an administator can you access this page. In this page, you can see all the informations about the candidates and users, and to modify them.

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

`from app import db`

`from app.models import User, Candidate`

`admin=User(username='',email='',password='',is_admin=True)`

`db.session.add(admin)`

`db.session.commit()`

# Testing
`python test.db -v`
