from django.urls import path
from hello_django.calc import views


urlpatterns = [
    path('<int:num1>/<int:num2>', views.calculate.as_view(), name='calc'),
]
