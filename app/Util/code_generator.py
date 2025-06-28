import random
from ..databases import Session

def generate_code(length):
    return "".join(random.choices("0123456789",k=length))


