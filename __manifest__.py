{
    'name': "Programa de Afiliados",
    'version': '0.1',
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
        'views/affiliate_views.xml',
        'views/commission_program_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}