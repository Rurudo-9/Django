import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'learning_log.settings')

import django
django.setup()

from MainApp.models import Topic, Entry
topics = Topic.objects.all()

t = Topic.objects.get(id=1)

print(t)

entries = t.entry_set.all()

for entry in entries:
    print(entry)

'''
from django.contrib.auth.models import User

for user in User.objects.all():
    print(user.username, user.id)




for t topics:
    print(f"Topic ID: {t.id}  Topic: {t}")

entries = t.entry_set.all()

print(t.text)
print(t.date_added)


'''
