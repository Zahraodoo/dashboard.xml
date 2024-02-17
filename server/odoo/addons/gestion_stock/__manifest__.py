# -*- coding: utf-8 -*-
# Part of haioun f zahra. See LICENSE file for full copyright and licensing details.

{
    'name': 'Gestion de Stock',
    'version': '0.1',
    'category': 'Sales/Sales',
    'depends': ['base', 'mail', 'uom'],
    'description': """
This is the base module for managing products and pricelists for Haioun F/Zahra.
========================================================================

Products support variants, different pricing methods, vendors information,
make to stock/order, different units of measure, packaging and properties.

Pricelists support:
-------------------
    * Multiple-level of discount (by product, category, quantities)
    * Compute price based on different criteria:
        * Other pricelist
        * Cost price
        * List price
        * Vendor price

Pricelists preferences by product and/or partners.

Print product labels with barcode.
    """,
    'data': [
        'data/categorie_data.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'wizard/product_label_layout_views.xml',
        'views/produit_views.xml',
        'views/vente_views.xml',
        'views/achat_views.xml',
        'views/categorie_views.xml',
        'views/menu_views.xml',
        # 'report/product_reports.xml',
        # 'report/product_product_templates.xml',
    ],
    'demo': [],
    'depends': ['base','calendar','fetchmail','web_tour','digest',
                'mail', 'website','attachment_indexation', 'mail',
                'web','mail_bot', ],
    'installable': True,
    'auto_install': False,
    'assets': {
        'web.assets_backend': [
            'gestion_stock/static/src/js/**/*',
        ],
        'web.report_assets_common': [
            'gestion_stock/static/src/scss/report_label_sheet.scss',
        ],
        'web.qunit_suite_tests': [
            'gestion_stock/static/tests/**/*',
        ],
        'web.assets_qweb': [
            'gestion_stock/static/src/xml/**/*',
        ],
    },
    'license': 'LGPL-3',
}
