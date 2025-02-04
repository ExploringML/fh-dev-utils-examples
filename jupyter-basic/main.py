from fasthtml.common import *
from fh_dev_utils.serve import *

DEV_MODE=True

app,rt = fast_app()

@rt('/')
def get(): return Div(P('Hello World!'))

if DEV_MODE: serve_dev(jupyter=True)
else: serve()