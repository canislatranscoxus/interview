'''

Write the code to display the following pattern:

    *
   **
  ***
 ****
*****

'''

size = 5

for i in range(1, size + 1 ):
    print( ' '*( size - i )  + '*'* i )