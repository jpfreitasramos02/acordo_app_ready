from flask import Flask, render_template, request, send_file
from docx import Document
import io

app = Flask(__name__)

perguntas = [
    "Qual é o nome da empresa?",
    "Qual é o objetivo social?",
    "Qual será o capital social?"
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        respostas = [request.form.get(f"pergunta_{i}") for i in range(len(perguntas))]
        doc = Document()
        doc.add_heading("Respostas do Questionário", level=1)
        for p, r in zip(perguntas, respostas):
            doc.add_paragraph(f"{p}: {r}")
        buf = io.BytesIO()
        doc.save(buf)
        buf.seek(0)
        return send_file(buf, as_attachment=True, download_name="respostas.docx")
    return render_template("index.html", perguntas=perguntas)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
