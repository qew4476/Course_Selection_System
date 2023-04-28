# 選課系統

一套使用Flask開發的選課系統，後端使用Oracle資料庫，利用Azure, Heroku架設網站。

* 學生：可以是使用者，或是有管理者身份的工讀生，因此學號不唯一，帳號則是唯一。其資料包含Account, Password, sId(學號), sName(姓名), major(科系)， sEmail(信箱), identity(是管理者或使用者)。
* 緊急聯絡人：學生的緊急聯絡人，此實體依附於學生，紀錄該人的身份證字號(Id)、電話(phone)、姓名(contName)。
* 課程：有課程編號(cId)、系所名稱(department)、課程名稱(cName)；其中課程編號為唯一。課程完全參與於教師，但允許課程建立時選課學生人數為零。
* 教室：教室編號(roomId)、可容納人數(num)。
* 老師：教師編號(tId)、教師姓名(tName)

# ERD
![](https://i.imgur.com/9dgkd9n.png)


# 關聯綱目
![](https://i.imgur.com/5y8CgdO.png)


# 程式系統架構

### 一、程式系統目的

此程式系統的目的是令使用者(學生)可以透過系統來進行選課，同時管理者(教務處工讀學生)可以管理課程、觀看選課情形。

### 二、程式系統流程

-   進入網站後，選擇對應身份
</br>
  ( i )學生: 尚未註冊 → 須先進行註冊 / 已註冊 → 使用帳號密碼登入
</br>
  ( ii )管理者：尚未註冊 → 須先進行註冊 / 已註冊 → 使用帳號密碼登入
</br></br>
-   登入後
</br>

#### 學生：可進行以下操作


 <br>   (a)課程導覽：供學生查看可選課程及選課(新增、查詢)
       </br>     
<br>(b)選課結果查詢：供學生查看選課結果及退選課程(刪除)
</br>

#### 管理者：可進行以下操作


<br>(a)課程管理：可新增(上架)課程、對現有課程進行編輯改動、刪除現有課程、瀏覽現有課程(查詢)
</br>
    <br>(b)教師資料：查看教師編號與姓名
</br>
    <br>(c)學生選課資料：查看目前學生之選課情形
</br>
    <br>(d)學生聯絡人資料：查看學生之緊急聯絡人
</br>
    <br>(e)資料分析：供管理者查看每堂課程選課學生之系所分佈
</br>
-   使用完畢，登出系統

### 三、程式系統模組

![](https://i.imgur.com/MZ3j4Dw.png)
</br>

( 1 ) api：api.py → 包含註冊、登入登出的api / sql.py → 包含所有對資料庫操作的api
</br>
( 2 ) backstage：後台(管理者)相關程式，包含 html 檔及 api ( py檔)
</br>
( 3 ) bookstore：前台(學生)相關程式，包含 html 檔及 api
</br>
( 4 ) static：css 和設計圖檔等
</br>
( 5 ) templates：其他頁面之 html


-   資料庫 sql 檔
  ![](https://i.imgur.com/eXOjHGz.png)
* 連線處理
  ![](https://i.imgur.com/ZxwtBBH.png)

  -   系統架構 - 使用者
    ![](https://i.imgur.com/1Dsbc1o.png)
* 系統架構 - 管理者
  ![](https://i.imgur.com/iAqJQke.png)
#### 工具

-   前端網頁  
  由 HTML, CSS 構成

-   後端運作
  Python, Flask
  資料庫  
	由 SQL、SQLDeveloper 構成
架設網站：Heroku, Azure

-   使用工具及架構
    ![](https://i.imgur.com/F5WMiSW.png)

# 使用說明
[第四組_中山選課系統 - YouTube](https://www.youtube.com/watch?v=KGXBogrHBIM)
## DEMO網址
使用Heroku架設網站</br>
</br>Heroku: https://dbprojc1.herokuapp.com/
</br>Github: https://github.com/qew4476/DB_project1_G4
</br>可連線時間：2023.05.01 ~ 2023.05.06 00:00-24:00

- 可註冊，或使用現成帳戶：
1. 管理者帳戶
   帳號：manager
   密碼：123
2. 使用者帳戶
   帳號：user
   密碼：123


# 使用方式
### 安裝環境
* Python 3.8.16

##### 安裝python套件
```
pip install -r requirements.txt
```
##### 啟動程式
```python=
python app.py
```

- [http://localhost:5000/] 進入首頁。
- 首次使用請點選註冊按鈕，並註冊帳號(分別有使用者&管理者兩個身份)。


##### 登入管理者帳戶
可在課程管理頁面新增、編輯、刪除課程。以下用新增課程舉例：
![](https://i.imgur.com/2tg141W.png)
![](https://i.imgur.com/UvVU4k6.png)

* 若新增已重複的課程，或者輸入不存在的教師編號，會出現錯誤訊息。![](https://i.imgur.com/dtcOXVr.png)
* 在後台資料分析頁面，可查看各課程的選課學生科系分佈
  1. 點擊查看分佈![](https://i.imgur.com/pJ2DG4f.png)
  2. ![](https://i.imgur.com/6kVABin.png)

##### 登入使用者帳戶
* 可在課程導覽處選課
  ![](https://i.imgur.com/hY9Ee9K.png)


* 在「選課結果查詢」頁面查看已選的課程，或者退選
  ![](https://i.imgur.com/2niBEKz.png)

