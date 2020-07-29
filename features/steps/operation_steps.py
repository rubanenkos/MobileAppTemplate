from behave import when, given, then


@given('App is running')
def verify_is_app_running(context):
    calculator_running = context.app.main_page.verify_main_screen()
    assert calculator_running


@when('Tap on Digit {given_digit}')
def tap_digit(context, given_digit):
    context.app.main_page.tap_digit(given_digit)


@when('Type Digits {given_digit}')
def type_digits(context, given_digit):
    for i in given_digit:
        if i == '.':
            context.app.main_page.tap_point()
        else:
            context.app.main_page.tap_digit(i)


@when('Tap on Point')
def tap_point(context):
    context.app.main_page.tap_point()


@when('Tap on Clear')
def tap_point(context):
    context.app.main_page.tap_clear()

@when('Tap on DELETE')
def tap_delete(context):
    context.app.main_page.tap_delete()


@when('Tap on Sum')
def operation_plus(context):
    context.app.main_page.tap_plus()


@when('Tap on Minus')
def operation_minus(context):
    context.app.main_page.tap_minus()


@when('Tap on Divide')
def operation_divide(context):
    context.app.main_page.tap_divide()


@when('Tap on Multiply')
def operation_miltiply(context):
    context.app.main_page.tap_multiply()


@when('Tap on Equality')
def equality(context):
    context.app.main_page.tap_equality()


@when('Tap on Arrow')
def click_arrow(context):
    context.app.advanced_page.tap_arrow()


@when('Open advanced operations')
def open_advanced_operations(context):
    context.app.advanced_page.open_advanced_operations_panel()


@when('Tap on Square root')
def click_arrow(context):
    context.app.advanced_page.tap_square_root()


@then('Result is shown and equal to {expected}')
def verify_result(context, expected):
    actual = context.app.main_page.get_result()
    assert actual == expected, f'Expected result should be {expected}'


@then('Now on the screen {expected}')
def verify_screen(context, expected):
    actual = context.app.main_page.get_screen_status()
    assert actual == expected, f'Expected result should be {expected}'


@then('Screen is empty')
def verify_is_screen_empty(context):
    verify_screen(context, expected='')



