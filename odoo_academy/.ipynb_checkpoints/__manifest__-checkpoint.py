# .. coding: utf-8 ..

{
    'name': 'Odoo Academy',
    
    'summary': '''Academy app to manage training''',
    
    'description': '''
        Academy Module to manage Training:
        - Courses
        - Sessions
        - Attendees
    ''',
    
    'author': 'Odoo',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Training',
    'version': '0.1',
    
    'depends': ['sale'],
    
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'view/academy_menuitems.xml',
        'view/course_views.xml',
        'view/session_views.xml',
        'view/sale_view_inherit.xml',
    ],
    
    'demo': [
        'demo/academy_demo.xml',
    ],
    
}