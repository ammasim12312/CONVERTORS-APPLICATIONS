from playground import views
from django.urls import path
# we are linking the url to the view func
urlpatterns = [
    path("calculations/",views.calculations,name="calculations"),
    path("country/",views.country),
    path("login/",views.login),
    path("options/",views.option,name="choices"),
    path("temperature/",views.temperature_converter,name="temperature"),
    path("weight/",views.Weight_Convertor,name="weight"),
    path("navigations/",views.navigations,name="navigations"),
    path("currency/",views.currency_convertor,name="currency"),
]

