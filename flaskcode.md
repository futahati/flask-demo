# flask 程式

## 無題一
```python
# flask套件名稱／Flask類別名稱(物件)
from flask import Flask

# app：變數名稱；Flask(__name__)：把目前檔案main.py當成伺服器
# 透過 Flask 產生伺服器
# __name__（代表：本地） == main.py
app = Flask(__name__) # 注意 Flask 的F是大寫


if __name__ == "__main__":
    # pass
    # （必要）最後一行，執行伺服器
    # 目前為偵測模式，需要知道錯誤資訊、執行資訊 debug= True
    # 若為正式使用模式時，debug=False
    app.run(debug=True)
```

- 執行程式碼後
```python
(.venv) C:\Users\USER\Desktop\django123\flask456\flask-pm25-project>c:/Users/USER/Desktop/django123/flask456/flask-pm25-project/.venv/Scripts/python.exe c:/Users/USER/Desktop/django123/flask456/flask-pm25-project/main.py 
 * Serving Flask app 'main'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 770-022-915

# 127.0.0.1：這是「本機位址」（Localhost本地端），代表你自己的電腦。
# 5000是連接埠號（Port Number）：這是一個「通訊埠」，用來指引電腦上正在執行的特定服務。在學習 Python 的 Flask 輕量級網頁框架 或其他 Web 應用程式開發時，5000 是預設的測試通訊埠。
 * Running on http://127.0.0.1:5000

# Ctrl + C → 關閉伺服器
Press CTRL+C to quit
```

## route路由器
- 首頁 "/"
    ```python
    # 透過 @app 建立 route路由器，下方一定是接函式def or 方法
    # / == 首頁
    @app.route("/")
    def index():
        # 有綁route一定要有return
        return "Hello flask!"
        
    # 網址 127.0.0.1:5000/
    ```

- route路由器`多項指定`
    ```python
    # 2個route共用一個函式def
    @app.route("/")
    @app.route("/hello")
    def index():
        # 有綁route一定要有return
        return "Hello flask!"
        
    # 網址 127.0.0.1:5000/
    # 網址 127.0.0.1:5000/hello
    ```

### def函式
- return 可以使用HTML標籤語法
    ```python
    @app.route("/")
    def index():
        # 使用HTML標籤語法
        return "<h1> Hello flask! </h1>"

    # 網址 127.0.0.1:5000/
    ```

- 單參數
    ```python
    # 從網址 /<name> 的name →傳遞至函式def的參數name →至return裡的 name，最終秀在網頁上。
    @app.route("/hello/<name>")
    def hello(name):
        return f"Welcome {name}"

    # 網址 127.0.0.1:5000/hello/irw
    ```
- 多項參數
    ```python
    # 從網址 /<name> 的name →傳遞至函式def的參數name →至return裡的 name，最終秀在網頁上。
    @app.route("/hello/<name>/<bmi>")
    def hello(name, bmi):
        return f"Welcome {name} BMI：{bmi}"

    # 網址 127.0.0.1:5000/hello/irw/21.7
    ```
- 參數 `型態` 設定
    - 網址傳遞至後端是字串型態 `str`
    - 若要計算要改為數值型態 `int`／`float`
    ```python
    # 從網址端傳進後端是字串型態

    @app.route("/hello/<name>/<height>/<weight>")
    def hello(name, height, weight):
        # bmi = eval(weight) / (eval(height) / 100) ** 2
        # 約定小數點
        bmi = round(eval(weight) / (eval(height) / 100) ** 2, 2)

        # 約定小數點
        # return f"Welcome {name} BMI：{bmi:.2f}"
        return f"Welcome {name} BMI：{bmi}"

    # 網址 127.0.0.1:5000/hello/irw/178/88
    ```
- 避免輸入錯誤 `try` `except`
    ```python
    @app.route("/hello/<name>/<height>/<weight>")
    def hello(name, height, weight):
        try:
            # 約定小數點
            bmi = round(eval(weight) / (eval(height) / 100) ** 2, 2)

            return f"Welcome {name} BMI：{bmi}"
        except Exception as e:
            return "輸入不正確：{e}"

    # 網址 127.0.0.1:5000/hello/irw/178/88
    # 網址 127.0.0.1:5000/hello/irw/178/abc
    ```

## BMI練習
```python
@app.route("/hello/<name>/<height>/<weight>")
def hello(name, height, weight):
    try:
        # 約定小數點
        bmi = round(eval(weight) / (eval(height) / 100) ** 2, 2)
        # category評語
        if bmi < 18.5:
            category = "過輕"
        elif bmi <24:
            category = "正常"
        elif bmi <27:
            category = "略重"
        else:
            category = "肥胖"

        return f"Welcome {name} BMI：{bmi} 評語：{category}"
    except Exception as e:
        return "輸入不正確：{e}"

# 網址 127.0.0.1:5000/hello/irw/178/88
# 網址 127.0.0.1:5000/hello/irw/178/abc
```

