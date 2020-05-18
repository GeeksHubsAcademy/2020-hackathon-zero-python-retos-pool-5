#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    letras = string.ascii_letters + string.digits + string.punctuation

    return ''.join(random.choice(letras) for i in range(passLen))
