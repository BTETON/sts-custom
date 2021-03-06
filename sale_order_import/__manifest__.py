# -*- coding: utf-8 -*-
# Copyright 2017 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Sales Order Import',
    'version': '11.0.1.0.0',
    'author': 'Quartile Limited',
    'website': 'https://www.odoo-asia.com',
    'category': 'Sales Management',
    'license': "AGPL-3",
    'description': """
Imports sales data and processes the following:
 - sales order creation
 - availability check on outgoing picking
 - customer invoice creation
 - payment creation
    """,
    'summary': "",
    'depends': [
        'sale_stock',
        'base_import_log',
        'account_voucher',
        'sale_management',
        'delivery'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_import_default.xml',
        'views/error_logs_views.xml',
        'views/sale_order_views.xml',
        'wizard/import_sale_view.xml',
    ],
    'installable': True,
}
