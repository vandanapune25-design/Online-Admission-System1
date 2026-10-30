from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

students = []

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        students.append({
            "name": request.form["name"],
            "email": request.form["email"],
            "password": request.form["password"]
        })
        return redirect(url_for("dashboard"))
    return render_template_string("""
    <h1>Student Registration</h1>
    <form method="POST">
    <input name="name" placeholder="Full Name" required><br><br>
    <input name="email" type="email" placeholder="Email" required><br><br>
    <input name="password" type="password" placeholder="Password" required><br><br>
    <button>Register</button>
    </form>
    """)

@app.route("/dashboard")
def dashboard():
    return render_template_string("""
    <h1>Student Dashboard</h1>
    <h2>Welcome to Online Admission System</h2>
    <a href="/admission">Apply for Admission</a>
    """)

@app.route("/admission", methods=["GET", "POST"])
def admission():
    if request.method == "POST":
        return "<h1>Application Submitted Successfully!</h1>"
    return render_template_string("""
    <h1>Admission Form</h1>
    <form method="POST">
    <input name="student_name" placeholder="Student Name" required><br><br>
    <input name="father_name" placeholder="Father's Name" required><br><br>
    <input name="mobile" placeholder="Mobile Number" required><br><br>
    <input name="course" placeholder="Course Name" required><br><br>
    <button>Submit Application</button>
    </form>
    """)

from flask import render_template_string

if __name__ == "__main__":
    app.run(debug=True)