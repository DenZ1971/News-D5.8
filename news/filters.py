# from django_filters import FilterSet, DateTimeFilter, ModelChoiceFilter, CharFilter
from django.forms import DateTimeInput
import django_filters
from .models import *


# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(django_filters.FilterSet):
    post_title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Название публикации'
    )

    added_after = django_filters.DateTimeFilter(
        field_name='timeCreation',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'}),
        label='Не старше'

    )

    post_category = django_filters.ModelChoiceFilter(
        field_name='postCategory',
        queryset=Category.objects.all(),
        label='Категория публикации'

    )

    # class Meta:
    # В Meta классе мы должны указать Django модель,
    # в которой будем фильтровать записи.
    # model = Post
    # В fields мы описываем по каким полям модели
    # будет производиться фильтрация.
    # fields = {

    # 'title',
    # 'timeCreation',
    # 'postCategory'
    # }
