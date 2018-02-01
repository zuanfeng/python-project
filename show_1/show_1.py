from PIL import Image, ImageDraw, ImageFont
# get an image
base = Image.open('computer_life.png')
draw = ImageDraw.Draw(base)

# color
fillcolor = "#00ff00"
width,height = base.size

# draw
draw.text((450,40),'1',fill=fillcolor)

# save
base.save('result.png')
