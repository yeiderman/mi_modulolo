{
    'name': 'Mi Módulo de Cuentas',
    'version': '1.0',
    'summary': 'Gestión básica de cuentas personalizadas',
    'description': """
        Este módulo proporciona funcionalidades básicas para la gestión de cuentas personalizadas en Odoo.
    """,
    'author': 'Tu Nombre',
    'website': 'Tu Sitio Web (opcional)',
    'license': 'LGPL-3',
    'category': 'Accounting',
    'depends': ['base', 'account'],  # Indica los módulos de los que depende este módulo
    'data': [
        # Aquí irán las rutas a tus archivos XML (vistas, menús, etc.)
    ],
    'demo': [
        # Aquí irán las rutas a tus archivos XML de datos de demostración (opcional)
    ],  # hola 31937452
    'installable': True,
    'application': False,
    'auto_install': False,
}