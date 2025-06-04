from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='tamplat', static_folder='static')

@app.route('/')
def home():
    profile_data = {
        'name': '김건우',
        'age': '25세',
        'grade': '4학년',
        'major': '컴퓨터공학과',
        'goal': '건강하게 살기!'
    }
    return render_template('index.html', profile=profile_data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)