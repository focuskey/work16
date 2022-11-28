# -*- coding: utf-8 -*-
{
    'name': "library_app",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    # 'description': """
    #     Long description of module's purpose
    # """,

    'author': "William WEI",
    "license": "AGPL-3",
    'website': "https://carpetCALL.com.au",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Services/Library',
    'version': '15.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    "application": True,

    # always loaded
    'data': [
            "security/library_security.xml",
            "views/library_menu.xml",

    #     # # 'security/ir.model.access.csv',
    #     # 'views/views.xml',
    #     # 'views/templates.xml',
    # ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    ],
}
