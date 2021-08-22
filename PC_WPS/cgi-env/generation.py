import zoo
import os
from flask import Flask, make_response, render_template, flash, request, redirect, url_for, send_from_directory, Request
from werkzeug.datastructures import ImmutableDict, ImmutableDictMixin
from werkzeug.utils import secure_filename
import random
import subprocess
import shutil

def PointCloud(conf,inputs,outputs):
	
	UPLOAD_FOLDER = "data/sample"
	ALLOWED_EXT = {'png', 'jpg', 'jpeg', 'bmp', 'tiff', 'tif' }
	
	
	import mimetypes
	mimetypes.add_type("application/javascript", ".js", True)
	
	def allowed_file(filename):
	        return '.' in filename and \
	                filename.rsplit('.', 1)[1].lower() in ALLOWED_EXT
	
	methods=['GET', 'POST']
	def upload_file():
	        ID='images'
	        if request.method == 'POST':
	                # check if the post request has the file part
	                if 'files[]' not in request.files:
	                        return 'Error: No file is chosen... Please upload a valid file. '
	
	                files = request.files.getlist('files[]')
	                outputID = ID
	                outputDir = os.path.join(UPLOAD_FOLDER, outputID)
	                if os.path.exists('UPLOAD_FOLDER'):
	                    for file_s in os.listdir('UPLOAD_FOLDER'):
	                        path = os.path.join('UPLOAD_FOLDER', file_s)
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
	
	                # recon_ply = "/undistorted/depthmaps/merged.ply"
	                
	                # return render_template("result.html", image=recon_ply)
	                        
	def uploaded_file(filename):
	        return send_from_directory(UPLOAD_FOLDER, filename)
        
	outputs["Result"]["value"]=UPLOAD_FOLDER +"/undistorted/depthmaps/merged.ply"
	return zoo.SERVICE_SUCCEEDED

