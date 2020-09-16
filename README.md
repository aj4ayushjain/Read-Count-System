# Read-Count-System
Assignment for Pratillipi Hiring


You are having a set of stories in your system. Each story has a title and content
Needs to build a system with following functionalities :
1. Signup with a username and password
2. Log in with User Id and password
3. A page for viewing all the stories titles, and clicking them should take to the story
page
4. The story page should contain the following details :
a) Story title
b) Story content
c) Number of people currently viewing this story
d) Total read count for the story
Points to consider :
1. A single user reading a story multiple times, will be considered as a single read
2. The UI can be pretty basic, and you don’t need to spend effort on much of UX either.
The backend services is where the evaluation will mostly be done on


# Live Url:-
---------------------------------------------------------------------------

Live Demo:- http://ayushj.pythonanywhere.com.

If you have any suggestions or feedback you can ping me up.
I will be happy to listen or answer any queries.




# Setting up the project locally
-----------------------------------------------------------------------------
```
1. After clone create a virtualenv in Read-Count-System dir
2. Activate the virtualenv
3. pip3 install -r requirements.txt
4. Run the Python shell and run following commands
    - from project import create_app
    - db.create_all(app=create_app())
5. FLASK_APP=project FLASK_ENV=development flask run
```

# Deploy the project 

We need to create `wsgi.py` inside the Read-Count-System/ dir
as we are using `Application factory pattern` in flask app 
for managing the project modularly.


wsgi.py
```
from project import create_app

app = create_app()

if __name__ == "__main__":
    app.run()

``` 
