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
        Div(
            Div(
                H2("Simple", cls="text-xl font-semibold mb-2"),
                P("Clean and intuitive design patterns", 
                  cls="text-gray-600"),
                cls="bg-white p-6 rounded-lg shadow-md hover:shadow-xl transition duration-300"
            ),
            Div(
                H2("Flexible", cls="text-xl font-semibold mb-2"),
                P("Adaptable to any design needs", 
                  cls="text-gray-600"),
                cls="bg-white p-6 rounded-lg shadow-md hover:shadow-xl transition duration-300"
            ),
            Div(
                H2("Modern", cls="text-xl font-semibold mb-2"),
                P("Built with latest best practices", 
                  cls="text-gray-600"),
                cls="bg-white p-6 rounded-lg shadow-md hover:shadow-xl transition duration-300"
            ),
            cls="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8"
        ),
        Div(
            Button("Get Started",
                  cls="cursor-pointer bg-indigo-500 text-white px-8 py-3 rounded-full hover:bg-indigo-700 transition duration-300"),
            cls="text-center"
        ),
        cls="max-w-5xl mx-auto p-6 my-20"
    ), Article(
        Header(
            H1('Exploring the Tailwind Typography Plugin', cls='text-3xl font-bold'),
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
                Code('<article class="prose lg:prose-xl">\r\n        <h1>Hello World</h1>\r\n        <p>This is a sample paragraph styled with Tailwind Typography.</p>\r\n      </article>', cls='language-html')
            )
        ),
        Section(
            H2('Conclusion'),
            P("Using the Tailwind Typography plugin makes content presentation effortless. Whether you're building a blog, documentation, or an article-based website, it provides a solid foundation for beautiful text styling."),
            Blockquote('"Good typography makes a difference in readability and engagement."')
        ),
        cls='prose lg:prose-xl mx-auto'
    ), Article(
        Header(
            H1('Building Beautiful Forms with Tailwind', cls='text-3xl font-bold'),
            P(
                'By',
                Span(' John Doe ', cls='font-semibold'),
                '| Published on',
                Time('February 4, 2025', datetime='2025-02-04'),
                cls='text-gray-600 text-sm'
            )
        ),
        Section(
            H2('Introduction'),
            P(
                'Forms are essential for user interactions on the web, from signups to contact forms. With',
                Strong(' Tailwind CSS '),
                ', we can make forms both functional and visually appealing with minimal effort.'
            )
        ),
        Section(
            H2('Basic Form Example'),
            P('Below is a simple form with styled inputs, labels, and a submit button.'),
            Form(
                Div(
                    Label('Name', cls='block text-sm font-semibold text-gray-700'),
                    Input(type='text', placeholder='Enter your name', cls='mt-1 w-full p-2 border border-gray-300 rounded-md focus:ring focus:ring-blue-300')
                ),
                Div(
                    Label('Email', cls='block text-sm font-semibold text-gray-700'),
                    Input(type='email', placeholder='you@example.com', cls='mt-1 w-full p-2 border border-gray-300 rounded-md focus:ring focus:ring-blue-300')
                ),
                Div(
                    Label('Message', cls='block text-sm font-semibold text-gray-700'),
                    Textarea(rows='4', placeholder='Type your message...', cls='mt-1 w-full p-2 border border-gray-300 rounded-md focus:ring focus:ring-blue-300')
                ),
                Button('Send Message', type='submit', cls='bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700'),
                cls='space-y-4 bg-gray-100 p-6 rounded-lg shadow-md'
            )
        ),
        Section(
            H2('Advanced Form Elements'),
            P('Forms often include checkboxes, radio buttons, and select dropdowns. Here’s how they look with Tailwind:'),
            Form(
                Div(
                    Label('Select an option', cls='block text-sm font-semibold text-gray-700'),
                    Select(
                        Option('Option 1'),
                        Option('Option 2'),
                        Option('Option 3'),
                        cls='mt-1 w-full p-2 border border-gray-300 rounded-md'
                    )
                ),
                Div(
                    Input(type='checkbox', id='subscribe', cls='mr-2'),
                    Label('Subscribe to newsletter', fr='subscribe', cls='text-sm text-gray-700'),
                    cls='flex items-center'
                ),
                Div(
                    Label('Choose one:', cls='text-sm text-gray-700'),
                    Input(type='radio', id='radio1', name='radio-group', cls='mr-1'),
                    Label('Option A', fr='radio1', cls='text-sm text-gray-700'),
                    Input(type='radio', id='radio2', name='radio-group', cls='ml-4 mr-1'),
                    Label('Option B', fr='radio2', cls='text-sm text-gray-700'),
                    cls='flex items-center space-x-4'
                ),
                cls='space-y-4 bg-gray-100 p-6 rounded-lg shadow-md'
            )
        ),
        Section(
            H2('Conclusion'),
            P('Tailwind makes styling forms easy and highly customizable. By combining utility classes with the typography plugin, we ensure both structure and readability in form-heavy content.'),
            Blockquote('"A well-designed form improves user experience and boosts conversions."')
        ),
        cls='prose lg:prose-xl mx-auto'
    )

if DEV_MODE: serve_dev(tw=True, jupyter=True)
else: serve()