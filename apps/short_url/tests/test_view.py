import pytest
from apps.short_url.tests.fixturies import preset_short_url
from rest_framework.test import APIClient


@pytest.mark.parametrize("url,expected_status", [
    ("http://localhost:8000/something-with-something-that-is-a-bit-longer/his-is-odd/", 201),
    ("localhost:8000/something-with-something-that-is-a-bit-longer/his-is-odd/", 400),
    ("http://localhost:8000/" + "something-with-something-that-is-a-bit-longer/his-is-odd/" * 50, 400)
])
@pytest.mark.django_db
def test_url_creation(url, expected_status, client):
    data = {"url": url}
    result = client.post("/short/", data)
    assert result.status_code == expected_status
    assert result.content


@pytest.mark.django_db
def test_existing_url_creation(preset_short_url, client):
    data = {"url": preset_short_url.origin_url}
    result = client.post("/short/", data)
    assert result.status_code == 200


@pytest.mark.django_db
def test_get_redirect_on_existing_entry(preset_short_url, client):
  result = client.get(f"/short/{preset_short_url.url_code}")
  assert result.status_code == 302
  assert result.headers["Location"] == preset_short_url.origin_url


@pytest.mark.django_db
def test_get_404_on_not_existing_entry(client):
  result = client.get("/short/dfaa223aa11")
  assert result.status_code == 404