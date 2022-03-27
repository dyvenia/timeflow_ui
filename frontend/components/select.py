from idom import component, html, use_state


@component
def Select(
    set_value,
    selectClass,
    wrapperClass,
    placeholder,
    items,
):
    dropdown = [html.option({'value': el}, el) for el in items]
    return html.div(
        {'class': wrapperClass},
        html.select({
            'class': selectClass,
            'onChange': lambda event: set_value(event["target"]["value"])
        },
            html.option({'disabled': True,
                         'selected': True}, placeholder),
            dropdown
        ),
    )
