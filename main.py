from flask import Flask
from flask_cors import CORS
import pymysql


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/hello')
def hello():
    host = "192.168.42.202"
    user = "root"
    password = "qwer1234"
    db = "ssg_db"
    conn = pymysql.connect(host=host, user=user, password=password, charset='utf8')
    curs = conn.cursor()
    sql = "select * from student"
    curs.execute(sql)

    rows = curs.fatchall()
    print(rows)
    conn.commit()
    conn.close()
    result = {"code" : 200, "message":rows}
    return result

if __name__ == "__main__":
    app.run(port=80, host='0.0.0.0')