from bottle import route,error,template,run,request,get,post,static_file,redirect,response
import os
import bottle

@route('/')
def slash():
	return template('s2',n="")

@post('/ls')
def ls():
	stdouterr = os.popen4('ls')[1].read()
	return template('s2',var=stdouterr,cname='ls')

run(host='localhost', port=8080, debug=True)
