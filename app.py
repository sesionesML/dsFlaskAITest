import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = "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"


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(animal),
            temperature=0.6,
            max_tokens=600,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(consulta):
    return """ Eres un especialista en solucionar consultas técnicas para SQL

Q: Como selecciono todos los campos de un tablas
A: SELECT * FROM tableName
Q: Como agrego un filtro de ingresos a una consulta de la tabla de personal 
A: SELECT * FROM tableName WHERE income > 50000  
Q: {}
A:""".format(
        consulta.capitalize()
    )
