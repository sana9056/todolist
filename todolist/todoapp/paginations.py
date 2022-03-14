from rest_framework.pagination import PageNumberPagination


class todoappPageNumberPagination(PageNumberPagination):
    page_size = 10

class todolistPageNumberPagination(PageNumberPagination):
    page_size = 20