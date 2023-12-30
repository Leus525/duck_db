from django.urls import path, include

import items.views

urlpatterns = [
    path('', items.views.index),
    path('insert/', items.views.insert, name='insert'),
]
