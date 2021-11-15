from flask import Flask, render_template, request
import tablib
import os
# import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/state/<string:name>")
def get_state_cases(name):
    df = pd.read_csv("static\cancer_profiles.csv")
    temp = df.to_dict('cancer_profiles')
    data = request.files["csvfile"]
    with open(f) as file:
        csvfile = csv.reader(file)
        data.append()
    #csv_dicts = {
        # state:case for state, case in data.items() 
        # if (data["Age-Adjusted Incidence Rate([rate note]) - cases per 100,000"] )
        # }
    return result

@app.route("/info", methods=["GET"])
def get_state_info():
    
    return render_template("info.html", analysis=result, info=info)


if __name__ == "__main__":
    app.run(debug=True)