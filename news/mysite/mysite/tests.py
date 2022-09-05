from django.test import TestCase
import os
# Create your tests here.

from background_task import background


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")


@background(schedule=10)
def aaa():
    print(342)


aaa()