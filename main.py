import math
from decimal import Decimal
from fractions import Fraction


class Moneda():
    def __init__(self, nombreMoneda, ratioConversion):
        self.nombreMoneda = nombreMoneda
        self.ratioConversion = ratioConversion
        if isinstance(ratioConversion, str):
            numerador = Decimal(ratioConversion[0])
            denominador = Decimal(ratioConversion[2:])
            ratioDecimal = Fraction(numerador / denominador)
            self.ratioConversion = float((ratioDecimal))

    def print_moneda(self):
        print(self.nombreMoneda, self.ratioConversion)

    def universal_value(self, cantidad):
        return self.ratioConversion * cantidad


class Dinero(Moneda):

    def __init__(self, nombreMoneda, ratioConversion, cantidad):
        super().__init__(nombreMoneda, ratioConversion)
        self.cantidad = cantidad
        if isinstance(cantidad, str):
            self.cantidad = float(cantidad)

    def print_dinero(self):
        print(self.nombreMoneda, self.ratioConversion, self.cantidad)

    def valor_dinero_universal(self):
        return Moneda.universal_value(self, self.cantidad)

    def transformar_moneda(self, Moneda):
        return str(round((self.valor_dinero_universal() * math.pow(Moneda.ratioConversion, -1)), 2)) + " " + str(
            Moneda.nombreMoneda)
