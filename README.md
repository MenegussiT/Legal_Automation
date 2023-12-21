# Portfolio: Automação Sulamerica

## Objetivo do Código
O código desenvolvido realiza a automação de tarefas no sistema da Sulamerica, utilizando a biblioteca Selenium em Python. As principais funcionalidades incluem a leitura de dados de um arquivo Excel, login no sistema, navegação em diferentes páginas, preenchimento de formulários e manipulação de elementos web.

## Bibliotecas Utilizadas
- **Pandas**: Utilizada para a leitura de dados do arquivo Excel e manipulação dos mesmos.
- **Selenium**: Utilizada para a automação de interações com o navegador web.
- **Time**: Utilizada para introduzir pausas no código, garantindo que as ações sejam realizadas no tempo correto.

## Fluxo do Código
1. **Leitura do Arquivo Excel:**
   - O código lê os dados de um arquivo Excel chamado "LAYOUT SAUDE_RODAR1.xlsx" e imprime o conteúdo.

2. **Configuração do Navegador:**
   - Configuração do serviço do navegador Chrome utilizando o WebDriver Manager.
   - Inicialização do navegador Chrome.

3. **Login no Sistema:**
   - Utilização de um loop para realizar o login no sistema. Se ocorrer uma exceção (NoSuchElementException), o código tenta novamente com um conjunto alternativo de credenciais.

4. **Iteração com os Dados do Excel:**
   - Utilização de um loop para iterar sobre as linhas do DataFrame lido do Excel.
   - Para cada linha, o código realiza uma série de ações no sistema da Sulamerica, como preenchimento de campos, seleção de opções, e clique em botões.

5. **Tratamento de Exceções:**
   - Um bloco try-except é utilizado para lidar com a exceção NoSuchElementException, permitindo que o código continue a execução em caso de erro.

6. **Tratamento de Sessão Expirada:**
   - Verificação da existência de um elemento que indica uma sessão expirada. Se detectado, o código confirma a sessão para continuar.

7. **Re-login em Caso de Logout:**
   - Verificação se o sistema realizou o logout. Em caso positivo, o código realiza o re-login com um conjunto específico de credenciais.

## Observações
- O código utiliza XPath para localizar elementos na página. Recomenda-se verificar periodicamente se há alterações na estrutura da página que possam impactar esses seletores XPath.
- É importante manter as bibliotecas (Pandas, Selenium, etc.) instaladas e atualizadas para garantir o correto funcionamento do código.

**Nota:** O código pode precisar de ajustes conforme as mudanças na estrutura da página web ou nos requisitos do sistema ao longo do tempo.
