from odoo import models, fields, api

class TipoCuentaPersonalizado(models.Model):
    _name = 'mi_modulo_cuentas.tipo_cuenta'
    _description = 'Tipos de Cuentas Personalizados'

    name = fields.Char(string='Nombre del Tipo de Cuenta', required=True)
    codigo = fields.Char(string='Código', size=10)
    descripcion = fields.Text(string='Descripción')