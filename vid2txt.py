from bottle import route,error,template,run,request,get,post,static_file,redirect,response
import pymongo
import os
import gridfs
import bottle

@route('/')
def slash():
	return template('index',n="")

@error(404)
def error404(error):
	return "SORRY!"

@route('/static/<filepath:path>')
def images(filepath):
	return static_file(filepath, root='./static/')

@post('/hello')
def hello():
	uploaded_file = request.files.get('uploaded_file')
	fname, extension=os.path.splitext(uploaded_file.filename)
	temp = uploaded_file.filename
	save_path = os.path.join("/home/foo/BEProject/input/",temp)
	ffmpeg_command = 'ffmpeg -i '+save_path+' -vf "select=gt(scene\,0.3)"  -qscale:v 2 -vsync vfr /var/www/html/static/images/data4/%02d.jpg'
	os.system('rm -r /var/www/html/static/images/data4/ && mkdir /var/www/html/static/images/data4/')	
	os.system(str(ffmpeg_command))
	#print "Frame Generation successful.."
	stdouterr = os.popen4('python /var/www/html/generate_caption_googlenet.py')[1].read()
	description = stdouterr
	return template('nldv',var=description)

@get('/demo')
def get_demo():
	os.system('rm -r /var/www/html/static/images/data4/ && mkdir /var/www/html/static/images/data4/')
	return template('nldv',var=0)

@post('/demo')
def demo():
	os.system('rm -r /var/www/html/static/images/data4/ && mkdir /var/www/html/static/images/data4/')
	return template('nldv',var=0)

run(host='localhost', port=8080, debug=True)
