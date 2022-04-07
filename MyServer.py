import os,zipfile
from flask import Flask, render_template, send_file


app = Flask(__name__)

def GetStoredFiles():
	Flnm=[]
	for (root,dirs,files) in os.walk('Data', topdown=True):
		for f in files:		
			Flnm+=[os.path.join(root,f)]
	return enumerate(Flnm)

@app.route('/')
def index():
    Flnm=	GetStoredFiles()
    return render_template('index.html',Flnm=Flnm)


@app.route('/download_files')
def download_all():
    # Zip file Initialization
    zipfolder = zipfile.ZipFile('Audiofiles.zip','w', compression = zipfile.ZIP_STORED) # Compression type 

    # zip all the files which are inside in the folder
    for root,dirs, files in os.walk('Data'):
        for file in files:
            zipfolder.write(os.path.join(root,file))
    zipfolder.close()

    return send_file('Audiofiles.zip',
            mimetype = 'zip',
            attachment_filename= 'Audiofiles.zip',
            as_attachment = True)

    # Delete the zip file if not needed
    os.remove("Audiofiles.zip")


if __name__ == '__main__':
    app.run()