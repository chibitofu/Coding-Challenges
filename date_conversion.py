# Given a date formatted as 9/23/2019 convert it to 092319
# All single digit numbers should be prepended with a 0

def date_convert(date_input):
    split_date = date_input.split("/")
    if int(split_date[0]) < 10:
        split_date[0] = "0" + split_date[0]
    
    if int(split_date[1]) < 10:
        split_date[1] = "0" + split_date[1]

    split_date[2] = split_date[2][-2:]
    
    return ''.join(split_date)

print(date_convert("9/23/2019"))