import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import cli.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "linux_cli_mastery.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            cli.routing.websocket_urlpatterns
        )
    ),
})
