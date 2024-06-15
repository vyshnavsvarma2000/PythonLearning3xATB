def allowed_to_enter(name, password):
    if name == "pramod":
        if password == "yes":
            print("allowed")
    else:
     print("Not allowed")

allowed_to_enter("pramod", "yes")