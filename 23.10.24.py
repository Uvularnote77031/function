# include"stdafx.h"
# include <iostream>
def calculate_tax(income, is_retired=False, is_disabled=False):

    if income < 50000:
        base_tax_rate = 0.05
    elif income <= 100000:
        base_tax_rate = 0.10
    else:
        base_tax_rate = 0.15
    if is_retired:
        base_tax_rate -= 0.03
    if is_disabled:
        base_tax_rate -= 0.05
    final_tax_rate = max(base_tax_rate, 0)

    # Расчет итогового налога
    tax_amount = income * final_tax_rate
    return tax_amount
income = float(input("Введите уровень дохода: "))
is_retired = input("Вы пенсионер? (да/нет): ").strip().lower() == 'да'
is_disabled = input("Вы инвалид? (да/нет): ").strip().lower() == 'да'
tax = calculate_tax(income, is_retired, is_disabled)
print(f"Итоговый налог: {tax:.2f} руб.")
