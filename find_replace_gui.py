import re
import streamlit as st
import pyperclip

# Define the regular expressions to search for and their replacements
patterns = [
    (r'<p.*?>', '<p style="margin: 20px 0;line-height: 1.5;">'),
    (r'<li.*?>', '<li><p style="margin: 20px 0;line-height: 1.5;">'),
    (r'</li>', '</p></li>'),
    (r'</?span.*?>', ''),
    (r'<h1.*?>', '<h1 style="margin: 20px 0;line-height: 1.5;font-size: 30px;font-weight: 400;">'),
    (r'<h2.*?>', '<h2 style="margin: 20px 0;line-height: 1.5;font-size: 24px;font-weight: 400;">'),
    (r'<h3.*?>', '<h3 style="margin: 20px 0;line-height: 1.5;font-size: 20px;font-weight: 400;">'),
    (r'<h4.*?>', '<h4 style="margin: 20px 0;line-height: 1.5;font-size: 18px;font-weight: 700;">'),
    (r'<table.*?>', '<table border="1" class="table-bordered" style=”border-collapse:collapse;”>'),
    (r'<img ', '<img class="img-responsive fr-fic fr-dii" ')
]

# Define the function to apply the substitutions
def apply_substitutions(text):
    # Apply the regular expressions and replacements to the text
    for pattern, replacement in patterns:
        text = re.sub(pattern, replacement, text)

    return text

# Set up the Streamlit app
def main():
    st.title('HTML Substitution Tool')

    # Create the input box for the user to paste in HTML
    input_text = st.text_area('Input HTML', height=200)

    # Create the button to apply the substitutions
    if st.button('Apply Substitutions'):
        output_text = apply_substitutions(input_text)
        # Display the modified HTML
        st.text_area('Modified HTML', value=output_text, height=200)

        # Create a button to copy the modified HTML
        if st.button('Copy Modified HTML'):
            pyperclip.copy(output_text)
            st.success('Modified HTML copied to the clipboard!')

if __name__ == '__main__':
    main()
