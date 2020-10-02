

class BinaryNode:
    data   = None
    left   = None
    right  = None
    parent = None

    def __init__( self, data, parent=None ):
        self.data   = data
        self.parent = parent
