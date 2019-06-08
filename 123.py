r=3
password="a123456"
while r>0:
	word = input("請輸入密碼")
	if password == word:
		print ("密碼登入成功")
		break
	else:
		r=r-1
		print ("密碼錯誤還有",r,"次機會")

		

