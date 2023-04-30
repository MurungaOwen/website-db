from flask import Flask, render_template,jsonify

app = Flask(__name__)
JOBS=[{
    'id':'1',
    'title':'software engineer',
    'location':'kisumu',
    'salary':243000,
  },
  {
    'id':'2',
    'title':'Backend engineer',
    'location':'Nairobi',
    'salary':430000,
  },
  {
    'id':'3',
    'title':'web designer',
    'location':'Mombasa',
    'salary':234000,
  }]

@app.route('/')  #the homepage...the @  is like a decorator
def home():
  return render_template('home.html',jobs=JOBS)

@app.route('/api/jobs')
def jobs():
  return jsonify(JOBS)
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)  #specify ythe host that is in replit
