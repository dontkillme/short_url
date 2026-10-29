import pytest
from apps.short_url.models import ShortUrl

@pytest.mark.django_db
def test_create_short_url_entry():
    short_url = ShortUrl.objects.create(origin_url="http://asdf.pl/asdf/asdf/asdf")
    assert short_url.url_code