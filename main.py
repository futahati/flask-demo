from flask import Flask, render_template, request
from datetime import datetime

# 本地端locahost http://127.0.0.1:5000
# Ctrl + C 終止（／關閉）伺服器
app = Flask(__name__)


@app.route("/calc-bmi")
def calc_bmi():
    height = request.args.get("height")  # .get("height") height從前端取得
    weight = request.args.get("weight")

    result = get_bmi(height, weight)

    return render_template("bmi.html", result=result, height=height, weight=weight)


@app.route("/bmi")
def bmi():
    return render_template("bmi.html", result=None)


# 建立第1個路由器
@app.route("/")
# @app.route("/hello") # 寫第2個，是共用首頁
# 緊接著函式
def index():
    # 有路由器，一定要 return
    # return "Hello Flask!!"
    # return "<h1> Hello Flask!! </h1>"
    stocks = [
        {"分類": "日經指數", "指數": "22,920.30"},
        {"分類": "韓國綜合", "指數": "2,304.59"},
        {"分類": "香港恆生", "指數": "25,083.71"},
        {"分類": "上海綜合", "指數": "3,380.68"},
    ]

    for stock in stocks:
        # print在後端看結果
        # print(stock)
        print(stock["分類"], stock["指數"])

    today = datetime.today()
    # print在後端看today的結果
    print(today)

    return render_template(
        "index.html", name="irw", stocks=stocks, today=today
    )  # name="irw" →這裡是後端的name, "irw"是要傳遞給前端使用的
    """stocks（這裡的參數，上方的內容啦）=stocks（要給前端的參數）"""


# 計算BMI
def get_bmi(height, weight):
    try:
        # def接收的參數都是「字串」，如果要計算，記得要轉換為int
        # bmi = eval(weight) / (eval(height) / 100) ** 2
        bmi = round(eval(weight) / (eval(height) / 100) ** 2, 2)
        if bmi < 18.5:
            category = "過輕"
        elif bmi < 24:
            category = "正常"
        elif bmi < 27:
            category = "略重"
        else:
            category = "肥胖"

        # print在後端看結果
        print(bmi, category)

        return {"success": True, "bmi": bmi, "category": category}

    except Exception as e:
        return {"success": False, "bmi": None, "category": None}


# 建立第2個路由器
@app.route("/hello/<name>/<height>/<weight>")
def hello(name, height, weight):
    today = datetime.today()

    result = get_bmi(height, weight)

    # if True
    if result["success"]:
        bmi = result["bmi"]
        category = result["category"]

        return f"<h2>{today.date()}</h2> Welcome {name} BMI:{bmi:.2f} 評語：{category}"

    else:
        return "輸入不正確"


if __name__ == "__main__":
    # pass
    app.run(debug=True)
