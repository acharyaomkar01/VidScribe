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
	return template('index')

@route('/static/<filepath:path>')
def images(filepath):
	return static_file(filepath, root='./static/')

@get('/video')
def get_video():
	return template('index')	

@post('/video')
def video():
	uploaded_file = request.files.get('uploaded_file')
	if uploaded_file is None:
		return template('nldv',var=0)
	fname, extension=os.path.splitext(uploaded_file.filename)
	temp = uploaded_file.filename
	save_path = os.path.join("/var/www/html/static/videos/",temp)
	ffmpeg_command = 'ffmpeg -i '+save_path+' -s 1920x1080 -vf "select=gt(scene\,0.5)"  -qscale:v 2 -vsync vfr /var/www/html/static/images/data4/%02d.jpg'
	os.system('rm -r /var/www/html/static/images/data4/ && mkdir /var/www/html/static/images/data4/')	
	os.system(str(ffmpeg_command))
	#print "Frame Generation successful.."
	stdouterr = os.popen4('python /var/www/html/generate_caption_googlenet.py')[1].read()
	stdouterr = stdouterr.strip()
	stdouterr = stdouterr.split('))')
	stdouterr = stdouterr[1].strip()
	stdouterr = stdouterr.split('.')
	stdouterr.pop()
	return template('nldv',var=stdouterr,videoname='/static/videos/'+temp)

@get('/demo')
def get_demo():
	os.system('rm -r /var/www/html/static/images/data4/ && mkdir /var/www/html/static/images/data4/')
	return template('nldv',var=0)

@post('/demo')
def demo():
	os.system('rm -r /var/www/html/static/images/data4/ && mkdir /var/www/html/static/images/data4/')
	return template('nldv',var=0)

run(host='localhost', port=8080, debug=True)
