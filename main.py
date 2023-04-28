from application_config import ApplicationConfig
from application import Application


def run():
    config = ApplicationConfig('Paint', 800, 400)
    application = Application(config)
    application.run()


if __name__ == '__main__':
    run()
