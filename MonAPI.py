from subprocess import *
from flask import Flask
app = Flask(__name__)
name = check_output("hostname", shell=False).decode("utf-8")

@app.route('/name')
def GetMyName():
    return name

@app.route('/<letter>/<number>')
def PrintLetters(letter, number):
    alpha = ""
    for i in range (0, int(number)):
        alpha = alpha + str(letter)
        i = i+1
    return alpha
