from random import randint
from gmpy import invert
from dataclasses import dataclass
from hashlib import sha1
from base64 import b64encode

'''
Signing and signature verification are implemented according to the ECDSA paper (see the link below)
http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.472.9475&rep=rep1&type=pdf
'''


class Party:
    @dataclass
    class Signature:
        r: int
        s: int

    def __init__(self, curve):
        self.curve = curve
        self.d = randint(0, curve.order)

    def get_public_key(self):
        return self.d * self.curve.generator

    @staticmethod
    def hash_message(message):
        message_bytes = bytes(message, 'utf-8')
        hash_bytes = sha1(b64encode(message_bytes)).digest()
        return int.from_bytes(hash_bytes, 'big')

    def sign_message(self, message):
        r, s = 0, 0
        while s == 0 or r == 0:
            k = randint(1, self.curve.order)
            r = (k * self.curve.generator).x
            k_inverse = invert(k, self.curve.order) % self.curve.order
            hashed_message = self.hash_message(message)
            s = (k_inverse * (hashed_message + self.d * r)) % self.curve.order

        return Party.Signature(r, s)

    def verify_signature(self, message, signer_public, signature):
        r, s = signature.r, signature.s
        assert 0 < r < self.curve.order and 0 < s < self.curve.order
        hashed_message = self.hash_message(message)
        w = invert(s, self.curve.order) % self.curve.order
        u1 = int((hashed_message * w) % self.curve.order)
        u2 = int((r * w) % self.curve.order)
        X = u1 * self.curve.generator + u2 * signer_public

        if X.x % self.curve.order == r:
            return True
        else:
            return False
