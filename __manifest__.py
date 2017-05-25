# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Thmdocument',
    'version': '1.1',
    'website': 'https://www.odoo.com/page/thmdocument-management',
    'category': 'Thmdocument',
    'sequence': 10,
    'summary': 'Thmdocuments, Tasks',
    'depends': [
        'base_setup',
        'product',
        'analytic',
        'mail',
        'resource',
        'web_kanban',
        'web_planner',
        'web_tour',
        'hr',
    ],
    'description': """
Track multi-level thmdocuments, tasks, work done on tasks
=====================================================

This application allows an operational thmdocument management system to organize your activities into tasks and plan the work you need to get the tasks completed.

Gantt diagrams will give you a graphical representation of your thmdocument plans, as well as resources availability and workload.

Dashboard / Reports for Thmdocument Management will include:
--------------------------------------------------------
* My Tasks
* Open Tasks
* Tasks Analysis
* Cumulative Flow
    """,
    'data': [
        'security/thmdocument_security.xml',
        'security/ir.model.access.csv',
        'data/thmdocument_data.xml',
        'report/thmdocument_report_views.xml',
        'views/thmdocument_views.xml',
        'views/thmdocument_field.xml',
        'views/thmdocument_file.xml',
        'views/res_partner_views.xml',
        'views/res_config_views.xml',
        'views/thmdocument_templates.xml',
        'views/tour_views.xml',
        'views/hr_department.xml',
        'data/web_planner_data.xml',
        'data/thmdocument_mail_template_data.xml',
    ],
    'qweb': ['static/src/xml/thmdocument.xml'],
    # 'demo': ['data/thmdocument_demo.xml'],
    # 'demo': ['data/thmdocument_demo2.xml'],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
