from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import Todo
from .forms import TodoForm

class HomeViewList(generic.View):
    template_name = "home/index.html"
    context = {}

    def get(self, request, *args, **kwargs):
        filter_type = request.GET.get("filter")
        queryset = Todo.objects.all()

        if filter_type == "ids":
            queryset = queryset.only("id")
        elif filter_type == "ids_titles":
            queryset = queryset.only("id", "title")
        elif filter_type == "ids_users":
            queryset = queryset.only("id", "userId")
        elif filter_type == "ids_titles_unresolved":
            queryset = queryset.filter(completed=False).only("id", "title")
        elif filter_type == "ids_users_unresolved":
            queryset = queryset.filter(completed=False).only("id", "userId")
        elif filter_type == "ids_titles_resolved":
            queryset = queryset.filter(completed=True).only("id", "title")
        elif filter_type == "ids_users_resolved":
            queryset = queryset.filter(completed=True).only("id", "userId")

        self.context = {
            "todos": queryset,
            "filter_type": filter_type
        }
        return render(request, self.template_name, self.context)


class Create(generic.CreateView):
    template_name = "home/create.html"
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy("home")

class Detail(generic.DetailView):
    template_name = "home/detail.html"
    model = Todo

class Update(generic.UpdateView):
    template_name = "home/update.html"
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy("home")


class Delete(generic.DeleteView):
    template_name = "home/delete.html"
    model = Todo
    success_url = reverse_lazy("home")
