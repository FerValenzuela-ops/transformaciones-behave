Feature: Transformacion de Monedas
  Como un cliente de un centro de cambio de monedas deseo cambiar mi dinero a otra moneda.

  Scenario: Transformar CLP a ARS
    Given Tengo la moneda CLP con ratio de cambio 1/813.50
    And  la deseo transformar a ARS que tiene ratio de cambio 1/99.70
    When cambio mis 1000 CLP a ARS
    Then mi dinero es de 99.7 ARS


  Scenario: Transformar BTC a BRL
    Given Tengo la moneda BTC con ratio de cambio 1/0.000016
    And  la deseo transformar a BRL que tiene ratio de cambio 1/5.64
    When cambio mis 1000 BTC a BRL
    Then mi dinero es de 352500000.0 BRL


  Scenario: Transformar EUR a USD
    Given Tengo la moneda EUR con ratio de cambio 1/0.86
    And  la deseo transformar a USD que tiene ratio de cambio 1/1.0
    When cambio mis 1000 EUR a USD
    Then mi dinero es de 1163.0 USD

  Scenario: Transformar ARS a BTC
    Given Tengo la moneda ARS con ratio de cambio 1/99.70
    And  la deseo transformar a BTC que tiene ratio de cambio 1/0.000016
    When cambio mis 100000 ARS a BTC
    Then mi dinero es de 0.02 BTC


  Scenario: Transformar BRL a CLP
    Given Tengo la moneda BRL con ratio de cambio 1/5.64
    And  la deseo transformar a CLP que tiene ratio de cambio 1/813.50
    When cambio mis 1000 BRL a CLP
    Then mi dinero es de 143989.5 CLP

  Scenario: Transformar USD a ARS
    Given Tengo la moneda USD con ratio de cambio 1/1.0
    And  la deseo transformar a ARS que tiene ratio de cambio 1/99.70
    When cambio mis 1000 USD a ARS
    Then mi dinero es de 99700.0 ARS



#    Tasas de cambio de las monedas al 30 de Octubre de 2021
#    CLP peso chileno 1.0/813.50
#    USD dolar de EEUU 1.0/1.0
#    EUR euro de la comunidad europea 1.0/0.86
#    ARS peso argentino 1.0/99.70
#    BRL real brasileÃ±o 1.0/5.64
#    BTC Bitcoin 1.0/0.000016