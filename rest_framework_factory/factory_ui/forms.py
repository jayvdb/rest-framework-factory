from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, HTML, Layout, Submit


class GenerateFactoryForm(forms.Form):
    """Generate a DRFF api

    This form will present the list of INSTALLED_APPS to the user, who will choose those she wishes
    to utilize to generate the api
    """
    pass

class GenerateYamlForm(forms.Form):
    """Generate YAML From existing apps/models

    This form will present the list of INSTALLED_APPS to the user, who will choose those she wishes to
    utilize to generate a YAML config file for
    """
    pass


class LoadYamlForm(forms.Form):
    """Load YAML from file"""
    pass

