# 0x03. User authentication service
`Back-end` `Authentification`

In the industry, you should **not** implement your own authentication system and use a module or framework that doing it for you (like in Python:[Flask-User](https://flask-user.readthedocs.io/en/latest/)). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.

## Resouces
**Read or watch:**
- [Flask documentation](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
- [Requests module](https://requests.kennethreitz.org/en/latest/user/quickstart/)
- [HTTP status codes](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html)

## Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), **without the help of Google**:
- How to declare API routes in a Flask app
- How to get and set cookies
- How to retrieve request from data
- How to return various HTTP status codes

## Setup
You will need to install `bcrypt`
```pip install bcrypt```