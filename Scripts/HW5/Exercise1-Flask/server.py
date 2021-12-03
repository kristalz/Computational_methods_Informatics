from flask import Flask, render_template, request, jsonify
import json
import pandas as pd
import plotly
import plotly.express as px
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/state/<string:name>")
def get_state_cases(name):
    df = pd.read_csv("Scripts\HW5\cancer_profiles.csv")
    result = {
        "State": name,
        "Cases_per_100k": float(df[df['State'].str.lower() == name.lower()]["Age-Adjusted Incidence Rate([rate note]) - cases per 100,000"])
        }
    return jsonify(result)

@app.route("/info", methods=["GET"])
def get_state_info():
    df = pd.read_csv("Scripts\HW5\cancer_profiles.csv")
    state = request.args.get("state")
    state_list = df["State"].to_list()
    states_lower = [x.lower() for x in state_list]
    if state.lower() not in states_lower: 
        error_statement = "Please enter a valid state."
        return render_template("error.html", error_statement=error_statement)

    result = float(df[df["State"].str.lower() == state.lower()]["Age-Adjusted Incidence Rate([rate note]) - cases per 100,000"])  
    return render_template("info.html", analysis=result, state=state)

@app.route("/plot")
def get_plot():
    df = pd.read_csv("Scripts\HW5\cancer_profiles.csv")
    fig = px.bar(df, x='State', 
    y='Age-Adjusted Incidence Rate([rate note]) - cases per 100,000', 
    title='Incidence Rate Report by State, 2014-2018',
    labels={'Age-Adjusted Incidence Rate([rate note]) - cases per 100,000':'Incidence Rate (cases per 100,000)'})
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    fig.write_html("Scripts\HW5\Exercise1-Flask\interactivefile.html")
    return render_template('plot.html', graphJSON=graphJSON)

if __name__ == "__main__":
    app.run(debug=True)