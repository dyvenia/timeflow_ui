from idom import component, html, use_state

from component.sidebar import Sidebar


@component
def Header():

    isOpen, set_isOpen = use_state(False)

    def handleOpenSidebar(event):
        set_isOpen(not isOpen)

    return html.div(
        html.header(
            {'class': "bg-header-bg"},
            html.div(
                {'class': 'w-full px-4 flex justify-between items-center py-4'},
                html.img({'src': '../static/img/svg/logo.svg'}),
                html.a({'href': 'javascript:void(0)', 'onClick': handleOpenSidebar},
                       html.img(
                    {'src': '../static/img/svg/Burger.svg', 'class': "w-8"}
                )
                )
            ),
            Sidebar(isOpen)
        )
    )
