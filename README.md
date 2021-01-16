[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![made-with-latex](https://img.shields.io/badge/Made%20with-flask-1f425f.svg)](https://flask.palletsprojects.com/en/1.1.x/)

https://www.twitpy.com

# Twitpy-URLshorterner
Web-app for URL shorterner

# How it works
- Using flask form to take in input from user from HTML
- Create a random 5 character string along using the input and put them both in the sql database
- The user now have the link with our domain name +/random string
- Whenever the user use the shortened link, the website query the database and redirect the user the matching URL of the random string in our database

# License
[MIT](https://choosealicense.com/licenses/mit/)
