import subprocess, time
from pathlib import Path
from flask import Flask, request, redirect, render_template_string, send_from_directory, Response

ROOT = Path.cwd()
app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<html>
<head>
<title>Thames Site Editor</title>
<style>
body{margin:0;font-family:Arial;background:#111;color:#eee}
header{padding:14px 20px;background:#07101a;border-bottom:1px solid #c9a96e}
main{display:grid;grid-template-columns:260px 1fr 1fr;height:calc(100vh - 56px)}
nav{padding:14px;background:#181818;overflow:auto}
nav a{display:block;color:#eee;padding:8px;text-decoration:none;border-bottom:1px solid #333}
section{padding:12px;overflow:auto}
textarea{width:100%;height:78vh;background:#0b0b0b;color:#f4edd8;font-family:Consolas,monospace;font-size:13px}
iframe{width:100%;height:78vh;background:white;border:1px solid #444}
button{padding:10px 14px;margin:5px;background:#c9a96e;border:0;cursor:pointer}
input{padding:10px;width:70%}
</style>
</head>
<body>
<header><b>Thames Club Site Editor</b> — {{file}}</header>
<main>
<nav>
{% for p in pages %}
<a href="/edit/{{p}}">{{p}}</a>
{% endfor %}
<hr>
<form method="post" action="/git">
<input name="msg" value="site edits">
<button>Commit + Push</button>
</form>
</nav>

<section>
<h3>Preview</h3>
<iframe src="/preview/{{file}}?v={{cachebuster}}"></iframe>
</section>

<section>
<h3>Edit HTML</h3>
<form method="post">
<textarea name="content">{{content}}</textarea><br>
<button type="submit">Save File</button>
</form>
</section>
</main>
</body>
</html>
"""

def pages():
    return sorted([p.name for p in ROOT.glob("*.html")])

@app.route("/")
def index():
    ps = pages()
    return redirect(f"/edit/{ps[0]}") if ps else "No HTML files found."

@app.route("/edit/<path:file>", methods=["GET","POST"])
def edit(file):
    path = ROOT / file
    if request.method == "POST":
        path.write_text(request.form["content"], encoding="utf-8")
        return redirect(f"/edit/{file}")
    return render_template_string(
        TEMPLATE,
        pages=pages(),
        file=file,
        content=path.read_text(encoding="utf-8", errors="replace"),
        cachebuster=int(time.time())
    )

@app.route("/preview/<path:file>")
def preview(file):
    path = ROOT / file
    html = path.read_text(encoding="utf-8", errors="replace")

    # 🔥 KEY FIX: force all absolute paths to behave locally
    html = html.replace('href="/', 'href="')
    html = html.replace('src="/', 'src="')

    return Response(html, mimetype="text/html")

@app.route("/git", methods=["POST"])
def git():
    msg = request.form.get("msg") or "site edits"
    subprocess.run(["git","add","."], cwd=ROOT)
    subprocess.run(["git","commit","-m",msg], cwd=ROOT)
    subprocess.run(["git","push","origin","master"], cwd=ROOT)
    return redirect("/")

@app.route("/<path:file>")
def static_files(file):
    return send_from_directory(ROOT, file)

if __name__ == "__main__":
    app.run(port=5050, debug=False)
