# Calculadora de precificação na reforma tributária

Simulador de uma página só, que abre direto no navegador, para enxergar o efeito da transição da reforma tributária sobre a guia, sobre o preço e sobre o que sobra para a empresa, ano a ano, de 2026 a 2033.

São três abas, uma por regime:

- **MEI** — o DAS fixo do ano, a carga efetiva sobre o faturamento, o limite anual de R$ 81.000 e o ponto que costuma passar batido: a nota do MEI quase não gera crédito para um cliente pessoa jurídica.
- **Simples Nacional** — compara ficar com a CBS e o IBS dentro do DAS com apurá-los por fora, pelo regime regular (art. 41, § 3º, da LC 214/2025). Entram o faturamento médio, o anexo, o ano, a fatia de clientes PJ, os insumos tributados e a redução de alíquota da atividade.
- **Fora do Simples** — quanto cobrar, no lucro presumido ou real, para manter o valor líquido desejado enquanto o ICMS e o ISS dão lugar ao IBS.

## Como usar

Abra o arquivo `index.html` no navegador. Não precisa de servidor nem de instalação, e todo o cálculo acontece na própria máquina de quem abre — nada é enviado para lugar nenhum.

## Metodologia

- A alíquota efetiva do DAS sai das tabelas dos anexos I a V da Lei Complementar 123/2006, usando doze vezes o faturamento médio informado como receita bruta dos últimos doze meses.
- A parcela de CBS e IBS dentro do DAS, em cada ano, é a parcela de PIS/COFINS (que vira CBS em 2027) somada à de ICMS/ISS multiplicada pelo avanço do IBS: 10% em 2029, 20% em 2030, 30% em 2031, 40% em 2032 e 100% em 2033. É o crédito que o cliente do regime regular consegue aproveitar quando o fornecedor fica na guia única, limitado ao que foi efetivamente pago (art. 47, § 9º, II, da LC 214/2025), e é também a parcela que sai da guia na opção pelo regime regular.
- A CBS e o IBS cobrados por fora usam 8,7% de CBS mais 0,1% de IBS em 2027 e 2028 (a alíquota de referência da CBS é reduzida em 0,1 ponto percentual nesses dois anos) e, de 2029 em diante, 8,8% de CBS mais 17,7% de IBS proporcionais ao avanço da transição. Em 2026, a fase de teste não alcança o Simples Nacional.
- O crédito sobre insumos, no cenário de apuração por fora, é a parcela de CBS e IBS embutida no valor pago aos fornecedores.
- A comparação entre os dois caminhos é feita mantendo a mesma sobra para a empresa e olhando quanto os clientes pagariam em cada cenário, ponderado pela fatia de clientes pessoa jurídica.

A alíquota de referência de 26,5% (8,8% de CBS e 17,7% de IBS) é a estimativa pública do Comitê Gestor do IBS. A alíquota definitiva só será fixada por resolução do Senado, com prazo até 15/12/2026, então nenhum número aqui é definitivo.

## Fontes e conferência das tabelas

Em 20/10/2026, as faixas, as alíquotas nominais, as parcelas a deduzir e a repartição dos tributos usadas no cálculo foram conferidas, uma a uma, com o texto compilado da Lei Complementar 123/2006 no site do Planalto (versão dada pela LC 155/2016, vigente desde 1º/1/2018, com a anotação de efeitos da LC 214/2025). Anexos I a V batem com o que está no código. A parcela de CBS usada no cálculo é a soma de COFINS e PIS/Pasep de cada faixa. Por exemplo, na 3ª faixa do anexo III: 13,64% + 2,96% = 16,6%.

O texto compilado não traz anexo novo nem alteração nas alíquotas e repartições. Ele registra que a LC 214/2025 e a LC 227/2026 mudaram regras do Simples (inclusive o repasse do IBS ao Comitê Gestor do IBS), mas as tabelas continuam as de 2018. Se uma resolução do CGSN ou uma nova lei trouxer outra repartição, esses valores precisam ser atualizados no código.

Mudanças de regra, a partir de 1º/1/2027, vêm das Resoluções CGSN 190 e 191/2026, que se somam à 183/2025 (fonte: Receita Federal, agosto de 2026). A opção pelo regime regular de CBS e IBS (o "Simples híbrido") tem janelas de 1º a 30/9/2026, para valer de janeiro a junho de 2027, e de 1º a 31/3/2027, para o segundo semestre. Há notícias de prorrogação do prazo de 2026, então confirme a data no Portal do Simples Nacional antes de orientar um cliente.

## Aba do comprador no lucro real

Na aba do Simples Nacional, o bloco "Se você compra desse fornecedor e é do lucro real" mostra quanto de crédito de CBS e IBS a nota do fornecedor gera para quem compra no lucro real, em reais e em percentual do preço, comparando fornecedor no DAS e fornecedor que apura por fora. O crédito do fornecedor no DAS é a alíquota efetiva do DAS multiplicada pela parcela de CBS e IBS da faixa. Os dados do fornecedor (anexo, faturamento, ano) são os campos da própria aba.

## O que o cálculo não considera

Teto de 5% do ISS na 5ª faixa, sublimite estadual, fator R (o anexo é escolhido na mão), IRPJ, CSLL e CPP recolhidos fora do DAS, Imposto Seletivo, regimes específicos e particularidades estaduais e municipais.

## Histórico, decisões e pendências

O contexto do projeto, as decisões tomadas e o que ficou em aberto estão em [docs/REGISTRO-DO-PROJETO.md](docs/REGISTRO-DO-PROJETO.md).

## Aviso

Simulação simplificada e educativa, sem validade fiscal. Não substitui a análise de um profissional sobre os números da empresa.

Feito para a ASSESCONT Serviços Contábeis.
