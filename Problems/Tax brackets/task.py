income = int(input())
precent = 0
calculated_tax = 0

if income >= 0 and income <= 15527:
    precent = 0
    calculated_tax = income * precent
elif income >= 15528 and income <= 42707:
    precent = 15
    calculated_tax = income * precent / 100
elif income >= 42708 and income <= 132406:
    precent = 25
    calculated_tax = income * precent / 100
elif income >= 132407:
    precent = 28
    calculated_tax = income * precent / 100
calculated_tax = round(calculated_tax)
print(f'The tax for {income} is {precent}%. That is {calculated_tax} dollars!')
