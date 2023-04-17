<<<<<<< HEAD
=======
- [X] 登入&註冊系統
- [X] 課程列表&搜尋功能
- [X] 加選功能
- [X] 退選功能<br>
- [X] 管理者課程增刪查改功能
- [X] 分析功能(各系選課人數長條圖)
===以上功能完成===
- [ ] (...待修前端功能：註冊時將'學級'改為'學系' & 下拉式選單)
- [ ] 前端修飾網頁
- [ ] 剩餘bug檢查 or 新增功能


- [ ] 更改網頁路徑名稱 p.s.最後再做，以免撰寫時有bug


>>>>>>> 7a4978f6b04f44d8389a99d51c56b666f7b6315d
# 選課系統
一套使用Flask開發的選課系統，後端使用Oracle資料庫。

* 學生：可以是使用者，或是有管理者身份的工讀生，因此學號不唯一，帳號則是唯一。其資料包含Account, Password, sId(學號), sName(姓名), major(科系)， sEmail(信箱), identity(是管理者或使用者)。
* 緊急聯絡人：學生的緊急聯絡人，紀錄該人的身份證字號(Id)、電話(phone)、姓名(contName)。不同學生可能有不同的緊急聯絡人，比如兩位學生有同一個家長。
* 課程：有課程編號(cId)、系所名稱(department)、課程名稱(cName)；其中課程編號為唯一。
* 教室：教室編號(roomId)、可容納人數(num)。
* 老師：教師編號(tId)、教師姓名(tName)

# ERD
![](https://i.imgur.com/o56QKTA.png)


# 關聯綱目
![](https://i.imgur.com/5y8CgdO.png)


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
- 註冊後，點選登入即可進入頁面；或使用我們所提供的現成帳戶，直接登入使用：
1. 管理者帳戶
   帳號：manager
   密碼：123
2. 使用者帳戶
   帳號：user
   密碼：123

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



# 程式系統架構
 

### 一、程式系統目的

此程式系統的目的是令使用者(學生)可以透過系統來進行選課，同時管理者(教務處工讀學生)可以管理課程、觀看選課情形。

### 二、程式系統流程

-   進入網站後，選擇對應身份
  ( i )學生: 尚未註冊 → 須先進行註冊 / 已註冊 → 使用帳號密碼登入
  ( ii )管理者：尚未註冊 → 須先進行註冊 / 已註冊 → 使用帳號密碼登入

-   登入後
	( i )學生：可進行以下操作
		(a)課程導覽：供學生查看可選課程及選課(新增、查詢)
		(b)選課結果查詢：供學生查看選課結果及退選課程(刪除)

	( ii )管理者：可進行以下操作
		(a)課程管理：可新增(上架)課程、對現有課程進行編輯改動、刪除現有課程、瀏覽現有課程(查詢)
		(b)教師資料：查看教師編號與姓名
		(c)學生選課資料：查看目前學生之選課情形
		(d)學生聯絡人資料：查看學生之緊急聯絡人
		(e)資料分析：供管理者查看每堂課程選課學生之系所分佈

-   使用完畢，登出系統

### 三、程式系統模組

![](https://i.imgur.com/MZ3j4Dw.png)


( 1 ) api：api.py → 包含註冊、登入登出的api / sql.py → 包含所有對資料庫操作的api
( 2 ) backstage：後台(管理者)相關程式，包含 html 檔及 api ( py檔)
( 3 ) bookstore：前台(學生)相關程式，包含 html 檔及 api
( 4 ) static：css 和設計圖檔等
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

-   使用工具及架構
    ![](https://i.imgur.com/F5WMiSW.png)



