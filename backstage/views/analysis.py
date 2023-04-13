from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from link import *
from api.sql import *
import imp, random, os, string
from werkzeug.utils import secure_filename
from flask import current_app

analysis = Blueprint('analysis', __name__, template_folder='../templates')

@analysis.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    if request.method == 'GET':
        if(current_user.role == 'user'):
            flash('No permission')
            return redirect(url_for('index'))
    elif 'look' in request.values:                                  #當使用者按下查看分佈的按鈕時會回傳'look'，將頁面導向分佈圖的頁面
        cid = request.values.get('look')
        return redirect(url_for('analysis.distribute', cid = cid))
    
    book_data = book()
    return render_template('dashboard.html', bookdata = book_data, user = current_user.name)

def book():
    book_row = Product.get_all_course()
    book_data = []
    for i in book_row:
        book = {
                '課程編號': i[0],
                '課程名稱': i[1],
                '開課系所': i[2],
                '教師姓名': Course.get_course_tname(i[0]),
                '教室代號': i[4]
            }
        book_data.append(book)
    return book_data

@analysis.route('/distribute')
@login_required
def distribute():
    cid = request.values.get('cid')                             #獲得要查看分佈的課程的 cid
    row = Analysis.category_sale(cid)                           #獲得該課程的選課學生系所人數(使用到 sql.py 的函數)
    data = []
    for i in row:
        temp = {
            '人數': i[0],
            '系所': i[1]
        }
        data.append(temp)
    
    # department = [會計,財金,資管,資工,電機,......]  //在一開始學生註冊帳號時建議用下拉式選單讓學生填寫其系所，因為這個環節目前是寫死的
    select_num = [0] * 8                                        #用來存該課程每個科系的選課人數
    for i in data:
        if i['系所'] == '會計學系':
            select_num[0] = i['人數']
        elif i['系所'] == '財務金融學系':
            select_num[1] = i['人數']
        elif i['系所'] == '資訊管理學系':
            select_num[2] = i['人數']
        elif i['系所'] == '資訊工程學系':
            select_num[3] = i['人數']
        elif i['系所'] == '電機工程學系':
            select_num[4] = i['人數']
        elif i['系所'] == '法律學系':
            select_num[5] = i['人數']
        elif i['系所'] == '機械工程學系':
            select_num[6] = i['人數']
        elif i['系所'] == '工商管理學系':
            select_num[7] = i['人數']
    return render_template('distribute.html', data = data, select_num = select_num, user = current_user.name)