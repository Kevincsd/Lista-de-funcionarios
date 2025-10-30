from datetime import datetime
funcionarios = []
contador = 0
somatotal= 0
while True:
    funcionamento = int(input("""
(1) Digite 1 para adicionar um funcionário.
(2) Digite 2 para Listar funcionários.
(3) Digite 3 para Buscar funcionário pelo nome.
(4) Digite 4 para calcular a média salárial dos funcionários.
(5) Digite 5 para fechar o programa.
"""))
    if funcionamento ==1:
        nome = input("Digite o nome do funcionário: ")
        cargo= input("Digite o cargo do funcionário: ")
        salario= float(input("Digite o salário do funcionário: "))
        data_admissao= datetime.now().strftime("%d/%m/%Y")

        
        funcionario={"nome": nome, "cargo":cargo, "salario":salario, "data_admissao":data_admissao}
        funcionarios.append(funcionario)


    elif funcionamento == 2:
        for i in funcionarios:
            print(i)
    
    elif funcionamento == 3:
        encontrar= input("Digite o nome do funcionário que deseja encontrar: ")
        for f in funcionarios:
            if encontrar == f['nome']:
                print("Nome: ", f['nome'], "|" "Cargo: ", f['cargo'], "|" "Salário: ", f['salario'], "|" "data_admissao:", f['data_admissao'] )
            else: "Funcionário não cadastrado ou escrito de maneira errada!"
    
    elif funcionamento == 4:
            for i in funcionarios:
                     contador += 1
                     somatotal += i['salario']
            print("A média salárial dos funcionários é igual a: ", somatotal/ contador)

                     

    elif funcionamento == 5:
         print("Fechando...")
         break
    
    else: print("Insira um valor válido por favor!")