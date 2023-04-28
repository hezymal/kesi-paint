from application_config import ApplicationConfig
from application import Application


def run():
    config = ApplicationConfig('Paint in Python', 1000, 600)
    application = Application(config)
    application.run()


if __name__ == '__main__':
    run()
