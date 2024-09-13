from odoo import models, fields

class HoursModel(models.Model):
    _name = 'hours.counter'
    _description = 'Modulo di test con calcolo ore'
    
    name = fields.Char(string='Name', required=True)
    date = fields.Date(string='Data', required=True)
    start_time = fields.Float(string='Ora di inizio', required=True)
    end_time = fields.Float(string='Ora di fine', required=True)
    afterhours = fields.Text(string='Ore di straordinari')