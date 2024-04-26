import re
import streamlit as st

# Define the regular expressions to search for and their replacements
patterns = [
    (r'<p>', '<p style="margin: 20px 0;line-height: 1.5;">'),
    (r'<p .*?>', '<p style="margin: 20px 0;line-height: 1.5;">'),
    (r'<li.*?>', '<li style="margin: 10px 0;line-height: 1.5;">'),
    #(r'</li>', '</p></li>'),
    (r'</?span.*?>', ''),
    (r'<h1.*?>', '<h1 style="margin: 20px 0;line-height: 1.5;font-size: 30px;font-weight: 400;">'),
    (r'<h2.*?>', '<h2 style="margin: 20px 0;line-height: 1.5;font-size: 24px;font-weight: 400;">'),
    (r'<h3.*?>', '<h3 style="margin: 20px 0;line-height: 1.5;font-size: 20px;font-weight: 400;">'),
    (r'<h4.*?>', '<h4 style="margin: 20px 0;line-height: 1.5;font-size: 18px;font-weight: 700;">'),
    (r'<table.*?>', '<table border="1" class="table-bordered" style="word-wrap: break-word;margin: 20px 0;border-collapse:collapse;">'),
    (r'<img ', '<img class="img-responsive fr-fic fr-dii" style="max-width:100%;" '),
    (r'<p style="margin: 20px 0;line-height: 1.5;">&nbsp;</p>', ''),
    (r'<p style="margin: 20px 0;line-height: 1.5;"><p style="margin: 20px 0;line-height: 1.5;">', '<p style="margin: 20px 0;line-height: 1.5;">'),
    (r'<div class="alert alert-info".*?>', '<div class="alert alert-info" style="margin: 20px 0;line-height: 1.5;padding: 15px;margin-bottom: 20px;border: 1px solid transparent;border-radius: 4px;background-color: #d9edf7;border-color: #bce8f1;">'),
    (r'</p></p>', '</p>')
]

# Define the function to apply the substitutions
def apply_substitutions(input_text):
    # Apply the <strong> substitution for <span> tags
    text = re.sub(r'<span style="font-weight:700">(.*?)</span>', r'<strong>\1</strong>', input_text)

    # Apply the <i> substitution for <span> tags
    text = re.sub(r'<span style="font-style:italic">(.*?)</span>', r'<i>\1</i>', text)

    # Add paragraph tag to ordered list items
    # text = re.sub(r'<li(?!(?:[^<]*<\/ul>|[^<]*<\/ol>))>(.*?)</li>', r'<li><p style="margin: 20px 0;line-height: 1.5;">\1</p></li>', text)

    # Apply the regular expressions and replacements to the text
    for pattern, replacement in patterns:
        text = re.sub(pattern, replacement, text)

    # Substitute paragraph tags within tables with empty string
    text = re.sub(r'<table(?:.|\n)*?>.*?<p.*?>.*?</p>(?:.|\n)*?</table>', lambda match: match.group(0).replace('</p>\n<p.*?>', '<br><br>').replace('<p.*?>', '').replace('</p>', ''), text)
    return text

# Define the function to apply the substitutions
def apply_substitutions(input_text):
    # Split the input text into lines
    lines = input_text.splitlines()

    # Check the first line
    if lines and lines[0] == '<p style="margin: 0px 0;line-height: 0;">&nbsp;</p>':
        return input_text  # If the first line matches, do nothing

    elif lines and lines[0] == '<p style="margin: 20px 0;line-height: 1.5;">&nbsp;</p>':
        # Replace the first line with the desired substitution
        lines[0] = '<p style="margin: 0px 0;line-height: 0;">&nbsp;</p>'

    else:
        # If the first line doesn't match any condition, insert a new line at the beginning
        lines.insert(0, '<p style="margin: 0px 0;line-height: 0;">&nbsp;</p>')

    # Reassemble the lines into a single string
    text = '\n'.join(lines)

    # Apply the <strong> substitution for <span> tags
    text = re.sub(r'<span style="font-weight:700">(.*?)</span>', r'<strong>\1</strong>', text)

    # Apply the <i> substitution for <span> tags
    text = re.sub(r'<span style="font-style:italic">(.*?)</span>', r'<i>\1</i>', text)

    # Apply the regular expressions and replacements to the text
    for pattern, replacement in patterns:
        text = re.sub(pattern, replacement, text)

    return text

 # Identify paragraph tags inside tables and set different margin style

    text = re.sub(r'<table(?:.|\n)*?>.*?<p.*?>.*?</p>(?:.|\n)*?</table>', lambda match: match.group(0).replace('<p.*?>', '<p style="margin: 5px 0;line-height: 1.5;" '), text)
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

if __name__ == "__main__":
    main()
