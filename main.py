from application_config import ApplicationConfig
from application import Application


def run():
    config = ApplicationConfig('My Paint', 1000, 600)
    application = Application(config)
    application.run()


if __name__ == '__main__':
    run()
