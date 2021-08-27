import yaml

swagger = yaml.safe_load(open(
    'C:/Users/robertod/OneDrive - HDI SEGUROS SA/Área de Trabalho/python-swagger/swagger_validator/cor-pty-person-credit-score-read-be.yaml'))
print('----------------------------------------------------------------------------------------------------------------------')
print('   **** Iniciando a validação do swagger ****')
corporate = ['broker', 'business', 'channel', 'finance', 'humanResources', 'integration',
             'legal', 'marketing', 'party', 'product', 'reference', 'reinsurance', 'security']
insurance = ['claim', 'coinsurance-policy', 'coinsurance-proposal',
             'coinsurance-quotation', 'policy', 'proposal', 'quotation', 'sales']
marketplace = ['policy', 'proposal', 'quotation', 'sales']

validSuperDomain = ['corporate', 'insurance', 'marketplace']

funcionalidade_tecnicas = ['calculate', 'check', 'create', 'delete',
                           'insert', 'list', 'pull', 'push', 'read', 'recieve', 'send', 'update']

# prefixo_repositorio_corporate = []
# prefixo_repositorio_insurance = []
# prefixo_repositorio_marketeplace = []                           


print('===== Validação do basePath =====')

# validação basepath
basePath = swagger['basePath']
try:
    'basePath' in locals()
    print('Has basePath')

    superDominio = basePath.split("/")[1]
    dominio = basePath.split("/")[2]

    if any(x.isupper() for x in superDominio):
        print(' *** O SuperDominio não poder ter letra maiúscula ***')

    if superDominio in validSuperDomain:
        print('Super Dominio OK: ' + (superDominio))
        if superDominio == 'corporate':
            swaggerSuperDomain = corporate
        elif superDominio == 'insurance':
            swaggerSuperDomain = insurance
        elif superDominio == 'marketplace':
            swaggerSuperDomain = marketplace
    else:
        print('O Super Dominio está ERRADO! ' + (superDominio))
        swaggerSuperDomain = dominio

except yaml.YAMLError as exc:
    print(exc)

if dominio in swaggerSuperDomain:
    if dominio in swaggerSuperDomain:
        print('Dominio de dados OK: ' + (dominio))
        print('basePath OK: ' + (basePath))
else:
    print(" *** ATENÇÃO  basePath com inconsistência ***")
    print('Verificar o Domínio de Dado:' + (dominio))

print('-------')

# Validando o host
print('===== Validação do host =====')
try:
    'host' in locals()
    print('Has host')
    host = swagger['host']

    api = host[0:4]
    if not api == 'api.':
        print('Erro no host add api no inicio')

    ponto = host[4:]
    indice_ponto = ponto.find('.')
    nome_servico = ponto[:indice_ponto]
    print('Nome do serviço: '  + (nome_servico))

    funcionalidade = nome_servico[::-1]

    find_traco = funcionalidade.find('-')

    tipo_de_servico = nome_servico[-find_traco:]
    if tipo_de_servico == 'be':
        print('Tipo de serviço: ' + (tipo_de_servico))
        servico = funcionalidade.split("-")[1]
        convert_service = servico[::-1]
        if convert_service in funcionalidade_tecnicas:
            print('Funcionalidade técnica: ' + convert_service)
        else:
            print('verificar a funcionaldiade de negocio')
    else:
        servico = funcionalidade.split("-")[1]

        if servico[::-1] in funcionalidade_tecnicas:
            print('Tipo de serviço: ' + (tipo_de_servico))
            print('Funcionalidade técnica: ' + (servico[::-1]))
        else:
            print('verificar a funcionaldiade de negocio: ' + (servico[::-1]))
except yaml.YAMLError as exc:
    print(exc)

print('---')

# validação securityDefinitions
securityDefinitions = swagger['securityDefinitions']
if 'securityDefinitions' in locals():

    print('Has securityDefinitions')
else:
    print(securityDefinitions)

print('---')
# validação security
security = swagger['security']
if 'security' in locals():

    print('Has security')
else:
    print(security)

print('---')
# validação parameters
parameters = swagger['parameters']
if 'parameters' in locals():

    print('Has parameters')
else:
    print(parameters)

print('---')
# validação responses
responses = swagger['responses']
if 'responses' in locals():

    print('Has responses')
else:
    print(responses)

print('---')
# validação paths
paths = swagger['paths']
try:
    'paths' in locals()
    print('Has paths')
except yaml.YAMLError as exc:
    print(exc)

print('---')
# validação definition/payload

# definitions = swagger['definitions']
# try:
#       'definitions' in locals()
#       print('Has definitions')
#       print(json.dumps(definitions, sort_keys=True, indent=2))
# except yaml.YAMLError as exc:
#       print(exc)
print('   **** Fim da validação ****')