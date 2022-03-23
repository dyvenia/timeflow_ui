from idom import component, html, run
from component.header import Header
from component.sidebar import Sidebar


@component
def page():
    return html.div(
        html.link({"href": "../static/css/styles.css", "rel": "stylesheet"}),
        Header(),
    )
