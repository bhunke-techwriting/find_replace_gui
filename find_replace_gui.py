import re
import streamlit as st

# Define the regular expressions to search for and their replacements
patterns = [
    (r'<p.*?>', '<p style="margin: 20px 0;line-height: 1.5;">'),
    #(r'<li.*?>', '<li><p style="margin: 20px 0;line-height: 1.5;">'),
    #(r'</li>', '</p></li>'),
    (r'</?span.*?>', ''),
    (r'<h1.*?>', '<h1 style="margin: 20px 0;line-height: 1.5;font-size: 30px;font-weight: 400;">'),
    (r'<h2.*?>', '<h2 style="margin: 20px 0;line-height: 1.5;font-size: 24px;font-weight: 400;">'),
    (r'<h3.*?>', '<h3 style="margin: 20px 0;line-height: 1.5;font-size: 20px;font-weight: 400;">'),
    (r'<h4.*?>', '<h4 style="margin: 20px 0;line-height: 1.5;font-size: 18px;font-weight: 700;">'),
    (r'<table.*?>', '<table border="1" class="table-bordered" style=”border-collapse:collapse;”>'),
    (r'<img ', '<img class="img-responsive fr-fic fr-dii" '),
    (r'<p style="margin: 20px 0;line-height: 1.5;">&nbsp;</p>', ''),
    (r'<p style="margin: 20px 0;line-height: 1.5;"><p style="margin: 20px 0;line-height: 1.5;">', '<p style="margin: 20px 0;line-height: 1.5;">'),
    (r'</p></p>', '</p>')
]

# Define the function to apply the substitutions
def apply_substitutions():
    # Get the text from the input box
    text = input_box.text_area('Input HTML', height=200)

    # Apply the <strong> substitution for <span> tags
    text = re.sub(r'<span style="font-weight:700">(.*?)</span>', r'<strong>\1</strong>', text)

    # Apply the <i> substitution for <span> tags
    text = re.sub(r'<span style="font-style:italic">(.*?)</span>', r'<i>\1</i>', text)

    # Add paragraph tag to list items
    text = re.sub(r'<li.*?>(.*?)</li>', r'<li><p style="margin: 20px 0;line-height: 1.5;">\1</p></li>', text)

    # Apply the regular expressions and replacements to the text
    for pattern, replacement in patterns:
        text = re.sub(pattern, replacement, text)

    # Display the modified HTML
    st.text_area('Modified HTML', value=text, height=200)

# Set up the Streamlit app
st.title('HTML Substitution Tool')

# Create the button to apply the substitutions
st.button('Apply Substitutions', on_click=apply_substitutions)

# Create the input box for the user to paste in HTML
input_box = st.empty()
