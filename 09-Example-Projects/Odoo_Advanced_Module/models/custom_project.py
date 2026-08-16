from odoo import models, fields, api

class CustomProject(models.Model):
    _name = 'custom.project'
    _description = 'Professional Project Management'

    name = fields.Char(string='Project Name', required=True)
    start_date = fields.Date(string='Start Date', default=fields.Date.today())
    end_date = fields.Date(string='End Date')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string='Status', default='draft')
    
    responsible_id = fields.Many2one('res.users', string='Responsible', default=lambda self: self.env.user)
    
    # Senior Calculation logic
    duration = fields.Integer(string='Duration (Days)', compute='_compute_duration', store=True)

    @api.depends('start_date', 'end_date')
    def _compute_duration(self):
        for record in self:
            if record.start_date and record.end_date:
                delta = record.end_date - record.start_date
                record.duration = delta.days
            else:
                record.duration = 0
