def exact_change(user_total):
    num_dollars = user_total//100
    user_total = user_total%100
    num_quarters = user_total//25
    user_total = user_total%25
    num_dimes=user_total//10
    user_total=user_total%10
    num_nickels = user_total//5
    user_total=user_total%5
    num_pennies = user_total
    return num_dollars,num_quarters,num_dimes,num_nickels,num_pennies

def main():
    input_val = int(input())
    num_dollars,num_quarters,num_dimes,num_nickels,num_pennies = exact_change(input_val)
    if num_dollars==0 and num_quarters==0 and num_dimes==0 and num_nickels==0 and num_pennies==0:
        print("no change")

    else:
        if num_dollars>=1:
            if num_dollars==1:
                print(num_dollars,"dollar")
            else:
                print(num_dollars,"dollars")
        if num_quarters>=1:
            if num_quarters==1:
                print(num_quarters,"quarter")
            else:
                print(num_quarters,"quarters")

        if num_dimes>=1:
            if num_dimes==1:
                print(num_dimes,"dimes")
            else:
                print(num_dimes,"dimes")

        if num_nickels>=1:
            if num_nickels==1:
                print(num_nickels,"nickel")
            else:
                print(num_nickels,"nickels")

        if num_pennies>=1:
            if num_pennies==1:
                print(num_pennies,"penny")
            else:
                print(num_pennies,"pennies")

if __name__ == '__main__':
    main()



