import streamlit
import os
streamlit.set_page_config("Emoji Collection | EmojiCord", page_icon="random")
streamlit.write("# Emoji Collection")
if not os.path.exists("EmojiCollection.txt"):
    with open("EmojiCollection.txt", "w"):
        pass

url = streamlit.text_input("Enter the url of an emoji", placeholder="https://example.com/epicemoji.png")

def addemoji():
    with open("EmojiCollection.txt", "a") as emojicollectionfile:
        emojicollectionfile.write("\n" + url)

streamlit.button("Add emoji", on_click=addemoji)

with open("EmojiCollection.txt") as emojicollectionfile:
    for emoji in emojicollectionfile.readlines():
        if emoji != "":
            streamlit.image(emoji.strip())