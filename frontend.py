from flask import Flask, request, url_for, g, session, json, render_template


app = Flask(__name__)


@app.route("/")
def index():
    if not authorized(): # not authorized():
        if request.is_xhr:
            abort(401)
        else:
            return redirect(url_for("login"))
    return render_template("index.html")


app.run(debug=False)
