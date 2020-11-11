from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_forms', '0013_add_field_is_enable_autofill_from_url_params'),
    ]

    operations = [
        migrations.AddField(
            model_name='formsubmission',
            name='user_id',
            field=models.IntegerField(default=False, help_text="User", verbose_name='User'),
        ),
    ]
