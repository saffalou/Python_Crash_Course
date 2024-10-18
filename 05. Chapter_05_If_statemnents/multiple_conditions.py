min_age = 18
max_age = 35

rider_age = 25
#rider_age = 18
#rider_age = 35
#rider_age = 17
#rider_age = 36

# If either test fails or if both tests fail, the expression evaluates to False.

if rider_age >= min_age and rider_age<= max_age:
    print("You can ride")
else:
    print("You can't ride because of insurance requirements")



min_age = 18
max_age = 35

#rider_age = 25
#rider_age = 18
#rider_age = 35
#rider_age = 17
rider_age = 36

# The keyword or allows you to check multiple conditions as well, 
# but it passes when either or both of the individual tests pass. 
# An or expression fails only when both individual tests fail.

# the above age limits will always equate as true using "or"
if rider_age >= min_age or rider_age<= max_age:
    print("Rider conditions met")
else:
    print("Rider condition failed")


min_age = 21
max_age = 21

#rider_age = 25
#rider_age = 18
#rider_age = 35
#rider_age = 17
rider_age = 36



# changing the test age and age limits will now equate as false
if rider_age <= min_age or rider_age<= max_age:
    print("Rider conditions met")
else:
    print("Rider condition failed")