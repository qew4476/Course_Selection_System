from typing import Optional
from link import *


class DB():
    def connect():
        cursor = connection.cursor()
        return cursor

    def prepare(sql):
        cursor = DB.connect()
        cursor.prepare(sql)
        return cursor

    def execute(cursor, sql):
        cursor.execute(sql)
        return cursor

    def execute_input(cursor, input):
        cursor.execute(None, input)
        return cursor

    def fetchall(cursor):
        return cursor.fetchall()

    def fetchone(cursor):
        return cursor.fetchone()

    def commit():
        connection.commit()


class Student():
    def get_student(account):
        sql = "SELECT ACCOUNT, PASSWORD,IDENTITY, SID, SNAME, SGRADE, SEMAIL  FROM STUDENT WHERE ACCOUNT = :id"
        return DB.fetchall(DB.execute_input(DB.prepare(sql), {'id': account}))

    def get_all_account():
        sql = "SELECT ACCOUNT FROM STUDENT"
        return DB.fetchall(DB.execute(DB.connect(), sql))

    def create_student(input):
        sql = 'INSERT INTO STUDENT VALUES (:account, :password,:sid,:sname, :sgrade, :semail, :identity)'
        DB.execute_input(DB.prepare(sql), input)
        DB.commit()

    def delete_class(account, cid):  # 刪除選課
        sql = 'DELETE * FROM RECORD WHERE ACCOUNT=:account and CID=:cid '
        DB.execute_input(DB.prepare(sql), {'account': account, 'cid': cid})
        DB.commit()

    def get_role(userid):
        sql = 'SELECT IDENTITY, SNAME FROM STUDENT WHERE ACCOUNT = :id '
        # userid是account
        return DB.fetchone(DB.execute_input(DB.prepare(sql), {'id': userid}))


class Member():
    def get_member(account):
        sql = "SELECT ACCOUNT, PASSWORD, MID, IDENTITY, NAME FROM MEMBER WHERE ACCOUNT = :id"
        return DB.fetchall(DB.execute_input(DB.prepare(sql), {'id': account}))

    def get_all_account():
        sql = "SELECT ACCOUNT FROM MEMBER"
        return DB.fetchall(DB.execute(DB.connect(), sql))

    def create_member(input):
        sql = 'INSERT INTO MEMBER VALUES (null, :name, :account, :password, :identity)'
        DB.execute_input(DB.prepare(sql), input)
        DB.commit()

    def delete_product(tno, pid):
        sql = 'DELETE FROM RECORD WHERE TNO=:tno and PID=:pid '
        DB.execute_input(DB.prepare(sql), {'tno': tno, 'pid': pid})
        DB.commit()

    def get_order(userid):
        sql = 'SELECT * FROM ORDER_LIST WHERE MID = :id ORDER BY ORDERTIME DESC'
        return DB.fetchall(DB.execute_input(DB.prepare(sql), {'id': userid}))

    def get_role(userid):
        sql = 'SELECT IDENTITY, NAME FROM MEMBER WHERE MID = :id '
        return DB.fetchone(DB.execute_input(DB.prepare(sql), {'id': userid}))

class Contact():
    def create_contact(input):
        sql = 'INSERT INTO CONTACT VALUES (:id, :phone, :contname,:account)'
        DB.execute_input(DB.prepare(sql), input)
        DB.commit()


class Cart():
    def check(user_id):
        sql = 'SELECT * FROM CART, RECORD WHERE CART.MID = :id AND CART.TNO = RECORD.TNO'
        return DB.fetchone(DB.execute_input(DB.prepare(sql), {'id': user_id}))

    def get_cart(user_id):
        sql = 'SELECT * FROM CART WHERE MID = :id'
        return DB.fetchone(DB.execute_input(DB.prepare(sql), {'id': user_id}))

    def add_cart(user_id, time):
        sql = 'INSERT INTO CART VALUES (:id, :time, cart_tno_seq.nextval)'
        DB.execute_input(DB.prepare(sql), {'id': user_id, 'time': time})
        DB.commit()

    def clear_cart(user_id):
        sql = 'DELETE FROM CART WHERE MID = :id '
        DB.execute_input(DB.prepare(sql), {'id': user_id})
        DB.commit()


