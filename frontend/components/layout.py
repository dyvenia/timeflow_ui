from idom import html, component


def Container(*args: html):
    return html.div({"class": "container w-full"}, args)
