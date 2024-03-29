import keyboard as k
import pyautogui as p
import time
import pandas as pd
import webbrowser as web
from urllib.parse import quote

def send_whatsapp(d_e, m_f, imgs_path):
    df = pd.read_excel(d_e, dtype={"Contact": str})
    name = df['Name'].values
    contact = df['Contact'].values
    files = m_f

    with open(files) as f:
        d=f.read()
    zipped=zip(name, contact)

    text_area=(767, 959)
    attach_btn=(627, 957)
    img_icon=(710, 687)
    path_bar=(322, 521)
    search_area=(144,270)
    chat_s=(157,432)

    c=0
    web.open(f"https://web.whatsapp.com")
    time.sleep(10)
    for i, (a, b) in enumerate(zipped):  
        msg=d.format(a)
        image_file=f"{imgs_path}\\{i+1}.jpg"  
        p.click(*search_area)
        time.sleep(1)
        p.write(a)
        time.sleep(1)
        p.click(*chat_s)
        p.click(*text_area)
        p.write(msg)
        time.sleep(1)
        p.click(*attach_btn)
        time.sleep(1)
        p.click(*img_icon)
        time.sleep(1)
        p.click(*path_bar)
        time.sleep(1)
        p.write(image_file)
        time.sleep(2)
        p.press('enter')
        time.sleep(3)
        k.press_and_release('enter')
        time.sleep(2)
        c+=1
        print(c, "message sent")
    print('Done')

d_e = r"C:\Users\acer\Desktop\wp\\contact.xlsx"
m_f = r"C:\Users\acer\Desktop\wp\msg.txt"
imgs_path = r"C:\Users\acer\Desktop\wp\imgs"

send_whatsapp(d_e, m_f, imgs_path)
    