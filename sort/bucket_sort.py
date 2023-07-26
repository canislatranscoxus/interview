'''
Bucket sort is used to sort an array or list of float numbers
in a range from 0 to 1.

links:
https://en.wikipedia.org/wiki/Bucket_sort

'''
import random

def bucket_sort( array, num_of_buckets = 10 ):

    # create buckets
    buckets = [ [] for i in range( num_of_buckets ) ]

    # insert values in buckets
    for value in array:
        b = int( value * 10 )
        buckets[ b ].append( value )

    # sort every bucket
    for bucket in buckets:
        bucket.sort()

    # create sorted array (or list) by concatenating buckets values
    sorted_arr = []
    for bucket in buckets:
        for i in bucket:
            sorted_arr.append( i )
        
    return sorted_arr



def generate_random_floats( num_of_items = 10, decimal_places = 2 ):
    data = []
    for i in range( 0, num_of_items ):
        n = random.uniform( 0.00, 0.99 )
        n = round( n, decimal_places )
        data.append( n )
    
    return data




data = generate_random_floats()
s = bucket_sort( data )

print( '\n\n Bucket sort \n' )
print( 'original data: {}'.format( data ) )
print( 'sorted data: {}'.format( s ) )