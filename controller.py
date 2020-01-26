import web
from models import RegisterModel

# URLs to route to
urls = (
    '/', 'Home',
    '/register', 'Register',
    '/postregistration', 'PostRegistration'
)

render = web.template.render("views/templates", base="MainLayout")
app = web.application(urls, globals())

# Classes/routes
class Home:
    def GET(self):
        return render.Home()

class Register:
    def GET(self):
        return render.Register()

class PostRegistration:
    def POST(self):
        data = web.input()
        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(data)
        return data

if __name__ == "__main__":
    app.run()