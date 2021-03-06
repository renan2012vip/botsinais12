################################ CONFIG #######################################
class Config(object):
  PACKAGE_NAME = 'proxybet'
  PACKAGE_VERSION = '0.0.1'
  DATABASE_USERNAME = 'postgres'
  DATABASE_PASSWORD = 'XXXXXXXX'
  # DOMAIN_NAME = 'dznet.host'
  LOG_FORMAT = '%(asctime)s - %(lineno)d - %(name)s: %(levelname)s %(message)s'
  LOG_PATH = 'log/{}.log'.format(__name__)
  SERVER_HOST = '0.0.0.0'
  SERVER_PORT = 5505
  # SERVER_NAME = '{}:{}'.format(DOMAIN_NAME, SERVER_PORT)
  SESSION_COOKIE_DOMAIN = True
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_ECHO = False

  def database_uri(DATABASE_NAME):
    return 'postgresql://{}:{}@{}/{}'.format(Config.DATABASE_USERNAME,
                                             Config.DATABASE_PASSWORD,
                                             Config.SERVER_HOST,
                                             DATABASE_NAME)


class Development(Config):
  DATABASE_NAME = '{}_dev'.format(Config.PACKAGE_NAME)
  DEBUG = True
  SECRET_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
  SQLALCHEMY_DATABASE_URI = Config.database_uri(DATABASE_NAME)
  TELEGRAM_API_ID = 'XXXXX'
  TELEGRAM_API_HASH = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
  TELEGRAM_BOT_TOKEN = '5202017406:AAFdT8D03ikLYgwzXpVkzV-RzPi8ADjBb3Q'
  TESTING = False


class Testing(Config):
  DATABASE_NAME = '{}_test'.format(Config.PACKAGE_NAME)
  DEBUG = True
  SECRET_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
  SQLALCHEMY_DATABASE_URI = Config.database_uri(DATABASE_NAME)
  TELEGRAM_API_ID = 'XXXXX'
  TELEGRAM_API_HASH = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
  TELEGRAM_BOT_TOKEN = '5202017406:AAFdT8D03ikLYgwzXpVkzV-RzPi8ADjBb3Q'
  TESTING = True


class Production(Config):
  DATABASE_NAME = '{}_prod'.format(Config.PACKAGE_NAME)
  DEBUG = False
  SECRET_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
  SQLALCHEMY_DATABASE_URI = Config.database_uri(DATABASE_NAME)
  TELEGRAM_API_ID = 'XXXXX'
  TELEGRAM_API_HASH = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
  TELEGRAM_BOT_TOKEN = '5202017406:AAFdT8D03ikLYgwzXpVkzV-RzPi8ADjBb3Q'
  TESTING = False
