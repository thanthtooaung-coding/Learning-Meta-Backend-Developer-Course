def calculate_tax(bill, tax_rate):
    return (bill * tax_rate) / 100.00

print('Total tax', calculate_tax(175.00, 15))