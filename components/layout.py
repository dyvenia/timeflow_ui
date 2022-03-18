from idom import component, html, use_state


@component
def Page(*args):
    return html.div(
        html.link({"href": "/static/_tailwind.css", "rel": "stylesheet"}), args
    )
