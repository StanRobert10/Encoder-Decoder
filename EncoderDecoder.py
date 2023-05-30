import sys
import pyperclip
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QRadioButton, \
    QGroupBox, QHBoxLayout

# The alphabet used for the Caesar Cipher
ALPHABET = "abcdefghijklmnopqrstuvwxyz0123456789 !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"


def caesar_cipher(txt, shift, encode_decode):
    """
    Applies the Caesar Cipher to the given text.

    Args:
        txt (str): The text to be encoded or decoded.
        shift (int): The shift value for the cipher.
        encode_decode (bool): If True, the text will be encoded. If False, the text will be decoded.

    Returns:
        str: The resulting text after applying the Caesar Cipher.
    """

    if not encode_decode:
        shift = -shift

    result = ''
    for letter in txt:
        if letter.lower() in ALPHABET:
            index = (ALPHABET.index(letter.lower()) + shift) % len(ALPHABET)
            result += ALPHABET[index]
        else:
            result += letter

    return result


def validate_input():
    """
    Validates the user input and performs the encoding or decoding operation.
    """

    direction = ''

    if encode_button.isChecked():
        direction = 'encode'
        encode_decode = True

    if decode_button.isChecked():
        direction = 'decode'
        encode_decode = False

    if direction:
        text = text_entry.text()
        password = shift_entry.text()

        shift = calculate_shift(password)

        result = caesar_cipher(text, shift, encode_decode)
        result_display.setText(result)


def calculate_shift(password):
    """
    Calculates the shift value based on the given password.

    Args:
        password (str): The password to calculate the shift value from.

    Returns:
        int: The calculated shift value.
    """

    shift = sum(ord(char) for char in password)
    return shift


def copy_to_clipboard():
    """
    Copies the result to the clipboard.
    """

    pyperclip.copy(result_display.text())


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Encoder Decoder')

# Group box for selecting the direction (encode/decode)
direction_groupbox = QGroupBox('Select direction:')
direction_groupbox.setStyleSheet("color: #50fa7b;")

encode_button = QRadioButton('Encode')
decode_button = QRadioButton('Decode')
encode_button.setChecked(False)
decode_button.setChecked(False)

text_label = QLabel('Type your message:')
text_label.setStyleSheet("color: #f8f8f2;")
text_entry = QLineEdit()

shift_label = QLabel('Type the password:')
shift_label.setStyleSheet("color: #f8f8f2;")
shift_entry = QLineEdit()

submit_button = QPushButton('Submit')
submit_button.clicked.connect(validate_input)

result_label = QLabel('Result:')
result_label.setStyleSheet("color: #f8f8f2;")
result_display = QLabel()

copy_button = QPushButton('Copy to Clipboard')
copy_button.clicked.connect(copy_to_clipboard)

layout = QGridLayout()
layout.addWidget(direction_groupbox, 0, 0, 1, 2)
layout.addWidget(text_label, 1, 0)
layout.addWidget(text_entry, 1, 1)
layout.addWidget(shift_label, 2, 0)
layout.addWidget(shift_entry, 2, 1)
layout.addWidget(submit_button, 3, 0, 1, 2)
layout.addWidget(result_label, 4, 0)
layout.addWidget(result_display, 4, 1)
layout.addWidget(copy_button, 5, 0, 1, 2)

direction_layout = QHBoxLayout()
direction_layout.addWidget(encode_button)
direction_layout.addWidget(decode_button)
direction_groupbox.setLayout(direction_layout)

# Set styles for the window and buttons
window.setStyleSheet("""
    background-color: #282a36;
    color: #f8f8f2;
    font-size: 14px;
    font-family: Arial;
""")

submit_button.setStyleSheet("""
    background-color: #50fa7b;
    color: #282a36;
    font-size: 14px;
    padding: 8px 16px;
    border: none;
""")

copy_button.setStyleSheet("""
    background-color: #50fa7b;
    color: #282a36;
    font-size: 14px;
    padding: 8px 16px;
    border: none;
""")

window.setLayout(layout)
window.setGeometry(300, 300, 500, 250)
window.show()

sys.exit(app.exec())
