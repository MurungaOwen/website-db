from flask import Flask

app = Flask(__name__)


@app.route('/')  #the homepage...the @  is like a decorator
def home():
  return "hood"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)#specify ythe host that is in replit
