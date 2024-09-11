from decimal import Decimal

from ons_python_template_keh_evisos.calculator import Calculator

calc = Calculator()

query_1 = calc.add(Decimal("10"))
print(query_1)

query_2 = calc.add(Decimal("20"))
print(query_2)

query_3 = calc.multiply(Decimal("2"))
print(query_3)

query_4 = calc.divide(Decimal("30"))
print(query_4)
