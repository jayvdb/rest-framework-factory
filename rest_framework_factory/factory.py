import os
from django.conf import settings

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


    def build_from_model(self, app_name=None, models=None):
        """Build a DRF API from an existing django model"""


    def build_from_app(self, app_name=None):
        assert app_name in settings.INSTALLED_APPS

