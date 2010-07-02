# text annotation
from PIL import Image, ImageDraw, ImageFont
from matplotlib import font_manager
wid = 1200

D = wid/24

font_str = font_manager.findfont('Vera')
ttf = ImageFont.truetype(font_str, 72)

img1 = Image.new('L', (wid, wid), 255)
draw1 = ImageDraw.Draw(img1)
draw1.ellipse((D, D, wid-D, wid-D), fill=128) 
draw1.text((wid/2, wid/2), 'A long string', font=ttf)

s = 'A long string'
img2 = Image.new('L', (wid, wid), 255)
draw2 = ImageDraw.Draw(img2)
width, height = draw2.textsize(s, font=ttf)
draw2.ellipse((D, D, wid-D, wid-D), fill=128) 
draw2.text((wid/2-width/2, wid/2-height/2), 'A long string', font=ttf)

delta = D
img = Image.new('L', ((wid+D)*2+delta, wid+D), 255)
img.paste(img1, (0, 0))
img.paste(img2, (delta+wid+D, 0))
img.show()



