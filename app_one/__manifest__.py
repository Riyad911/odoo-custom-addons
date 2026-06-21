{
    'name': 'App One',
    'author': 'Riyad alkabbani',
    'version': '17.0.0.1.0',
    'category': '',
    'summary': '',
    'depends': ['base', 'sale_management', 'account', 'mail', 'contacts'
                ],
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/property_view.xml',
        'views/owner_view.xml',
        'views/tag_view.xml',
        'views/sale_order_view.xml',
        'views/res_partner_view.xml',
        'views/account_move_view.xml',

    ],
    'assets': {
        'web.assets_backend': ['app_one/static/src/css/property.css']
    },
    'application': True,
}
