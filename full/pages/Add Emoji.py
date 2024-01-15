from PIL import Image
import os
import streamlit

streamlit.set_page_config("Add Emoji | EmojiCord")
streamlit.write("# Add Emoji")
emojifile = streamlit.file_uploader("Upload an image to convert into an emoji", ["png", "jpg", "gif"], False)
def emojify():
    if not emojifile == None:
        emojiimage = Image.open(emojifile)
        emojiimage.thumbnail((32, 32))
        emojiimage.save(os.path.join("emojis", os.path.splitext(emojifile.name)[0] + ".gif"))
streamlit.button("Emojify!", on_click=emojify)