from django.urls import path, include

import items.views

urlpatterns = [
    path('', items.views.index)
]
