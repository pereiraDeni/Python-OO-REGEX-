# olhar docs python
import re
padrao = "[0-9]{4,5}-*[0-9]{4}"
# Vamos testar esse padrão.
texto =  "Meu número para contato é (81)26335723"
retorno = re.search(padrao,texto)
print(retorno.group())

