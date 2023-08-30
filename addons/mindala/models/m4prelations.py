from odoo import models,fields

class M4PRelations(models.Model):
    _name = "mindala.relations"
    _description = "Relations de Mindala"

    type_model_source = fields.Char('Tipo de modelo')
    id_model_source = fields.Integer('Id Modelo')
    type_model_target = fields.Char('Tipo de modelo')
    id_model_source = fields.Integer('Id Modelo')

    def _get_items_models(self):
        query = '''SELECT * FROM res_partner'''
        self.env.cr.execute(query)
        result = self.env.cr.fetchall()
