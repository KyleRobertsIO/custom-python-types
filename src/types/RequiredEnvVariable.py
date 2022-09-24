from src.exceptions.NoneTypeError import NoneTypeError

from typing import Optional
from os import getenv

class RequiredEnvVariable:
    """
    Type for collecting required environment variable from the operating system.

    Use this type so that applications/scripts will fail on initialization because of missing
    required configuration.
    """
    def __init__(self, envVarName: Optional[str]):
        try:
            envVarValue: Optional[str] = getenv(envVarName)
        except TypeError:
            raise TypeError("Passed environment variable name was 'NoneType' when 'str' was expected.")
        if envVarValue == None:
            raise NoneTypeError()
        self.value = envVarValue

    def __str__(self) -> str:
        return self.value

    def __len__(self) -> int:
        return len(self.value)