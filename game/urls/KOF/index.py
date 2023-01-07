from django.urls import path, re_path
from game.views.KOF.index import index

urlpatterns = [
        re_path(r".*", index, name="kof_index"),
        
]


