import tornado.web
import tornado.httpserver
from tornado.options import options
import tornado.ioloop

from urls import *
from config import *

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), '../template'),
    static_path=os.path.join(os.path.dirname(__file__), '../static'),
)


class Application(tornado.web.Application):

    def __init__(self):
        tornado.web.Application.__init__(self,
                                         hanlers,
                                         debug=True,
                                         **settings
                                         )


def main():
    init_config()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
