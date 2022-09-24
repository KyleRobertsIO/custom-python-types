class NoneTypeError(Exception):
    '''
    Exception to be raised when a variable is expected to not be NoneType.
    '''
    def __init__(self):
        super().__init__(
            "Variable value was determined to be NoneType which is not allowed."
        )