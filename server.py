from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def defaultPage():
    return render_template("index.html")


@app.route('/ninja')
def displayNinja():
    return render_template("ninja.html")

@app.route('/ninja/blue')
def displayBlue():
    return render_template("blue.html")

@app.route('/ninja/orange')
def displayOrange():
    return render_template("orange.html")

@app.route('/ninja/red')
def displayRed():
    return render_template("red.html")

@app.route('/ninja/purple')
def displayPurple():
    return render_template("purple.html")

@app.route('/ninja/<vararg>')
def displayRandom(vararg):
    return render_template("notapril.html")

app.run(debug=True)