from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    # Account Endpoints
    path("user-check/", views.user_check),
    path("login/", obtain_auth_token),
    path("register/step1/", views.AccountRegister.as_view()),
    path("register/step2/", views.add_plan),
    path("register/step3/", views.add_phone_number),
    path("<int:pk>/", views.AccountRetrieveUpdate.as_view()),

    # Profile Endpoints
    path("<int:account_id>/profiles/", views.ProfileList.as_view()),
    path("profiles/new/", views.ProfileCreate.as_view()),
    path("profiles/<int:pk>/", views.ProfileRetrieveUpdateDestroy.as_view()),
    path("profiles/<int:profile_id>/login/", views.profile_login),
    path("profiles/images/", views.ProfileImageList.as_view()),

    # Plan Endpoints
    path("plans/", views.PlanList.as_view()),
]
