print(format_name1(input("What is your name?"), input("What is your last name? ")))

#Return as an early exit
def format_name1(f_name,l_name):
    """ Take a first and last name and format it to return the title  case 
       verison of the name
    """
    if f_name=="" or l_name=="":
        return "You didn't provide any input"
    formatted_name=f_name.title()
    formatted_lname=l_name.title()
    return f"Result : {formatted_name} {formatted_lname}"

print(format_name1(input("What is your name?"), input("What is your last name? ")))
