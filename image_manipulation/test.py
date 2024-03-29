from PIL import Image,ImageDraw,ImageFont

def add_text_to_image(image_path,text,pos,font_path="arial.ttf",font_size=20):
    image=Image.open(image_path)
    draw=ImageDraw.Draw(image)
    try:
        font=ImageFont.truetype(font_path, font_size)
    except IOError:
        font=ImageFont.load_default()
    
    draw.text(pos,text,font=font,fill=(0,0,0))
    
    image.save('C:\\Users\\acer\\Desktop\\wp\\imgs\\sample.png')
    image.show()


image_path='C:\\Users\\acer\\Desktop\\wp\\imgs\\template.png'
text='sample text'

x,y=1150,404
xtl,ytl=530,242

pos=(x-xtl, y-ytl)  
font_path='arial.ttf'  
font_size=20

add_text_to_image(image_path,text,pos,font_path,font_size)
