# simulacao-logistica
Visando estudar o funcionamento de classes e arquivos .json, criei esse programa para auxiliar em meu aprendizado.

# Como funciona?
É um programa que simula o envio e devolução de mercadorias através de um sistema de entregas. Foram criados 4 Unidades de Tratamento,
que enviam mercadorias através de seus caminhões para os Centros de Distribuição, que entregam as mercadorias através de suas vans para
as residências do local daquele centro. Devoluções podem acontecer, e nesse caso a mercadoria faz todo o caminho oposto.  
A cada dia da semana, é mostrado as operações entre todas as Unidades de Tratamento e seus respectivos Centros de Distribuição, com estes,
por fim, entregando nas residências ou levando de volta para devolução.

# Salvamento de estado
O programa salva automaticamente o estado da simulação a cada vez que se passa um dia, preservando o estoque de todas as Unidades
e Centros. Também salva em qual semana a simulação está. A semana é atualizada depois que o sábado (último dia da semana de atividades) termina.

# Opção de resetar
Caso desejado, você pode resetar todos os dados salvos indo no programa "resetar.py" e executando. Os arquivos .json referentes aos estoques e ao tempo serão resetados (ou melhor dizendo, apagados).
