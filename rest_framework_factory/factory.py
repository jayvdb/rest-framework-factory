import os
from django.conf import settings
from django.apps import apps

skel_dir = os.path.join(os.path.dirname(__file__), 'skel')

class Factory:
    def __init__(self):
        self.skel_file_model = os.path.join(skel_dir, 'models.py.txt')
        self.skel_file_api = os.path.join(skel_dir, 'api.py.txt')

        self.apis = {}
        self.apis['TestModel'] = self.create_from_scratch(model_name='TestModel')


    def create_from_scratch(self, model_name=None):
        """Create a new DRF API, model and all. """
        model_name_lcase = model_name.lower()
        with open(self.skel_file_model) as f:
            content = f.read().format(model_name=model_name, model_name_lcase=model_name_lcase)
        with open(self.skel_file_api) as f:
            content += f.read().format(model_name=model_name, model_name_lcase=model_name_lcase)
        return content

    def build_from_model(self, app_name=None, model_name=None):
        """Build a DRF API from an existing django model
        The model name should be given as it appears in models.py ie it should be Upper case
        """
        model = self._get_model_or_die(app_name, model_name)  # the model class, itself.
        # we know we have a valid model, for now all we do is build the api string.
        content = self._generate_api_content(model_name=model_name)
        api_id = "{0}.{1}".format(app_name, model_name)
        self.apis[api_id] = content



    def build_from_app(self, app_name=None, model_list='__all__'):
        """Build DRF APIs for all or a subset of the models in a django app"""
        app = self._get_app_or_die(app_name)

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

    def _get_app_or_die(self, app_name=None):
        """Return the app from django.apps.app_configs[app_name] or die trying"""
        if app_name is None:
            raise ValueError("App name is required")
        try:
            app = apps.app_configs[app_name]
            return app
        except KeyError:
            print('An app named {0} does not exist or is not registered with Django'.format(app_name))
            raise

    def _get_model_or_die(self, app_name=None, model_name=None):
        """Return the model from app_configs[app_name].get_model[model_name] or die trying"""
        if not model_name:
            raise ValueError("A model name is required")
        app = self._get_app_or_die(app_name)
        try:
            model = app.get_model(model_name)
            return model
        except KeyError:
            print("Model named {0} not found in app {1}".format(model_name, app_name))
            raise

    def _generate_api_content(self, model_name=None):
        if not model_name:
            raise ValueError("Model name required")
        with open(self.skel_file_api) as f:
            content = f.read().format(model_name=model_name, model_name_lcase=model_name.lower())
        return content



