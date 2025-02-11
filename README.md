# Django Flexible Breadcrumbs
**Django Flexible Breadcrumbs** is a simple and flexible package for managing and displaying breadcrumbs in Django projects. It allows you to dynamically add breadcrumbs to any page and render them using customizable HTML templates. The package includes built-in templates for popular CSS frameworks like Bootstrap, Foundation, and Tailwind CSS.

## Features
- Dynamically manage breadcrumbs for each request.
- Support for multiple pre-built templates (Bootstrap, Foundation, Tailwind CSS).
- Easy-to-use API for adding and managing breadcrumbs.
- Integration with Django's context processors.

## Installation
To install the package, run the following command:

```bash
pip install django-flexible-breadcrumbs
```
Alternatively, if you're installing from a local source:

```bash
pip install -e /path/to/django-flexible-breadcrumbs
```
## Configuration

**1- Add to `INSTALLED_APPS`**

Add the package to the `INSTALLED_APPS` list in your `settings.py` file:

```bash
INSTALLED_APPS = [
    ...
    'django_flexible_breadcrumbs',
    ...
]
```

**2- Add Context Processor**

To make breadcrumbs available across all pages, add the context processor to the `TEMPLATES` setting in `settings.py`:

```bash
TEMPLATES = [
    {
        ...
        'OPTIONS': {
            'context_processors': [
                ...
                'django_flexible_breadcrumbs.context_processors.breadcrumbs',
            ],
        },
    },
]
```

**3- Customize Template (Optional)**

The package provides several pre-built templates for different CSS frameworks. You can specify which template to use by setting the `BREADCRUMBS_TEMPLATE` variable in `settings.py`. For example:

```bash
BREADCRUMBS_TEMPLATE = 'breadcrumbs_bootstrap.html'  # Use Bootstrap template
```

Available templates:

`breadcrumbs.html` (Default template)
`breadcrumbs_bootstrap.html` (Bootstrap-compatible)
`breadcrumbs_foundation.html` (Foundation-compatible)
`breadcrumbs_tailwind.html` (Tailwind CSS-compatible)

If this setting is not provided, the package will use the default template (`breadcrumbs.html`).

## Usage
**1- Adding Breadcrumbs**

Use the `add_breadcrumb` function in your views to add breadcrumbs dynamically:

```bash
from django.shortcuts import render
from django_flexible_breadcrumbs.context_processors import add_breadcrumb

def my_view(request):
    add_breadcrumb(request, label='Home', url='/')
    add_breadcrumb(request, label='Current Page')
    return render(request, 'my_template.html')
```

**2- Rendering Breadcrumbs in Templates**

To render breadcrumbs in your templates, use the `{% render_breadcrumbs %}` template tag:

```html
{% load breadcrumbs_tags %}
<!DOCTYPE html>
<html>
<head>
    <title>My Website</title>
</head>
<body>
    <div class="breadcrumbs">
        {% render_breadcrumbs %}
    </div>
    <div class="content">
        <!-- Page content -->
    </div>
</body>
</html>
```

**3- Default Template**

The default template (`breadcrumbs.html`) looks like this:

```bash
{% if breadcrumbs %}
    <nav aria-label="breadcrumb">
        <ol>
            {% for breadcrumb in breadcrumbs %}
                <li>
                    {% if breadcrumb.url %}
                        <a href="{{ breadcrumb.url }}">{{ breadcrumb.label }}</a>
                    {% else %}
                        {{ breadcrumb.label }}
                    {% endif %}
                </li>
            {% endfor %}
        </ol>
    </nav>
{% endif %}
```

## Pre-Built Templates

The package includes several pre-built templates for popular CSS frameworks. Below are examples of how breadcrumbs are rendered in each template.

**1- Bootstrap (`breadcrumbs_bootstrap.html`)**

```bash
<nav aria-label="breadcrumb">
    <ol class="breadcrumb">
        {% for breadcrumb in breadcrumbs %}
            <li class="breadcrumb-item">
                {% if breadcrumb.url %}
                    <a href="{{ breadcrumb.url }}">{{ breadcrumb.label }}</a>
                {% else %}
                    <span>{{ breadcrumb.label }}</span>
                {% endif %}
            </li>
        {% endfor %}
    </ol>
</nav>
```

**2- Foundation (`breadcrumbs_foundation.html`)**
```bash
<nav aria-label="You are here:" role="navigation">
    <ul class="breadcrumbs">
        {% for breadcrumb in breadcrumbs %}
            <li>
                {% if breadcrumb.url %}
                    <a href="{{ breadcrumb.url }}">{{ breadcrumb.label }}</a>
                {% else %}
                    <span>{{ breadcrumb.label }}</span>
                {% endif %}
            </li>
        {% endfor %}
    </ul>
</nav>
```
**3- Tailwind CSS (`breadcrumbs_tailwind.html`)**
```bash
<nav aria-label="Breadcrumb">
    <ol class="flex items-center space-x-2">
        {% for breadcrumb in breadcrumbs %}
            <li>
                {% if breadcrumb.url %}
                    <a href="{{ breadcrumb.url }}" class="text-blue-500 hover:underline">{{ breadcrumb.label }}</a>
                {% else %}
                    <span class="text-gray-500">{{ breadcrumb.label }}</span>
                {% endif %}
            </li>
            {% if not forloop.last %}
                <li>/</li>
            {% endif %}
        {% endfor %}
    </ol>
</nav>
```
## Utilities

**`get_breadcrumbs(request)`**

You can retrieve the list of breadcrumbs from the request object using the `get_breadcrumbs` utility function:

```bash
from django_flexible_breadcrumbs.utils import get_breadcrumbs

def my_view(request):
    breadcrumbs = get_breadcrumbs(request)
    # Do something with breadcrumbs
```

## Examples

**Example 1: Adding Breadcrumbs in Multiple Steps**

```bash
from django.shortcuts import render
from django_flexible_breadcrumbs.context_processors import add_breadcrumb

def product_detail(request, product_id):
    add_breadcrumb(request, label='Home', url='/')
    add_breadcrumb(request, label='Products', url='/products/')
    add_breadcrumb(request, label=f'Product {product_id}')
    return render(request, 'product_detail.html')
```

**Example 2: Using a Custom Template**

If you want to use a custom template, specify its path in `settings.py`:

```bash
BREADCRUMBS_TEMPLATE = 'custom_breadcrumbs.html'
```

Then, create your custom template:
```bash
<nav>
    <ul>
        {% for breadcrumb in breadcrumbs %}
            <li>
                {% if breadcrumb.url %}
                    <a href="{{ breadcrumb.url }}">{{ breadcrumb.label }}</a>
                {% else %}
                    <span>{{ breadcrumb.label }}</span>
                {% endif %}
            </li>
        {% endfor %}
    </ul>
</nav>
```

## Contributing
If you'd like to contribute to this project, feel free to submit a Pull Request or open an Issue on GitHub.
