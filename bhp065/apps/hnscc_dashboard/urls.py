from .classes import HnsccDashboard

from django.conf.urls import url
from django.contrib.auth.decorators import login_required

urlpatterns = []
for pattern in HnsccDashboard.get_urlpatterns():
    urlpatterns.append(
        url(pattern,
            login_required(HnsccDashboard.as_view()),
            name=HnsccDashboard.dashboard_url_name)
        )
