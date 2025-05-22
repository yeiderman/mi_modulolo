{
    'name': 'Mi Módulo de Cuentas',
    'version': '1.0',
    'summary': 'Gestión básica de cuentas personalizadas en Odoo',
    'description': """
        Este módulo proporciona funcionalidades básicas para la gestión
        de cuentas personalizadas dentro de la plataforma Odoo.
        Incluye modelos para cuentas y operaciones, así como vistas
        para su interacción en la interfaz de usuario.
    """,
    'author': 'Tu Nombre', # ¡Cambia esto por tu nombre!
    'website': 'http://www.tu_sitio_web.com', # Opcional: Tu sitio web
    'license': 'LGPL-3', # Licencia del módulo
    'category': 'Accounting/Custom Modules', # Categoría donde aparecerá en Odoo
    'depends': [
        'base',    # Módulo base de Odoo, casi siempre necesario
        'account', # Módulo de contabilidad de Odoo, si vas a interactuar con cuentas contables
    ],
    'data': [
         'security/ir.model.access.csv', # Archivo de seguridad para permisos de acceso
         'views/views.xml',               # Archivo XML con la definición de vistas
         'views/menus.xml',               # Archivo XML con la definición de menús
    ],
    'demo': [
        # 'demo/demo_data.xml', # Opcional: Archivos XML con datos de demostración
    ],  #hola 31937452
    'installable': True,
    'application': True,
    'auto_install': False, # Si se instala automáticamente al instalar sus dependencias
}