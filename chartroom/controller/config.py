from tornado.options import define


def init_config():
    define('port', default=8000, type=int, help='chartroom')
