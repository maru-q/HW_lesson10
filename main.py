import json
from flask import Flask, request, render_template


with open("candidates.json", "r", encoding="utf-8") as file:
    candidates = json.load(file)

app = Flask(__name__)


@app.route("/", )
def page_index():

    content = ""
    for candidate in candidates:
        content += "Имя кандидата - " + candidate["name"] + "\n"
        content += "Позиция кандидата - " + candidate["position"] + "\n"
        content += "Навыки: " + candidate["skills"] + "\n"
        content += "\n"

    return "<pre>"+content+"</pre>"


@app.route("/candidate/<int:x>", )
def page_candidate(x):
    content = ""
    for candidate in candidates:
        if candidate["id"] == x:

            content += "Имя кандидата - " + candidate["name"] + "\n"
            content += "Позиция кандидата - " + candidate["position"] + "\n"
            content += "Навыки: " + candidate["skills"] + "\n"

    return "<pre>"+content+"</pre>"


@app.route("/skill/<x>", )
def page_candidate_skills(x):
    content = ""
    skilled_candidates = []
    x_lower = x.lower()

    for candidate in candidates:
        skills_list = candidate["skills"].lower().split(", ")
        if x_lower in skills_list:
            skilled_candidates.append(candidate)

    for candidate in skilled_candidates:

        content += "Имя кандидата - " + candidate["name"] + "\n"
        content += "Позиция кандидата - " + candidate["position"] + "\n"
        content += "Навыки: " + candidate["skills"] + "\n" + "\n"

    return "<pre>" + content + "</pre>"


app.run()
