def add_breadcrumb(request, label, url=None):
    """
    Add a breadcrumb to the request object.
    """
    if not hasattr(request, '_breadcrumbs'):
        request._breadcrumbs = []
    request._breadcrumbs.append({
        'label': label,
        'url': url,
    })


def get_breadcrumbs(request):
    """
    Get the list of breadcrumbs from the request object.
    """
    return getattr(request, '_breadcrumbs', [])