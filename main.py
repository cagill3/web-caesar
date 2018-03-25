from flask import Flask, request
from caesar import rotate_string
app = Flask(__name__)
app.config['DEBUG'] = True


form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width:  540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form methods="post">
        <div>
            <label for="rot">Rotate by</label>
            <input type="text" id="rot" name="rot" value="0" />
        </div>
            <textarea type="text" id ="text" name="text">{0}</textarea>
            <br>
            <input type="submit" />
        </form>
    </body>
</html>
"""


@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    text = request.form['text']
    rot = request.form[str(rot)]
    return "<h1>" + rotate_string(text, rot) + "</h1>"

app.run()
