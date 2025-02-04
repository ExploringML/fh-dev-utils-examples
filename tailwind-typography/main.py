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
        Div(
            H1("Welcome to FastHTML", 
               cls="text-4xl font-bold text-white mb-4"),
            P("Building beautiful interfaces with Tailwind CSS", 
              cls="text-xl text-white/80"),
            cls="bg-gradient-to-br from-purple-600 to-blue-500 p-12 rounded-xl shadow-lg mb-8 text-center"
        ),
        cls="max-w-5xl mx-auto p-6 my-8"
    ), Article(
        Header(
            H1('Beautiful Typography', cls='text-3xl font-bold'),
            P(
                'By ',
                Span('John Doe ', cls='font-semibold'),
                '| Published on',
                Time('February 4, 2025', datetime='2025-02-04'),
                cls='text-gray-600 text-sm'
            )
        ),
        Section(
            H2('Introduction'),
            P(
                'The ',
                Strong('Tailwind Typography'),
                ' plugin is an essential tool for enhancing text-based content with a clean and readable design. It simplifies styling for articles, documentation, and blogs.'
            )
        ),
        Section(
            H2('Why Use the Typography Plugin?'),
            Ul(
                Li('Provides default styles for common HTML elements.'),
                Li('Ensures consistent typography across different sections.'),
                Li('Works seamlessly with Tailwind’s utility classes.')
            )
        ),
        Section(
            H2('Code Example'),
            P('Here’s an example of how you can apply the typography plugin:'),
            Pre(
                Code('<article class="prose lg:prose-xl">\r\n\t<h1>Hello World</h1>\r\n\t<p>This is a sample paragraph styled with Tailwind Typography.</p>\r\n</article>')
            )
        ),
        Section(
            H2('Conclusion'),
            P("Using the Tailwind Typography plugin makes content presentation effortless. Whether you're building a blog, documentation, or an article-based website, it provides a solid foundation for beautiful text styling."),
            Blockquote('"Good typography makes a difference in readability and engagement."')
        ),
        cls='prose lg:prose-xl mx-auto mb-20'
    )

if DEV_MODE: serve_dev(tw=True)
else: serve()