import FreeSimpleGUI as gui
import Controller as con

def main_window():
    layout = [
        [gui.Button('Add Category'), gui.Button('Add Purchase'), gui.Button('Add Income'), gui.Button('Movements')],[gui.Button('Exit')],
    ]

    window = gui.Window('Financial Manager', layout)

    while True:
        event, values = window.read()
        if event == gui.WIN_CLOSED:
            break
        elif event == 'Add Category':
            add_category()
        elif event == 'Add Purchase':
            add_purchase()
        elif event == 'Add Income':
            add_income()
        elif event == 'Movements':
            movements()
        elif event == 'Exit':
            window.close()
    window.close()

def add_category():
    layout = [
        [gui.Text('Type a cetegory:'), gui.Input(key='category'), gui.Button('Add'), gui.Button('Cancel')],
    ]
    window = gui.Window('Category', layout)

    while True:
        event, values = window.read()
        if event == gui.WIN_CLOSED:
            break
        elif event == 'Add':
            category = values['category'].strip()
            if category != '':
                con.create_category_file(category)
                gui.popup(f'"{category}" category created!')
                window.close()
            else:
                gui.popup('First, type a category in order to continue.',title='Error')
        elif event == 'Cancel':
            window.close()
    window.close()


def add_purchase():
    try:
        list = con.open_category_file()
        layout = [
            [gui.Text('Category:'), gui.Combo(list, readonly=True, default_value=list[0], key='category')],
            [gui.Text('Description:'), gui.Input(key='description')],
            [gui.Text('Purchase amount:'), gui.Input(key='amount')],
            [gui.Button('Add'), gui.Button('Cancel')],
        ]

        window = gui.Window('Add Purchase', layout)

        while True:
            event, values = window.read()
            if event == gui.WIN_CLOSED:
                break
            elif event == 'Add':
                description = values['description'].strip()
                amount = values['amount'].strip()
                if not description or not values:
                    gui.popup('Please make sure to fill the empty inputs before submiting.', title='Error')
                else:
                    try:
                        amount_number = float(amount)
                        if amount_number < 1:
                            gui.popup('The amount cannot be less than 1.')
                        else:
                            object = con.add_financial_flow('Purchase', values['category'], description, amount_number)
                            con.create_financial_flow_file(object)
                            gui.popup('Purchase added!')
                            window.close()
                    except ValueError:
                        gui.popup('The purchase amount can only contain numbers.', title='Error')  
            elif event == 'Cancel':
                window.close()
        window.close()
    except TypeError:
        gui.popup('Please, first create a category before adding a purchase.', title='Error')              


def add_income():
    try:
        list = con.open_category_file()
        layout = [
            [gui.Text('Category:'), gui.Combo(list, readonly=True, default_value=list[0], key='category')],
            [gui.Text('Description:'), gui.Input(key='description')],
            [gui.Text('Income amount:'), gui.Input(key='amount')],
            [gui.Button('Add'), gui.Button('Cancel')],
        ]

        window = gui.Window('Add Purchase', layout)

        while True:
            event, values = window.read()
            if event == gui.WIN_CLOSED:
                break
            elif event == 'Add':
                description = values['description'].strip()
                amount = values['amount'].strip()
                if not description or not values:
                    gui.popup('Please make sure to fill the empty inputs before submiting.', title='Error')
                else:
                    try:
                        amount_number = float(amount)
                        if amount_number < 1:
                            gui.popup('The amount cannot be less than 1.')
                        else:
                            object = con.add_financial_flow('Income', values['category'], description, amount_number)
                            con.create_financial_flow_file(object)
                            gui.popup('Income Added!')
                            window.close()
                    except ValueError:
                        gui.popup('The income can only contain numbers', title='Error')  
            elif event == 'Cancel':
                window.close()
        window.close()
    except TypeError:
        gui.popup('Please, first create a category before adding a purchase.', title='Error')  


def movements():
    data = con.open_financial_flow_file()
    if data == FileNotFoundError:
        gui.popup('A purchase or income has to be added first before displaying the information.', title='Error')
    else:
        values = data[1:]

        layout = [
            [gui.Table(values=values, 
                    headings=['Type','Category','Description','Amount'],
                    max_col_width=35,
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='left',
                    num_rows=10,
                    key='table',
                    row_height=35,
                    )],
            [gui.Button('Return')],
        ]

        window = gui.Window('Movements', layout)

        while True:
            event, values = window.read()
            if event == gui.WIN_CLOSED:
                break
            elif event == 'Return':
                window.close()
        window.close()