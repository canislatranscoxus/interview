'''
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

list_objs = list(student_objects)
sort_criterion = ( ('grade', True), ('age', False) )

p5 = multisort(list_objs, sort_criterion )

print( '\n grade DESC, age ASC' )
print( p5 )



