from behave import *
from main import *


@given(u"Tengo la moneda {nombreMoneda} con ratio de cambio {ratioConversion}")
def step_impl(context, nombreMoneda, ratioConversion):
    context.nombreMoneda = nombreMoneda
    context.ratioConversion = ratioConversion
    context.moneda1 = Moneda(context.nombreMoneda, context.ratioConversion)


@given(u"la deseo transformar a {otraMoneda} que tiene ratio de cambio {otroRatioConversion}")
def step_impl(context, otraMoneda, otroRatioConversion):
    context.otraMoneda = otraMoneda
    context.otroRatioConversion = otroRatioConversion
    context.moneda2 = Moneda(context.otraMoneda, context.otroRatioConversion)


@when(u"cambio mis {dinero} {nombreMoneda} a {otraMoneda}")
def step_impl(context, dinero, nombreMoneda, otraMoneda):
    context.dinero = dinero
    context.nombreMoneda = context.moneda1.nombreMoneda
    context.otraMoneda = context.moneda2
    context.miDinero = Dinero(context.moneda1.nombreMoneda, context.moneda1.ratioConversion, context.dinero)
    context.resultado = context.miDinero.transformar_moneda(context.otraMoneda)


@then(u'mi dinero es de {miPlataFinal}')
def step_impl(context, miPlataFinal):
    context.miPlataFinal = miPlataFinal
    assert context.resultado == (miPlataFinal)
