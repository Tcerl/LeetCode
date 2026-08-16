{
    'name': 'Senior Advanced Module Pattern',
    'version': '1.0',
    'summary': 'Example of Senior-level Odoo module structure',
    'category': 'Extra Tools',
    'author': 'Senior Expert',
    'license': 'LGPL-3',
    'depends': ['base', 'sale', 'stock'], # Real-world dependencies
    'data': [
        'security/ir.model.access.csv',
        'security/record_rules.xml',
        'views/view_template.xml',
        'views/report_template.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'description': """
        This module follows the best practices:
        - Decoupled logic using super()
        - Detailed Access Rights
        - Optimized Views and Search
    """,
}
