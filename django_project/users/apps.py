from django.apps import AppConfig



class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):        # for using signals, here it call signals
        import users.signals 
