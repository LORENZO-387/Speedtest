# pip install speedtest-cli

from tkinter import *
from speedtest import Speedtest

print ("""
.____    ________ _____________________ _______  __________________  ________    _______________ 
|    |   \_____  \\______   \_   _____/ \      \ \____    /\_____  \ \_____  \  /  __  \______  \

|    |    /   |   \|       _/|    __)_  /   |   \  /     /  /   |   \  _(__  <  >      <   /    /
|    |___/    |    \    |   \|        \/    |    \/     /_ /    |    \/       \/   --   \ /    / 
|_______ \_______  /____|_  /_______  /\____|__  /_______ \\_______   /______  /\______  //____/  
        \/       \/       \/        \/         \/        \/        \/       \/        \/       
        
                 DOUBLE CLIK VERRY SLOWLY AND WHAIT PLEASE

        """)

def update_text():
    speed_test = Speedtest()
    download = speed_test.download()
    upload = speed_test.upload()
    download_speed = round(download / (10**6), 2)
    upload_speed = round(upload / (10**6), 2)
    down_label.config(text= "Download Speed - " + str(download_speed) + "Mbps") 
    up_label.config(text= "Upload Speed - " + str(upload_speed) + "Mbps") 


root = Tk()
root.title("Internet Speed Tracker")
root.geometry('300x300')
button = Button(root, text="Get Speed ((By LORENZO387))", width=30, command=update_text)
button.pack()
down_label = Label(root, text="")
down_label.pack()
up_label = Label(root, text="")
up_label.pack()

root.mainloop()
