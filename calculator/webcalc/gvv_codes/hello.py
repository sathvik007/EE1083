#Importing the Flask class
from flask import Flask
app = Flask(__name__)
@app.route('/')

def student():
	return "Hello World"

if __name__ == '__main__':
	app.run() #Runs application on local server
	
