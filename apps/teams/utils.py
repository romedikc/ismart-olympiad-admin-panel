from apps.teams.models import Team, Participant
import csv

def top_teams(group_number):
    teams_in_group = Team.objects.filter(sumo_group=group_number)
    ranked_teams = teams_in_group.order_by('-round_robin_total')
    if ranked_teams[2].round_robin_total == ranked_teams[3].round_robin_total:
        return ranked_teams[:4]
    else:
        return ranked_teams[:3]
    

model_to_dict = {
    Participant: "apps/data/ismart2.csv"
}

def parse_data_from_csv(model, csv_file):
    data_list = read_csv_to_dict(csv_file)
    for data in data_list:
        model.objects.create(school=data['school'],
                             name=data['name'],
                             subcategory=data['subcategory'],
                             second_subcategory=data['second_subcategory'])

def read_csv_to_dict(file_path):
    data_list = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data_list.append(row)
    except Exception as e:
        print("Error found:", e)
    return data_list

def parse():
    for model, csv_file in model_to_dict.items():
        try:
            parse_data_from_csv(model, csv_file)
        except Exception as e:
            print(e)

parse()