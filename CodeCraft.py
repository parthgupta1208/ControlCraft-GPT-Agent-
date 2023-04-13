from flask import Flask, render_template, request
import openai
import os
import pyperclip

# setup flask
app = Flask(__name__)

# home route
@app.route("/")
def hello():
    return render_template("index.html")

# copy code route
@app.route("/copycode")
def copycode():
    pyperclip.copy(html)
    return "<center><h1>Code copied to clipboard</h1></center>"

# preview route
@app.route('/Text', methods=['POST'])
def processtext():
    global html
    text = request.form['textboxinputdata']
    openai.api_key = os.getenv("OPENAI_KEY")
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages = [{"role": "system", "content" : "You are FridayAI, a large language model trained by Parth Gupta. Answer as concisely as possible. I will be giving you a prompt on how a webpage should look like and what will its function be. Give me the code for it but don't explain how the code works. The code should contain css and javscript code so the page is responsive. Ise the <script> and <style> tags instead of creating separate files"},
    {"role": "user", "content" : text}]
    )
    print(completion['choices'][0]['message']['content'])
    html=completion['choices'][0]['message']['content']
    html=(html.split("```"))[1].split("```")[0]
    ehtml=html[:html.find("</body>")]+"<center><a href='/copycode'>Copy Code</a></center>"+html[html.find("</body>"):]
    return render_template("result.html", textboxdata=ehtml)


if __name__ == "__main__":
    app.run(debug=True)