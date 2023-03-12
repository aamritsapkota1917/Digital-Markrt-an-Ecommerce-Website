from django.urls import path
from base.views import product_views as views

from rest_framework.routers import DefaultRouter
from ..views.product_views import API
router = DefaultRouter()
router.register('api-render', viewset=API)

urlpatterns = [
    path('',views.getProducts,name='products'),
    path('create/',views.createProduct,name='product-create'),
    path('upload/',views.uploadImage,name='image-upload'),
    path('<str:pk>/reviews/',views.createProductReview,name='create-review'),
    path('top/',views.getTopProducts,name='top-products'),
    path('<str:pk>/',views.getProduct,name='product'),
    path('update/<str:pk>/',views.updateProduct,name='product-update'),
    path('<str:pk>/recommend/', views.recommend, name="recommend"),
    path('delete/<str:pk>/',views.deleteProduct,name='product-delete'),
    # path('api/', view=views.API)
]+ router.urls
