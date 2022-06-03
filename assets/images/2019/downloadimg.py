import requests

image_url = 'http://static.zybuluo.com/pluto-the-lost/rmg5xgrpnj9an17h1l5vx6fk/image.png'
img_data = requests.get(image_url).content
with open('test.png', 'wb') as handler:
    handler.write(img_data)