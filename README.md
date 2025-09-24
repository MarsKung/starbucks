# Starbucks 自動化註冊腳本

## 專案簡介
本專案用於自動化註冊 Starbucks 信箱。

## 安裝方式
1. 安裝 Python 3.8 以上版本
2. 建立虛擬環境(可選)
3. 安裝 Chrome 瀏覽器
4. 安裝依賴套件：
   ```bash
   pip install -r requirements.txt
   ```
5. 在環境變數(或`.env`)中新增`MAILSAC_KEY`
6. 如需自定義密碼，新增在環境變數(或`.env`)中新增`PASSWD`(可選)

## 使用方法
1. 至MAILSAC 取得 API-KEY 並加入環境變數
2. 執行主程式：
   ```bash
   python main.py
   ```
3. 依照程式提示操作。
