from .exceptions import *

class Calculadora():
    def soma(self, a, b):
    	if a < 0 or b < 0:
    		raise ParametroNegativoException()
    	else:
    		return a + b

    def subtrai(self, a, b):
    	if a < 0 or b < 0:
    		raise ParametroNegativoException()
    	else:
    		if a - b < 0:
    			raise ResultadoNegativoException(a, b)
    		else:
    			return a - b

    def multiplica(self, a, b):
    	if a == 1 or b == 1:
    		raise OperacaoMuitoFacilException(a, b)
    	else:
    		return a * b

    def divide(self, a, b):
    	if b == 0:
    		raise ParametroZeroException()
    	else:
    		return a / b