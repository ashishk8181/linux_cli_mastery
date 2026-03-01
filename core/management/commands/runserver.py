from django.core.management import call_command
from django.core.management.base import CommandError

try:
    # Use Daphne's runserver when installed so ASGI behavior is preserved.
    from daphne.management.commands.runserver import Command as RunserverCommand
except ImportError:
    from django.core.management.commands.runserver import Command as RunserverCommand


class Command(RunserverCommand):
    help = "Loads all modules and starts the development server"
    _modules_loaded = False

    def _load_modules(self):
        self.stdout.write(self.style.SUCCESS("Loading all modules..."))
        for i in range(1, 8):
            module_command = f"load_module{i}"
            self.stdout.write(f"Loading Module {i}...")
            try:
                call_command(module_command)
            except CommandError as exc:
                raise CommandError(f"Failed while running '{module_command}': {exc}") from exc
        self.stdout.write(self.style.SUCCESS("All modules loaded."))
        self.stdout.write("")

    def inner_run(self, *args, **options):
        if not self._modules_loaded:
            self._load_modules()
            self._modules_loaded = True
        super().inner_run(*args, **options)
