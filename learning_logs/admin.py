from django.contrib import admin

from learning_logs.models import Topic, Entry

# tells django to manage model via admin site
admin.site.register(Topic)
admin.site.register(Entry)
