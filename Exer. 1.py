class Maioridade:

    def validacao(self, idade):

        if idade >= 18:
            print ("Essa pessoa é maior de idade!")

        else:
            print ("Essa pessoa não é maior de idade! Ela tem menos de 18 anos.")

validador_idade = Maioridade()
idade = int (input("Digite a idade: "))
validador_idade.validacao(idade)
