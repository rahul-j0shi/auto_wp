import keyboard as k
import pyautogui as p
import time
import pandas as pd
import webbrowser as web
from urllib.parse import quote

def send_whatsapp(d_e, m_f, image_path):
    df = pd.read_excel(d_e, dtype={"Contact": str})
    name = df['Name'].values
    contact = df['Contact'].values
    files = m_f

    with open(files) as f:
        d = f.read()
    zipped = zip(name, contact)

    text_area=(767,959)
    attach_btn=(627, 957)  
    img_icon= (710,687)
    path_bar=(322,521)

    c=0

    for (a, b) in zipped:
        msg = d.format(a)
        web.open(f"https://web.whatsapp.com/send?phone={b}")
        time.sleep(10)  

        p.click(*text_area)
        p.write(msg)  
        p.click(*attach_btn)  
        p.click(*img_icon)  
        p.click(*path_bar)
        time.sleep(1)
        p.write(image_path)  
        time.sleep(2)
        p.press('enter')
        time.sleep(1)
        k.press_and_release('enter')
        time.sleep(1)
        k.press_and_release('ctrl+w')  
        time.sleep(1)
        k.press_and_release('enter')
        c+=1
        print(c, " message sent")
    print('Done')

d_e=r"C:\Users\acer\Desktop\wp\\contact.xlsx"
m_f=r"C:\Users\acer\Desktop\wp\msg.txt"
image_path=r"C:\Users\acer\Desktop\wp\holi.webp"


send_whatsapp(d_e, m_f, image_path)
