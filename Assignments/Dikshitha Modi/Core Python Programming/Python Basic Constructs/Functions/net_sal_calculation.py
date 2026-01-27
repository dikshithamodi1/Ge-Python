def cal_net_sal(gross_salary,tax_rate):
    tax_amount=gross_salary*(tax_rate/100)
    net_sal=gross_salary-tax_amount
    print("net salary:",net_sal)
gross_salary=50000
tax_rate=10
cal_net_sal(gross_salary,tax_rate)

