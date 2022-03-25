from idom import component, html
from components.icons import arrow_left, arrow_right

pageButtonClass = 'w-8 h-8 mx-3 flex items-center justify-center cursor-pointer rounded-full hover:bg-pagination-hover hover:w-8 hover:h-8'
wrapperClass = 'flex items-center w-full justify-center text-pagination mb-8 xl:justify-end'


@component
def PageButton(number):
    return html.a(
        {'class': pageButtonClass},
        number + 1
    )


@component
def Pagination(quantity):
    pageButtons = [PageButton(number) for number in range(quantity)]
    return html.div(
        {
            'class': wrapperClass
        },
        html.a(
            {'class': pageButtonClass},
            arrow_left
        ),
        pageButtons,
        html.a(
            {'class': pageButtonClass},
            arrow_right
        ),
    )
