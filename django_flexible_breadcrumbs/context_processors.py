def breadcrumbs(request):
    """
    Add breadcrumbs to the template context.
    """
    if hasattr(request, '_breadcrumbs'):
        return {'breadcrumbs': request._breadcrumbs}
    return {'breadcrumbs': []}