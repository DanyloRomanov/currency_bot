##Files
bot.py
Procfile
requirements.txt

##Commands how to start 
heroku login
heroku create

git init
git add .
git commit -m "first commit"
heroku git:remote -a YourAppName
git push heroku master

heroku ps:scale web=1

git add .
git commit -m "changing python3 to python in Procfile"
git push heroku master

heroku logs --tail

