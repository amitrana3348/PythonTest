#test Flask
#              sudo pip install flask


from flask import Flask
import datetime
app = Flask(__name__)

@app.route("/")
def hello():
     now = datetime.datetime.now()
     timestring = now.strftime("%Y-%m-%d %H:%M")
     templateData = {
          'title':'Hello',
          'time':timestring
          }
     return render_template('main.html',**templateData)

if __name__ == "__main__":
     app.run(host='0.0.0.0',port=80,debug=True)


























from flask import Flask, render_template
import datetime
app = Flask(__name__)
@app.route("/")
def hello():
     now = datetime.datetime.now()
     timeString = now.strftime("%Y-%m-%d %H:%M")
     templateData = {
          'title' : 'HELLO!',
          'time': timeString
          }
     return render_template('main.html', **templateData)

if __name__ == "__main__":
     app.run(host='0.0.0.0', port=80, debug=True)


###BELOW IS THE HTML CODE FOR IT
     <!DOCTYPE html>
<head>
<title>{{ title }}</title>
</head>
<body>
<h1>Hello, World!</h1>
<h2>The date and time on the server is: {{ time }}</h2>
</body>
</html>
