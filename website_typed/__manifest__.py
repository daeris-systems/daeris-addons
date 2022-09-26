# -*- coding: utf-8 -*-

{
    'name': 'Website Typed',
    'version': '1.0',
    'author': "Daeris",
    'support': "https://www.daeris.com",
    'website': 'https://www.daeris.com',
    'maintainer': 'daeris.iberia@gmail.com',
    'license': 'Other proprietary',
    'category': 'Website',
    'summary': "This module includes typed javascript library in website",
    'description': "This module includes typed javascript library in website",
    'depends': ['website'],
    'data': [],
    'assets': {
        'web.assets_frontend': [
            'website_typed/static/src/vendor/typedjs/typed.min.js',
            'website_typed/static/src/js/website_typed.js',
        ],
    },
    'demo': [],
    'installable': True,
    'auto_install': False,
}