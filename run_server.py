from flask import Flask, request, render_template, redirect, url_for
import pymysql

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# CCTV 페이지 렌더링
@app.route('/cctv')
def cctv():
    return render_template('cctv.html')

# traffic 처리 get/post로 접근가능
@app.route('/scheduler')
def scheduler():
    # 요청이 get이면
    if request.method == 'GET':
        return schedulerdao.getTraffic()

    #요청이 post면
    if request.method == 'POST':
        _id = request.form['_id']
        traffic = request.form['traffic']
        # traffic을 전송
        return  setScheduler(_id, traffic)

#데이터 삽입
@app.route('/input')
def input():
    #cursor의 값이 어떤 형식으로 반환되는지 확인하기!!!
    rows = getTraffic()
    num = 10;
    setTraffic(2, num)




    return redirect(url_for('index'))



#db연결
def getConnection():
    return pymysql.connect(host='localhost', user='root', password='s971029', db='temp_project', charset='utf8')

#sql 중복 부분 리팩토링
def sql_template(type, sql):
    # Connection 연결
    connetion = getConnection()
    try:
        #insert, update, delete 사용
        if type == 3 :
            with connetion.cursor() as cursor :
                # 데이터 입력
                rows = cursor.execute(sql)
                # commit
                connetion.commit()
                return rows
        else :
            # 1 = fetchall() 2 = fetchone()
            with connetion.cursor(pymysql.cursors.DictCursor) as cursor :
                # SQL 처리
                cursor.execute(sql)
                # 처리된 data 가져옴
                if type == 1 :
                    return cursor.fetchall()
                elif type == 2 :
                    return cursor.fetchone()
    finally:
        # Connection 닫기
        connetion.close()

#등록된 데이터 가져오기(지역 별 traffic)
def getTraffic():
    sql = "select id, traffic from cctv ORDER BY traffic DESC"
    return sql_template(2, sql);

#데이터 수정하기(cctv번호 -> traffic+1)
def setTraffic(_id, new_traffic):
    sql = "UPDATE cctv SET traffic = "+str(new_traffic)+" WHERE id = "+str(_id)
    return sql_template(3, sql)


if __name__ == "__main__":
    app.run(debug=True)
