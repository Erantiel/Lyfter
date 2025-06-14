global_variable = 10

def local_function(local_variable):
    print(local_variable)


def change_global_variable():
    global global_variable
    global_variable += 20


def main():
    local_function(local_variable="I'm a local variable that is being accessed to my function via parameter.")
    change_global_variable()
    print(global_variable)


main()