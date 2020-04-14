"""pizza_order URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView,LogoutView
from django.conf.urls import include
from django.urls import path
from .router import router
from rest_framework.authtoken import views
from order.views import home, pizza_booking, order_update,order_delivery_update,OrdersListView
from user.views import signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-token-auth/',views.obtain_auth_token,name='api-token-auth'),
    path('', home,name='home'),
    path('checkout/', pizza_booking,name='pizza_booking'),
    path('orders/',OrdersListView ,name='all-orders'),
    path('order/<int:id>/update/',order_update ,name='order_update'),
    path('order/update/delivery',order_delivery_update ,name='order_delivery_update'),
    path('signup/', signup, name='signup'),
    path('login/', LoginView.as_view(template_name='user/login.html',), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
