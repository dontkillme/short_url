import pytest
from rest_framework.test import APIClient
from apps.short_url.models import ShortUrl


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def preset_short_url(db):
    return ShortUrl.objects.create(origin_url="http://localhost:8000/magic-with-magic-is-magic/still",
                                   url_code="asdfasdf")