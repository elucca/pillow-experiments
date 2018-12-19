from PIL import Image, ImageDraw

BIG_CARD_RES = (1269, 2205)
MED_CARD_RES = (508, 883)

def draw():
    image = Image.open("images/test.png")
    d = ImageDraw.Draw(image)
    d.text((10,10), "Hello World", fill=(255,255,0))

    image.save("images/result.png")