import os
from django.conf import settings
from django.apps import apps

skel_dir = os.path.join(os.path.dirname(__file__), 'skel')

class Factory:
    def __init__(self):
        self.apis = {}
        self.apis['TestModel'] = self.create_from_scratch(model_name='TestModel')


    def create_from_scratch(self, model_name=None):
        """Create a new DRF API, model and all. """
        model_name_lcase = model_name.lower()
        skel_file_model = os.path.join(skel_dir, 'models.py.txt')
        skel_file_api = os.path.join(skel_dir, 'api.py.txt')
        with open(skel_file_model) as f:
            content = f.read().format(model_name=model_name, model_name_lcase=model_name_lcase)
        with open(skel_file_api) as f:
            content += f.read().format(model_name=model_name, model_name_lcase=model_name_lcase)
        return content

    def build_from_model(self, app_name=None, model_name=None):
        """Build a DRF API from an existing django model"""
        print('bild from model placeholder')

    def build_from_app(self, app_name=None, model_list='__all__'):
        """Build DRF APIs for all or a subset of the models in a django app"""
        if not app_name:
            raise(ValueError, "Application Name is required")
        if not app_name in apps.app_configs.keys():
            raise ModuleNotFoundError("App module does not exist: ", app_name)

        try:
            app = apps.app_configs(app_name)
        except Exception:
            raise SyntaxError("Error getting app named {0}".format(app_name))

        if model_list == '__all__':
            models = [x for x in app.get_models()]
        else:
            models = []
            for m in model_list:
                try:
                    models.append(app.get_model(model_name=m))
                except LookupError:
                    raise ValueError("Model named {0} does not exist".format(m))
        for model in models:
            model_name = model._meta.object_name
            model_name_lcase = model._meta.model_name
            content = self.build_from_model()




