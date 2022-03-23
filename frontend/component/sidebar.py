from idom import component, html

aClass = """text-nav text-xs py-2""",
mainDivClass = """absolute w-screen h-full bg-header-bg z-10 min-h-screen""",
container = """container""",
h1Class = """text-general-heading font-black uppercase text-xl font-black tracking-[2px] my-4""",
navClass = """flex flex-col"""


@component
def Sidebar(isOpen):
    mainDivClass if isOpen else mainDivClass + """hidden""",
    return html.div(
        {'class': mainDivClass},
        html.div(
            {'class': container},
            html.h1(
                {'class': h1Class}, "timeflow"),
            html.nav({'class': navClass},
                     html.a({'href': '#', 'class': aClass}, 'Timelogs'),
                     html.a({'href': '#', 'class': aClass}, 'Forecasts'),
                     html.a({'href': '#', 'class': aClass}, 'Admin')
                     )
        )
    )
