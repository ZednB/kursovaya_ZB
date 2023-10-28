import json


def get_operations():
    """ Получает данные из файла operations.json"""
    with open('json', "r") as file:
        data = json.load(file)
        return data


def remove_empty_items(data):
    """ Удаление пустых элементов из списка"""
    return [d for d in data if "date" in d]


def sort_key(e):
    """ Ключ для сортировки файла по дате"""
    return e["date"]


def sort_datas(data):
    """ Сортировка данных по дате от большей к меньшей"""
    data.sort(reverse=True, key=sort_key)
    return data


def filter_executed(data):
    """Фильтрация данных по статусу EXECUTED"""
    return [d for d in data if d['state'] == "EXECUTED"]


def get_first_number_last(data, number_last):
    """Возврат первых number_last значений для отображения"""
    return data[:number_last]


def get_result_data(number_last):
    """Подготовка data для вывода"""
    get_data = get_operations()
    remove_data = remove_empty_items(get_data)
    sort_data = sort_datas(remove_data)
    executed_data = filter_executed(sort_data)
    result_data = get_first_number_last(executed_data, number_last)
    return result_data


# def filter_json(data):
#     """Фильтрация данных по статусу EXECUTED"""
#     return [d for d in data if d['state'] == "EXECUTED"]
#
#
# def sort_transactions_by_date(transactions_data):
#     sorted_transactions = sorted(transactions_data, key=lambda x: datetime.fromisoformat(x['date']), reverse=True)
#     return sorted_transactions
#
#
# def print_last_five_transactions(transactions_data):
#     sorted_transactions = sort_transactions_by_date(transactions_data)
#     last_five_transactions = sorted_transactions[:5]
#     for transaction in last_five_transactions:
#         return transaction
#
#
# def get_date_and_description(transaction):
#     """Функция возвращает дату совершения операции"""
#     date = transaction['date']
#     parsed_date = datetime.fromisoformat(date)
#     formatted_date = parsed_date.strftime("%d.%m.%Y")
#     description = transaction.get('description', '')
#     return formatted_date, description
#
#
# def print_from_word(transaction):
#     """А эта возвращает название платежной системы
#     карты с которого была совершена операция"""
#     source = transaction.get('from', '')
#     parts = source.split()
#     from_word = parts[0] if len(parts) > 0 else ''
#     return f"{from_word}"
#
#
# def get_account_number(transaction):
#     """Функция берет первые четыре
#     цифры с номера карты"""
#     account_info = transaction.get('from', '')
#     parts = account_info.split()
#     if len(parts) > 1:
#         account_number = parts[1]
#         first_six_digits = account_number[:4]
#         return account_info, first_six_digits
#     return account_info, ''
#
#
# def get_account_number1(transaction):
#     """Функция берет пятую
#     и шестую цифру с номера карты"""
#     account_info = transaction.get('from', '')
#     parts = account_info.split()
#     if len(parts) > 1:
#         account_number = parts[1]
#         two_digits = account_number[4:6]
#         return account_info, two_digits
#     return account_info, ''
#
#
# def from_four_numbers(transaction):
#     """Функция берет последние четыре
#     цифры с номера карты, с которого совершен первевод"""
#     account_info = transaction.get('from', '')
#     parts = account_info.split()
#     if len(parts) > 1:
#         account_number = parts[1]
#         last_four_digits = account_number[-4:]
#         return last_four_digits
#
#
# def print_from_word1(transaction):
#     """Функция берет первое слово чтобы
#     узнать платежную систему"""
#     source = transaction.get('to', '')
#     parts = source.split()
#     from_word = parts[0] if len(parts) > 0 else ''
#     return f"{from_word}"
#
#
# def from_four_numbers1(transaction):
#     """Последние четыре цифры второй карты"""
#     account_info = transaction.get('to', '')
#     parts = account_info.split()
#     if len(parts) > 1:
#         account_number = parts[1]
#         last_four_digits = account_number[-4:]
#         return last_four_digits
#
#
# def amount1(transaction):
#     """Сумма перевода и валюта"""
#     amount = transaction['operationAmount']['amount']
#     currency_name = transaction['operationAmount']['currency']['name']
#     return amount, currency_name
