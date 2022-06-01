# CollabCube
Sourcode for CollabCube


# Installation
* 1 - clone repo https://github.com/jaswanth9959/CollabCube/
* 2 - create a virtual environment and activate
*  - pip install virtualenv
*  - virtualenv envname
*  - envname\scripts\activate
* 3 - cd into project "cd CollabCube"
* 4 - pip install -r requirements.txt
* 5 - Create an account on agora.io and create an app to generate an APP ID
* 6 - Update APP ID, Temp Token and Channel Name in streams.js of static/js directory and in views.py of videochat/ directory
```javascript
let APP_ID = "YOU-APP-ID"
```
```javascript
appId = ""
appCertificate = ""
```
* 7 - Update EMAIL_HOST_USER, EMAIL_HOST_PASSWORD in settings.py of collabcube/ for sending mails to users.
```javascript
EMAIL_HOST_USER = "YOUR EMAIL ID"
EMAIL_HOST_PASSWORD = "YOUR EMAIL PASSWORD"
```
* 8 - python manage.py runserver



# Features
* Share Projects
* Message other students
* Rate others work
* Search other students
* Video Conference
* Groups similar to WhatsApp
* Resume Builder
* Notes and Announcements section for students
* Collaborative Editor 

# Tech Stack
* Django
* Postgres
* AWS

# Home Page
<img src="./resources/HomePage.jpg">


# Projects Page
<img src="./resources/ProjectsPage.jpg">


# Account Page
<img src="./resources/Account.jpg">


# User Profile Page
<img src="./resources/UserProfile.jpg">


# User Project Page
<img src="./resources/UserProject.jpg">


# Rooms Page
<img src="./resources/Rooms.jpg">
<img src="./resources/RoomMessage.jpg">


# Video Conference Page
<img src="./resources/collabchat.png">


# Collaborative Editor Page
<img src="./resources/TextEditor.jpg">


# Resume Builder Page
<img src="./resources/resume.png">


# Notes Page
<img src="./resources/notes.jpg">


# Announcements Page
<img src="./resources/announcements.jpg">
