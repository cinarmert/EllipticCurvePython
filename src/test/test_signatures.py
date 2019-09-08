from src.curve_factory import CurveFactory
from src.test.party import Party


class TestSignatureVerification:
    def __init__(self, curve):
        super().__init__()
        self.curve = curve

    def create_parties(self):
        alice = Party(self.curve)
        bob = Party(self.curve)

        self.assertTrue(self.curve.is_on_curve(alice.get_public_key()) and self.curve.is_on_curve(bob.get_public_key()))

        return alice, bob

    def verify_signature(self):
        message = 'test message'
        alice, bob = self.create_parties()
        signature = alice.sign_message(message)
        self.assertTrue(bob.verify_signature(message, alice.get_public_key(), signature))

    @staticmethod
    def assertTrue(x):
        return x is True


if __name__ == '__main__':
    curves = CurveFactory.get_available_curves()
    for curve in curves:
        TestSignatureVerification(CurveFactory.get_curve_by_name(curve)).verify_signature()

    print('passed all!')
