# 設定步驟
- VScode
- GitHub

## VScode
1. 建立／新增專案Folder
    - 選單目錄 File → Open Folder...
        - `不是滑鼠右鍵 → New Folder...`
        - （鍵盤流）快捷鍵 `Ctrl + K` → `Ctrl + O`
    - (新視窗名稱)Open Folder
        1. 滑鼠右鍵 → 新增 → 資料夾 → 輸入專案名稱 → Enter
        2. 用滑鼠`點一下`剛才建立的資料夾 → 按 `Select folder`
        3. 打勾勾 → ⬜Trust the authors of all files in the parent folder 'xxxxxxx'
        4. 按 `Yes,I trust the authors`
1. 建立／新增 main.py 檔案file
    - 開啟Explorer (檔案總管)
        - 在 Explorer 裡，滑鼠右鍵 → New File...
        - 輸入 main.py → Enter
        - （鍵盤流）快捷鍵 `Ctrl + B` **快速顯示/隱藏 Explorer 視窗**
        - （鍵盤流）快捷鍵 `Ctrl + Shift + E` **進入／離開 Explorer 視窗**
1. 建立/安裝 Python 虛擬環境
    - **方式1：（直接使用VScode的建立方式）**
        - `Ctrl + Shift + P` →代表：選擇某個Python的直譯器
        - 點 or 輸入 `Python: Select Interpreter` 並點選它
        - 點 or 輸入 `Create Virtual Environment...` 代表：建立虛擬環境
            - 在選單中找路徑包含 .venv 的那一項（應該會顯示 Python 3.14.4 ('.venv': venv)），點選它
            - Quick Create venv•Create a virtual environment in workspace root
                - 快速建立 venv 步驟 (Quick Create)
                - 快速建立位於工作區根目錄 (Workspace Root) 的 Python 虛擬環境 (venv)
            - (?)Python 3.14.3 ~\AppData\Local\Programs\Python314\python.exe  Global
        - 開啟 Terminal 終端機，檢查是否建立虛擬環境成功
            - 選單目錄 Terminal → New Terminal
            - （鍵盤流）快捷鍵 ``Ctrl + Shift + ` ``
            - （鍵盤流）快捷鍵 `Ctrl+ J` or ``Ctrl + ` `` **進入/離開 Terminal 視窗**
            ```python
            # 開頭是 (.venv) 代表成功
            (.venv) C:\Users\USER\Desktop\django123\flask456\flask-pm25-project>

            # 輸入指令檢查新建立的虛擬環境
            pip lis
            ```
    - 方式2：
        - 開啟終端機 Terminal
            - 選單目錄 Terminal → New Terminal
            - （鍵盤流）快捷鍵 ``Ctrl + Shift + ` ``
        - 輸入指令
            ```python
            python -m venv venv
            ```
1. 安裝 flask 套件
    - 開啟終端機 Terminal
        - 選單目錄 Terminal → New Terminal
        - （鍵盤流）快捷鍵 ``Ctrl + Shift + ` ``
        - （鍵盤流）快捷鍵 `Ctrl+ J` or ``Ctrl + ` `` **進入/離開 Terminal 視窗**
    - 輸入指令
        ```python
        pip install flask
        ```
    - 查看是否安裝成功／虛擬環境有那些套件
        ```python
        pip list
        ```
1. 格式化文件 (Format Document)／格式化程式碼
    - （鍵盤流）快捷鍵 `Alt + Shift + F` → 進入插件安裝視窗
        - 搜尋框輸入 Black Formatter
        - 點擊 Install
    - 點 左下角`齒輪` → Settings
        - 搜尋框輸入 format
        - 找 Editor:Default Formatter
        - 修改下拉選單為 Black Formatter

1. 公共電腦下載 GitHub 專案
    > 條件：建立temp_work資料夾在桌面，使用完畢後，可直接刪除temp_work資料夾
    - 狀態1：`未`在桌面建立temp_work資料夾
        1. 打開 VS Code → File > Open Folder... → 選擇 Desktop
        2. 開啟 VS Code 的終端機（Terminal），依序輸入：
            ```python
            # 1. 建立暫存資料夾並進入
            mkdir temp_work
            cd temp_work
            
            # 2. Clone 專案並進入專案目錄
            # 請將 YOUR_USERNAME 改為你的 GitHub 帳號名稱；將 YOUR_REPOSITORY 改為你的 GitHub 專案名稱
            git clone https://github.com/ YOUR_USERNAME / YOUR_REPOSITORY .git
            cd YOUR_REPOSITORY
            
            # 3. 讓 VS Code 直接切換視窗到 fix-flow 專案
            code . -r

            # 裝環境與套件
            python -m venv venv
            venv\Scripts\activate
            pip install -r requirements.txt

            # 跑專案與修改
            # 修改了 models.py 時，必須先按 Ctrl + C 關掉伺服器（執行 makemigrations → migrate → runserver）
            python manage.py makemigrations  # 資料庫專用
            python manage.py migrate         # 資料庫專用

            # 使用條件：GitHub 有 initial_data.json 測試資料 + 其他電腦需要執行測試時，才要執行這一段程式碼
            python manage.py loaddata initial_data.json

            # 啟動本地測試伺服器，在瀏覽器輸入 [http://127.0.0.1:8000/](http://127.0.0.1:8000/) 看成果
            python manage.py runserver

            # ============================================================
            # 將測試資料打包匯出 (dumpdata)initial_data.json 的純文字檔，這份 .json 檔案可以隨著 git push 一起上傳到 GitHub
            # 使用條件：任何地方建立了測試資料，想打包供日後使用時
            python manage.py dumpdata --indent 2 > initial_data.json
            ```
        3. 使用完後，公共電腦刪除步驟：
           ```txet
           1. 關閉 VS Code
           2. Win + R → control credentialmgr → 刪除 git:[https://github.com](https://github.com) 憑證
           3. 桌面 Shift + Delete 刪除 temp_work
           ```

    - 狀態2：`已手動`在桌面建立temp_work資料夾
        1. 打開 VS Code → File > Open Folder... → 選擇 C:\Users\USER\Desktop\temp_work
        2. 開啟 VS Code 終端機（此時終端機預設路徑就在 temp_work 了），直接下指令：
            ```python
            # 請將 YOUR_USERNAME 改為你的 GitHub 帳號名稱；將 YOUR_REPOSITORY 改為你的 GitHub 專案名稱
            git clone https://github.com/ YOUR_USERNAME / YOUR_REPOSITORY .git
            cd YOUR_REPOSITORY
            code . -r
            ```

## GitHub
1. 建立git
    - 開啟終端機 Terminal
        - 選單目錄 Terminal → New Terminal
        - （鍵盤流）快捷鍵 ``Ctrl + Shift + ` ``
    - 輸入指令（初始化）
        ```python
        git init 
        ```
        - 初始化後，會產生 .git/ 隱藏資料夾 **←勿手殘刪除**
    - 建立／新增２個檔案file：`.gitignore`、`README.md`
        - 開啟 Explorer (檔案總管)在 Explorer 裡，滑鼠右鍵 → New File...
            - .gitignore（不需要追蹤及版本記錄的隱藏檔）
                - 對 `.gitignore` 點2下開啟
                - 輸入內容後，`Ctrl + S` 存檔
                    ```python
                    # 將不需追蹤的檔案或資料夾，一行寫一個
                    # 單檔案 => 檔案名稱.副檔名
                    3.txt
                    # 單副檔名 => .副檔名
                    .env
                    # 全部副檔名 => *.副檔名
                    *.db
                    *.pem
                    # 資料夾 => 資料夾名稱
                    .venv/
                    .vscode/
                    ```
            - README.md（說明文字檔）
        - （鍵盤流）快捷鍵 `Ctrl + B` **快速顯示/隱藏 Explorer**

    > 讓新建立的倉庫（git init）預設分支名稱為 main 
    - cmd 輸入指令 ```git config --global init.defaultBranch main```
    >> 將「預設初始化分支名稱」設定為 main。之後，在任何新資料夾下輸入 git init 時，Git 就會自動使用 main 而不是 master

1. 在 GitHub 建立遠端儲存庫
    - 申請
        1. 點 章魚貓圖示
        1. 點 綠色圖示 `New`
        1. (新畫面)→ Repository name* → 輸入 專案的遠端儲存庫名稱
        1. Choose visibility* 選 `Public` 公開
        1. 點 綠色圖示 `Create repository`
    - 取得遠端儲存庫位址
        ```python
        git remote add origin 遠端儲存庫位址

        # 2擇1(僅第一次push使用)上傳本地端儲存庫至『遠端儲存庫』
        git push -u origin master
        # git push -u origin main
        ```
1. 上傳 GitHub
    - 開啟終端機 Terminal
        - 選單目錄 Terminal → New Terminal
        - （鍵盤流）快捷鍵 ``Ctrl + Shift + ` ``
    - 輸入指令
        ```python
        # 連線GitHub遠端儲存庫(將本地的 Git 專案連結到遠端伺服器)
        git remote add origin 遠端儲存庫位址
        # 檢視雲端網址是否綁定成功
        git remote -v

        git status
        git add .
        git commit -m "說明文字"
        # 2擇1(僅第一次push使用)上傳本地端儲存庫至『遠端儲存庫』
        git push -u origin master
        # git push -u origin main
        ```
