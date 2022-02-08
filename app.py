from flask import Flask, render_template, request,url_for,redirect
from Backend import *


app = Flask(__name__)


@app.route('/', methods=["POST","GET"])
def main_Window():
    if request.method == "GET":
        return render_template("main.html")
    else:
        if request.form['submit_button'] == "Beach":
            record_Scene("Beach")
            return render_template("main.html")



if __name__ == '__main__':
    app.run()







