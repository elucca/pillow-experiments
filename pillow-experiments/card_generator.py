from PIL import Image, ImageDraw, ImageFont


BIG_CARD_RES = (1269, 2205)
MED_CARD_RES = (508, 883)

def draw():
    image = Image.open("assets/templates/card_base_1.png")
    font = ImageFont.truetype("assets/fonts/Oswald-Bold.ttf", 94)

    d = ImageDraw.Draw(image)
    d.text((10,10), "Hello World", fill=(255,255,0), font=font)

    image.save("assets/result.png")