from django.urls import path
from django.views.decorators.cache import cache_page

from mail.apps import MailConfig
from mail.views import ClientListView

app_name = MailConfig.name

urlpatterns = [
    # path('', HomeListView.as_view(), name='home'),
    path('clients/', cache_page(60)(ClientListView.as_view()), name='client_list'),
    # path('contacts/', ContactsView.as_view(), name='contacts'),
    # path('products/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product'),
    #
    # path('products/create/', ProductCreateView.as_view(), name='product_create'),
    # path('products/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    # path('products/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    #
    # path('categories/', CategoryListView.as_view(), name='category_list'),
]