from app.backend.config import app
from app.backend.routes import init_routes


def run():
    init_routes()
    app.run(debug=True)


if __name__ == '__main__':
    run()

