from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        super(AccountsConfig, self).ready()
        import accounts.signals