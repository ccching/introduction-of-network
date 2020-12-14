accounts = []
account = input("請輸入新帳號：")
accounts.append(account)
print("深石公司登入系統")
an = input("請輸入帳號：")
if an in accounts:
    print("歡迎進入深石系統")
else:
    print("你的帳號錯誤")
