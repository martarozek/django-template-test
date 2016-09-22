This is a simple test which runs every view in a Django project
and checks whether a template was rendered correctly.

To check for missing variables in templates you need to set
```python
'string_if_invalid': "INVALID: %s"
```
in your TEMPLATES OPTIONS in settings.
