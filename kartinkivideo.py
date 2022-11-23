from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import *
import os
directory = 'C:\Users\student\Desktop\работы\132'
files = os.listdir(directory)
images = list(filter(lambda x: x.endswith('.jpg'), files))
clips = [ImageClip(m).set-duration(2) for m in images]

final_clip = concatenate_videoclips(clips, method='compose')
final_clip.write_videofile('test.mp4', fps=24)


def m(s, i):
    im = Image.new('RGB', (1000, 800), color=('#FAACAC'))
    font = ImageFont.truetype('C:/Windows/Fonts/ARIAL.TTF', size=25)
    draw_text = ImageDraw.Draw(im)
    draw_text.text(
        (500, 400),
        s,
        font=font,
        fill='#1C0606')
    im.show()
    im.save(str(i)+"qeqeqe.png")


s = ['красиво', 'очень красиво', 'ну такое', 'что-нибудь',
     'lf', 'да', 'нет', 'привет', 'ну да', 'ага']
print('Что хочешь?\n 1) Видео\n 2) Картинки')
a = input()
if a == 1:
    video()
elif a == 2:
    for i in range(10):
    m(s[i], i)
else:
    print('Выбери нормально')
