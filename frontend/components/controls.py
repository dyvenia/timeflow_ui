from idom import component, html
from components.icons import filter, done, delete, batch_action, edit

aClass = 'flex items-center mr-9 py-3'


@component
def Button(label):
    return html.div(
        {'class': "w-full flex justify-center md:w-auto md:flex-1 md:justify-start 2xl:flex-none 2xl:w-auto"},
        html.button(
            {
                "type": "submit",
                "class": f"py-3 px-4 border-[1px] border-button-bg bg-button-bg text-button-text rounded-[3px] w-[145px] flex items-center justify-center font-black tracking-wider",
            },
            html.span(label)
        )
    )


@component
def TableActions():
    return html.div(
        {'class': 'flex items-center flex-wrap mt-4  md:justify-start'},
        html.a(
            {'href': 'javascript:void(0)', 'class': aClass},
            batch_action,
            html.span('Batch actions')
        ),
        html.a(
            {'href': 'javascript:void(0)', 'class': aClass},
            filter,
            html.span('Filter')
        ),
        html.a(
            {'href': 'javascript:void(0)', 'class': aClass},
            edit,
            html.span('Edit selected')
        ),
        html.a(
            {'href': 'javascript:void(0)', 'class': aClass},
            delete,
            html.span('Delete')
        ),
        html.a(
            {'href': 'javascript:void(0)', 'class': aClass},
            done,
            html.span('Done')
        )
    )
