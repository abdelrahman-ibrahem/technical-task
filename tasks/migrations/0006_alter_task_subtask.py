# Generated by Django 3.2 on 2022-06-11 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_task_subtask'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='subtask',
            field=models.ManyToManyField(related_name='_tasks_task_subtask_+', to='tasks.Task'),
        ),
    ]
