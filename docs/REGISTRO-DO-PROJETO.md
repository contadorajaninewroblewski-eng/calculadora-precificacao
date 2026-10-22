# Registro do projeto: calculadora de precificação na reforma tributária

Este arquivo reúne o contexto, as decisões tomadas e o que ficou em aberto, para que o trabalho possa ser retomado em qualquer computador. Data do registro: 22/10/2026 (atualizado no mesmo dia, após a limpeza das branches).

## Onde está tudo

- Repositório: https://github.com/contadorajaninewroblewski-eng/calculadora-precificacao (público)
- Conta do GitHub dona do projeto: `contadorajaninewroblewski-eng`
- Calculadora publicada (GitHub Pages, a partir da branch `main`): https://contadorajaninewroblewski-eng.github.io/calculadora-precificacao/
- Arquivo principal: `index.html` (página única, sem servidor, cálculo feito no navegador). Descrição geral e metodologia no `README.md`.
- Pull Requests mesclados: [#1](https://github.com/contadorajaninewroblewski-eng/calculadora-precificacao/pull/1) (crédito para comprador no lucro real) e [#2](https://github.com/contadorajaninewroblewski-eng/calculadora-precificacao/pull/2) (prévia do link).

## O que foi feito

1. **Bloco "Se você compra desse fornecedor e é do lucro real"** na aba Simples Nacional. Mostra, em reais e em % do preço, o crédito de CBS/IBS que a nota do fornecedor gera para quem compra no lucro real, comparando fornecedor no DAS e fornecedor que apura por fora. Mostra também o valor máximo da nota do fornecedor do DAS para empatar o custo líquido com o de um fornecedor do regime regular.
2. **Tabelas conferidas** com o texto compilado da LC 123/2006 no Planalto (anexos I a V: faixas, alíquotas, parcelas a deduzir e repartição). Nenhuma divergência.
3. **Artigos da LC 214/2025 conferidos** no texto do Planalto: art. 41, § 3º (opção pelo regime regular) e art. 47, § 1º, II, e § 9º, II (crédito de quem compra de optante do Simples). O texto do bloco foi ajustado para refletir o art. 47.
4. **README e aviso legal** atualizados com a LC 227/2026 e as Resoluções CGSN 190 e 191/2026.
5. **`<meta charset="utf-8">`** acrescentado, porque sem ele os acentos quebravam em servidores que não informam a codificação.
6. **Tags Open Graph** (título, descrição, endereço) acrescentadas para a prévia do link no WhatsApp mostrar "Sua Empresa na Reforma".

## Como o crédito é calculado

Alíquota efetiva do DAS × parcela de CBS/IBS da faixa. A parcela de CBS é a soma de COFINS e PIS/Pasep da repartição da faixa.

Exemplo: anexo III, faturamento de R$ 40.000 por mês (RBT12 de R$ 480.000, 3ª faixa), ano de 2027.
- Alíquota efetiva: (480.000 × 13,5% − 17.640) ÷ 480.000 = 9,83%
- Parcela de CBS na 3ª faixa: 13,64% + 2,96% = 16,6%
- Crédito: 9,83% × 16,6% = 1,63% do preço, ou R$ 652,38 em R$ 40.000 de serviço.

Se o fornecedor apurasse CBS/IBS por fora, o crédito seria de 8,8% em 2027 (R$ 3.520,00 no mesmo serviço).

O valor máximo da nota do fornecedor do DAS usa a premissa de que o fornecedor regular cobra o mesmo preço de serviço sem o IVA. Se os preços reais forem diferentes, a comparação muda.

## Decisões tomadas

- Trabalhar sempre com a conta `contadorajaninewroblewski-eng`. A conta `janinewroblewski-ND` não tem repositórios e não foi alterada.
- Mesclar os dois PRs na `main`, o que publica a versão nova no link do GitHub Pages.
- **Não registrar domínio próprio** (a decisão foi não pagar por um). O link continua sendo o endereço do GitHub Pages.
- Link para a bio do Instagram: https://contadorajaninewroblewski-eng.github.io/calculadora-precificacao/
- Aviso de que a simulação é educativa e sem validade fiscal permanece na página.
- Em 22/10/2026, as branches já mescladas (`feature/credito-lucro-real`, `fix/previa-link` e `docs/registro-do-projeto`) foram apagadas do GitHub. Sobrou só a `main`. Os PRs #1, #2 e #3 continuam no histórico e permitem restaurar qualquer branch.

## Pendente ou não decidido

- **Teto de 5% do ISS na 5ª faixa dos anexos III e IV:** o cálculo não trata esse teto. A LC 123 prevê uma repartição diferente quando a alíquota efetiva passa de 14,92537% (anexo III) ou 12,5% (anexo IV).
- **Sublimite de R$ 3,6 milhões:** as Resoluções CGSN 190 e 191/2026 estendem o sublimite também ao IBS. O código só trata o sublimite na 6ª faixa e não foi atualizado para essa regra.
- **Fator R:** o anexo é escolhido manualmente pelo usuário.
- **IRPJ, CSLL e CPP fora do DAS, Imposto Seletivo, regimes específicos e particularidades estaduais e municipais:** não considerados.
- **Alíquota de referência de 26,5%** (8,8% de CBS e 17,7% de IBS) é estimativa do Comitê Gestor. A definitiva sai por resolução do Senado, com prazo até 15/12/2026. Revisar os números depois disso.
- **Prazo de opção pelo regime regular (Simples híbrido):** a Receita Federal informa 1º a 30/9/2026 (valendo de janeiro a junho de 2027, com cancelamento até 30/11) e uma segunda janela de 1º a 31/3/2027 (segundo semestre). A CBIC noticiou prorrogação até 30/10/2026. Confirmar no Portal do Simples Nacional.
- **Prévia do link no WhatsApp:** não foi possível testar daqui. O WhatsApp guarda a prévia de cada link por um tempo. Se mostrar só o domínio, enviar o link com `?v=2` no final.
- **Teste em celular:** a página foi testada apenas no computador.
- **Nome do repositório:** foi levantada a possibilidade de renomear para um endereço mais curto (por exemplo `calculadora`), mas não foi decidido. O GitHub redireciona o endereço antigo.
- **Sem testes automatizados:** a verificação foi feita abrindo a página e conferindo os valores.

## Fontes consultadas

- Texto compilado da LC 123/2006: https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm
- Texto compilado da LC 214/2025: https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm
- Receita Federal, sobre as Resoluções CGSN 190 e 191/2026: https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2026/agosto/cgsn-atualiza-regras-do-simples-nacional-para-adequacao-a-reforma-tributaria-do-consumo
- CBIC, sobre a prorrogação do prazo de opção: https://cbic.org.br/reforma-tributaria-prazo-para-opcao-pelo-simples-nacional-e-regime-regular-do-ibs-e-da-cbs-e-prorrogado/
- Senado Notícias, implementação da reforma em 2026: https://www12.senado.leg.br/noticias/materias/2026/01/02/ano-de-2026-marca-implementacao-da-reforma-tributaria

## Dicas para trabalhar em outro computador

- Clonar com a conta certa do GitHub CLI: `gh auth switch -u contadorajaninewroblewski-eng` e depois `gh repo clone contadorajaninewroblewski-eng/calculadora-precificacao`.
- Se o `git push` der erro 403 (permissão negada à outra conta), o Git está usando um login salvo de outra conta. Solução: `git config --local credential.helper "!gh auth git-credential"` dentro da pasta do projeto, ou remover a entrada `git:https://github.com` do Gerenciador de Credenciais do Windows.
- Para ver a página localmente sem quebrar os acentos, servir a pasta com um servidor que informe UTF-8 (agora o arquivo já declara `<meta charset="utf-8">`, então abrir direto também funciona).
