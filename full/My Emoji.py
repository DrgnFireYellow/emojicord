import os
import streamlit

streamlit.set_page_config("My Emoji | EmojiCord", page_icon="random")
streamlit.write("# My Emoji")

for emoji in os.listdir("emojis"):
    if not emoji == ".gitkeep":
        streamlit.write(os.path.splitext(emoji)[0])
        streamlit.image(os.path.join("emojis", emoji))
