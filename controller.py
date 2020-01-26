import web

urls = (
    '/', 'home'
)

render = web.template.render("Views/Templates", base="mainlayout")
app = web.application(urls, globals())

# classes/routes

class home:
    def GET(self):
        return render.home()

if __name__ == "__main__":
    app.run()