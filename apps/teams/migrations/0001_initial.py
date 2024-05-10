# Generated by Django 4.2.11 on 2024-05-10 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=100)),
                ('is_arrived', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_last_sumo_game', models.BooleanField(default=False)),
                ('sumo_group', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'First Group'), (2, 'Second group'), (3, 'Third group')], null=True)),
                ('sumo_total_score', models.PositiveIntegerField(default=0)),
                ('round_robin_total', models.IntegerField(db_index=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TimeCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_time', models.FloatField(default=0.0)),
                ('second_time', models.FloatField(default=0.0)),
                ('third_time', models.FloatField(default=0.0)),
                ('least_time', models.FloatField(default=0.0)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.subcategory')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.team')),
            ],
        ),
        migrations.CreateModel(
            name='TeamParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.participant')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.team')),
            ],
            options={
                'unique_together': {('team', 'participant')},
            },
        ),
        migrations.AddField(
            model_name='team',
            name='participants',
            field=models.ManyToManyField(through='teams.TeamParticipant', to='teams.participant'),
        ),
        migrations.AddField(
            model_name='team',
            name='second_subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teams_second_subcategory', to='games.subcategory'),
        ),
        migrations.AddField(
            model_name='team',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams_subcategory', to='games.subcategory'),
        ),
        migrations.CreateModel(
            name='RoundRobin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_team1', models.PositiveIntegerField(default=0)),
                ('score_team2', models.PositiveIntegerField(default=0)),
                ('team1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team1_match', to='teams.team')),
                ('team2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team2_match', to='teams.team')),
            ],
        ),
    ]
