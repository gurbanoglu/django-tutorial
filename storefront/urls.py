"""
URL configuration for storefront project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from quickstart import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# URLConf (URL Configuration)
urlpatterns = [
    path('admin/', admin.site.urls),

    # Any URLs that begin with 'playground/'
    # should be routed to the playground app.

    # When a request is made to the following URL, only
    # "hello" is sent to the urls.py module in the
    # "playground" app:
    # http://localhost:8000/playgroud/hello
    path('playground/', include('playground.urls')),

    # Wire up our API using automatic URL routing.
    # Additionally, we include login URLs for the browsable API.
    path('', include(router.urls)),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('snippets.urls')),

    # Configure the global URLconf in the storefront project
    # to include the URLconf defined in polls.urls.
    # include() chops off whatever part of the URL matched up
    # to that point and sends the remaining string to the
    # included URLconf for further processing.
    path("polls/", include("polls.urls"))
] + debug_toolbar_urls()