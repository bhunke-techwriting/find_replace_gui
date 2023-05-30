import re
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

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
def apply_substitutions():
    # Get the text from the input box
    text = input_box.get('1.0', tk.END)

    # Apply the regular expressions and replacements to the text
    for pattern, replacement in patterns:
        text = re.sub(pattern, replacement, text)

    # Update the output box with the modified text
    output_box.delete('1.0', tk.END)
    output_box.insert('1.0', text)

# Set up the GUI
root = tk.Tk()
root.title('HTML Substitution Tool')

# Create the input box for the user to paste in HTML
input_box = ScrolledText(root, width=80, height=20, font=('Arial', 12))
input_box.pack(padx=10, pady=10)

# Create the button to apply the substitutions
button = tk.Button(root, text='Apply Substitutions', command=apply_substitutions)
button.pack(pady=10)

# Create the output box to display the modified HTML
output_box = ScrolledText(root, width=80, height=20, font=('Arial', 12))
output_box.pack(padx=10, pady=10)

# Start the GUI event loop
root.mainloop()