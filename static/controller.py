import web

# URLs to route to
urls = (
    '/', 'home',
    '/register', 'register'
)

render = web.template.render("views/templates", base="MainLayout")
app = web.application(urls, globals())

# Classes/routes
class home:
    def GET(self):
        return render.Home()

class register:
    def GET(self):
        return render.Register()

if __name__ == "__main__":
    app.run()