import math
from decimal import Decimal
from fractions import Fraction


class Moneda:
    def __init__(self, nombre_moneda, ratio_conversion):
        self.nombreMoneda = nombre_moneda
        self.ratioConversion = ratio_conversion
        if isinstance(ratio_conversion, str):
            numerador = Decimal(ratio_conversion[0])
            denominador = Decimal(ratio_conversion[2:])
            ratio_decimal = Fraction(numerador / denominador)
            self.ratioConversion = float(ratio_decimal)

    def print_moneda(self):
        print(self.nombreMoneda, self.ratioConversion)

    def universal_value(self, cantidad):
        return round(float(self.ratioConversion * cantidad))


class Dinero(Moneda):

    def __init__(self, nombre_moneda, ratio_conversion, cantidad):
        super().__init__(nombre_moneda, ratio_conversion)
        self.cantidad = cantidad
        if isinstance(cantidad, str):
            self.cantidad = float(cantidad)
        elif isinstance(cantidad, tuple):
            self.cantidad = cantidad[0]

    def print_dinero(self):
        print(self.nombreMoneda, self.ratioConversion, self.cantidad)

    def valor_dinero_universal(self):
        return float(Moneda.universal_value(self, self.cantidad))

    def transformar_moneda(self, moneda):
        calculo = float(round(self.valor_dinero_universal() * math.pow(moneda.ratioConversion, -1), 2))
        calculo_str = f"{calculo} {moneda.nombreMoneda}"
        return calculo_str, Dinero(moneda.nombreMoneda, moneda.ratioConversion, calculo)

# Ejemplos de creacion de objeto, se usa la misma logica con behave
# pesoChileno = Moneda('CLP', 1.0 / 812.50)
# pesoArgentino = Moneda('ARS', 1.0 / 99.70)
# dolarUSD = Moneda('USD', 1.0 / 1.0)
# euro = Moneda('EUR', 1.0 / 0.86)
# realBr = Moneda('BRL', 1.0 / 5.64)
# bitCoin = Moneda('BTC', 1.0 / 0.000016)
#
#
# dineroChileno = Dinero(pesoChileno.nombre_moneda, pesoChileno.ratio_conversion, 1000)
# dineroArgentino = Dinero(pesoArgentino.nombre_moneda, pesoArgentino.ratio_conversion, 122.56)
# dineroUSD = Dinero(dolarUSD.nombre_moneda, dolarUSD.ratio_conversion, 1000)
# dineroEuro = Dinero(euro.nombre_moneda, euro.ratio_conversion, 1000)
# dineroBR = Dinero(realBr.nombre_moneda, realBr.ratio_conversion, 10000000)
# dineroBTC = Dinero(bitCoin.nombre_moneda, bitCoin.ratio_conversion, 1000)
#
