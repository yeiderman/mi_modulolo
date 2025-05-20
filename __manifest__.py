{
    'name': 'Mi Módulo de Cuentas',
    'version': '1.0',
    'summary': 'Gestión básica de cuentas personalizadas',
    'description': """
        Este módulo proporciona funcionalidades básicas para la gestión de cuentas personalizadas en Odoo.
    """,
    'author': 'Tu Nombre',
    'website': '',
    'license': 'LGPL-3',
    'category': 'Accounting',
    'depends': ['base', 'account'],  # Indica los módulos de los que depende este módulo
    'data': [
        'views/views.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
        # Aquí irán las rutas a tus archivos XML de datos de demostración (opcional)
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}