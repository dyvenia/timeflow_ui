from idom import component, html, use_state


@component
def counter():
    count, set_count = use_state(0)

    def handle_button(event):
        set_count(count + 1)

    return html.div(
        html.p(f"The lastest count is {count}"),
        html.button({"onClick": handle_button}, "Add 1"),
    )
