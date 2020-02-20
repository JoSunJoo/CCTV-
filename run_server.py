from flask import Flask, request, render_template, redirect, url_for
import pymysql

app = Flask(__name__)



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


#db연결
def getConnection():
    return pymysql.connect(host='specialist1.iptime.org', user='whtjswn1029', password='s971029', db='dashboard', charset='utf8')

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
    sql = "select * from cctv ORDER BY count DESC"
    return sql_template(1, sql);

#해당 CCTV의 traffic 정보 가져오기
def getCCTVTraffic(num):
    sql = "select count from cctv where cctv_num = "+str(num)
    return sql_template(3, sql)

#데이터 수정하기(cctv번호 -> traffic+1)
def setTraffic():
    #rows = getCCTVTraffic(num)
    sql = "select * from cctv where cctv_num = 1"

    rows=sql_template(1, sql)
    data = 0
    for i in rows:
        data = i['count'] + 1
        sql = "UPDATE cctv SET count = "+str(data)
    return sql_template(3, sql)

@app.route('/input')
def input():
    num = 2
    setTraffic();
    return redirect(url_for('index'))

@app.route('/')
def index():
    rows = getTraffic()

    data_lists=[]
    location_lists=[]
    cctv_lists=[]
    for i in rows:
        cctv_lists.append(i['cctv_num'])
        data_lists.append(i['count'])
        location_lists.append(i['location'])
        #setTraffic(i['id'], i['traffic']+1)
    return render_template('index.html', trafData1=data_lists[0], trafData2=data_lists[1], trafData3=data_lists[2], trafData4=data_lists[3], trafData5=data_lists[4],
                           loc1=location_lists[0], loc2=location_lists[1], loc3=location_lists[2], loc4=location_lists[3], loc5=location_lists[4],
                           cctv1=cctv_lists[0], cctv2=cctv_lists[1], cctv3=cctv_lists[2], cctv4=cctv_lists[3], cctv5=cctv_lists[4])

if __name__ == "__main__":
    app.run(debug=True)
