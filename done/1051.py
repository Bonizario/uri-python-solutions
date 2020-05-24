# 1051 Taxes
salary = float(input())
taxes = 0

if salary <= 2000:
    print("Isento")
elif (salary >= 2000.01) and (salary <= 3000):
    tax_8 = salary - 2000
    taxes += tax_8 * 0.08
    print("R$ {:.2f}".format(taxes))
elif (salary >= 3000.01) and (salary <= 4500):
    tax_18 = salary - 3000
    tax_8 = salary - 2000 - tax_18
    taxes += tax_18 * 0.18 + tax_8 * 0.08
    print("R$ {:.2f}".format(taxes))
elif (salary >= 4500.01):
    tax_28 = salary - 4500
    tax_18 = salary - 3000 - tax_28
    tax_8 = salary - 2000 - tax_28 - tax_18
    taxes += tax_28 * 0.28 + tax_18 * 0.18 + tax_8 * 0.08
    print("R$ {:.2f}".format(taxes))
