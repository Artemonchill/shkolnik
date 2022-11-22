from PIL import Image, ImageDraw, ImageFont
def m(s,i)
    im = Image.open('C:/Users/user/Pictures/derevya.jpg')
    im = Image.new('RGB', (700,600), color=('#FAACAC'))
    font=ImageFont.truetype('C:/Windows/Fonts/ALGER.TTF', size=100)
    draw_text = ImageDraw.Draw(im)
    draw_text.text(
        (300,300),
        'show v programme',
        fill=('#1C0606')
        )
    im.show()
