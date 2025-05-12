## Clonar o repositório:

``git clone https://github.com/Carlos1681/sispar-back.git``

## Instalar dependências e executar o projeto:

``pip install -r requirements.txt``

``flask run``

## Principais rotas:

``'/todos-colaboradores'`` - Obter colaboradores.

``'/cadastrar'`` - Cadastrar novo colaborador.

``'/atualizar/<int:id_colaborador>'`` - Atualizar colaborador existente.

``'/login'`` - Logar no sistema.

``'/solicitar'`` - Solicitar novo reembolso.

``'/<int:num_prestacao>'`` - Buscar por número de prestação da conta.
