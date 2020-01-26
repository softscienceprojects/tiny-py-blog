import web

urls = (
    '/', 'home'
)

render = web.template.render("views/templates", base="MainLayout")
app = web.application(urls, globals())

# classes/routes

class home:
    def GET(self):
        return render.Home()

if __name__ == "__main__":
    app.run()