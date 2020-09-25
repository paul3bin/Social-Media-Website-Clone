from django.shortcuts import render
from .models import Group, GroupMember
from django.contrib.auth.mixins import (LoginRequiredMixin, PermissionRequiredMixin)
from django.urls import reverse
from django.views import generic


class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields = ('name','description')
    model = Group

class SingleGroup(generic.DetailView):
    model = Group

class ListGroup(generic.ListView):
    model = Group