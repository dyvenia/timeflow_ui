from typing import Container
from idom import component, html, run, use_state
from components.layout import Container
from components.heading import H3
from components.input import Input
from components.controls import TableActions
from components.tablebatch import Tablebatch
from components.paginaton import Pagination

quantity = 5


@component
def YourTimelog():
    input_value, set_input_value = use_state('')
    return html.section(
        {'class': "py-6 xl:py-8"},
        Container(
            html.div(
                {'class': 'flex flex-wrap justify-between items-center'},
                H3('Your Timelog'),
                Input(input_value, set_input_value),
            ),
            TableActions(),
            Tablebatch(),
            Pagination(quantity)
        )
    )
