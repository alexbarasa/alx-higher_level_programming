#!/usr/bin/python3
"""
Text Indentation Module:
Indents text properly.
Useful for formatting text blocks.
"""


def text_indentation(text):
    """
    Indent text properly.

    Args:
        text (str): The text to be indented.

    Raises:
        TypeError: If text is not a string.
    """
    # Check if text is a string, otherwise raise a TypeError
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Replace punctuation marks with new lines followed by two new lines
    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')

    # Split the text into lines, strip each line of
    # leading and trailing spaces,
    # then join them back together with new lines
    indented_text = "\n".join([line.strip() for line in text.split("\n")])

    # Print the indented text without adding any space at the end
    print(indented_text, end="")
