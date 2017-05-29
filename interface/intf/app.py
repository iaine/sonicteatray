import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename

IMAGE_UPLOAD_FOLDER = '/path/to/the/uploads'
AUDIO_UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS_AUDIO = set(['mp3'])
ALLOWED_EXTENSIONS_PIC = set(['jpg', 'png', 'jpeg'])

app = Flask(__name__)
app.config['IMAGE_UPLOAD_FOLDER'] = IMAGE_UPLOAD_FOLDER
app.config['AUDIO_UPLOAD_FOLDER'] = AUDIO_UPLOAD_FOLDER

#set up a global for audio. 

@app.route('/picture/<string>', methods=['POST'])
def query_picture_position(uid_str):
    '''
       Takes the (x,y) tuple from post and retrieves the audio if near
    '''
    x = request.form['x']
    y = request.form['y']

    pos_audio = check_audio(x,y)
    if check_audio(x,y) is not None:
        play(pos_audio)
    

def check_audio(x,y):
    return "Hello"

def play(filename):
    return "Play Hello"
 
def allowed_file(filename, extension):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in extension

@app.route('/record/<string>', methods=['GET', 'POST'])
def upload_file(uid):
    if request.method == 'PUT':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename, ALLOWED_EXTENSIONS_AUDIO):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['AUDIO_UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
    if request.method == 'GET':
        fname = "turner.jpg"
        return render_template('record.html', fname=record)

def get_records():
    return ['a', 'b', 'c']

@app.route('/record', methods=['GET', 'POST'])
def get_files():
    if request.method == 'GET':
        records = get_records()
        return render_template('records.html')
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename, ALLOWED_EXTENSIONS_PIC):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['IMAGE_UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
    
