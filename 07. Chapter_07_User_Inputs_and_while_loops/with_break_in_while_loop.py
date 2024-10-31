# with a break added
while True:
    consent = input("Do you want to continue and buy a ticket? Enter yes or no: ")
    if consent.lower() == "no":
        print("OK, have a nice day and we'll see you back here soon")
        break
    else:
        age = int(input("How old are you?: "))
        under_3 = 'free'
        from_3_to_12 = '$10'
        over_12 = '$15'

        if age < 3:
            print(f'Your ticket is {under_3}')
        elif age >= 3 and age <= 12:
            print(f'Your ticket cost is {from_3_to_12}')
        else:
            print(f'Your ticket cost is {over_12}')
            break

