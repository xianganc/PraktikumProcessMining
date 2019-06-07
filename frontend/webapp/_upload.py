import os
from flask import Flask, request, url_for, send_from_directory, flash, render_template
from werkzeug import secure_filename

ALLOWED_EXTENSIONS = set(['csv', 'xes'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "/data/"
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024 * 1024


html = '''
    <!DOCTYPE html>
    <title>Upload File</title>
    <h1>Upload your CSV or XES file here!</h1>
    <form method=post enctype=multipart/form-data>
         <input type=file name=file>
         <input type=submit value=UPLOAD>
    </form>
    <div id="div2"></div>
    '''


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file_url = url_for('uploaded_file', filename=filename)
            return html
            # return html + '<br><img src=' + file_url + '>'
        else:
            return render_template('upload.html', 'error')
    return html


if __name__ == '__main__':
    app.run()