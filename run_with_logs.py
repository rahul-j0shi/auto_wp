import keyboard as k
import pyautogui as p
import time
import pandas as pd
import webbrowser as web
from urllib.parse import quote
import logging
import os
from datetime import datetime

def setup_logging():
    logs_dir=r"C:\Users\SHANTANU\Desktop\wp\logs"
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
    today_dir=os.path.join(logs_dir,datetime.now().strftime('%Y-%m-%d'))
    if not os.path.exists(today_dir):
        os.makedirs(today_dir)
        
    log_file_name=datetime.now().strftime('%H-%M-%S')+'.log'
    log_file_path=os.path.join(today_dir,log_file_name)
    
    logging.basicConfig(filename=log_file_path,level=logging.INFO,format='%(asctime)s-%(levelname)s-%(message)s')
    logging.info("Logging started")



def send_whatsapp(d_e, m_f,imgs_path):
    setup_logging()
    logging.info("WhatsApp message sending script started")
    
    df=pd.read_excel(d_e, dtype={"Contact": str})
    zipped = zip(df['Name'].values, df['Contact'].values)

    web.open("https://web.whatsapp.com")
    wait_for_login()
    
    for i, (name, contact) in enumerate(zipped):  
        with open(m_f) as f:
            msg = f.read().format(name)
        #image_file=f"{imgs_path}\\{i+1}.jpg"
        
        p.click(144, 270)  
        time.sleep(1)
        p.write(name)
        time.sleep(1)
        p.click(157, 432)  
        p.click(767, 959)  
        p.write(msg)
        time.sleep(2)
        #p.click(627, 957)  
        #time.sleep(1)
        #p.click(710, 687)  
        #time.sleep(1)
        #p.click(322, 521)  
        #time.sleep(1)
        #p.write(image_file)
        #time.sleep(2)
        #p.press('enter')
        #time.sleep(3)
        k.press_and_release('enter')
        time.sleep(2)
        
        logging.info(f"Message sent to {name} ({contact}).")
    
    logging.info("All messages sent. Script completed.")

d_e=r"C:\Users\SHANTANU\Desktop\wp\\contact.xlsx"
m_f=r"C:\Users\SHANTANU\Desktop\wp\msg.txt"
imgs_path=r"C:\Users\SHANTANU\Desktop\wp\imgs"

send_whatsapp(d_e,m_f,imgs_path)
