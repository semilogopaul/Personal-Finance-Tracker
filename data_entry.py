from datetime import datetime

date_format = '%d-%m-%Y'
CATEGORIES = {'I': 'Income', 'E': 'Expense'}

def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except Exception as e:
        print(f'Invalid date format: {e}')
        return get_date(prompt, allow_default)
        

def get_amount():
    try:
        amount = float(input('Enter the amount: '))
        if amount <=0:
            raise ValueError('Amount must be greater than 0')
        return amount
    except ValueError as e:
        print(f'Invalid amount: {e}')
        return get_amount()

def get_category():
    category = input("Enter the category ('I' for Income or 'E' for Expense): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    print("Invalid category, Please enter 'I' for Income or 'E' for Expense")
    return get_category()
    

def get_description():
    return input('Enter a description (optional): ')