- 將 `try` `except` 獨立出來，寫一個函式
    - def get_bmi() → return 回傳 `{}字典` 型態
    - def hello() → 呼叫get_bmi()
    ```python
    # 計算BMI + 評語
    def get_bmi(height, weight):
        try:
            # 約定小數點
            bmi = round(eval(weight) / (eval(height) / 100) ** 2, 2)
            # category評語
            if bmi < 18.5:
                category = "過輕"
            elif bmi <24:
                category = "正常"
            elif bmi <27:
                category = "略重"
            else:
                category = "肥胖"

            # 回傳 {}字典 型態
            return {"success":True, "bmi":bmi, "category":category}
        except Exception as e:
            return {"success":False, "bmi":None, "category":None}


    @app.route("/hello/<name>/<height>/<weight>")
    def hello(name, height, weight):

        # 呼叫get_bmi()
        result = get_bmi(height, weight)
        bmi = result["bmi"]
        category = result["category"]

        if result["success"]:
            return f"Welcome {name} BMI：{bmi} 評語：{category}"
        else:
            return "輸入不正確。"

    # 網址 127.0.0.1:5000/hello/irw/178/88
    # 網址 127.0.0.1:5000/hello/irw/178/abc
    ```

## 回傳靜態網頁 `render_template`
- 在專案中，建立／新增Folder
    - 開啟Explorer (檔案總管)
        - 在 Explorer 裡，滑鼠右鍵 → New Folder...
        - 輸入 *templates* → Enter
            - `templates`不能打錯字
            - 滑鼠移至 `templates` 上 → 按右鍵 → New File...
            - 輸入 *index.html*
        - （鍵盤流）快捷鍵 `Ctrl + B` **快速顯示/隱藏 Explorer 視窗**
        - （鍵盤流）快捷鍵 `Ctrl + Shift + E` **進入／離開 Explorer 視窗**
    ```python
    from flask import Flask, render_template

    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template("index.html")
    ```

### Jinja2模板
#### `{變數}` 前、後端區分
- index.html
    ```html
    <!DOCTYPE html>
    <html lang="zn_TW">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <h1>首頁</h1>
        <!-- 下方name名稱，就是後端 name="irw" 的 name名稱 -->
        姓名：{{name}}
    </body>
    </html>
    ```
- route路由器
    ```python
    @app.route("/")
    def index():
        # name 給前端html用的名稱
        # ="irw" 代表：後端的資料
        return render_template("index.html", name="irw")
    ```
#### stocks回傳前端的格式？
- index.html
    ```html
    <body>
        <h1>首頁</h1>
        <!-- 下方name名稱，就是後端 name="irw" 的 name名稱 -->
        姓名：{{name}}

        <!-- 僅輸出資料結構，不是html格式 -->
        <p>{{stocks}}</p>

        <!-- html格式應為 -->
        <h2>日經指數
            <span style="color:red">22,920.30</span>
        </h2>

    </body>
    ```
- route路由器
    ```python
    @app.route("/")
    def index():
        stocks=[
        {'分類': '日經指數', '指數': '22,920.30'},
        {'分類': '韓國綜合', '指數': '2,304.59'},
        {'分類': '香港恆生', '指數': '25,083.71'},
        {'分類': '上海綜合', '指數': '3,380.68'}
        ]
        
        return render_template("index.html", name="irw", stocks=stocks)
    ```
#### `{% for %}` `{% endfor %}` 格式處理：for迴圈輸出
- index.html
    ```html
    <body>
        <h1>首頁</h1>
        <!-- 下方name名稱，就是後端 name="irw" 的 name名稱 -->
        姓名：{{name}}

        {% for stock in stocks %}

        <!-- html格式應為 -->
        <h2>{{stocks['分類']}}
            <span style="color:red">{{stocks['指數']}}</span>
        </h2>

        {% endfor %}

    </body>
    ```
- route路由器
    ```python
    @app.route("/")
    def index():
        stocks=[
        {'分類': '日經指數', '指數': '22,920.30'},
        {'分類': '韓國綜合', '指數': '2,304.59'},
        {'分類': '香港恆生', '指數': '25,083.71'},
        {'分類': '上海綜合', '指數': '3,380.68'}
        ]

        # 字典取值 key:values
        # print()後端測試看結果用的
        for stock in stocks:
            print(stocks['分類'], stocks['指數'])
        
        return render_template("index.html", name="irw", stocks=stocks)
    ```