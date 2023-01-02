''' program yang meminta user untuk memasukkan sebuah password. 
Jika user memasukkan password yang benar maka program menginformasikan 
bahwa user telah berhasil login. Namun, jika password salah, program akan meminta''' 


while True :
	password = input ("masukkan password :")
	ulang = input("masukkan ulang password :")
	if password == ulang :
		print ("login")
		break
	
	elif password != ulang :
		print ("masukkan password yang benar !")
		
		
	
 	