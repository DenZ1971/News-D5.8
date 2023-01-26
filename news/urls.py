from .views import PostsList, PostDetail, PostCreate, PostUpdate, PostDelete, upgrade_user
from django.urls import path

urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', PostsList.as_view(), name='post_list'),
   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('<int:pk>', PostDetail.as_view()),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('create/<int:pk>/edit/', PostUpdate.as_view(), name='post_edit'),
   path('create/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('upgrade/', upgrade_user, name='upgrade_user')
]