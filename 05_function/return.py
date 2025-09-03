def chai_report():
    return 100, 200

def chai_report_2():
    return 100, 200, 1010

sold, remaining = chai_report() # unpacking the tuple, this is called tuple unpacking. value must be same as the number of variables.

sold2, remaining2, _ = chai_report_2() # _ is a placeholder for the value that is not needed.



print(f"sold: {sold}\nremaining: {remaining}")