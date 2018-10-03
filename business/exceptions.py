class ParametroNegativoException(Exception):
	def __str__(self):
		return "Número negativo à vistaaaa!"

class ResultadoNegativoException(Exception):
	def __init__(self, num1, num2):
		self.num1 = num1
		self.num2 = num2

	def __str__(self):
		return "Resultado negativo à vistaaaa!! Resultado -> {}".format((self.num1 - self.num2)) 

class OperacaoMuitoFacilException(Exception):
	def __init__(self, num1, num2):
		self.num1 = num1
		self.num2 = num2

	def __str__(self):
		return "Resultado muitoooo fácil brother!! Resultado -> {}".format((self.num1 * self.num2))


class ParametroZeroException(ZeroDivisionError):
	def __str__(self):
		return "Não dá pra dividir por zero né zé ruela!!"