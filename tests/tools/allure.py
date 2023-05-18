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
