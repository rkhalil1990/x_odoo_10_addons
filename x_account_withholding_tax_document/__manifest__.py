# -*- coding: utf-8 -*-

{
    'name': 'Withholding Tax Document',
    'version': '1.0',
    'license': 'AGPL-3',
    'category': 'Accounting & Finance',
    'description': """
        Withholding Tax Document""",
    'depends': ['hr_expense',
                'purchase',
                'report'],
    'summary': 'Withholding Tax Document',
    'data': [
        # Security
        'security/x_withholding_tax_document_groups.xml',
        'security/ir.model.access.csv',
        'security/ir_rule.xml',
        # Menu and Action
        'actions/x_withholding_tax_document_act_window.xml',
        'actions/x_withholding_tax_product_act_window.xml',
        'views/x_withholding_tax_document_menu_view.xml',
        'views/x_withholding_tax_product_menu_view.xml',
        # Views
        'views/x_withholding_tax_document_form_view.xml',
        'views/x_withholding_tax_document_tree_view.xml',
        'views/x_withholding_tax_document_filter_view.xml',
        'views/x_withholding_tax_product_form_view.xml',
        # Sequence
        'data/x_withholding_tax_document_sequence_data.xml',

        # Reports
        'reports/x_withholding_tax_document_report.xml',
        # Report Templates
        'reports/templates/x_withholding_tax_document_template.xml',
        'reports/templates/x_wht_document_company_section_template.xml',
        'reports/templates/x_wht_document_taxpayer_section_template.xml',
        'reports/templates/x_wht_document_income_section_template.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'auto-install': True,
}
