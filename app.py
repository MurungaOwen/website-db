from flask import Flask, render_template,jsonify
from database import load_jobs,engine

app = Flask(__name__)


@app.route('/')  #the homepage...the @  is like a decorator
def home():
  jobs = load_jobs()
  return render_template('home.html', jobs=jobs)


@app.route('/no')
def listjobs():
  jobs = load_jobs()
  return jsonify(jobs)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)  #specify ythe host that is in replit
