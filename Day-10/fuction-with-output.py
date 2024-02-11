def format_name(fname, lname):
    formatted_f_name = fname.title()
    formatted_l_name = lname.title()
    return f"{formatted_f_name} {formatted_l_name}"

print(format_name("Nikhil", "gayakwad"))


def format_name1(fname,lname):
    if(fname=="" or lname==""):
        return "You didn't provide any input"
    formatted_fname = fname.title()
    formatted_lname = lname.title()
    return f"Result : {formatted_fname} {formatted_lname}"

print(format_name1("Nicky","choudhary"))