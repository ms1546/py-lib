import pyocr
from PIL import Image

tools = pyocr.get_available_tools()
tool = tools[0]

path = './sample.png'
img = Image.open(path)

text = tool.image_to_string(
    img,
    lang="jpn",
    builder=pyocr.builders.TextBuilder(tesseract_layout=6)
)

print(text)