class Course():
    def count():
        sql = 'SELECT COUNT(*) FROM COURSE'
        return DB.fetchone(DB.execute(DB.connect(), sql))

    def get_course(cid):
        sql = 'SELECT * FROM COURSE WHERE CID = :id'
        return DB.fetchone(DB.execute_input(DB.prepare(sql), {'id': cid}))

    def get_all_course():
        sql = 'SELECT * FROM COURSE'
        return DB.fetchall(DB.execute(DB.connect(), sql))

    def get_course_tname(cid):
        sql = 'SELECT tName FROM COURSE, TEACHER WHERE COURSE.tId = TEACHER.tId AND CID = :id'
        return DB.fetchone(DB.execute_input(DB.prepare(sql), {'id': cid}))



class Product():
    def count():
        sql = 'SELECT COUNT(*) FROM PRODUCT'
        return DB.fetchone(DB.execute(DB.connect(), sql))

    def get_product(pid):
        sql = 'SELECT * FROM PRODUCT WHERE PID = :id'
        return DB.fetchone(DB.execute_input(DB.prepare(sql), {'id': pid}))

    def get_all_product():
        sql = 'SELECT * FROM PRODUCT'
        return DB.fetchall(DB.execute(DB.connect(), sql))

    def get_name(pid):
        sql = 'SELECT PNAME FROM PRODUCT WHERE PID = :id'
        return DB.fetchone(DB.execute_input(DB.prepare(sql), {'id': pid}))[0]

    def add_product(input):
        sql = 'INSERT INTO PRODUCT VALUES (:pid, :name, :price, :category, :description)'

        DB.execute_input(DB.prepare(sql), input)
        DB.commit()

    def delete_product(pid):
        sql = 'DELETE FROM PRODUCT WHERE PID = :id '
        DB.execute_input(DB.prepare(sql), {'id': pid})
        DB.commit()

    def update_product(input):
        sql = 'UPDATE PRODUCT SET PNAME=:name, PRICE=:price, CATEGORY=:category, PDESC=:description WHERE PID=:pid'
        DB.execute_input(DB.prepare(sql), input)
        DB.commit()


class Selerecord():
    def check_course(userid, cid):  #檢查是否選過這門課
        sql = 'SELECT * FROM SELERECORD WHERE CID = :cid AND ACCOUNT = :id'
        return DB.fetchone(DB.execute_input(DB.prepare(sql), {'id': userid, 'cid': cid}))
        # user_id是account
    def get_oneRecord(userid):  #檢查是否有選課
        sql = 'SELECT * FROM SELERECORD WHERE ACCOUNT = :id'
        return DB.fetchone(DB.execute_input(DB.prepare(sql), {'id': userid}))

    def add_course(input):
        sql = 'INSERT INTO SELERECORD VALUES (:id, :cid)'
        DB.execute_input(DB.prepare(sql), input)
        DB.commit()
    def get_record(account):    #找出這個人選過的所有課
        sql = 'SELECT * FROM SELERECORD WHERE ACCOUNT = :id'
        return DB.fetchall(DB.execute_input(DB.prepare(sql), {'id': account}))

    def delete_course(userid, cid):
        sql = 'DELETE FROM SELERECORD WHERE CID = :cid AND ACCOUNT = :id'
        DB.execute_input(DB.prepare(sql), {'id': userid, 'cid': cid})
        DB.commit()

