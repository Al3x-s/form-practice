from flask import Flask, render_template, request
app = Flask('app')
users = []

@app.route('/', methods=["GET", "POST"])
def home():
    x = 0
    if request.method == "POST":
        x = x + 1
        print(request.form)
        users.append(
            [
            x,
            request.form.get("email"),
            request.form.get("password"),   
            request.form.get("Radios"),
            request.form.get("adult")
            ]
        )
    return render_template('index.html')

@app.route('/results')
def result():
    return render_template('results.html', info=users)

