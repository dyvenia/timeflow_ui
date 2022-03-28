from idom import component, html, use_state, event
from components.layout import Container
from components.select import Select
from components.controls import Button
from components.heading import H3

selectClass = "w-full border-select-border py-3 pl-3 border-[1px] rounded-[3px] appearance-none"
wrapperClass = "block relative w-full sm:w-[48%] md:w-[121px] md:mr-2 my-4 before:content-[''] before:border-[6px] before:border-[transparent] before:border-t-appearance before:top-1/2 before:right-5 before:-translate-y-0.5 before:absolute 2xl:w-[14%] 2xl:mr-0"


@component
def CurrentProject():
    user, set_user = use_state('')
    epic, set_epic = use_state('')
    month, set_month = use_state('')
    day, set_day = use_state('')
    start_time, set_start_time = use_state('')
    end_time, set_end_time = use_state('')

    opt = [
        "Lorem",
        "Lorem1",
        "Lorem2",
    ]

    @event(prevent_default=True)
    def hande_submit(event):
        print(f"{user, epic, month, day, start_time, end_time}")

    return html.section(
        {'class': "bg-filter-block-bg py-4 text-sm"},
        Container(
            H3('Your current project'),
            html.form(
                {
                    'class': "flex flex-wrap justify-between items-center md:justify-start 2xl:justify-between",
                    "onSubmit": hande_submit,
                },
                Select(
                    set_user,
                    selectClass,
                    wrapperClass,
                    'User',
                    opt
                ),
                Select(
                    set_epic,
                    selectClass,
                    wrapperClass,
                    'Epic',
                    opt
                ),
                Select(
                    set_month,
                    selectClass,
                    wrapperClass,
                    'Month',
                    opt
                ),
                Select(
                    set_day,
                    selectClass,
                    wrapperClass,
                    'Day',
                    opt
                ),
                Select(
                    set_start_time,
                    selectClass,
                    wrapperClass,
                    'Start time',
                    opt
                ),
                Select(
                    set_end_time,
                    selectClass,
                    wrapperClass,
                    'End time',
                    opt
                ),
                Button('Submit'),
            )
        )
    )
