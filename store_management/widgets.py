from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Change')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'store_management/custom_widget_templates/custom_clearable_file_input.html'