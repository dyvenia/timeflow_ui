from idom import component, html

from components.layout import Container

aClass = "text-nav text-xs py-2",
mainDivClass = "hidden absolute w-screen h-full bg-header-bg z-10 md:w-48 md:right-0 md:min-h-0 md:h-auto xl:w-full xl:block xl:static xl:h-auto",
mainDivClassOpen = "absolute w-screen h-full bg-header-bg z-10 md:w-48 md:right-0 md:min-h-0 md:h-auto xl:w-full xl:block xl:static xl:h-auto",
container = "container",
h1Class = "text-general-heading font-black uppercase text-xl font-black tracking-[2px] my-4",
navClass = "flex flex-col pb-4"


@component
def Sidebar(isOpen):
    return html.div(
        {
            'class': mainDivClassOpen if isOpen else mainDivClass,
        },
        Container(
            html.h1(
                {'class': h1Class},
                "timeflow"
            ),
            html.nav(
                {'class': navClass},
                html.a({'href': '#', 'class': aClass}, 'Timelogs'),
                html.a({'href': '#', 'class': aClass}, 'Forecasts'),
                html.a({'href': '#', 'class': aClass}, 'Admin')
            )
        )
    )
