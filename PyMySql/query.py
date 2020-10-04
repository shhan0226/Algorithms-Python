# -*- coding:utf-8 -*-
import pymysql

db = pymysql.connect(host='192.168.50.50', port=3306, user='tester', passwd='stack', db='testdb', charset='utf8')
cursor = db.cursor()

if __name__=='__main__':
    sql = "select * from testtable"
    cursor.execute(sql)

#    sql2 = "INSERT INTO testtable (name,email) VALUES ('A', 'cc@naver.com');"
#    cursor.execute(sql2)

    sql3 = "select * from testtable"
    cursor.execute(sql3)

    result = cursor.fetchall()

#   print(result)
    for row in result:
        print(row)

    db.commit()
    db.close()