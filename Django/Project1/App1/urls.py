from django.urls import path, include
# from .views import View1
from .views import view1

urlpatterns = [
    # path('', View1.as_view(), name='view1'),  #class based view
    path('', view1, name='view1'),  #function based view
]