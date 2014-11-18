# -*- encoding: utf-8 -*-
from osv import osv,fields

class cadastro_cadastro(osv.osv):
    _name = 'cadastro.cadastro'
    _inherit = 'cadastro.cadastro'


    _columns = {
    'novo_campo':fields.char('novo campo',size=16,required = True,translate = True),
    }
    
cadastro_cadastro()