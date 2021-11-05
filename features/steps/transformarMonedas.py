from behave import *

from main import *


@given(u"Tengo la moneda {nombre_moneda} con ratio de cambio {ratio_conversion}")
def step_impl(context, nombre_moneda, ratio_conversion):
    context.nombreMoneda = nombre_moneda
    context.ratioConversion = ratio_conversion
    context.moneda1 = Moneda(context.nombreMoneda, context.ratioConversion)


@given(u"la deseo transformar a {nombre_otra_moneda} que tiene ratio de cambio {otro_ratio_conversion}")
def step_impl(context, nombre_otra_moneda, otro_ratio_conversion):
    context.nombreOtraMoneda = nombre_otra_moneda
    context.otroRatioConversion = otro_ratio_conversion
    context.moneda2 = Moneda(context.nombreOtraMoneda, context.otroRatioConversion)


@when(u"cambio mis {dinero} {nombre_moneda} a {otra_moneda}")
def step_impl(context, dinero, nombre_moneda, otra_moneda):
    context.dinero = dinero
    context.nombreMoneda = context.moneda1.nombreMoneda
    context.otraMoneda = context.moneda2
    context.miDinero = Dinero(context.moneda1.nombreMoneda, context.moneda1.ratioConversion, context.dinero)
    context.cantidadCambiada = context.miDinero.transformar_moneda(context.otraMoneda)
    context.nuevoDinero = Dinero(context.otraMoneda, context.otroRatioConversion, context.cantidadCambiada)


@then(u'mi dinero es de {mi_dinero_transformado}')
def step_impl(context, mi_dinero_transformado):
    context.miDineroTransformado = mi_dinero_transformado
    assert context.nuevoDinero.cantidad == context.miDineroTransformado
