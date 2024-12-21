from tkinter import *
from tkinter import ttk
import os as os
import subprocess

listcfgs = []

directory = os.fsencode("/usr/share/nbfc/configs/")

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    #print(filename)
    listcfgs.append(filename)

root = Tk()
root.title("NBFC GUI")
root.geometry("250x300")
root.resizable(False,False)

#ttk.Style().configure("TCombobox", padding=5, relief="flat")

Cfgs = ttk.Combobox(root, values=listcfgs)
Cfgs.pack(pady=20)

def app():
    if Cfgs.get() != "":
        subprocess.run(['sudo','nbfc', 'config','-a',Cfgs.get()])

def auto():
    result = subprocess.run(['nbfc','get-model-name'], stdout=subprocess.PIPE)
    strres = str(result.stdout)
    strres = strres.replace("b'", "")
    strres = strres.replace("\\n'", "")
    strres = strres + ".json"
    for i in range(0,len(listcfgs)):
        if listcfgs[i] == strres:
            Cfgs.current(i)

    #subprocess.run(['sudo','nbfc', 'config','-a',strres])
    #print(strres)

app = ttk.Button(root, text='Apply', command=app)
app.pack()

aut = ttk.Button(root, text='Auto Choose', command=auto)
aut.pack(pady=20)

def rest():
    subprocess.run(['sudo', 'nbfc', 'restart'])

def stop():
    subprocess.run(['sudo', 'nbfc', 'stop'])

res = ttk.Button(root, text='Restart', command=rest)
res.pack(pady=20)

stp = ttk.Button(root, text='Stop', command=stop)
stp.pack()

#/usr/share/nbfc/configs/
root.mainloop()