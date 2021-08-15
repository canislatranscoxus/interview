from operator import itemgetter, attrgetter


class Multi_sort:
    #

    def get_order_by( self, txt_order_by ):
        ''' take as input a string that represent an ORDER BY clause,
        and return as output a tuple of tuples.
        
        example of valid inputs:

            'grade DESC, age ASC, name'
            'ORDER BY grade DESC, age ASC, name'
            'grade desc, age asc, name'
        '''
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


    def multisort( self, list_objs, order_by ):
        ''' take as input a list of objects, and a tuple of tuples representing the
        ORDER BY clause, and return as output a sorted list of objects '''

        for key, reverse in reversed( order_by ):
            list_objs.sort( key = attrgetter( key ), reverse = reverse)

        return list_objs

    def get_sorted( self, list_objs, txt_order_by ):
        ''' take as input a list of objects, and a string representing the
        ORDER BY clause, and return as output a sorted list of objects '''

        order_by = self.get_order_by( txt_order_by )
        list_objs = self.multisort( list_objs, order_by )
        return list_objs




class Student:

    def __init__(self, name, grade, age):
        self.name   = name
        self.grade  = grade
        self.age    = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))


students = [
    Student('mary'      , 'C',  5),
    Student('john'      , 'A', 15),
    Student('saweeti'   , 'C',  5),
    Student('jane'      , 'B', 12),
    Student('elsa'      , 'C',  5),    
    Student('dave'      , 'B', 10),
]

# -----------------------------------------------------------------------------

multi_sort = Multi_sort()
txt_order_by = 'ORDER BY grade DESC, age ASC, name'
a = multi_sort.get_sorted( students, txt_order_by )

print( '\n order by clause: \n {} \n'.format( txt_order_by ) )
for i in a:
    print( i )
print( '\n' )