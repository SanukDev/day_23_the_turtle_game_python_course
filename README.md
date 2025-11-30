Jogo Turtle Crossing 


 Visão Geral
Este código implementa um mini jogo inspirado no clássico Frogger.
O jogador controla uma tartaruga que deve atravessar a rua evitando carros em movimento.
A cada travessia bem-sucedida, o nível aumenta e o jogo fica mais rápido.
 Estrutura do Jogo
O programa utiliza:
The_turtle → controla o jogador (classe externa)
Car → cria e movimenta carros
Scoreboard → controla pontuação e mensagens
Turtle Screen → exibe o jogo
 Controles
Seta para CIMA (Up Arrow) → move a tartaruga para frente
 Loop Principal
O loop principal do jogo executa:
Atualiza a tela (screen.update())
Controla a velocidade com base no nível
Gera carros aleatórios
Move todos os carros
Verifica colisões
Verifica se o jogador completou a travessia
 Condições de Game Over
O jogo termina quando:
A tartaruga colide com um carro (distance < 25)
 Condições de Vitória Parcial
Quando o jogador chega ao topo:
A tartaruga retorna ao início
A dificuldade aumenta
A pontuação sobe
