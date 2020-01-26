import web

urls = (
    '/(.*)', 'index'
)

app = web.application(urls, globals()) # routes defined above

class index:
    def GET(self, name):
        return "Hello, " + name + " how are you today?"

if __name__ == "__main__":
    app.run()