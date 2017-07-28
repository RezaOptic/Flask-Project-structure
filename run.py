from project.config import DevConfig
from project.factory import create_app

app = create_app(DevConfig)

if __name__ == "__main__":
    app.run()
