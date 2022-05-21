import sanic

if __name__ == '__main__':
    app = sanic.Sanic("WorkManager")
    app.run(host="127.0.0.1", port=8080)