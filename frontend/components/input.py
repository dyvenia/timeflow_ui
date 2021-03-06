from idom import component, html, run

wrapperClass = 'w-full md:w-1/2 flex justify-between items-center border-input-border border-[1px] rounded-[3px] py-3 px-4'
checkboxTd = 'w-6 pr-4 pt-4 pb-3'


@component
def Input(input_value, set_input_value):

    def handle_click(event):
        set_input_value('')

    return html.div(
        {'class': wrapperClass},
        html.img({'src': '../static/img/svg/search.svg'}),
        html.input({
            'type': 'text',
            'placeholder': 'Search your timelog here',
            'value': input_value,
            'onChange': lambda event: set_input_value(event["target"]["value"]),
            'class': 'w-10/12 outline-none'
        }, ),
        html.img({
            'class': 'cursor-pointer',
            'src': '../static/img/svg/cross.svg',
            'onClick': handle_click,
        })
    )


@component
def Checkbox():
    return html.td(
        {'class': checkboxTd},
        html.input({'class': 'w-4 h-4', 'type': 'checkbox'})
    )
