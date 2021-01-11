from django.urls import path
from ebooks.api.views import (EbookListCreateAPIView, EbookDetailAPIView, ReviewCreateAPIView, ReviewDetailAPIView)
# from ebooks.api.views import EbookAPIView

urlpatterns = [path('ebooks/', EbookListCreateAPIView.as_view(), name='ebook-list'),
               path('ebooks/<int:pk>/', EbookDetailAPIView.as_view(), name='ebook-detail'),
               # `ebook_pk` is from perform_create method on CreateAPIView:
               path('ebooks/<int:ebook_pk>/review/', ReviewCreateAPIView.as_view(), name='ebook-review'),
               path('reviews/<int:pk>', ReviewDetailAPIView.as_view(), name='review-detail'),
               ]
