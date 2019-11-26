def leap_year(year):
    """Take in a year and determines if it's a leap year"""
    
    ## Is the year evenly divisible by 4
    if year % 4 is 0:
        ## Is not evenly divisible by 100
        ## Unless it's also evenly divisible by 400
        if year % 100 is 0 and year % 400 is 0:
            return True
        elif year % 100 is not 0:
            return True
        else:
            return False
    else:
        return False


print(leap_year(1997))
print(leap_year(1996))
print(leap_year(1900))
print(leap_year(2000))