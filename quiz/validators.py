def validate_name(name):

    if name is None:
        return False, "Enter your name."

    name = name.strip()

    if len(name) < 2:
        return False, "Name must be at least 2 letters."

    return True, ""


def validate_choice(choice, total_options):
   
    if choice is None or choice == -1:
        return False, "Please select an answer."

    if choice < 0 or choice >= total_options:
        return False, "Invalid answer."

    return True, ""