from fasthtml.common import *
from fh_dev_utils.serve import *

DEV_MODE=True

app,rt = fast_app(
    pico=False,
    live=True,
    hdrs=(
        Link(rel="stylesheet", href=f"/public/app.css{cache_buster() if DEV_MODE else ''}", type="text/css"),
    )
)

def card(icon="🎨", heading="Heading", text="Add content here."):
    return Div(
        Div(icon, cls="text-3xl bg-blue-100 w-12 h-12 rounded-xl flex items-center justify-center mb-4"),
        H2(heading, cls="text-xl font-bold text-gray-900 mb-3"),
        P(text, cls="text-gray-600 leading-relaxed"),
        Div(cls="absolute bottom-0 left-0 h-1 scale-x-0 transform bg-blue-500 transition-transform duration-300 ease-in-out group-hover:scale-x-100"),
        cls="group relative bg-white p-8 rounded-2xl shadow-sm hover:shadow-lg transition-shadow duration-300 border border-gray-100"
    ),

@rt('/')
def get():
    return Div(
        Div(
            H1("Welcome to FastHTML", 
               cls="text-4xl font-bold text-white mb-4"),
            P("Building beautiful interfaces with Tailwind CSS", 
              cls="text-xl text-white/80"),
            cls="bg-gradient-to-br from-purple-600 to-blue-500 p-12 rounded-xl shadow-lg mb-8 text-center"
        ),
        Div(
            card(icon="✨", heading="Simple", text="Enjoy a smooth development experience. Watch UI updates in realtime."),
            card(icon="🛠️", heading="Flexible", text="Create stunning user interfaces with minimal effort using utility classes."),
            card(icon="🚀", heading="Modern", text="Use the latest Tailwind v4 cutting-edge features to boost your project."),
            cls="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-6xl mx-auto  mb-10"
        ),
        Div(
            Button("Get Started",
                  cls="cursor-pointer bg-indigo-500 text-white px-8 py-3 rounded-full hover:bg-indigo-700 transition duration-300"),
            cls="text-center"
        ),
        cls="max-w-5xl mx-auto p-6 my-20"
    )

if DEV_MODE: serve_dev(tw=True)
else: serve()