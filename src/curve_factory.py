from src.elliptic_curve import EllipticCurve


class CurveFactory:
    available_curves = {
        "secp256r1": {
            'size': 256,
            'p': 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f,
            'a': 0,
            'b': 7,
            'gx': 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
            'gy': 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8,
            'order': 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
        },

        "brainpool-p256r1": {
            'size': 256,
            'p': 0xa9fb57dba1eea9bc3e660a909d838d726e3bf623d52620282013481d1f6e5377,
            'a': 0x7d5a0975fc2c3057eef67530417affe7fb8055c126dc5c6ce94a4b44f330b5d9,
            'b': 0x26dc5c6ce94a4b44f330b5d9bbd77cbf958416295cf7e1ce6bccdc18ff8c07b6,
            'gx': 0x8bd2aeb9cb7e57cb2c4b482ffc81b7afb9de27e1e3bd23c23a4453bd9ace3262,
            'gy': 0x547ef835c3dac4fd97f8461a14611dc9c27745132ded8e545c1d54c72f046997,
            'order': 0xa9fb57dba1eea9bc3e660a909d838d718c397aa3b561a6f7901e0e82974856a7
        }
    }

    @staticmethod
    def get_curve_by_name(name):
        if name not in CurveFactory.available_curves.keys():
            raise CurveNotAvailableError

        return EllipticCurve(**CurveFactory.available_curves[name])

    @staticmethod
    def get_available_curves():
        return CurveFactory.available_curves


class CurveNotAvailableError(ValueError):
    pass
