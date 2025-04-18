# ==============================================================================
# Vários argumentos xargs nomeando parametros
# ==============================================================================

def agencia(**carro):
    return carro

print( agencia(marca='gol', cor='branco', motor=1.0, placa='hxx4593') )
print( agencia(marca='gol', cor='preto', motor=1.6) )
print( agencia(marca='gol', cor='verde', motor=1.0) )

print( type(agencia(marca='gol', cor='branco', motor=1.0)) )