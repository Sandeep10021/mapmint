import os
from flask import Flask, make_response, render_template, flash, request, redirect, url_for, send_from_directory, Request
from werkzeug.utils import secure_filename
import random
import subprocess


UPLOAD_FOLDER = "uploads/"
ALLOWED_EXT = {'png', 'jpg', 'jpeg', 'bmp', 'tiff', 'tif' }

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

import mimetypes
mimetypes.add_type("application/javascript", ".js", True)

def allowed_file(filename):
        return '.' in filename and \
                filename.rsplit('.', 1)[1].lower() in ALLOWED_EXT

@app.route('/', methods=['GET', 'POST'])
def upload_file():
        ID=random.randint(1, 10000000)
        if request.method == 'POST':
                # check if the post request has the file part
                if 'files[]' not in request.files:
                        return 'Error: No file is chosen... Please upload a valid file. '

                files = request.files.getlist('files[]')
                outputID = str(ID)
                outputDir = os.path.join(app.config['UPLOAD_FOLDER'], outputID)
                if os.path.exists(outputDir):
                        ID+=1
                        outputID = str(ID) 
                        outputDir = os.path.join(app.config['UPLOAD_FOLDER'], outputID)
                        os.mkdir(outputDir, exist_ok=True)
                else:
                        os.mkdir(outputDir)
                        
                for file in files:
                        if file and allowed_file(file.filename):
                                filename = secure_filename(file.filename)
                                # save images to file system
                                file.save(os.path.join(outputDir, filename))
                                
                os.system("ls {}".format(outputDir)) 
                command =  'OpenSfM/bin/opensfm_run_all '+ outputDir
                subprocess.call([command], shell=True)         
                #recon = os.system("python3 openMVG/src/software/SfM/SfM_GlobalPipeline.py.in {} {}".format(outputDir, outputDir+"/recon"))
                recon_ply = "/merged.ply"
                
                return render_template("result.html", image=recon_ply)
                        
        return render_template("generating.html")
        

@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
	app.run(debug=True) 
