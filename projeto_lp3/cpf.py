from validate_docbr import CPF

cpf = CPF()

print(cpf.generate(True))
print(cpf.generate(False))

print(cpf.validate("242.148.602-50"))
print(cpf.validate("24214860250"))