from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# CCTV 페이지 렌더링
@app.route('/cctv')
def cctv():
    return render_template('cctv.html')

if __name__ == "__main__":
    app.run()
