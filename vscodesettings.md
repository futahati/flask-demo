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
    - （鍵盤流）快捷鍵 `Alt + Shift + F`
    - 進入插件安裝視窗
        - 輸入 Black Formatter
        - 點擊 Install
    - 點 左下角`齒輪` → Settings
        - 輸入 format
        - 找 Editor:Default Formatter
        - 修改下拉選單為 Black Formatter

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
1. 在 GitHub 建立遠端儲存庫
    - 取得遠端儲存庫位址
        ```python
        git remote add origin 遠端儲存庫位址
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
        # (僅第一次push使用)上傳本地端儲存庫至『遠端儲存庫』
        git push -u origin master
        ```