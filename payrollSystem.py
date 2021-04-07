def payroll():
    hrs, rate, salary = dataentry()
    normal_hrs, overtime_hrs, overtime= computepay(hrs, rate)
    reguralpay, total_pay_overtime = preovertime_hrs (hrs, rate,overtime, salary)
    displyPay(rate, normal_hrs, overtime_hrs, reguralpay, total_pay_overtime, salary)


def dataentry():
    name = input('Name of Staff>  ')
    hrs = float(input('Enter week hrs >  '))
    rate = float(input('Enter the pay rate >  '))
    salary= float (input('salary>  '))
    return hrs, rate, salary


def computepay(hrs, rate):
    if hrs < 40:
        normal_hrs=hrs
        overtime_hrs=0
    else:
        normal_hrs=40
        overtime_hrs = hrs-40
    if hrs > 40:
        overtimerate = 3.5 * rate
        overtime = (hrs-40) * overtimerate
    else:
        overtime = 0
    return normal_hrs, overtime_hrs, overtime


def preovertime_hrs(hrs, rate, overtime, salary):
    reguralpay = salary
    total_pay_overtime = reguralpay + overtime
    return reguralpay, total_pay_overtime


def displyPay (rate, normal_hrs, overtime_hrs, reguralpay, total_pay_overtime, salary):
    print('Salary $' + format(reguralpay, '.2f'))
    print('Total $' + format(total_pay_overtime, '.2f'))


payroll()

