from django.apps import AppConfig as AppConfig1


class AppConfig(AppConfig1):
    name = 'app'

    def ready(self):
    	import app.signals
