from django.urls import path, re_path
from .views import fusion_installation,fusion_homepage,fusion_documentation

urlpatterns = [
    path('',fusion_homepage, name="home_page"),
    path('documentation/',fusion_documentation, name="documentation"),
    path('installation/',fusion_installation, name="installation"),
]


from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView,PasswordResetConfirmView

urlpatterns += [
    re_path('admin/password_reset/', PasswordResetView.as_view(), name='admin_password_reset'),
    re_path('admin/password_reset/done/', PasswordResetDoneView.as_view(), name='admin_password_reset_done'),
    re_path('admin/password_reset/confirm/<str:uidb64>/<str:token>/',PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]