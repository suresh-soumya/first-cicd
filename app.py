from flask import Flask, request

app = Flask(__name__)

text_data = ""

@app.route("/", methods=["GET", "POST"])
def home():
    global text_data
    if request.method == "POST":
        text_data = request.form.get("text")

    return f"""
    <h2>Simple Notepad</h2>
    <form method="POST">
        <textarea name="text" rows="10" cols="50">{text_data}</textarea><br>
        <button type="submit">Save</button>
    </form>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
