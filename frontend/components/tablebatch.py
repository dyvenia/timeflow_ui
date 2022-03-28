from idom import component, html, run
from components.input import Checkbox
from components.tablebatch_row import TablebatchRow

thClass = 'w-[176px] text-left text-text-table-head uppercase py-1 leading-5'


@component
def Tablebatch():
    return html.div(
        {'class': 'overflow-auto py-6 text-xs'},
        html.table(
            {'class': 'w-[905px] mx-auto xl:w-full'},
            html.thead(
                {},
                html.tr(
                    {'class': 'bg-table-head'},
                    html.th(
                        {'class': 'w-6'}
                    ),
                    html.th(
                        {'class': thClass},
                        'timelog id'
                    ),
                    html.th(
                        {'class': thClass},
                        'start time'
                    ),
                    html.th(
                        {'class': thClass},
                        'end time'
                    ),
                    html.th(
                        {'class': thClass},
                        'count hours'
                    ),
                    html.th(
                        {'class': thClass},
                        'count days'
                    )
                )
            ),
            html.tbody(
                {},
                TablebatchRow('2', '2022-02-1 08:00',
                              '2022-02-1 18:00', '2.0', '0.25'),
                TablebatchRow('2', '2022-02-1 08:00',
                              '2022-02-1 18:00', '2.0', '0.25'),
                TablebatchRow('2', '2022-02-1 08:00',
                              '2022-02-1 18:00', '2.0', '0.25'),
                TablebatchRow('2', '2022-02-1 08:00',
                              '2022-02-1 18:00', '2.0', '0.25'),
                TablebatchRow('2', '2022-02-1 08:00',
                              '2022-02-1 18:00', '2.0', '0.25')
            )
        )
    )
