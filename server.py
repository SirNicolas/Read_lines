import os
import json
import tornado.ioloop
import tornado.web
from cache import Cache

cache = Cache(timeout=60 * 60)


class ReadLogHandler(tornado.web.RequestHandler):

    def post(self):
        chunk_size = int(self.get_argument("chunk_size", default=10))
        offset = int(self.get_argument("offset", default=0))
        next_offset = offset + chunk_size
        lines = []
        local_total_size = 0
        total_size = cache.get('total_size')

        with open('test_log', 'r') as f:
            for i, line in enumerate(f):
                if i > offset:
                    lines.append(line)
                if total_size is None:
                    local_total_size += 1
                elif i >= next_offset:
                    break

        if local_total_size:
            lines = lines[:chunk_size]
            total_size = local_total_size
            cache.set('total_size', total_size)
        next_offset = min(next_offset, total_size)

        message = {
            'ok': True,
            'messages': lines,
            'total_size': total_size,
            'next_offset': next_offset
        }
        self.write(message)

    def get(self):
        self.render("index.html")

    def write_error(self, status_code, **kwargs):
        reason = kwargs.get('exc_info')
        reason = reason[1] or 'Unknown error reason'
        self.set_status(status_code=200)
        self.write({'ok': False, 'reason': str(reason)})


def make_app():
    return tornado.web.Application(
        [(r"^.*", ReadLogHandler)],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
    )


if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
