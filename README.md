# 專案指引

目前 Python 專案之「開發環境」，其平台架構之主要組件如下：

- 編輯器（Editor）／整合式開發工具（IDE）： Neovim 0.8x / VS Code
- Language Server： Pyright
- Linter：PyLint
- Formatter：autopep8

各主要組件，為提供豐富之功能，以應各種需求，故而多有自個「專用」之
設定檔，如：

- VS Code 編輯器：使用 settings.json
- Pyright (Python Language Server)：使用 pyright.json
- PyLint (Python Linter)： .pylintrc

另外，Python 直譯器版本管理器／套件管理器／虛擬環境（如：pyenv, pip,
pipenv, virtualenv, ....），亦是 Python 軟體專案需進行管理之工作事項。

所以，採用 Python 開始軟體之專案，其初始之「建置作業」，便有許多細碎之事
得要完成。否則，因為「環境設定」不全；乃至有誤，將導致程式編碼時，編輯器
的 Auto-completion, Module Import 這些工作無法正常執行；而檢查程式碼的
Linter 更是會發出許多警示；更別談完成 Build 作業後的程式，可正常執行。

目前正逐漸蔚為風潮的 Poetry ，有人認為正是為解決上述問題的【解決方案】。
事實是否真是如此？我的 Python 專案，能否導入引用？！

本專案之啟動，便是用於驗證：【我的 Python 專案，能否採用 Poetry 作為：

（1）Python 套件管理器：取代原用之 pipenv / Pipfile / requirements.txt；

（2）Pyright Language Server 設定檔：取代原用之 pyright.json

（3）PyLint Linter 設定檔：取代原用之 .pylintrc

若是幸運，上述之問題，皆得正面之結果，則本專案將為：「建置 Python 專案時，
所參考之『Python 專案模版』」。
