"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from account.views import home_view, user_create_view, dynamic_lookup_view, user_delete_view, user_list_view,\
    UserListView, UserSingleView, UserCreateView, UserUpdateView, UserDeleteView

urlpatterns = [
    # path('', user_list_view, name='user-list'),
    path('', UserListView.as_view(), name='user-list'),
    # path('user/<int:id>', dynamic_lookup_view, name='user'),
    path('user/<int:id>', UserSingleView.as_view(), name='user'),
    path('admin/', admin.site.urls),
    # path('create/', user_create_view),
    path('create/', UserCreateView.as_view(), name='user-create'),
    path('user/<int:id>/update/', UserUpdateView.as_view(), name='user-update'),
    # path('user/<int:id>/delete/', user_delete_view, name='user-delete'),
    path('user/<int:id>/delete/', UserDeleteView.as_view(), name='user-delete'),
]
