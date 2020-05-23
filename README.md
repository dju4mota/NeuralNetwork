# NeuralNetwork
### Estudos na área de Redes Reurais utilizando Python 3


Guia de estudo é principalmente o livro, Rede Neurais Artificiais- Ivan Nunes, Danilo Hernane e Rogério Andrade

[Anotações](https://www.notion.so/Machine-Learning-7e1eef1e85c84e809d6d87fe99e76038) 

<hr>

### Resumo do Resumo
#### Perceptron Simples (uma camada) :
* Classificação de problemas Linearmente separáveis
* Arquitetura FeedForward
* Cada entrada será multiplicada por seu peso correspondente, depois ocorre o somatório e aplicação de uma função para apresentar o resultado final
* Para treinar a rede, os novos pesos devem ser iguais há: peso antigo + (taxa de aprendizagem x entrada correspondete ao peso x diferença do  valor esperado ao valor obtido)
* Bias (limiar de ativação) - em todo amostra a primeira entrada vale -1, também é criado um peso aleatorio para essa entrada.
<hr>

#### Adaline 
* Parecida com a Rede Perceptron Simples, porém calcula o erro de uma forma muito diferente, o que possibilita solucionar problemas não linearmente separáveis
* O gráfico do erro passa a ser uma parábola com concavidade voltada para cima e o objetivo da rede é se aproximar o máximo do menor ponto. (Xv,Yv) - idealmente
* O valor da taxa de aprendizado deve ser escolhido cuidadosamente para não resultar em um mínimo local
* O desempenho pode ser melhorado com uma normalização dos dados de entrada
##### Erro 
* Erro médio absoluto ao quadrado (Penaliza muito mais erros distantes da média)
* Erro médio absoluto = Somatório de | média - valor atual |
* Erro médio absoluto em uma rede = Somatório de | valor esperado - valor calculado |
* Calcula o erro quadrático máximo, uma média, e após isso compara com o último erro calculado até estar abaixo de um valor de precisão mínimo escolhido previamente. 
