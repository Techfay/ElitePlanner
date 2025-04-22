# cgi.py - dummy module to satisfy Django 3.2
def parse_header(line):
    return line, {}

class FieldStorage:
    def __init__(self, *args, **kwargs):
        pass
