'''
The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.


Sample Input 0

3
2
Sample Output 0

5
1
6


'''



if __name__ == '__main__':
    a = int(input('Enter 1st number: '))
    b = int(input('Enter 2nd number: '))
    
    add = a+b
    diff = a-b
    prod = a*b
    
    print(add)
    print(diff)
    print(prod)
