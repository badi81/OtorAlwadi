# -*- coding: utf-8 -*-
{
    'name': "Restrictions",

    'summary': """
         Add restriction to users for some fields (warehouse,journal, analytic account and branch) """,

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'sale_stock',
        'account_accountant',
        'analytic',
        'sale_management'
    ],

    # always loaded
    'data': [
        'security/security.xml',
        'views/sale_order_view.xml',
        'views/user_views.xml',
    ],

}
