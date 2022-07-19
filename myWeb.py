# -*- coding: utf-8 -*-

import web
urls = (
    '/demo/(.*)', 'demo',
    '/(js|css|images)/(.*)', 'static'
)
app = web.application(urls, globals())
render = web.template.render('templates/')

class demo:
    def GET(self, text):
        print('input:' + text)
        return render.demo(content=text.upper())

class static:
    def GET(self, media, file):
        try:
            f = open(media+'/'+file, 'rb')
            return f.read()
        except:
            return ''

if __name__ == "__main__":
    app.run()