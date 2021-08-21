import os
from flask import Flask, make_response, render_template, flash, request, redirect, url_for, send_from_directory, Request
from werkzeug.datastructures import ImmutableDict, ImmutableDictMixin
from werkzeug.utils import secure_filename
import random
import subprocess
import shutil

UPLOAD_FOLDER = "data/sample"
ALLOWED_EXT = {'png', 'jpg', 'jpeg', 'bmp', 'tiff', 'tif' }

app = Flask(__name__)
app.secret_key='dont tell anyone'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

import mimetypes
mimetypes.add_type("application/javascript", ".js", True)

def allowed_file(filename):
        return '.' in filename and \
                filename.rsplit('.', 1)[1].lower() in ALLOWED_EXT

@app.route('/', methods=['GET', 'POST'])
def upload_file():
        ID='images'
        if request.method == 'POST':
                # check if the post request has the file part
                if 'files[]' not in request.files:
                        return 'Error: No file is chosen... Please upload a valid file. '
		
                files = request.files.getlist('files[]')
                outputID = ID
                outputDir = os.path.join(app.config['UPLOAD_FOLDER'], outputID)
                if os.path.exists('data/sample'):
                    for file_s in os.listdir('data/sample'):
                        path = os.path.join('data/sample', file_s)
                        try:
                            shutil.rmtree(path)
                        except OSError:
                            os.remove(path)    
                    os.mkdir(outputDir)       
                else:
                    os.mkdir(outputDir)
                        
                for file in files:
                        if file and allowed_file(file.filename):
                                filename = secure_filename(file.filename)
                                # save images to file system
                                file.save(os.path.join(outputDir, filename))
                                
                os.system("ls {}".format(outputDir)) 
                command =  'bin/opensfm_run_all data/sample'
                subprocess.call([command], shell=True) 

                flash('Point Cloud has been generated sucessfully!')

                # recon_ply = "/undistorted/depthmaps/merged.ply"
                
                # return render_template("result.html", image=recon_ply)
                        
        return render_template("generating.html")
        

@app.route('/data/sample/<path:filename>')
def uploaded_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/result')  
def result(): 
    recon_ply = "/undistorted/depthmaps/merged.ply"
    return render_template("result.html", image=recon_ply);  



if __name__ == '__main__':
	app.run(debug=True) 
