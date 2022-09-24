from src.types.RequiredEnvVariable import RequiredEnvVariable

SYSTEM_USER = RequiredEnvVariable("USER")

print(SYSTEM_USER)

def strLength(val: str):
    print(len(val))

strLength(SYSTEM_USER)