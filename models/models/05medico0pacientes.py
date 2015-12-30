# -*- coding: utf-8 -*-


# Opções para formulários
ufs = ['SP', 'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA',
        'MT', 'MS', 'MG', 'PR', 'PB', 'PA', 'PE', 'PI', 'RJ', 'RN', 'RS',
          'RO', 'RR', 'SC', 'SE', 'TO']
escolaridade = ['Nenhuma', '1º grau', '2º grau', 'Superior']
cor = ['Branca', 'Negra', 'Parda', 'Indígena', 'Asiática']
estadocivil = ['Casada', 'Solteira (sem união estável)',
               'Solteira (com união estável)', 'Outra']
sexo = ['Feminino', 'Masculino']


db.define_table('pacientes',
                Field('nome', label='Nome', requires=IS_NOT_EMPTY()),
                Field('sexo', label='Sexo', default='Feminino', requires=IS_IN_SET(sexo)),
                Field('cpf', label='CPF'),
                Field('profissao', label='Profissão'),
                Field('nascimento', label='Data de nascimento', type='date',
                    requires=IS_EMPTY_OR(IS_DATE(format='%d/%m/%Y'))),
                Field('telefone', label='Telefone'),
                Field('escolaridade', label='Escolaridade',
                    requires=IS_EMPTY_OR(IS_IN_SET(escolaridade))),
                Field('estadocivil', label='Estado civil',
                    requires=IS_EMPTY_OR(IS_IN_SET(estadocivil))),
                Field('cor', label='Cor',
                      requires=IS_EMPTY_OR(IS_IN_SET(cor))),
                Field('image', 'upload', label='Foto'),
                Field('endereco', label='Endereço'),
                Field('cidade', label='Cidade'),
                Field('uf', label='UF', default='SP',
                      requires=IS_EMPTY_OR(IS_IN_SET(ufs))),
                Field('cep', label='CEP'),
                Field('observacoes', label='Observações', type='text'),
                format='%(nome)s'
                )

