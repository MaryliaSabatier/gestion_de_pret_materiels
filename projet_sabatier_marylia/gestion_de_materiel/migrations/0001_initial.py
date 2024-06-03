# Generated by Django 5.0.6 on 2024-05-22 12:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enseignant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default='aucun', max_length=50, null=True)),
                ('prenom', models.CharField(default='aucun', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Salle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default='aucun', max_length=50, null=True)),
                ('etage', models.CharField(default='aucun', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Materiel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default='', max_length=100, null=True)),
                ('budget', models.CharField(default='', max_length=100, null=True)),
                ('possesseur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='materiels_en_possession', to='gestion_de_materiel.enseignant')),
                ('proprietaire', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='materiels_possedes', to='gestion_de_materiel.enseignant')),
                ('lieu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion_de_materiel.salle')),
            ],
        ),
        migrations.CreateModel(
            name='AccessoireMateriel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=100)),
                ('present', models.BooleanField(default=True)),
                ('etat', models.CharField(blank=True, max_length=100, null=True)),
                ('material', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion_de_materiel.materiel')),
            ],
        ),
        migrations.CreateModel(
            name='TransfertMateriel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_transfert', models.DateField()),
                ('occasion', models.CharField(max_length=100)),
                ('objectif', models.TextField()),
                ('ancien_lieu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transferts_sortants', to='gestion_de_materiel.salle')),
                ('ancien_possesseur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transferts_sortants', to='gestion_de_materiel.enseignant')),
                ('material', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion_de_materiel.materiel')),
                ('nouveau_lieu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transferts_entrants', to='gestion_de_materiel.salle')),
                ('nouveau_possesseur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transferts_entrants', to='gestion_de_materiel.enseignant')),
            ],
        ),
        migrations.CreateModel(
            name='TransfertAccessoire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ancienne_presence', models.BooleanField(default=True)),
                ('nouvelle_presence', models.BooleanField(default=True)),
                ('ancien_etat', models.CharField(blank=True, max_length=100, null=True)),
                ('nouveau_etat', models.CharField(blank=True, max_length=100, null=True)),
                ('accessoire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_de_materiel.accessoiremateriel')),
                ('transfert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_de_materiel.transfertmateriel')),
            ],
        ),
    ]
