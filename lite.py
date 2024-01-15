from PIL import Image
from bottle import route, static_file, run
import os
imagesize = (32, 32)
for image in os.listdir("input"):
    emojiimage = Image.open(os.path.join("input", image))
    emojiimage.thumbnail(imagesize)
    emojiimage.save(os.path.join("output", os.path.splitext(image)[0] + ".gif"), save_all=True)
    print(f"Resizing {image}")

@route("/emojis/<path:path>")
def emoji_static(path):
    return static_file(path, "output")

@route("/")
def index():
    indexcontents = '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous"><script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script><body class="text-light bg-dark text-center"><h1>EmojiCord</h1>\nRight click an emoji and select copy image to copy the emoji'
    for emoji in os.listdir("output"):
        indexcontents += f'<br><img src="{os.path.join("emojis", emoji)}">'
    indexcontents += '</body>'
    return indexcontents
run()