def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer value."
    if n > 0:
        num_string = ''
        for num in range(1,n+1):
            num_string += str(num)
            if num < n:
                num_string += " "
        return num_string
    else:
        return "Argument must be an integer greater than 0."
print(number_pattern(-4))