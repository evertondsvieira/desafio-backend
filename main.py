from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from leitor import *
from database import *
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")


@app.route('/send', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      readfile()
      result = databaseFatch()
      return render_template("result.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
