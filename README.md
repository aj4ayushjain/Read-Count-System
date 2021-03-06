# Read-Count-System
## Assignment for Pratillipi Hiring


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

Tested ion firefox browser.

# Tech Stack

1. Python Flask
2. Sqllite
3. Bulma+Jinja2
4. Javascript(For tracking browser close event)

Design Considerations or modifications if we think on deploying at Scale

+ Sqllite3 database is not resilient at high scale so we could shift to something resilient,
  scalable database
 
+ Use of flask-socketio for further extension on the chats belonging to story which currently 
  i didn't implement because in this it kindda be wastage of resources for just tracking the live
  viewer count.
 
+ I have tracked those count via `table(user_id,book_id)` for the unique view count

+ And appended `book_id_currently_reading` column to `users` table and set it when user is reading
  and otherwise set it back to None in all other actions.


# Packages Used
  1. Blueprint:- Modular way to organize group of related views and other code
  2. werkzeug.security:- For hashing the password 
  3. Flask_login - For handling of the session cookies in the system across threads without memory error
  4. Flask_sqlalchemy - Handling databases tables along with session
  5. Flask_table-  To create dynamic table with links

# Directory Structure and Files
  
  1. Project/
   - `models.py` - Declare database models for interaction in this file
   - `__init__.py` - Application initialization and configuration
   - `main.py` - Logic of the application for browsing after signup/login
   - `auth.py` - Signup and login of the user
   - `books.py` - Model for creating dynamic table(book/story) 
  2. `wsgi.py` - File to be used for wsgi deployment 

# Future Advancements 
----------------------------------------------------------------------------
  1. Design / UI
   - The design of the system for story titles(dashboard.html) and storypage(storpage.html)
      should be redesigned
  2. Extension across Browsers-(Event of Browser Closing)
   -  So if a user abruptly closes the browser or tab while reading the story 
      the event isn't properly captured in some browsers(Chrome) so current
      viewer are not updated  

  
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
