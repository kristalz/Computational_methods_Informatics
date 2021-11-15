from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == "POST":
        file = request.files['csvfile']
        if not os.path.isdir("static"):
            os.mkdir('static')
        filepath = os.path.join("static", file.filename)
        file.save(filepath)
        return 'The file name of the uploaded file is: {}'.format(file.filename)
    return render_template('upload.html')

if __name__ == "__main__":
    app.run(debug=True)