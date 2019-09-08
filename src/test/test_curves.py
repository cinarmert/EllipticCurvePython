from src.curve_factory import CurveFactory
from src.point import Point


class CurveTests:
    @staticmethod
    def test_doubling(point, result):
        assert point.curve.double_point(point) == result

    @staticmethod
    def test_addition(p1, p2, res):
        assert (p1 + p2) == res

    @staticmethod
    def test_multiplication(n, p1, res):
        assert n * p1 == res

    @staticmethod
    def test_secp256r1():
        curve_secp256r1 = CurveFactory.get_curve_by_name('secp256r1')

        point1 = Point(0xfff97bd5755eeea420453a14355235d382f6472f8568a18b2f057a1460297556,
                       0xae12777aacfbb620f3be96017f45c560de80f0f6518fe4a03c870c36b075f297,
                       curve_secp256r1)

        point2 = Point(0x2f01e5e15cca351daff3843fb70f3c2f0a1bdd05e5af888a67784ef3e10a2a01,
                       0x5c4da8a741539949293d082a132d13b4c2e213d6ba5b7617b5da2cb76cbde904,
                       curve_secp256r1)

        # results are obtained from http://extranet.cryptomathic.com/elliptic/index
        addition_result = Point(0x499fdf9e895e719cfd64e67f07d38e3226aa7b63678949e6e49b241a60e823e4,
                                0xcac2f6c4b54e855190f044e4a7b3d464464279c27a3f95bcc65f40d403a13f5b,
                                curve_secp256r1)

        doubling_result = Point(0xd01115d548e7561b15c38f004d734633687cf4419620095bc5b0f47070afe85a,
                                0xa9f34ffdc815e0d7a8b64537e17bd81579238c5dd9a86d526b051b13f4062327,
                                curve_secp256r1)

        multiplication_result = Point(0x68809a32574292480e99bd0527e7b31a55d184759f90e05dd8c2413de25eefeb,
                                      0x12125af69bf7814f4040634090331e9c7a894139e67ad9a739bd429a1a667b,
                                      curve_secp256r1)

        CurveTests.test_doubling(point1, doubling_result)
        CurveTests.test_addition(point1, point2, addition_result)

        n = 0xaa93b72f52fa105d1bb0bdfb1f349f6c9e6f067fdb557bfe4175815bd68c68b9
        CurveTests.test_multiplication(n, point1, multiplication_result)

    @staticmethod
    def test_brainpool_p256r1():
        # is further tested with signatures
        curve_brainpool_p256r1 = CurveFactory.get_curve_by_name('brainpool-p256r1')
        generator = curve_brainpool_p256r1.generator

        n = 0xaa93b72f52fa105d1bb0bdfb1f349f6c9e6f067fdb557bfe4175815bd68c68b9
        assert curve_brainpool_p256r1.is_on_curve(n * generator) is True
        assert curve_brainpool_p256r1.is_on_curve(generator + generator) is True

    @staticmethod
    def run_tests():
        CurveTests.test_secp256r1()
        CurveTests.test_brainpool_p256r1()


if __name__ == '__main__':
    CurveTests.run_tests()
    print('passed all!')
