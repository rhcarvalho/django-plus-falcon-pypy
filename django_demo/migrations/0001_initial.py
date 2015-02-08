# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.contrib.auth import get_user_model


def create_super_user(apps, schema_editor):
    UserModel = get_user_model()
    UserModel._default_manager.create_superuser(
        username="admin",
        password="admin",
        email="",
    )


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(create_super_user),
    ]
