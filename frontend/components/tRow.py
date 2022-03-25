from idom import component, html, run
from components.input import Checkbox

tdClassActive = 'w-[176px] pt-4 pb-3'
tdClassDisable = 'w-[176px] pt-4 pb-3 text-text-disable'
trClass = 'border-b-[1px] border-border-table'


@component
def TRow(id, start, end, hours, days):

    return html.tr(
        {'class': trClass},
        Checkbox(),
        td(tdClassActive, id),
        td(tdClassActive, start),
        td(tdClassActive, end),
        td(tdClassDisable, hours),
        td(tdClassDisable, days)
    )


@component
def td(tdClass, value):

    return html.td(
        {'class': tdClass},
        value
    )
