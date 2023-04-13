from flask import Flask, render_template, request
import openai
import os
import pyperclip

# setup flask
app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_KEY")

# home route
@app.route("/")
def hello():
    return render_template("index.html")

# preview route
@app.route('/Text', methods=['POST'])
def processtext():
    text = request.form['textboxinputdata']
    
    #building various cases
    if 'python' in text:
        text=text.replace("```python","```")
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages = [{"role": "system", "content" : "You are FridayAI, a large language model trained by Parth Gupta. Answer as concisely as possible. I will be giving you a prompt on what will a code do. Give me the code for it but don't explain how the code works. The code should come as a single output, i.e don't output the code in various parts. If creating functions, always include code for main as well"},
        {"role": "user", "content" : text}]
        )
        print(completion['choices'][0]['message']['content'])
        output=completion['choices'][0]['message']['content']
        output=(output.split("```"))[1].split("```")[0]
        with open("C:\\Everything\\Code\\Python\\Projects\\CodeCraft\\Codes\\codefile.py", "w") as f:
            f.write(output)
        os.system("code C:\\Everything\\Code\\Python\\Projects\\CodeCraft\\Codes\\codefile.py")
        os.system("python C:\\Everything\\Code\\Python\\Projects\\CodeCraft\\Codes\\codefile.py")
        return render_template("result.html", textboxdata="<center><h2>VS Code Window is Opened</h2></center>")
    elif 'html' in text:
        text=text.replace("```html","```")
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
    elif 'java' in text:
        pass
    elif 'javascript' in text:
        pass
    elif 'css' in text:
        pass
    elif 'c++' in text:
        pass
    elif 'c#' in text:
        pass
    elif 'c' in text:
        pass
    else:
        pass

if __name__ == "__main__":
    app.run(debug=True)