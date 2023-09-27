# Imports
import os
import qrcode
from flask import Flask, render_template, request, send_file, redirect
from io import BytesIO

# path of index.html
template_dir = os.path.abspath('./templates')
# setting up the app
app = Flask(__name__, template_folder=template_dir)
# secret key for app
app.config['SECRET_KEY'] = 'dafqdafqdafq'
# setting up decorators to select the web path and methods in use
@app.route('/', methods=['GET', 'POST'])
# index app structure
def index():
    if request.method == 'POST':
        data = request.form.get('data')
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        
        qr_code_io = BytesIO()
        img.save(qr_code_io)
        
        qr_code_io.seek(0)
    
        return send_file(
            qr_code_io,
            mimetype="image/png",
            as_attachment=True,
            download_name="qrcode.png",
        )
    
    return render_template('index.html')

@app.route('/github')
def gitPage():
    return redirect('https://github.com/ailsonguedes/QR-Generator-/tree/main')

if __name__ == '__main__':
    app.run(debug=True)