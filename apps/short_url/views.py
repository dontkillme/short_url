from rest_framework.response import Response
from django.core.exceptions import ValidationError
from rest_framework.decorators import api_view
from apps.short_url.models import ShortUrl

@api_view(["POST"])
def create_short_url(request):
    url = request.data.get("url")
    try:
        short_url, created = ShortUrl.objects.get_or_create(origin_url=url)
    except ValidationError:
        return Response("Invalid url", status=400)

    if created:
        return Response(short_url.url_code, status=201)
    return Response(short_url.url_code)


@api_view(["GET"])
def redirect_to_url(request, code):
    if len(code) > 16:
        return Response("Too long code")

    short_url = ShortUrl.objects.filter(url_code=code).first()

    if not short_url:
        return Response("No Such Url", status=404)
    return Response(status=302, headers={"Location": short_url.origin_url})
