from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserForm
from .models import User
from django.urls import reverse

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)


def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})


def user_create_view(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = UserForm()

    context = {
        'form': form
    }
    return render(request, 'user-create.html', context)


# def user_single_view(request):
#     obj = User.objects.get(id=1)
#     # context = {
#     #     'email': obj.email,
#     #     'number': obj.number
#     # }
#     context = {
#         'object': obj
#     }
#     return render(request, 'user-single.html', context)


def dynamic_lookup_view(request, id):
    # obj = User.objects.get(id=id)
    odj = get_object_or_404(User, id=id)
    # try:
    #     obj = User.objects.get(id=id)
    # except User.DoesNotExist:
    #     raise Http404
    context = {
        'object': odj
    }
    return render(request, 'user-single.html', context)


def user_delete_view(request, id):
    odj = get_object_or_404(User, id=id)
    if request.method == 'POST':
        odj.delete()
        return redirect('../../')
    context = {
        'object': odj
    }
    return render(request, 'user-delete.html', context)

def user_list_view(request):
    queryset = User.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'user-list.html', context)


class UserListView(ListView):
    template_name = 'user-list.html'
    queryset = User.objects.all()


class UserSingleView(DetailView):
    template_name = 'user-single.html'
    queryset = User.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(User, id=id_)


class UserCreateView(CreateView):
    template_name = 'user-create.html'
    form_class = UserForm
    queryset = User.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class UserUpdateView(UpdateView):
    template_name = 'user-create.html'
    form_class = UserForm

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(User, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class UserDeleteView(DeleteView):
    template_name = 'user-delete.html'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(User, id=id_)

    def get_success_url(self):
        return reverse('user-list')