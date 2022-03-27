from idom import component, html
from components.header import Header
from components.layout import Container
from components.yourTimelog import YourTimelog
from components.currentProject import CurrentProject


@component
def page():
    return html.div(
        {'class': 'xl:flex'},
        html.link({"href": "../static/css/styles.css", "rel": "stylesheet"}),
        Header(),
        html.main(
            {'class': 'relative xl:w-[calc(100%-15rem)]'},
            CurrentProject(),
            YourTimelog()
        )
    )
