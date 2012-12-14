import os
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
    def get(self):
        if self.request.get('page'):
            page=self.request.get('page')+".html"
        else:
            page="index.html"
        path = os.path.join(os.path.dirname(__file__), page)
        try:
            self.response.out.write(template.render(path, None))
        except:
            self.response.out.write(template.render("404.html", None))
        
application = webapp.WSGIApplication(
                                     [('/', MainPage)],
                                     debug=True)
        
def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
