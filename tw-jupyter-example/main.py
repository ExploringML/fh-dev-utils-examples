from fasthtml.common import *
from fh_dev_utils.serve import *

DEV_MODE=True

app,rt = fast_app(
    pico=False,
    live=True,
    hdrs=(
        Link(rel="stylesheet", href=f"/public/app.css{cache_buster() if DEV_MODE else ""}", type="text/css"),
    )
)

@rt('/')
def get():
    return Div(
        P('Hello World!', cls="text-[#bada55] bg-gradient-to-r from-blue-400 to-purple-600 p-4 rounded-lg shadow-lg"),
        P('Blue Background', cls="bg-blue-500 text-white p-2 round"),
        P('Gradient Text', cls="bg-gradient-to-r from-pink-500 to-yellow-500 text-transparent bg-clip-text p-6"),
        cls="m-[41px] space-y-4"
    )

if DEV_MODE: serve_dev(tw=True, jupyter=True)
else: serve()