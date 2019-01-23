from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

#TODO make a global variable named form and set its value to be HTML
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
            textarea{{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>

        <form action="/" method ="POST">
            <label for="rot">Rotate by:</label>
            <input type= "text" name= "rot" value=0 />
            <br>
            <textarea name="text">{0}</textarea>   
                              
            <input type="submit" value="Submit Query"/>
            
        </form>
       
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")


@app.route("/", methods=['POST'])
def encrypt():
    buzz = int(request.form['rot'])
    houston = request.form['text']
    #moon = rotate_string(houston, buzz)
    #return"<h1>"  encrypted_message  "</h1>"
    return form.format(rotate_string(houston, buzz))
    

   
app.run()