import cgi

from google.appengine.api import users
import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            # self.response.headers['Content-Type'] = 'text/plain'
            # self.response.out.write('Hello, ' + user.nickname())
            self.response.out.write("""
              <html>
                <body>
                  <form action="/sign" method="post">
                    <div><textarea name="content" rows="3" cols="60"></textarea></div>
                    <div><input type="submit" value="Sign Guestbook"></div>
                  </form>
                </body>
              </html>""")
        else:
            self.redirect(users.create_login_url(self.request.uri))





class Guestbook(webapp2.RequestHandler):
    def post(self):
        self.response.out.write('<html><body>You wrote:<pre>')
        self.response.out.write(cgi.escape(self.request.get('content')))
        self.response.out.write('</pre></body></html>')



application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', Guestbook)
], debug=True)



def main():
    application.run()

if __name__ == "__main__":
    main()