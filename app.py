from flask import Flask, render_template
import json 
import os 

app = Flask(__name__)

@app.route('/<int:page_num>')
def show_page(page_num):
    return render_template('index.html', page_num=page_num)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)