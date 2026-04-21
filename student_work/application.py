from flask import Flask, request, redirect, url_for, render_template_string, session
import sqlite3
import bcrypt
app = Flask(__name__)
app.secret_key = "supersecretkey"

# ---------- DATABASE SETUP ----------
def get_db():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT,
            favoriteFoid TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# ---------- STYLE ----------
base_style = """
<style>
body {
    font-family: Arial, sans-serif;
    background: #f4f6f8;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}
.card {
    background: white;
    padding: 25px;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    width: 300px;
    text-align: center;
}
input {
    width: 90%;
    padding: 8px;
    margin: 8px 0;
}
button {
    padding: 10px;
    width: 60%;
    background: #4CAF50;
    color: white;
    border: none;
}
.error {
    color: red;
}
</style>
"""

login_page = f"""{base_style}
<div class="card">
<h2>Login</h2>
<form method="POST">
  <input name="username" placeholder="Username"><br>
  <input name="password" type="password" placeholder="Password"><br>
  <button type="submit">Login</button>
</form>
<a href="/register">Create an account</a>
<p class="error">{{{{ error }}}}</p>
</div>
"""

register_page = f"""{base_style}
<div class="card">
<h2>Register</h2>
<form method="POST">
  <input name="username" placeholder="Username"><br>
  <input name="password" type="password" placeholder="Password"><br>
  <input name="favoriteFoid" type="text" placeholder="Favorite Foid"><br> 
  <button type="submit">Sign Up</button>
</form>
<a href="/">Back to login</a>
<p class="error">{{{{ error }}}}</p>
</div>
"""

secret_page = f"""{base_style}
<div class="card">
<h2>🎉 Not So Secret Room</h2>
<h3>Welcome, {{{{ username }}}}!</h3>
<p><strong>Your Favorite Foid:</strong> {{{{favoriteFoid}}}}</p>
<p>You got into the secret room!</p>
    <div style="display: flex; gap: 10px; justify-content: center; margin-top: 20px; margin-bottom: 10 px;">
        <a href="/test_page"><button>Test Page</button></a>
        <a href="/logout"><button>Logout</button></a>
    </div>
</div>
"""
test_page = f"""{base_style}
<div class="card">
<h2>Test Page</h2>
<p>This is a test page.</p>
<a href="/"><button>Back to login</button></a>
</div>
"""
# ---------- ROUTES ----------
@app.route("/", methods=["GET", "POST"])
def login():
    error = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db()
        user = conn.execute(
            "SELECT * FROM users WHERE username=?",
            (username,)
        ).fetchone()
        conn.close()

        if user and bcrypt.checkpw(password.encode("utf-8"), user["password"]):
            session["user"] = username
            return redirect(url_for("secret"))
        else:
            error = "Incorrect username or password"

    return render_template_string(login_page, error=error)

@app.route("/register", methods=["GET", "POST"])
def register():
    error = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        favoriteFoid = request.form["favoriteFoid"]

        if not username or not password:
            error = "Fields cannot be empty"
        else:
            conn = get_db()
            try:
                hashed_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

                conn.execute(
                    "INSERT INTO users (username, password, favoriteFoid) VALUES (?, ?, ?)",
                    (username, hashed_pw, favoriteFoid)
                )
                conn.commit()
                
                return redirect(url_for("login"))
            except sqlite3.IntegrityError:
                conn.rollback()
                error = "Username already exists"
            except Exception:
                conn.rollback()
                error = "Unexpected error during registration"
            finally:
                conn.close()

    return render_template_string(register_page, error=error)

@app.route("/secret")
def secret():
    if "user" not in session:
        return redirect(url_for("login"))

    conn = get_db()
    user = conn.execute(
        "SELECT favoriteFoid FROM users WHERE username = ?",
        (session["user"],)
    ).fetchone()
    conn.close()

    favoriteFoid = user["favoriteFoid"] if user else ""
    return render_template_string(secret_page, username=session["user"], favoriteFoid=favoriteFoid)

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/test_page")
def testPage():
    return render_template_string(test_page)

# ---------- RUN ----------
app.run(host="0.0.0.0", port=5000)