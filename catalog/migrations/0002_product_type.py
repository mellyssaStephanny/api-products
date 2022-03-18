from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.IntegerField(choices=[(1, 'TV'), (2, 'Celular'), (4, 'Notebook')], default=1),
            preserve_default=False,
        ),
    ]
