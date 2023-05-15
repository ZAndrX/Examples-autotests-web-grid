import csv
from io import StringIO
import allure


@allure.step('Прикрепление csv файла')
def attach_table(table_dict: list[dict], name_file: str) -> None:
    """
    Прикрепление csv файла
    :param table_dict: Словарь с данными таблицы table_to_dict
    :param name_file: Имя файла
    """
    csv_content = StringIO()
    writer = csv.DictWriter(csv_content, fieldnames=table_dict[0].keys())
    writer.writeheader()
    for line in table_dict:
        writer.writerow(line)
    allure.attach(csv_content.getvalue(), name=name_file, attachment_type=allure.attachment_type.CSV)


@allure.step('Поиск по словарю значений в table_dict')
def search_in_table_dict(table_dict, regex_dict):
    result = []
    for line_dict in table_dict:
        is_match = True
        for key_regex, value_regex in regex_dict.items():
            try:
                if line_dict[key_regex] != value_regex:
                    is_match = False
                    break
            except KeyError:
                is_match = False
                break
        if is_match:
            result.append(line_dict)
    return result
