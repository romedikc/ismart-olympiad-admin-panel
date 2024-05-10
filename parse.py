import csv

# from .games.models import Category, Subcategory
from apps.teams.models import Participant

model_to_dict = {
    Participant: "apps/data/ismart2.csv"
}

def parse_data_from_csv(model_name, csv_file):
    data_list = read_csv_to_dict(csv_file)
    for data in data_list:
        model_name.objects.create(**data)


def read_csv_to_dict(file_path):
    data_list: list = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data_list.append(row)

    except Exception as e:
        print("Error found:", e)
        pass

    return data_list


def parse():
    for key, value in model_to_dict:
        try:
            parse_data_from_csv(key, value)
        except Exception as e:
            print(e)
            pass