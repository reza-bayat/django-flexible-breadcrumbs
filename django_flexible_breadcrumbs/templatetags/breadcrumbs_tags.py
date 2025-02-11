from django import template

from django.conf import settings

register = template.Library()

@register.inclusion_tag(getattr(settings, 'BREADCRUMBS_TEMPLATE', 'breadcrumbs.html'), takes_context=True)
def render_breadcrumbs(context):
    """
    Render breadcrumbs in the template.
    If BREADCRUMBS_TEMPLATE is not set, use the default template ('breadcrumbs.html').
    """
    breadcrumbs = context.get('breadcrumbs', [])
    return {'breadcrumbs': breadcrumbs}