# -*- coding: utf-8 -*-
# @author Kitcharoen Poolperm <kitcharoenp@gmail.com>
# @copyright Copyright (C) 2017
# @license http://opensource.org/licenses/gpl-3.0.html GNU Public License

{
    'name': 'Telco Purchase Order',
    'version': '0.01',
    'category': 'Purchases',
    "author": "kicharoenp@gmail.com",
    'summary': 'Purchase Orders',
    'description': """
    """,
    'depends': ['purchase'],
    'data': [
        'data/telco_purchase_sequence_data.xml',
        # Views
        'views/telco_purchase_order_tree_view.xml',
        'views/telco_purchase_order_form_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}