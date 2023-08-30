import os,random,datetime
from datetime import datetime

class Menu:
	def __init__(self):
		self.kontol=[]
	
	def register(self):
		print("""
   __    ____  _  _  _  _  ____  ___  _   _  ____ 
  /__\  (  _ \( )/ )( \( )(_  _)/ __)( )_( )(_  _)
 /(__)\  )   / )  (  )  (  _)(_( (_-. ) _ (   )(  
(__)(__)(_)\_)(_)\_)(_)\_)(____)\___/(_) (_) (__) 
		""")
		print(" Masukan Nama Untuk Daftar")
		nama = input(" Masukan Nama : ")
		open("data/nama","w").write(nama)
		open("data/yen","w").write("5")
		self.menu()
		
	def menu(self):
		try:
			nama = open("data/nama","r").read()
			yen = open("data/yen","r").read()
		except:
			self.register()
		os.system("clear")
		print("""
   __    ____  _  _  _  _  ____  ___  _   _  ____ 
  /__\  (  _ \( )/ )( \( )(_  _)/ __)( )_( )(_  _)
 /(__)\  )   / )  (  )  (  _)(_( (_-. ) _ (   )(  
(__)(__)(_)\_)(_)\_)(_)\_)(____)\___/(_) (_) (__) 
		""")
		print(f" Nama : {nama}")
		print(f" Yen : {yen}¥")
		print("")
		print(" 1. Gacha Arknight")
		print(" 2. Daily Yen 10¥")
		print(" 3. Cek Inventory")
		ask = input("\n Pilih : ")
		if ask == "1":
			Gacha().main()
		elif ask =="2":
			self.daily()
		elif ask =="3":
			self.inven()
		else:
			print(" Pilih Yang Ada Di Menu")
			input("\n Tekan Enter Kembali Ke Menu")
			self.menu()
		
	def inven(self):
		file = open("data/inventory","r").read().splitlines()
		for data in file:
			data = data.split(",")
			print(f"""\n ID    : {data[0]}\n Nama  : {data[0]}\n Stars : {data[1]}★""")
		input("\n Tekan Enter Kembali Ke Menu")
		self.menu()
		
	def daily(self):
		previous = open("data/daily","r").read()
		if previous =="":
			previous = str(datetime.now()).split(".")[0].replace("-","").replace(" ","").replace(":","")
			open("data/daily","w").write(previous)
		now = str(datetime.now()).split(".")[0].replace("-","").replace(" ","").replace(":","")
		if int(now)-int(previous) > 1000000:
			open("data/daily","w").write(now)
			ask = input(" Ketik 'yen' Untuk Claim Daily : ")
			if ask.lower() == "yen":
				yen = open("data/yen","r").read()
				open("data/yen","w").write(str(int(yen)+10))
				print(" Berhasil Mengklaim Yen")
			input("\n Tekan Enter Kembali Ke Menu")
			self.menu()
		else:
			print(" Kamu Sudah Daily Hari Ini")
			input("\n Tekan Enter Kembali Ke Menu")
			self.menu()
	
class Gacha:
	def __init__(self):
		self.file = open("assets/arknight","r").read().splitlines()
		
	def main(self):
		total = input(" Jumlah Gacha : ")
		yen = open("data/yen","r").read()
		if int(yen)-int(total)*5 < 0:
			print(" Yen Kamu Tidak Mencukupi Untuk Gacha")
			input("\n Tekan Enter Kembali Ke Menu")
			Menu().menu()
		for z in range(int(total)):
			gacha = self.arkn_gacha()
			user = gacha.split(",")
			saldo = open("data/yen","r").read()
			open("data/yen","w").write(str(int(saldo)-5))
			print(f"""\n ID    : {user[0]}\n Nama  : {user[1]}\n Stars : {user[2]}★""")
			open("data/inventory","a").write(str(gacha)+"\n")
			
	def arkn_gacha(self):
		rate = {
			"1": 80.8,
			"2": 92.4,
			"3": 28.8,
			"4": 8.2,
			"5": 1.2,
			"6": 0.01
		}
		data = []
		star = random.choices(list(rate.keys()), weights=list(rate.values()))[0]
		for chara in self.file:
			if star in chara.split(",")[1]:
				data.append(chara)
		return random.choice(data)
			
Menu().menu()