import json
import xlrd
from flask import Flask, request, render_template,jsonify
import requests

app = Flask(__name__)

@app.route('/handle_form', methods=['POST'])
def handle_form():
    value=""
    req = jsonify(request.form)
    wb = xlrd.open_workbook('Output_file.xlsx')
    sh = wb.sheet_by_index(0)
    print(req.json["fname"])
    for rownum in range(1, sh.nrows):
        row_values = sh.row_values(rownum)
        if row_values[0] == int(req.json["fname"]) :
           print("hello World: ",row_values[1])
           value=row_values[1]
    return render_template("/result.html",ID=req.json["fname"],Value=value)
    

@app.route("/")
def index():
    return render_template("index1.html");   


if __name__ == "__main__":
    app.run(debug=True)