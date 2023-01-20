# Generated by Django 4.0.8 on 2023-01-01 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50, verbose_name='Job Category name')),
                ('subcategory_of', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='childrencategory', to='jobs.category')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100, verbose_name='Job Location')),
                ('description', models.TextField(max_length=500, verbose_name='Job Description')),
                ('timing', models.CharField(max_length=100, verbose_name='Job Time')),
                ('experience', models.CharField(max_length=100, verbose_name='Experience')),
                ('type', models.CharField(choices=[('1', 'Physical'), ('2', 'Remote')], default='1', max_length=20)),
                ('title', models.CharField(max_length=100, verbose_name='Job Title')),
                ('industry', models.CharField(max_length=100, verbose_name='Industry')),
                ('is_active', models.BooleanField(default=True)),
                ('salary', models.CharField(max_length=100, verbose_name='Salary Offered')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.CharField(blank=True, max_length=200, null=True)),
                ('category', models.ManyToManyField(related_name='jobs', to='jobs.category', verbose_name='Job Cateogry')),
            ],
        ),
    ]
