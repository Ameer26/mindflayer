from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def test():
    return "Sic Mundus Creatus Est"
@app.route("/home")
def testhome():
    return render_template('index.html')
@app.route("/home/sleep")
def testsleep():
    return render_template('login.html')
@app.route("/home/sleep/welcome")
def testwake():
    return render_template('home.html')
@app.route("/home/wake")
def testwakes():
    return render_template('cmp.html')
if(__name__=="__main__"):
    app.run(debug=True)