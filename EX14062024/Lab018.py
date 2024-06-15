def allowed_to_enter(name):
    match name:
        case "dell":
            print(name, "is allowed to enter ")

        case "lenovo":
            print(name, "is allowed to enter ")
        case "lg":
            print(name, "is allowed to enter ")
        case _:
            print(name, "Not allowed to enter")

allowed_to_enter("lenovo")