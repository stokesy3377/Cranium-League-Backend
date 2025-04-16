import openpyxl

workbook = openpyxl.load_workbook('CL_S1.xlsx')
worksheet = workbook.active

def get_numeric(cell):
    val = worksheet[cell].value
    try:
        return float(val)
    except (TypeError, ValueError):
        return 0

x = 5
while x <= 13:
    current_balance = get_numeric('I' + str(x))
    previous_balance = get_numeric('H' + str(x)) + get_numeric('N' + str(x))

    # Uncomment below if updating H column is needed
    worksheet['H' + str(x)].value = previous_balance + current_balance

    worksheet['G' + str(x)].value = 0
    worksheet['N' + str(x)].value = 0

    x += 1

workbook.save('CL_S1.xlsx')
print("Current balance copied to previous balance.")
