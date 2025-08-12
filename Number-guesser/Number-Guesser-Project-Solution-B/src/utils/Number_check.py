def valid_number(input_num):


    if not input_num.isdigit():
        print("Eror! Please try agian (pleaas enter int number)")
        return False

    input_num = int(input_num)

    if input_num > 100 or input_num < 1:
        print("your nubmer is out if range (The range is 1 to 100)")
        return False

    return True
