stack = []
allowed_operators = ['+', '*']
next_state = 'q0'
input_string = ""
calculation_string = ""
next_element = ''
accepted_state = False
unaccepted_state = False
result_stack = []


def set_next_state(next_state_value):
    global next_state
    next_state = next_state_value


def set_accepted_state(accepted_state_value):
    global accepted_state
    accepted_state = accepted_state_value


def set_next_element(next_element_value):
    global next_element
    next_element = next_element_value


def set_input_string(input_string_value):
    global input_string
    input_string = input_string_value


def set_unaccepted_state():
    global unaccepted_state
    unaccepted_state = True


def remove_first_character():
    global input_string
    input_string = input_string[1:]


def delta_q0(next_element):
    if next_element.isdigit():
        result_stack.append(int(next_element))
        set_next_state('q1')
    else:
        set_unaccepted_state()


def delta_q1(next_element):
    if next_element.isdigit() and not stack:
        stack.append(next_element)
        result_stack.append(int(next_element))
        set_next_state('q1')
    elif next_element.isdigit() and len(stack) > 0 and stack[0].isdigit():
        stack.append(next_element)
        result_stack.append(int(next_element))
        set_next_state('q1')
    elif next_element in allowed_operators and len(stack) > 0 and stack[0].isdigit():
        calculate(result_stack.pop(), result_stack.pop(), next_element)
        stack.pop()
        set_next_state('q2')
    else:
        set_unaccepted_state()


def delta_q2(next_element):
    if not stack:
        set_next_state('q3')
    elif next_element in allowed_operators and stack[0].isdigit():
        calculate(result_stack.pop(), result_stack.pop(), next_element)
        stack.pop()
        set_next_state('q2')
    elif next_element.isdigit() and stack[0].isdigit():
        stack.append(next_element)
        result_stack.append(int(next_element))
        set_next_state('q2')
    else:
        set_unaccepted_state()


def delta_q3(next_element):
    if len(input_string) == 0:
        set_accepted_state(True)
    elif next_element.isdigit() and not stack:
        stack.append(next_element)
        result_stack.append(int(next_element))
        set_next_state('q1')
    else:
        set_unaccepted_state()


def transition_state(next_element, next_state):
    states = {
        'q0': lambda: delta_q0(next_element),
        'q1': lambda: delta_q1(next_element),
        'q2': lambda: delta_q2(next_element),
        'q3': lambda: delta_q3(next_element),
    }
    func = states.get(next_state, lambda: 'Invalid')
    func()


def calculate(first_number, second_number, operation):
    global result
    operations = {
        '+': lambda a, b: a + b,
        '*': lambda a, b: a * b,
    }
    result_stack.append(operations[operation](first_number, second_number))


def main():
    set_input_string(input("Please provide automata input for calculation..."))
    global calculation_string
    calculation_string = input_string
    while not accepted_state:
        if unaccepted_state:
            print("input not accepted")
            exit(0)
        if len(input_string) != 0:
            set_next_element(input_string[0])
        transition_state(next_element, next_state)
        if len(input_string) != 0 and next_state != 'q3':
            remove_first_character()
    print("accepted state")
    print(result_stack[0])
    exit(0)


if __name__ == "__main__":
    main()
