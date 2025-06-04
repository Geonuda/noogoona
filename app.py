from flask import Flask, render_template
import os

# tamplat 폴더를 템플릿 폴더로 지정
app = Flask(__name__, template_folder='tamplat', static_folder='static')

@app.route('/')
def home():
    # 개인 정보 데이터
    profile_data = {
        'name': '김건우',
        'age': '25세',
        'grade': '4학년',
        'major': '컴퓨터공학과',
        'goal': '건강하게 살기!'
    }
    return render_template('index.html', profile=profile_data)

if __name__ == '__main__':
    # Render에서는 PORT 환경변수를 사용
    port = int(os.environ.get('PORT', 8080))
    print("🚀 Flask 서버를 시작합니다...")
    print(f"📱 포트 {port}에서 실행 중...")
    app.run(host='0.0.0.0', port=port, debug=False)