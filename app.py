from flask import Flask, render_template, redirect, url_for, request
#from Cryptography.StudentExamTaker.templates.login import RegistrationForm

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("index.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('/teacher_home'))
    return render_template('login.html', error=error)


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")



if __name__ == "__main__":
    app.run(port=5678)
