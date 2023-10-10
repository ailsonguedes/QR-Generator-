# Imports
import os
import qrcode
from flask import Flask, render_template, request, send_file, redirect, url_for
from io import BytesIO

# path of index.html
template_dir = os.path.abspath('./templates')
# setting up the app
app = Flask(__name__, template_folder=template_dir)
# secret key for app
app.config['SECRET_KEY'] = 'dafqdafqdafq'

@app.route('/', methods=['GET'])
def mainPage():
    return render_template('index.html')

# setting up decorators to select the web path and methods in use
@app.route('/', methods=['GET', 'POST'])
# index app structure and qr gen fun
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

@app.route('/docs/', methods=['GET'])
def docs():
    return render_template('docs.html')

@app.route('/contact/', methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/blog/', methods=['GET'])
def blog():
    return render_template('blog.html')

@app.route('/github/', methods=['GET'])
# func to redirect to a external link using GitHub button on page
def gitPage():
    return redirect('https://github.com/ailsonguedes/QR-Generator-/tree/main')

# Call main aplication
if __name__ == '__main__':
    app.run(debug=True)
    
