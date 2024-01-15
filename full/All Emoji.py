import os
import streamlit

streamlit.set_page_config("All Emoji | EmojiCord")
streamlit.write("# All Emoji")

for emoji in os.listdir("emojis"):
    if not emoji == ".gitkeep":
        streamlit.write(os.path.splitext(emoji)[0])
        streamlit.image(os.path.join("emojis", emoji))
