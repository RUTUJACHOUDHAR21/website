from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy users
users = {
    "admin": "admin123",
    "user": "user123"
}

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if users.get(username) == password:
            return f"<h2>Welcome, {username}!</h2>"
        else:
            message = "Invalid username or password."
    return render_template("login.html", message=message)

if __name__ == '__main__':
    app.run(debug=True)
