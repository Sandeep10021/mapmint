#!/usr/bin/env python3
# Import modules for CGI handling 
print ('Content-type:text/html\n')
print ()
import cgi, os
import random
import subprocess
import shutil
from werkzeug.utils import secure_filename
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
# Get filename here.
print()

UPLOAD_FOLDER = "/var/www/html/PointCloud/data/sample"
ALLOWED_EXT = {'png', 'jpg', 'jpeg', 'bmp', 'tiff', 'tif' }

import mimetypes
mimetypes.add_type("application/javascript", ".js", True)

def allowed_file(filename):
        return '.' in filename and \
                filename.rsplit('.', 1)[1].lower() in ALLOWED_EXT

files = form['files[]']
OUTPUTID='images'
outputDir = os.path.join(UPLOAD_FOLDER, outputID)
if os.path.exists(UPLOAD_FOLDER):
    for file_s in os.listdir(UPLOAD_FOLDER):
        path = os.path.join(UPLOAD_FOLDER, file_s)
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
              
# Run the command in backend to generate Point Cloud  
os.system("ls {}".format(outputDir)) 
command =  '/var/www/html/PointCloud/bin/opensfm_run_all data/sample'
subprocess.call([command], shell=True)  
 
message = 'The Point Cloud is generated successfully!'

#print ("<html><body><p>%s</p></body></html>" % (message))


with open("/var/www/html/PointCloud/result.html", "r", encoding='utf-8') as fs:
    text=fs.read()
    print(text)
'''for ele in os.listdir():
    if ele.endswith(".html"):
        # Prints only text file present in My Folder
        print(ele)'''