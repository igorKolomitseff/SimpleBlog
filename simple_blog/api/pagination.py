from django.conf import settings
from rest_framework.pagination import PageNumberPagination


class BasePagination(PageNumberPagination):
    page_size = settings.PAGE_SIZE
