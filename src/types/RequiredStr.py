from src.exceptions.NoneTypeError import NoneTypeError

from typing import Optional

class RequiredStr:
    '''
    Type for collecing required string variables.
    '''

    def __init__(self, string: Optional[str]):
        if string == None:
            raise NoneTypeError()
        self.value = string
    
    def __str__(self) -> str:
        return self.value
    
    def __len__(self) -> int:
        return len(self.value)