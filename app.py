from flask import Flask, render_template
import json 
import os 

app = Flask(__name__)

# JSON 데이터 파일을 읽어오는 함수
def load_data():
    # data.json 파일이 app.py와 같은 폴더에 있다고 가정
    with open('data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/<int:page_num>')
def show_page(page_num):
    data = load_data()
    # json의 키값은 문자열이므로 숫자를 문자열로 변환하여 찾습니다.
    page_key = str(page_num) 
    
    # 해당 번호의 이미지 목록을 가져옵니다. 없으면 빈 리스트를 반환합니다.
    images = data.get(page_key, [])
    
    return render_template('index.html', page_num=page_num, images=images)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)