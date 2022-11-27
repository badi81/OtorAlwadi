# -*- coding: utf-8 -*-
{
    'name': "Cubes Sale Order By Group",

    'summary': """
        Cubes Sale Order Visibility By Group
        """,

    'description': """
        Made By Abdulwahed Frea 2022-09-25
    """,

    'author': "Cubes  Company",
    'website': "http://www.cubes.ly",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','sale','sales_team','sale_stock','stock'],

    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/branch_view.xml',
        'views/res_user.xml',
        'views/sale_order.xml',
        'views/account_move.xml',
        'views/account_move_line_view.xml',
        'views/account_payment.xml',
        'views/stock_picking_view.xml',
        'views/menuitem.xml',
        'reports/external_layout.xml',
    ],
}
