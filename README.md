This is a simple test which runs every view in a Django project
and checks whether a template was rendered correctly.

To check for missing variables in templates you need to set
```python
'string_if_invalid': "INVALID: %s"
```
in your TEMPLATES OPTIONS in settings.

The test should be placed in the Django project root directory (the main app of the project).

Note that the test is stupid and runs through all urls found in the project, no matter if it's a TemplateView or not.