class Record():
    def get_total_money(tno):
        sql = 'SELECT SUM(TOTAL) FROM RECORD WHERE TNO=:tno'
        return DB.fetchone(DB.execute_input(DB.prepare(sql), {'tno': tno}))[0]

    def check_product(pid, tno):
        sql = 'SELECT * FROM RECORD WHERE PID = :id and TNO = :tno'
        return DB.fetchone(DB.execute_input(DB.prepare(sql), {'id': pid, 'tno': tno}))

    def get_price(pid):
        sql = 'SELECT PRICE FROM PRODUCT WHERE PID = :id'
        return DB.fetchone(DB.execute_input(DB.prepare(sql), {'id': pid}))[0]

    def add_product(input):
        sql = 'INSERT INTO RECORD VALUES (:id, :tno, 1, :price, :total)'
        DB.execute_input(DB.prepare(sql), input)
        DB.commit()

    def get_record(tno):
        sql = 'SELECT * FROM RECORD WHERE TNO = :id'
        return DB.fetchall(DB.execute_input(DB.prepare(sql), {'id': tno}))

    def get_amount(tno, pid):
        sql = 'SELECT AMOUNT FROM RECORD WHERE TNO = :id and PID=:pid'
        return DB.fetchone(DB.execute_input(DB.prepare(sql), {'id': tno, 'pid': pid}))[0]

    def update_product(input):
        sql = 'UPDATE RECORD SET AMOUNT=:amount, TOTAL=:total WHERE PID=:pid and TNO=:tno'
        DB.execute_input(DB.prepare(sql), input)

    def delete_check(pid):
        sql = 'SELECT * FROM RECORD WHERE PID=:pid'
        return DB.fetchone(DB.execute_input(DB.prepare(sql), {'pid': pid}))

    def get_total(tno):
        sql = 'SELECT SUM(TOTAL) FROM RECORD WHERE TNO = :id'
        return DB.fetchall(DB.execute_input(DB.prepare(sql), {'id': tno}))[0]


class Order_List():
    def add_order(input):
        sql = 'INSERT INTO ORDER_LIST VALUES (null, :mid, TO_DATE(:time, :format ), :total, :tno)'
        DB.execute_input(DB.prepare(sql), input)
        DB.commit()

    def get_order():
        sql = 'SELECT OID, NAME, PRICE, ORDERTIME FROM ORDER_LIST NATURAL JOIN MEMBER ORDER BY ORDERTIME DESC'
        return DB.fetchall(DB.execute(DB.connect(), sql))

    def get_orderdetail():
        sql = 'SELECT O.OID, P.PNAME, R.SALEPRICE, R.AMOUNT FROM ORDER_LIST O, RECORD R, PRODUCT P WHERE O.TNO = R.TNO AND R.PID = P.PID'
        return DB.fetchall(DB.execute(DB.connect(), sql))


class Analysis():
    def month_price(i):
        sql = 'SELECT EXTRACT(MONTH FROM ORDERTIME), SUM(PRICE) FROM ORDER_LIST WHERE EXTRACT(MONTH FROM ORDERTIME)=:mon GROUP BY EXTRACT(MONTH FROM ORDERTIME)'
        return DB.fetchall(DB.execute_input(DB.prepare(sql), {"mon": i}))

    def month_count(i):
        sql = 'SELECT EXTRACT(MONTH FROM ORDERTIME), COUNT(OID) FROM ORDER_LIST WHERE EXTRACT(MONTH FROM ORDERTIME)=:mon GROUP BY EXTRACT(MONTH FROM ORDERTIME)'
        return DB.fetchall(DB.execute_input(DB.prepare(sql), {"mon": i}))

    def category_sale():
        sql = 'SELECT SUM(TOTAL), CATEGORY FROM(SELECT * FROM PRODUCT,RECORD WHERE PRODUCT.PID = RECORD.PID) GROUP BY CATEGORY'
        return DB.fetchall(DB.execute(DB.connect(), sql))

    def member_sale():
        sql = 'SELECT SUM(PRICE), MEMBER.MID, MEMBER.NAME FROM ORDER_LIST, MEMBER WHERE ORDER_LIST.MID = MEMBER.MID AND MEMBER.IDENTITY = :identity GROUP BY MEMBER.MID, MEMBER.NAME ORDER BY SUM(PRICE) DESC'
        return DB.fetchall(DB.execute_input(DB.prepare(sql), {'identity': 'user'}))

    def member_sale_count():
        sql = 'SELECT COUNT(*), MEMBER.MID, MEMBER.NAME FROM ORDER_LIST, MEMBER WHERE ORDER_LIST.MID = MEMBER.MID AND MEMBER.IDENTITY = :identity GROUP BY MEMBER.MID, MEMBER.NAME ORDER BY COUNT(*) DESC'
        return DB.fetchall(DB.execute_input(DB.prepare(sql), {'identity': 'user'}))
