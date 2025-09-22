from flask import Flask, request, render_template

app = Flask(__name__)

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift  # reverse shift
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

@app.route("/", methods=["GET", "POST"])
def home():
    encrypted = decrypted = ""
    if request.method == "POST":
        message = request.form["message"]
        shift = int(request.form["shift"])
        action = request.form["action"]

        if action == "Encrypt":
            encrypted = caesar_cipher(message, shift, 'encrypt')
        elif action == "Decrypt":
            decrypted = caesar_cipher(message, shift, 'decrypt')

    return render_template("index.html", encrypted=encrypted, decrypted=decrypted)

if __name__ == "__main__":
    app.run(debug=True)
