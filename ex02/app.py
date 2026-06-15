from flask import Flask, render_template, request, json

from cipher.transposition import TranspositionCipher

app = Flask(__name__)

# 2. ĐÃ SỬA: Khởi tạo sẵn các đối tượng cipher ở đầu file để dùng chung

transposition_cipher = TranspositionCipher()


# ==================== ROUTER FOR HTML PAGES ====================
@app.route("/")
def home():
    return render_template('index.html')



@app.route("/transposition")
def transposition():
    return render_template('transposition.html')



# ==================== TRANSPOSITION CIPHER ====================
@app.route('/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    encrypted_text = transposition_cipher.encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route('/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    decrypted_text = transposition_cipher.decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"


# ==================== MAIN FUNCTION ====================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)