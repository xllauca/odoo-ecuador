# -*- coding: utf-8 -*-
# © <2016> <Cristian Salamea>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountTaxGroup(models.Model):
    _inherit = 'account.tax.group'

    """
            ('vat', 'IVA Diferente de 0%'),
            ('vat0', 'IVA 0%'),
            ('novat', 'No objeto de IVA'),
            ('ret_vat_b', 'Retención de IVA (Bienes)'),
            ('ret_vat_srv', 'Retención de IVA (Servicios)'),
            ('ret_ir', 'Ret. Imp. Renta'),
            ('no_ret_ir', 'No sujetos a Ret. de Imp. Renta'),
            ('imp_ad', 'Imps. Aduanas'),
            ('imp_sbs', 'Super de Bancos'),
            ('ice', 'ICE'),
            ('other', 'Other')
    """

    code = fields.Char('Código')


class AccountTax(models.Model):

    _inherit = 'account.tax'

    percent_report = fields.Char('% para Reportes')


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    def compute_compensaciones(self):
        res = []
        for line in self.tax_line_ids:
            if line.group_id.code == 'comp':
                res.append({
                    'codigo': line.tax_id.description,
                    'tarifa': line.tax_id.percent_report,
                    'valor': abs(line.amount)
                })
        return res or False
