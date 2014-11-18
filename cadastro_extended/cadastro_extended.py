# -*- encoding: utf-8 -*-
from osv import osv,fields

class cadastro_cadastro(osv.osv):
    _name = 'cadastro.cadastro'
    _inherit = 'cadastro.cadastro'

    def fnct(self, cr, uid, ids, fields, arg, context):
        x = {}

        for record in self.browse(cr, uid, ids):
            x[record.id] = record.valor1 + record.valor2
        return x
    
    _columns = {
    'novo_campo':fields.char('novo campo',size=16,required = True,translate = True),
    }
    
cadastro_cadastro()
