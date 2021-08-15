'''
https://docs.python.org/3/howto/sorting.html
https://docs.python.org/3/howto/sorting.html
'''
from operator import itemgetter, attrgetter


class Student:

    def __init__(self, name, grade, age):
        self.name   = name
        self.grade  = grade
        self.age    = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))


student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]


def multisort(xs, specs):
    print( 'multisort () '    )
    print( 'reversed specs: {}'.format( reversed(specs) ) )


    print( '\n loop \n' )
    for key, reverse in reversed(specs):
        print( 'key: {}'.format( key ) )
        
        xs.sort( key = attrgetter(key), reverse = reverse)

    return xs

# -----------------------------------------------------------------------------

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
p1 = sorted(student_tuples, key=itemgetter(2))
print( '\n using itemgetter 2, age' )
print( p1 )
#[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

p2 = sorted(student_objects, key=attrgetter('age'))
print( '\n using attrgetter age' )
print( p2 )

# -----------------------------------------------------------------------------


p3 = sorted(student_tuples, key=itemgetter(2), reverse=True)
print( '\n descending 2' )
print( p3 )

p4 = sorted(student_objects, key=attrgetter('age'), reverse=True)
print( '\n descending age' )
print( p4 )

# -----------------------------------------------------------------------------
DESC = True
ASC  = False
#p5 = multisort(list(student_objects), (('grade', True), ('age', False)))

list_objs = list( student_objects )
sort_criterion = ( ('grade', DESC), ('age', ASC) )

p5 = multisort( student_objects , sort_criterion )
#p5 = multisort(list_objs, sort_criterion )

print( '\n grade DESC, age ASC' )
print( p5 )

# -----------------------------------------------------------------------------

# create sort criterion
# 
#  
txt_order_by = 'grade DESC, age ASC, name'

def get_order_by( txt_order_by ):
    order_by = ()

    txt_order_by = txt_order_by.lower().strip()
    if txt_order_by.startswith( 'order by ' ):
        txt_order_by = txt_order_by.replace( 'order by ', '' )

    a = txt_order_by.split( ',' )
    for s in a:
        
        s = s.lower().strip()
        criterion = s.split()

        if len( criterion ) == 0 or len( criterion ) > 2:
            print( '''Every ORDER BY criterion, must have maximum 2 words, 
            one for column, and one for ascending or descending order.
            Example: grade DESC, age ASC, name
            ''' )
            raise

        column = criterion[ 0 ]
        reverse = False

        if len( criterion ) == 2:
            reverse = criterion[1] == 'desc'

        t = ( column, reverse )   
        order_by = order_by + (t,) 
    return order_by

order_by = get_order_by( txt_order_by )
print( order_by )
# -----------------------------------------------------------------------------


list_objs = list(student_objects)
p6 = multisort(list_objs, order_by )

print( '\n {}'.format( txt_order_by ) )
print( p6 )
