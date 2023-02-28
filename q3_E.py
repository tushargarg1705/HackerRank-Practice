


'''
The provided code stub reads and integer, n, from STDIN. For all non-negative integers i<n, print i^2.

Sample Input 0

5
Sample Output 0

0
1
4
9
16
'''



if __name__ == '__main__':
    n = int(input("Enter a number upto which you want to print squares: "))
    i=0
    while(i<n):
            print(i**2)
            i+=1
