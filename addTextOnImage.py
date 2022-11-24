from PIL import Image, ImageFont, ImageDraw
my_image = Image.open(r"C:\/Users/Mandeep/Downloads/Screenshot_3.png")
title_font = ImageFont.truetype('arial.ttf', 18)
title_text = "The Beauty of Nature"
image_editable = ImageDraw.Draw(my_image)
image_editable.text((15,15), title_text, (237, 230, 211), font=title_font)
my_image.save("result.jpg")
