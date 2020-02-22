from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    pagetitle = "HomePage"
    return render_template("index2.html",
                            mytitle=pagetitle,
                            mycontent='''
                            Mi contenido
                            linea dos''')

app.run()