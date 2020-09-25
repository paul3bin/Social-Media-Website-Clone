from django.contrib import admin
from . import models
# Register your models here.

# This class enables for a dbadmin to click on row containing the group details and edit group members from the same.
class GroupMemberInLine(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)