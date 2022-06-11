
def relation_to_luke(name):
    relation = {"Darth Vader": "father", "Leia": "sister", "Han": "brother in law", "R2D2": "droid"}
    return f"Luke, I am your {relation[name]}"

# Since f-strings aren't accepted on Edabit I'll use string formatting

def relation_to_luke(name):
    relation = {"Darth Vader": "father", "Leia": "sister", "Han": "brother in law", "R2D2": "droid"}
    return f"Luke, I am your {}".format(relation[name])
