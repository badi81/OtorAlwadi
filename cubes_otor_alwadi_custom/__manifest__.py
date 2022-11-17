{
    'name': "Cubes Otor Alwadi Custom",
    'version': '1.0',
    'depends': ['base','account','stock','point_of_sale'],
    'author': "Cubes",

    'category': 'Category',
    'description': """
    Cubes Otor Alwadi Custom Module made by Abdalwahed 2022-11-16
    """,
    # data files always loaded at installation
    'data': [
        'view/account_edited_view.xml',
        'view/pos_config_edited_view.xml',
    ],

    'installable': True,
    'auto_install': False,
    'license': 'AGPL-3',
}
