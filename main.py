def calculate_pay_taxes_bonus(raw_pay, company_years_worked):
    net_pay = 0

    if raw_pay < 190000:
        net_pay = raw_pay - (raw_pay * 0.20)
    elif 190000 <= raw_pay < 690000:
        net_pay = raw_pay - (raw_pay * 0.25)
    elif 690000 <= raw_pay:
        net_pay = raw_pay - (raw_pay * 0.30)

    if company_years_worked <= 5:
        net_pay = net_pay + (net_pay * 0.01)
    elif company_years_worked > 5:
        net_pay = net_pay + (net_pay * 0.10)
    elif company_years_worked > 10:
        net_pay = net_pay + (net_pay * 0.20)

    print(net_pay)
    return net_pay


if __name__ == '__main__':
    calculate_pay_taxes_bonus(120000, 4)
