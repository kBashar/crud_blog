# A CRUD Blog app built on Django framework
The app has following capabilities
1. Log in  user 
2. Log out
3. Create a blog post
4. Show a detail of a blog post
5. Update a blog post
6. Delete a blog post
7. Filter for the offensive words as defined in the carneige melon offensive word list

## The project dependencies
```
Django==2.1.2
django-crispy-forms==1.7.2
pytz==2018.5 (Django dependency)
Bootstrap4 (CSS)
```
 
## Install
It's recommended that you use a virtual environement before installing the project to avoid version conflicts with your other projects.
1. Install dependencies
```
pip install -r requirements.txt
```
2. Run Django migrations to make your database up and ready
```sh
python manage.py migrate
```
3. Run Django server 
```sh
python manage.py runserver
```

## Screenshots
* #### Home Screen
![home](https://imgur.com/cPFnEDo.png)
* #### Log In Screen
![login](https://imgur.com/aon1Nsw.png)
* #### Delete Screenshot
![Delete](https://i.imgur.com/WtZUykl.png)
* #### Detail of a blog post
![detail](https://imgur.com/MEFzKoY.png)
* #### Create a blog post
![create](https://imgur.com/7pUzZ4j)
* #### Update or create a post
![update](https://imgur.com/EHlZY8L.png)
* #### Check for offensive words
![offensive](https://imgur.com/xtBUt7t.png)
