import streamlit as st
from pathlib import Path
import os
import glob
from PIL import Image

# Directory where your images are stored
image_path: Path = "c:/Users/rauldiaz/src/streamlit_test/images"
image_directory: str = image_path.as_posix()

def find_image(filename):
    # Search for the image in the directory tree
    for filepath in glob.iglob(f'{image_directory}/**/{filename}', recursive=True):
        return filepath
    return None

def main():
    st.title("Image Viewer")

    # User input for filename
    filename = st.text_input("Enter the name of the image file")

    if filename:
        # Find the image in the directory
        image_path = find_image(filename)

        if image_path and os.path.isfile(image_path):
            # Display the image
            image = Image.open(image_path)
            st.image(image, caption=f"Displaying: {filename}")
        else:
            st.warning("Image not found. Please check the filename.")

        # Buttons for next or quit
        col1, col2 = st.columns(2)
        with col1:
            next = st.button("Next")
        with col2:
            quit = st.button("Quit")

        if next:
            # Just clear the current state and wait for new input
            st.experimental_rerun()

        if quit:
            # Stop the Streamlit server
            st.stop()

if __name__ == "__main__":
    main()
