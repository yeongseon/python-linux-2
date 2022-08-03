import bottle
from bottle import route, run, Response, template
import json
import image
from pyinstrument import Profiler #Import Library
profiler = Profiler() #Instantiate class object

def call_service():
    directoryName = 'photos'
    image.process(directoryName)

@route('/')
def index():
    """Home page"""
    profiler.start()	
    title = "Image Processor App"
    call_service()
    profiler.stop()
    prin(profiler.output_text(unicode=True, color=True))	
    return template('index.tpl',data="Request completed!", title=title)

if __name__ == '__main__':
	run(host='0.0.0.0', port=8000, debug=False, reloader=True)
	
app = bottle.default_app()
