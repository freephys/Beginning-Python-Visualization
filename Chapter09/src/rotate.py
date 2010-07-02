from PIL import Image
# collage of rotated and rorated and expanded image
img = Image.new('RGB', (200, 300), (0, 0, 255))
img30 = img.rotate(30)
img30e = img.rotate(30, expand = True)

delta = 5
img_both = Image.new('RGB', (img30.size[0]+img30e.size[0]+delta, \
    img30e.size[1]), (255, 255, 255))

img_both.paste(img30, (0, (img_both.size[1]-img30.size[1])/2))
img_both.paste(img30e, (delta+img30.size[0], 0))
img_both.show()
