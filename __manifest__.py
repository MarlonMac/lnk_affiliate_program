{
    'name': "Programa de Afiliados",
    'version': '0.1.0',
    'depends': ['base', 'website'],
    'author': 'Marlon Macario',
    'company': 'Link GT',
    'website': 'https://link-gt.com'
    'category': 'Marketing',
    'description': """
    Módulo para gestionar un programa de afiliados.
    """,
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/affiliate_views.xml',
        'views/commission_program_views.xml',
        'views/sale_order_views.xml', 
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}