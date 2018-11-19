from makeweb import (
    Doc, CSS, JS,
    head, meta, title, style, script,
    body, h1, h2, button, ul, li, span, a
)

css = CSS()

css('*',
    font__family='Verdana', )
css('body',
    background__color='#fefefe',
    color='#232323',
    )
css('h1',
    text__align='center',
    )
css('h2',
    text__align='center',
    )


def render(name):
    doc = Doc('html')
    with head():
        meta(charset='utf-8')  # Define charset first.
        title(name)
        with style():
            css.embed()
    with body():
        h2(f"Hello, I'm {name}.")
        h1(f"I am from The Internet.")
    return str(doc)
