# -*- encoding: utf-8 -*-
from osv import osv,fields

class cadastro_cadastro(osv.osv):
    '''as funções precisam vir antes da declaração dos campos '''
    _name = 'cadastro.cadastro'


    def fnct(self, cr, uid, ids, fields, arg, context):
        x = {}

        for record in self.browse(cr, uid, ids):
            x[record.id] = record.valor1 + record.valor2
        return x
    
    _columns = {
    'nome':fields.char('Nome do cliente',size=16,required = True,translate = True),
    'idade':fields.integer('Idade'),
    'taxa':fields.float('Taxa',help = 'taxa'),
    'ativo':fields.boolean('Ativo'),
    'check':fields.boolean('Checkbox'),
    'detalhes':fields.text('Detalhes'),
    'valor1' : fields.integer('Valor1'),
    'valor2' : fields.integer('Valor2'),
    'total' : fields.function(fnct, method=True, string='Total',type='integer'),
    }
    
cadastro_cadastro()
