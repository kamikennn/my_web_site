from django.urls import path
from .views import (
    InquiryListView,
    InquiryUpdateView,
    InquiryDetailView,
    InquiryDeleteView,
    InquiryCreateView,
    ContactView,
)

urlpatterns = [
    path('<int:pk>/edit/', InquiryUpdateView.as_view(), name='inquiry_edit'),
    path('<int:pk>/',InquiryDetailView.as_view(), name='inquiry_detail'),
    path('<int:pk>/delete/',InquiryDeleteView.as_view(),name='inquiry_delete'),
    path('new/', InquiryCreateView.as_view(), name='inquiry_new'),
    path('',InquiryListView.as_view(),name='inquiry_list'),
    path('contact/', ContactView.as_view(), name='contact'),
]