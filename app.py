import os

from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from helpers import login_required, apology
from werkzeug.security import check_password_hash, generate_password_hash

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///money.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
def home():
    """Start of the page"""
    if request.method == "POST":
        return redirect("/login")
    else:
        return render_template("home.html")

@app.route("/history")
@login_required
def history():
    """Show history of Purchased tickets"""
    user_id = session["user_id"]
    history = db.execute("SELECT island, time, ticket, price, year, month ||'/'|| day as date FROM history WHERE user_id = ?", user_id)
    cashes = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    cash = cashes[0]["cash"]
    return render_template("history.html", history=history, cash=cash)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)
        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("Not Found")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/index")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Forget any user_id
    session.clear()

    if request.method == "GET":
        return render_template("register.html")

    # For post request
    else:
        # For input
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        # For errors
        if (password == ""):
            return apology("Please Provide Password", 400)
        if (username == ""):
            return apology("Please Provide Username", 400)
        if (confirmation == ""):
            return apology("Submit Your Confirmation Password", 400)
        if (password != confirmation):
            return apology("Password Don't Match", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # To see that if the user already exist
        if len(rows) == 1:
            return apology("User alreay exist", 400)

        hash = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", request.form.get("username"), hash)
        # Redirect user to the homepage
        return redirect("/login")

@app.route("/index")
@login_required
def index():
    """Show ABout Island"""

    # Redirect user
    return render_template("index.html")

@app.route("/book", methods=["GET", "POST"])
@login_required
def book():
     """Buy Tikcets"""

     # For get request
     if request.method == "GET":
         # To remeber user
         user_id = session["user_id"]
         info = db.execute("SELECT * FROM info")
         cash = db.execute("SELECT cash FROM users WHERE id =?", user_id)
         cash_rnd = cash[0]["cash"]
         cashes = round(cash_rnd)
         return render_template("book.html", info=info, cashes=cashes)

     # For Post request
     else:
         island = request.form.get("island")
         ticket = request.form.get("ticket")
         month = request.form.get("month")
         day = request.form.get("day")
         year = request.form.get("year")

         # For errors
         if island == None:
             return apology("Information is Missing")
         if ticket == None:
             return apology("Information is Missing")
         if month == None:
             return apology("Schedule Information Is Missing")
         if day == None:
             return apology("Schedule Information Is Missing")
         if year == None:
              return apology("Schedule Information Is Missing")
         if not request.form.get("ticket").isdigit():
            return apology("Please Recheck input")
         if not request.form.get("day").isdigit():
            return apology("Please Recheck input")
         if not request.form.get("month").isdigit():
            return apology("Please Recheck input")
         if not request.form.get("year").isdigit():
            return apology("Please Recheck input")

         # Buy tickets
         else:
             # To remeber user
             user_id = session["user_id"]

             see = db.execute("SELECT price FROM info WHERE island = ?", island)
             prices = see[0]["price"]
             price = int(prices)
             tickets = int(ticket)
             total = price * tickets
             db.execute("INSERT INTO history (user_id, island, ticket, price, day, month, year)VALUES(?, ?, ?, ?, ?, ?, ?)", user_id, island, ticket, total, day, month, year)

             # To update user cash
             user_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
             cashes = user_cash[0]["cash"]
             cash = int(cashes)
             sum = round(cash - total)
             db.execute("UPDATE users SET cash = ? WHERE id = ?", sum, session["user_id"])

             return render_template("confirm.html", total=total, island=island, ticket=ticket, month=month, day=day, year=year)

@app.route("/password", methods=["GET", "POST"])
@login_required
def password():
    """ Change Password """

    # if method GET, display password change form
    if request.method == "GET":
        return render_template("password.html")

    # if method POST, change password
    else:
        # return apologies if form not filled out
        if not request.form.get("oldpass") or not request.form.get("newpass") or not request.form.get("confirm"):
            return apology("missing old or new password", 403)

        # save variables from form
        oldpass = request.form.get("oldpass")
        newpass = request.form.get("newpass")
        confirm = request.form.get("confirm")

        # user's previous password
        hash = db.execute("SELECT hash FROM users WHERE id = ?", session["user_id"])
        hash = hash[0]['hash']

        # if old password incorrect, return apology
        if not check_password_hash(hash, oldpass):
            return apology("old password incorrect", 403)

        # if new passwords don't match, return apology
        if newpass != confirm:
            return apology("new passwords do not match", 403)

        # hash new password
        hash = generate_password_hash(confirm)

        # Insert new hashed password into users table
        db.execute("UPDATE users SET hash = ? WHERE id = ?", hash, session["user_id"])

        # Rediret user
        return redirect("/logout")

