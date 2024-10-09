# Generated by Django 3.2.25 on 2024-10-07 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0059_auto_20240329_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('stage', models.CharField(choices=[('sourcing', 'Sourcing'), ('due_diligence', 'Due Diligence'), ('closing', 'Closing'), ('completed', 'Completed')], max_length=50)),
                ('investment_size', models.DecimalField(decimal_places=2, max_digits=12)),
                ('valuation', models.DecimalField(decimal_places=2, max_digits=12)),
                ('irr_target', models.DecimalField(decimal_places=2, max_digits=5)),
                ('acquisition_date', models.DateField(blank=True, null=True)),
                ('company_name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('commitment', models.DecimalField(decimal_places=2, max_digits=12)),
                ('distributions', models.DecimalField(decimal_places=2, max_digits=12)),
                ('last_contact', models.DateField(blank=True, null=True)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioCompany',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('industry', models.CharField(max_length=255)),
                ('date_of_acquisition', models.DateField()),
                ('total_investment', models.DecimalField(decimal_places=2, max_digits=12)),
                ('revenue', models.DecimalField(decimal_places=2, max_digits=12)),
                ('ebitda', models.DecimalField(decimal_places=2, max_digits=12)),
                ('company_overview', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioCompanyPerformance',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('report_date', models.DateField()),
                ('revenue', models.DecimalField(decimal_places=2, max_digits=12)),
                ('ebitda', models.DecimalField(decimal_places=2, max_digits=12)),
                ('net_profit', models.DecimalField(decimal_places=2, max_digits=12)),
                ('employee_count', models.IntegerField()),
                ('portfolio_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.portfoliocompany')),
            ],
        ),
    ]