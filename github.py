from flask import Flask,redirect,url_for,render_template,request
import requests
base_url = "https://api.github.com/users/"

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        # Handle POST Request here
        githubname = request.form.get("githubname")
        response = requests.get(base_url + githubname)
        user_info = response.json()
        return render_template('index.html', profile = user_info)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)