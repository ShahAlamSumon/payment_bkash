# -*- coding: utf-8 -*-
{
    'name': 'bKash Payment Gateway',
    'version': '1.0',
    'summary': 'Integrate bKash Payment Gateway with Odoo',
    'description': """
        Bkash payment integration
        =========================
        Integrating payment gateway like bKash (a popular mobile financial service in Bangladesh) with 
        Odoo involves. This can handle API interactions for payment transactions.
    """,
    'category': 'Accounting',
    'website': 'https://logicbite.wordpress.com',
    'author': 'Shah Alam Sumon',
    'depends': ['payment'],
    'data': [
        'views/payment_provider_views.xml',
        'views/payment_templates.xml',
        'views/payment_transaction_views.xml',
        'data/payment_provider_data.xml',
    ],
    'post_init_hook': 'post_init_hook',
    'uninstall_hook': 'uninstall_hook',
    'license': 'LGPL-3',
}
