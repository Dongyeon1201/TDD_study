from django.urls import path

from user.views import UserAPIViewSet

urlpatterns = [path("", UserAPIViewSet.as_view({"get": "list"}), name="test")]
