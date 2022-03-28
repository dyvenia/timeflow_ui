from idom import component, html, run, use_effect, use_state
from components.input import Checkbox

tdClassActive = 'w-[176px] pt-4 pb-3'
tdClassDisable = 'w-[176px] pt-4 pb-3 text-text-disable'
trClass = 'border-b-[1px] border-border-table'


@component
def TablebatchRow(id, timelog_id, start, end, hours, days, checked, set_checked):
    value_checkbox, set_value_checkbox = use_state(False)

    def fill_checked():
        if id in checked:
            return
        else:
            set_checked({**checked, id: value_checkbox})

    use_effect(fill_checked)

    def handle_change(event):
        set_value_checkbox(not value_checkbox)
        set_checked({**checked, id: not value_checkbox})

    return html.tr(
        {
            'class': trClass,
            'id': id
        },
        Checkbox(value_checkbox, handle_change),
        td(tdClassActive, timelog_id),
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
