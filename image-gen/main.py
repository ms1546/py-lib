ccccfrom PIL import Image, ImageDraw, ImageFont

width, height = 800, 400
background_color = (0, 0, 0)  # 黒

image = Image.new("RGB", (width, height), color=background_color)

draw = ImageDraw.Draw(image)

text = "Hello, World!"
text_color = (255, 255, 255) # 白

font = ImageFont.load_default()

draw.text((width / 2, height / 2), text, fill=text_color, font=font, anchor="mm")

image.save("dist_path/hello.png")
