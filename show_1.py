from PIL import Image, ImageDraw, ImageFont
# get an image
base = Image.open('computer_life.png')

draw = ImageDraw.Draw(base)

fillcolor = "#00ff00"
width,height = base.size
draw.text((450,40),'1',fill=fillcolor)
base.save('result.png')
