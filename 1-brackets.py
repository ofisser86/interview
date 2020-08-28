# The number of correct bracket sequences with brackets of the same type coincides with the Catalan numbers.
# The main formula of Catalan number is Cn = (2n)! / ((n + 1)!n!)
def catalan_number(num):
    # Recursion Base case
    if num <= 1:
        return 1
    
    # Recursion Recursive case
    res_num = 0
    for i in range(num):
        res_num += catalan_number(i) * catalan_number(num - i - 1)
    return res_num

# Check if program call from the main mudule 
if __name__ == '__main__':
    pairs_of_brackets = int(input("Enter amount pairs of brackets --> "))
    print(catalan_number(pairs_of_brackets))
