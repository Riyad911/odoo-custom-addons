from odoo import models, fields, api


class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'Task'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    task_name = fields.Char()
    assign_to = fields.Many2one('res.users', string='Assigned To')
    description = fields.Text()
    due_date = fields.Date(tracking=1)
    status = fields.Selection([
        ('new','New'),
        ('in_progress','In Progress'),
        ('completed','Completed')
    ], default='new', tracking=1)

    def action_new(self):
        for rec in self:
            print("function draft is work")
            rec.status = 'new' # we should choose the value stored in database not what see the user ('Draft')

    def action_in_progress(self):
        for rec in self:
            print("function pending is work")
            rec.status = 'in_progress'

    def action_completed(self):
        for rec in self:
            print("function sold is work")
            rec.status = 'completed'