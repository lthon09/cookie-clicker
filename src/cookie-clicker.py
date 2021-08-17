import platform, os, time

def clr():
	if platform.system() == "Windows":
		os.system("cls")
	elif platform.system() == "Linux":
		os.system("clear")
	else:
		print("This program doesn't support your OS!")
		time.sleep(1.5)
		exit()

versions = ("2", "3.1", "3.2", "3.3", "3.4", "3.5")

if platform.python_version().startswith(versions):
	print("Your Python version must be above 3.5 to use this program!")
	time.sleep(1.5)
	clr()
	exit()

import subprocess, sys, tkinter, tkinter.messagebox, os.path, ctypes, json, webbrowser, os

inst1 = subprocess.check_output([sys.executable, "-m", "pip", "freeze"])
inst2 = [r.decode().split("==")[0] for r in inst1.split()]

clr()

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

window = tkinter.Tk()
window.withdraw()

if "Pillow" not in inst2:
	ask = tkinter.messagebox.askyesno(title="Cookie Clicker", message="There is a package missing for this program, do you want to install it?")
	if ask:
		os.system("pip install pillow")
	else:
		exit()

from PIL import Image, ImageTk

if not os.path.exists("cookie.png"):
	box = tkinter.messagebox.showerror(title="Cookie Clicker", message="File missing! (cookie.png)")
	time.sleep(1.5)
	exit()
if not os.path.exists("data.json"):
	box = tkinter.messagebox.showerror(title="Cookie Clicker", message="File missing! (data.json)")
	time.sleep(1.5)
	exit()

with open("data.json", "r") as f:
	cont = f.read()

if not cont:
	wr = """{
	\"data\": {
		\"cookies\": 0,
		\"upgrade\": 0
	}
}"""

	with open("data.json", "w") as f:
		f.write(wr)

with open("data.json", "r") as f:
	data = json.load(f)

costs = {
	"0": 100,
	"1": 450,
	"2": 700,
	"3": 1000,
	"4": 1500,
	"5": 2050,
	"6": 4000,
	"7": 7500,
	"8": 9000,
	"9": 15000,
	"10": 25000,
	"11": 30000,
	"12": 50000,
	"13": 85000,
	"14": 100000,
	"15": 200000
}

window.title("Cookie Clicker")
window.geometry("300x550")
window.resizable(False, False)

window.deiconify()

def callc():
	click()

def callu():
	upgrade()

opn = Image.open("cookie.png")
opn = opn.resize((200, 200), Image.ANTIALIAS)
image = ImageTk.PhotoImage(opn)
cookie = tkinter.Button(window, image=image, command=callc)
cookie.pack()

cookies = data["data"]["cookies"]

count = tkinter.Label(window, text=f"Cookies: {cookies}\n\n\n\n")
count.pack()

def click():
	new = data["data"]["cookies"] + data["data"]["upgrade"] + 1
	count.configure(text=f"Cookies: {new}\n\n\n\n")
	data["data"]["cookies"] += data["data"]["upgrade"] + 1

	with open("data.json", "w") as f:
		json.dump(data, f, indent=2)

def reset():
	count.configure(text="Cookies: 0\n\n\n\n")
	curu.configure(text="Current Upgrade: 0 | 1 Cookie(s) per Click")
	upc.configure(text="Next Upgrade: 100 Cookies")
	data["data"]["cookies"] = 0
	data["data"]["upgrade"] = 0

	with open("data.json", "w") as f:
		json.dump(data, f, indent=2)

reset = tkinter.Button(window, text="Reset", command=reset, fg="red")
reset.pack()

br = tkinter.Label(window, text="")
br.pack()

upgrade = tkinter.Button(window, text="Upgrade", command=callu, fg="darkblue")
upgrade.pack()

curup = data["data"]["upgrade"]
eachc = data["data"]["upgrade"] + 1
upgc = costs[f"{curup}"]

if data["data"]["upgrade"] < 15:
	curu = tkinter.Label(window, text=f"Current Upgrade: {curup} | {eachc} Cookie(s) per Click")
	upc = tkinter.Label(window, text=f"Next Upgrade: {upgc} Cookies")
else:
	curu = tkinter.Label(window, text=f"Current Upgrade: {curup} (MAX UPGRADE) | {eachc} Cookie(s) per Click")
	upc = tkinter.Label(window, text="Next Upgrade: ??? Cookies")

curu.pack()
upc.pack()

def upgrade():
	if data["data"]["upgrade"] < 15:
		if data["data"]["cookies"] >= costs[f"{curup}"]:
			cur = data["data"]["upgrade"]
			n1 = data["data"]["upgrade"] + 1
			n2 = data["data"]["upgrade"] + 1
			n3 = costs[f"{n1}"]
			n4 = costs[f"{cur}"]
			nc = data["data"]["cookies"] - n4
			data["data"]["upgrade"] += 1
			data["data"]["cookies"] -= n4
			count.configure(text=f"Cookies: {nc}\n\n\n\n")
			n2 += 1
			if data["data"]["upgrade"] == 14:
				curu.configure(text=f"Current Upgrade: {n1} (MAX UPGRADE) | {n2} Cookie(s) per Click")
				upc.configure(text="Next Upgrade: ??? Cookies")
			else:
				curu.configure(text=f"Current Upgrade: {n1} | {n2} Cookie(s) per Click")
				upc.configure(text=f"Next Upgrade: {n3} Cookies")

			with open("data.json", "w") as f:
				json.dump(data, f, indent=2)

def itchio():
	webbrowser.open_new_tab("https://lthon09.itch.io/cookie-clicker")

def source():
	webbrowser.open_new_tab("https://github.com/lthon09/cookie-clicker")

source = tkinter.Button(window, text="Source Code", command=source, fg="cadetblue")
source.pack(side=tkinter.RIGHT)

itchio = tkinter.Button(window, text="itch.io Page", command=itchio, fg="darkred")
itchio.pack(side=tkinter.RIGHT)

author = tkinter.Label(window, text="Cookie Clicker by lthon09", fg="red")
author.pack(side=tkinter.BOTTOM)

window.mainloop()
