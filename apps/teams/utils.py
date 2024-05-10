from apps.teams.models import Team


def top_teams(group_number):
    teams_in_group = Team.objects.filter(sumo_group=group_number)
    ranked_teams = teams_in_group.order_by('-round_robin_total')
    if ranked_teams[2].round_robin_total == ranked_teams[3].round_robin_total:
        return ranked_teams[:4]
    else:
        return ranked_teams[:3]
