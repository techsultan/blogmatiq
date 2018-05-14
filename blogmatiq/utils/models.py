def get_model_field_names(model, exclude_fields=None):
    model_fields = model._meta.get_fields()
    model_field_names = [field.name for field in model_fields]
    if exclude_fields:
        for i in exclude_fields:
            model_field_names.remove(i)
    return tuple(model_field_names)
