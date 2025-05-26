def relatorioReservas():
    #Joga todo o reservas.txt dentro do listaUsuarios.
    arquivo = open("reservas.txt", "r")
    listaUsuarios = arquivo.readlines()
    arquivo.close()

    if len(listaUsuarios) >0:

        #Declarando listas e tabelas que serão utilizadas adiante.
        numerosInMenu = ['1','2','3','4','5','6']
        menuRelatorios = ('''
    -----Opções de Relatório-----
    |1- Relatório de Status R.
    |2- Relatório de Status C.
    |3- Relatório de Status A.
    |4- Relatório de Status F.
    |5- Relatório $$ total recebido.
    |6- Relatório de Reserva por pessoa.
    ''')
        #solicitando a opção a ser realizada.
        respostaRelatorio = input('{}\nQual das seguintes opções você deseja realizar? '.format(menuRelatorios))

        #não vai passar se não for nenhuma das mostradas no Menu.
        while respostaRelatorio not in numerosInMenu:
            print('Escolha um número presente na tabela!')
            respostaRelatorio = input('{}\nQual das seguintes opções você deseja realizar? '.format(menuRelatorios))
        else:
            #Ao passar, filtra por if e elif até cair no certo.            
            if int(respostaRelatorio) == 1:
                listaR = list()
                numeroStatus = 0
                #for para definir as respectivas caracterisicas de cada componente da lista
                for r in listaUsuarios:
                    idzao, titular, cepef, numeroPessoas, tipoQuarto, numeroDias, calculoValor, status = r.split(',')
                    #procura especificamente pelos status da lista, quando acertar soma 1 na variável.
                    if status == 'R\n':
                        listaR.append(r)
                        numeroStatus+=1

                auxiliar5 = 0
                print('>>>Relatório de Status "R":')
                for z in listaR:
                    print('-'*50)
                    print('|QUARTO -> {}'.format(listaR[auxiliar5]))
                    auxiliar5+=1
                print('>>>Totalizando:{} Quarto(s)'.format(numeroStatus))

            elif int(respostaRelatorio) == 2:
                listaC = list()
                numeroStatus = 0
                #for para definir as respectivas caracterisicas de cada componente da lista
                for c in listaUsuarios:
                    idzao, titular, cepef, numeroPessoas, tipoQuarto, numeroDias, calculoValor, status = c.split(',')
                    #procura especificamente pelos status da lista, quando acertar soma 1 na variável.
                    if status == 'C\n':
                        listaC.append(c)
                        numeroStatus+=1

                auxiliar5 = 0
                print('>>>Relatório de Status "C":')
                for z in listaC:
                    print('-'*50)
                    print('|QUARTO -> {}'.format(listaC[auxiliar5]))
                    auxiliar5+=1
                print('>>>Totalizando:{} Quarto(s)'.format(numeroStatus))

            elif int(respostaRelatorio) == 3:
                numeroStatus = 0
                listaA = list()
                #for para definir as respectivas caracterisicas de cada componente da lista
                for a in listaUsuarios:
                    idzao, titular, cepef, numeroPessoas, tipoQuarto, numeroDias, calculoValor, status = a.split(',')
                    #procura especificamente pelos status da lista, quando acertar soma 1 na variável.
                    if status == 'A\n':
                        listaA.append(a)
                        numeroStatus+=1

                auxiliar5 = 0
                print('>>>Relatório de Status "A":')
                for z in listaA:
                    print('-'*50)
                    print('|QUARTO -> {}'.format(listaA[auxiliar5]))
                    auxiliar5+=1
                print('>>>Totalizando:{} Quarto(s)'.format(numeroStatus))

            elif int(respostaRelatorio) == 4:
                listaF = list()
                numeroStatus = 0
                #for para definir as respectivas caracterisicas de cada componente da lista
                for f in listaUsuarios:
                    idzao, titular, cepef, numeroPessoas, tipoQuarto, numeroDias, calculoValor, status = f.split(',')
                    #procura especificamente pelos status da lista, quando acertar soma 1 na variável.
                    if status == 'F\n':
                        listaF.append(f)
                        numeroStatus+=1

                auxiliar5 = 0
                print('>>>Relatório de Status "F":')
                for z in listaF:
                    print('-'*50)
                    print('|QUARTO -> {}'.format(listaF[auxiliar5]))
                    auxiliar5+=1
                print('>>>Totalizando:{} Quarto(s)'.format(numeroStatus))

            elif int(respostaRelatorio) == 5:
                valorzao = 0
                #for para definir as respectivas caracterisicas de cada componente da lista
                for dinheiro in listaUsuarios:
                    idzao, titular, cepef, numeroPessoas, tipoQuarto, numeroDias, calculoValor, status = dinheiro.split(',')
                    #para cada for, o valorzao é atualizado somando cada calculoValor(valor dos alugueis) respectivo das reservas FINALIZADAS.
                    if status == 'F\n':
                        valorzao = int(calculoValor)+valorzao
                print('-'*30)
                print('>>>O relatório final para a soma do valor de todos os aluguéis é de {} R$.'.format(valorzao))

            elif int(respostaRelatorio) == 6:
                #Solicita o CPF para filtragem
                cpfParaRelatorio = input('\nPara qual CPF você deseja obter o relatório? ')
                cpfParaRelatorioNoIsDigit = cpfParaRelatorio.isdigit()
                while len(cpfParaRelatorio) != 11 or cpfParaRelatorioNoIsDigit == False:
                    print('Erro, por favor, tente novamente. ')
                    cpfParaRelatorio = input('\nPara qual CPF você deseja obter o relatório? ')
                    cpfParaRelatorioNoIsDigit = cpfParaRelatorio.isdigit()
                else:
                    listaParaPessoas = list()
                    numeroDeReservasDaPessoa = 0
                    for pessoas in listaUsuarios:
                        idzao, titular, cepef, numeroPessoas, tipoQuarto, numeroDias, calculoValor, status = pessoas.split(',')
                        if cpfParaRelatorio == cepef:
                            listaParaPessoas.append(pessoas)
                            numeroDeReservasDaPessoa+=1

                    auxiliar5 = 0
                    print('>>>Relatório para o CPF "{}":'.format(cpfParaRelatorio))
                    for z in listaParaPessoas:
                        print('-'*50)
                        print('|QUARTO -> {}'.format(listaParaPessoas[auxiliar5]))
                        auxiliar5+=1
                    print('>>>Totalizando {} reservas registradas.'.format(numeroDeReservasDaPessoa))
    else:
        print('Nenhum registro encontrado.')
    return 


def alterarreserva():
    #Jogando tudo do arquivo txt pra variavel listaUsuarios
    arquivo = open("reservas.txt", "r")
    listaUsuarios = arquivo.readlines()
    arquivo.close()

    if len(listaUsuarios) >1:

        listaBusca = list()
        listaFinal = list()
        #pede o cpf pra realizar o filto. Enquanto não for == 11 dígitos, sendo eles exclusivamente NUMÉRICOS, não vai passar.
        buscaCpf = input('Para realizar a busca, digite o CPF cadastrado: ')
        conferecpf = buscaCpf.isdigit()
        while len(buscaCpf) != 11 or conferecpf == (False):
            print('CPF inválido, por favor tente novamente.')
            buscaCpf = input('Para realizar a busca, digite o CPF cadastrado: ')
            conferecpf = buscaCpf.isdigit()
        else:
            for usuario in listaUsuarios:
                idzao, titular, cepef, numeroPessoas, tipoQuarto, numeroDias, calculoValor, status = usuario.split(',')
                #Compara a resposta do usuário com todos os CPFs do arquivo txt, aqueles que forem iguais serão adicionados na listaBusca, o resto na listaFinal.
                if buscaCpf == cepef:
                    listaBusca.append(usuario)
                else:
                    listaFinal.append(usuario)

        #declarando uns Menus que serão usados adiante
        menuAlteracao = ('''
    -OPÇÕES PARA ALTERAÇÃO-
    |1- Número de pessoas.
    |2- Tipo do Quarto.
    |3- Número de dias.
    |4- Status
                        ''')
        tabeladeStatus = ('''
    |R- Reservado.
    |C- Cancelado.
    |A- Ativo.
    |F- Finalizado
                        ''')
        tabeladeQuartos = ('''
    |S- Standard
    |D- Deluxe
    |P- Premium
                        ''')

        if len(listaBusca) >1:
            #Entrou, significa que tem pelo menos 2 registros no CPF. O for vai enumerálos em forma de tabela.
            auxiliar = 0
            for z in listaBusca:
                print('-'*50)
                print('|RESERVA -> {}'.format(listaBusca[auxiliar]))
                auxiliar+=1

            #le todos os ids e joga numa lista
            listacomosIds = list()
            for filtroId in listaBusca:
                idzao, titular, cepef, numeroPessoas, tipoQuarto, numeroDias, calculoValor, status = filtroId.split(',')
                listacomosIds.append(idzao)

            #Mostra a lista de reservas, cada reserva com seu próprio ID, o usuário deve digitar um dos IDs apresentados(presentes na listacomosIds()), enquanto nao for um dos ids certos, nao vai sair do while
            buscaReserva = input('Qual das reservas você gostaria de realizar a Alteração? ')
            while buscaReserva not in listacomosIds:
                print('Por favor, digite o código da reserva presente na tabela.')
                buscaReserva = input('Qual das reservas você gostaria de realizar a Alteração? ')
            else:
                for reserva in listaBusca:
                    idzao, titular, cepef, numeroPessoas, tipoQuarto, numeroDias, calculoValor, status = reserva.split(',')
                    #para aqueles IDs que diferem do escolhido (buscaReserva), serão jogados dentro da listaFinal. O problema é que, quando encontra aquele igual o ID, os que vem depois morrem
                    if buscaReserva != idzao:
                        listaFinal.append('{},{},{},{},{},{},{},{}'.format(idzao, titular, cepef, numeroPessoas, tipoQuarto, numeroDias, calculoValor, status))
                    else:
                        opcoesTabela = [1,2,3,4]
                        respostaAlteracao = input('{}\nQual das opções você deseja realizar? '.format(menuAlteracao))
                        while respostaAlteracao not in str(opcoesTabela):
                            print('Escolha um número presenta na tabela.\n')
                            respostaAlteracao = input('{}\nQual das opções você deseja realizar? '.format(menuAlteracao))
                        else:
                            if int(respostaAlteracao) == 1:
                                alteracao1 = int(input('Qual o novo número de Pessoas? '))
                                while str(alteracao1) == numeroPessoas or alteracao1 <=0:
                                    print('Esse já é o número atual de Pessoas ou é inválido.')
                                    alteracao1 = int(input('Qual o novo número de Pessoas? '))
                                else:
                                    #Aqui o número de pessoas é atualizado
                                    numeroPessoas = int(alteracao1)
                                    #Aqui é definido o novo valor de Aluguel.
                                    #Como o número de pessoas mudou, o valor do aluguel também deve.
                                    if tipoQuarto == "S":
                                        novoCalculo = (numeroPessoas*100)*int(numeroDias)
                                        calculoValor = str(novoCalculo)
                                    elif tipoQuarto == "D":
                                        novoCalculo = (numeroPessoas*200)*int(numeroDias)
                                        calculoValor = str(novoCalculo)
                                    elif tipoQuarto == "P":
                                        novoCalculo = (numeroPessoas*300)*int(numeroDias)
                                        calculoValor = str(novoCalculo)

                            elif int(respostaAlteracao) == 2:
                                listaQuartos = ['S', 'D', 'P']
                                alteracao2 = input('{}\nQual o novo tipo de Quarto? '.format(tabeladeQuartos))
                                alteracao2 = alteracao2.upper()
                                #Enquanto alteracao2 for igual ao tipoQuarto(atual) ou não está na listaQuartos, não sai do while.
                                while alteracao2 == tipoQuarto or alteracao2 not in listaQuartos:
                                    print('Esse já é o quarto atual ou é inválido.')
                                    alteracao2 = input('{}\nQual o novo tipo de Quarto? '.format(tabeladeQuartos))
                                    alteracao2 = alteracao2.upper()
                                else:
                                    #Define o novo tipo de Quarto
                                    if alteracao2 == 'S':
                                        tipoQuarto = str(alteracao2)
                                    elif alteracao2 == 'D':
                                        tipoQuarto = str(alteracao2)
                                    elif alteracao2 == 'P':
                                        tipoQuarto = str(alteracao2)

                                #Como o tipo do quarto foi alterado, o valor também será.
                                if tipoQuarto == "S":
                                    novoCalculo = (int(numeroPessoas)*100)*int(numeroDias)
                                    calculoValor = str(novoCalculo)
                                elif tipoQuarto == "D":
                                    novoCalculo = (int(numeroPessoas)*200)*int(numeroDias)
                                    calculoValor = str(novoCalculo)
                                elif tipoQuarto == "P":
                                    novoCalculo = (int(numeroPessoas)*300)*int(numeroDias)
                                    calculoValor = str(novoCalculo)

                            elif int(respostaAlteracao) == 3:
                                alteracao3 = input('Qual o novo número de dias? ')
                                while alteracao3 == numeroDias or int(alteracao3) <=0:
                                    print('Esse número já é o atual ou é inválido.')
                                    alteracao3 = input('Qual o novo número de dias? ')
                                else:
                                    numeroDias = alteracao3

                                #Como o número de dias de hospedagem mudou, o Valor também deve.
                                if tipoQuarto == "S":
                                    novoCalculo = (int(numeroPessoas)*100)*int(numeroDias)
                                    calculoValor = str(novoCalculo)
                                elif tipoQuarto == "D":
                                    novoCalculo = (int(numeroPessoas)*200)*int(numeroDias)
                                    calculoValor = str(novoCalculo)
                                elif tipoQuarto == "P":
                                    novoCalculo = (int(numeroPessoas)*300)*int(numeroDias)
                                    calculoValor = str(novoCalculo)

                            elif int(respostaAlteracao) == 4:
                                listacomStatus = list()
                                listacomStatus.append(status)
                                listadeStatus = ['R\n','C\n','A\n','F\n']
                                alteracao4 = input('{}\nQual o novo Status? '.format(tabeladeStatus))
                                alteracao4 = alteracao4.upper()
                                alteracao4 = (alteracao4+'\n')
                                listacomAlteracao = list()
                                listacomAlteracao.append(alteracao4)
                                while listacomAlteracao == listacomStatus or alteracao4 not in listadeStatus:
                                    print('Esse status já é o atual ou é inválido.')
                                    alteracao4 = input('{}\nQual o novo Status? '.format(tabeladeStatus))
                                    alteracao4 = alteracao4.upper()
                                    alteracao4 = (alteracao4+'\n')
                                    listacomAlteracao.pop(0)
                                    listacomAlteracao.append(alteracao4)
                                else:
                                    if alteracao4 == 'R\n':
                                        status = str(alteracao4)
                                    elif alteracao4 == 'C\n':
                                        status = str(alteracao4)
                                    elif alteracao4 == 'A\n':
                                        status = str(alteracao4)
                                    elif alteracao4 == 'F\n':
                                        status = str(alteracao4)
                        #Joga as modificações para listaFinal, juntando assim todas as reservas numa lista só.
                        listaFinal.append('{},{},{},{},{},{},{},{}'.format(idzao, titular, cepef, numeroPessoas, tipoQuarto, numeroDias, calculoValor, status))
                #Se chegou aqui, significa que alguma alteração foi feita com êxito, portanto, agora é só atualizar o txt inteiro com as modificações já feitas.
                print('Alteração realizada com sucesso!')
                arquivo = open("reservas.txt", "w")
                arquivo.writelines(listaFinal)
                arquivo.close()
        else:
            for reserva in listaBusca:
                idzao, titular, cepef, numeroPessoas, tipoQuarto, numeroDias, calculoValor, status = reserva.split(',')

                opcoesTabela = [1,2,3,4]
                respostaAlteracao = input('{}\nQual das opções você deseja realizar? '.format(menuAlteracao))
                while respostaAlteracao not in str(opcoesTabela):
                    print('Escolha um número presenta na tabela.\n')
                    respostaAlteracao = input('{}\nQual das opções você deseja realizar? '.format(menuAlteracao)) 
                else:
                    if int(respostaAlteracao) == 1:
                        alteracao1 = int(input('Qual o novo número de Pessoas? '))
                        while str(alteracao1) == numeroPessoas or alteracao1 <=0:
                            print('Esse já é o número atual de Pessoas ou é inválido.')
                            alteracao1 = int(input('Qual o novo número de Pessoas? '))
                        else:
                            #Aqui o número de pessoas é atualizado
                            numeroPessoas = alteracao1
                            #Aqui é definido o novo valor de Aluguel.
                            #Como o número de pessoas mudou, o valor do aluguel também deve.
                            if tipoQuarto == "S":
                                novoCalculo = (numeroPessoas*100)*int(numeroDias)
                                calculoValor = str(novoCalculo)
                            elif tipoQuarto == "D":
                                novoCalculo = (numeroPessoas*200)*int(numeroDias)
                                calculoValor = str(novoCalculo)
                            elif tipoQuarto == "P":
                                novoCalculo = (numeroPessoas*300)*int(numeroDias)
                                calculoValor = str(novoCalculo)

                    elif int(respostaAlteracao) == 2:
                        listaQuartos = ['S', 'D', 'P']
                        alteracao2 = input('{}\nQual o novo tipo de Quarto? '.format(tabeladeQuartos))
                        alteracao2 = alteracao2.upper()
                        #Enquanto alteracao2 for igual ao tipoQuarto(atual) ou não está na listaQuartos, não sai do while.
                        while alteracao2 == tipoQuarto or alteracao2 not in listaQuartos:
                            print('Esse já é o quarto atual ou é inválido.')
                            alteracao2 = input('{}\nQual o novo tipo de Quarto? '.format(tabeladeQuartos))
                            alteracao2 = alteracao2.upper()
                        else:
                            #Define o novo tipo de Quarto
                            if alteracao2 == 'S':
                                tipoQuarto = str(alteracao2)
                            elif alteracao2 == 'D':
                                tipoQuarto = str(alteracao2)
                            elif alteracao2 == 'P':
                                tipoQuarto = str(alteracao2)

                        #Como o tipo do quarto foi alterado, o valor também será.
                        if tipoQuarto == "S":
                            novoCalculo = (int(numeroPessoas)*100)*int(numeroDias)
                            calculoValor = str(novoCalculo)
                        elif tipoQuarto == "D":
                            novoCalculo = (int(numeroPessoas)*200)*int(numeroDias)
                            calculoValor = str(novoCalculo)
                        elif tipoQuarto == "P":
                            novoCalculo = (int(numeroPessoas)*300)*int(numeroDias)
                            calculoValor = str(novoCalculo)

                    elif int(respostaAlteracao) == 3:
                        alteracao3 = input('Qual o novo número de dias? ')
                        while alteracao3 == numeroDias or int(alteracao3) <=0:
                            print('Esse número já é o atual ou é inválido.')
                            alteracao3 = input('Qual o novo número de dias? ')
                        else:
                            numeroDias = alteracao3

                        #Como o número de dias de hospedagem mudou, o Valor também deve.
                        if tipoQuarto == "S":
                            novoCalculo = (int(numeroPessoas)*100)*int(numeroDias)
                            calculoValor = str(novoCalculo)
                        elif tipoQuarto == "D":
                            novoCalculo = (int(numeroPessoas)*200)*int(numeroDias)
                            calculoValor = str(novoCalculo)
                        elif tipoQuarto == "P":
                            novoCalculo = (int(numeroPessoas)*300)*int(numeroDias)
                            calculoValor = str(novoCalculo)

                    elif int(respostaAlteracao) == 4:
                        listacomStatus = list()
                        listacomStatus.append(status)
                        listadeStatus = ['R\n','C\n','A\n','F\n']
                        alteracao4 = input('{}\nQual o novo Status? '.format(tabeladeStatus))
                        alteracao4 = alteracao4.upper()
                        alteracao4 = (alteracao4+'\n')
                        listacomAlteracao = list()
                        listacomAlteracao.append(alteracao4)
                        while listacomAlteracao == listacomStatus or alteracao4 not in listadeStatus:
                            print('Esse status já é o atual ou é inválido.')
                            alteracao4 = input('{}\nQual o novo Status? '.format(tabeladeStatus))
                            alteracao4 = alteracao4.upper()
                            alteracao4 = (alteracao4+'\n')
                            listacomAlteracao.pop(0)
                            listacomAlteracao.append(alteracao4)
                        else:
                            if alteracao4 == 'R\n':
                                status = str(alteracao4)
                            elif alteracao4 == 'C\n':
                                status = str(alteracao4)
                            elif alteracao4 == 'A\n':
                                status = str(alteracao4)
                            elif alteracao4 == 'F\n':
                                status = str(alteracao4)       
                    #Joga tudo pra dentro da listaFinal, depois substitui txt inteiro.
                    listaFinal.append('{},{},{},{},{},{},{},{}'.format(idzao, titular, cepef, numeroPessoas, tipoQuarto, numeroDias, calculoValor, status))
            arquivo = open("reservas.txt", "w")
            arquivo.writelines(listaFinal)
            arquivo.close()
    else:
        print('Não foi encontrada nenhuma reserva.')
    return


def checkout():
    #Jogando tudo do arquivo txt pra variavel listaUsuarios
    arquivo = open("reservas.txt", "r")
    listaUsuarios = arquivo.readlines()
    arquivo.close()

    listaBusca = list()
    listaFinal = list()
    #pede o cpf pra realizar o filto. Enquanto não for == 11 dígitos, sendo eles exclusivamente NUMÉRICOS, não vai passar.
    buscaCpf = input('Para realizar a busca, digite o CPF cadastrado: ')
    cpfNoIsDigit = buscaCpf.isdigit()
    while len(buscaCpf) != 11 or cpfNoIsDigit == (False):
        print('>>>CPF incorreto, por favor tente novamente!')
        buscaCpf = input('Para realizar a busca, digite o CPF cadastrado: ')
        cpfNoIsDigit = buscaCpf.isdigit()
    else:
        for usuario in listaUsuarios:
            idzao, titular, cepef, numeroPessoas, tipoQuarto, numeroDias, calculoValor, status = usuario.split(',')
            #Compara a resposta do usuário com todos os CPFs do arquivo txt, aqueles que forem iguais serão adicionados na listaBusca, o resto na listaFinal.
            if buscaCpf == cepef: 
                if status == 'F\n' or status == 'R\n' or status == 'C\n':
                    listaFinal.append(usuario)#Se o status já for 'F' ou 'R' ou 'C', não tem pq ser alterado, então ele já vai direto pra listaFinal.
                else:
                    listaBusca.append(usuario)#Se o status for 'A', vai entrar na listaBusca (lista dos cpfs seletos)
            else:
                listaFinal.append(usuario) #Aqui entram todas as reservas que não são do CPF solicitado.

    if len(listaBusca) >1:
        #Entrou, significa que tem pelo menos 2 registros no CPF. O for vai enumerálos em forma de tabela.
        auxiliar = 0
        for z in listaBusca:
            print('-'*50)
            print('|RESERVA -> {}'.format(listaBusca[auxiliar]))
            auxiliar+=1

        listacomosIds = list()
        for filtroId in listaBusca:
            idzao, titular, cepef, numeroPessoas, tipoQuarto, numeroDias, calculoValor, status = filtroId.split(',')
            listacomosIds.append(idzao)

        #Após a leitura da tabela acima, o usuário deve escolher qual das reservas ele deseja realizar o checkin.
        #Enquanto o usuário não escolher corretamente o respectivo número das opções de reserva, não vai sair do while.
        buscaReserva = input('Qual das reservas você gostaria de realizar o Check-In? ')
        while buscaReserva not in listacomosIds or buscaReserva.isdigit() == False:
            print('Por favor, escolha um número presente na tabela.')
            buscaReserva = input('Qual das reservas você gostaria de realizar o Check-In? ')
        else:
            for reserva in listaBusca:
                idzao, titular, cepef, numeroPessoas, tipoQuarto, numeroDias, calculoValor, status = reserva.split(',')
                if int(buscaReserva) == int(idzao):
                    status = 'F\n'
                    listaFinal.append('{},{},{},{},{},{},{},{}'.format(idzao, titular, cepef, numeroPessoas, tipoQuarto, numeroDias, calculoValor, status))
                else:
                    listaFinal.append(reserva)

            print('>>>Check-out realizado com sucesso!')
            arquivo = open("reservas.txt", "w")
            arquivo.writelines(listaFinal)
            arquivo.close()
    else:
        #Se caiu aqui, significa que só tem 1 única reserva registrada no CPF, então é só fazer alteração automática.
        for reserva in listaBusca:
            idzao, titular, cepef, numeroPessoas, tipoQuarto, numeroDias, calculoValor, status = reserva.split(',')
            status = 'F\n'
            listaFinal.append('{},{},{},{},{},{},{},{}'.format(idzao, titular, cepef, numeroPessoas, tipoQuarto, numeroDias, calculoValor, status))

        print('>>>Check-out realizado com sucesso!')
        arquivo = open("reservas.txt", "w")
        arquivo.writelines(listaFinal)
        arquivo.close()
    return arquivo


#DEF para opção 2 da tabela -> Realizar Check-In de uma reserva
def checkin():
    #Jogando tudo do arquivo txt pra variavel listaUsuarios
    arquivo = open("reservas.txt", "r")
    listaUsuarios = arquivo.readlines()
    arquivo.close()

    listaBusca = list()
    listaFinal = list()
    #pede o cpf pra realizar o filto. Enquanto não for == 11 dígitos, sendo eles exclusivamente NUMÉRICOS, não vai passar.
    buscaCpf = input('Para realizar a busca, digite o CPF cadastrado: ')
    cpfNoIsDigit = buscaCpf.isdigit()
    while len(buscaCpf) != 11 or cpfNoIsDigit == (False):
        print('>>>CPF incorreto, por favor tente novamente!')
        buscaCpf = input('Para realizar a busca, digite o CPF cadastrado: ')
        cpfNoIsDigit = buscaCpf.isdigit()
    else:
        for usuario in listaUsuarios:
            idzao, titular, cepef, numeroPessoas, tipoQuarto, numeroDias, calculoValor, status = usuario.split(',')
            idzao = int(idzao)
            #Compara a resposta do usuário com todos os CPFs do arquivo txt, aqueles que forem iguais serão adicionados na listaBusca, o resto na listaFinal.
            if buscaCpf == cepef: 
                if status == 'A\n' or status == 'F\n' or status == 'C\n':
                    listaFinal.append(usuario)#Se o status já for 'A' ou 'F' ou 'C', não tem pq ser alterado, então ele já vai direto pra listaFinal.
                else:
                    listaBusca.append(usuario) #Aqui estão todas as reservas 'R' do CPF solicitado.
            else:
                listaFinal.append(usuario) #Aqui entram todas as reservas que não são do CPF solicitado.
    

    if len(listaBusca) >1:
        #Entrou, significa que tem pelo menos 2 registros no CPF. O for vai enumerálos em forma de tabela.
        auxiliar = 0
        for z in listaBusca:
            print('-'*50)
            print('|RESERVA -> {}'.format(listaBusca[auxiliar]))
            auxiliar+=1

        listacomosIds = list()
        for filtroId in listaBusca:
            idzao, titular, cepef, numeroPessoas, tipoQuarto, numeroDias, calculoValor, status = filtroId.split(',')
            listacomosIds.append(idzao)

        buscaReserva = input('Qual das reservas você gostaria de realizar o Check-In? ')
        #Após a leitura da tabela acima, o usuário deve escolher qual das reservas ele deseja realizar o checkin.
        #Enquanto o usuário não escolher corretamente o respectivo número das opções de reserva, não vai sair do while.
        while buscaReserva not in listacomosIds or buscaReserva.isdigit() == False:
            print('Por favor, escolha um número presente na tabela.')
            buscaReserva = input('Qual das reservas você gostaria de realizar o Check-In? ')
        else:
            for reserva in listaBusca:
                idzao, titular, cepef, numeroPessoas, tipoQuarto, numeroDias, calculoValor, status = reserva.split(',')
                if int(buscaReserva) == int(idzao):
                    status = 'A\n'
                    listaFinal.append('{},{},{},{},{},{},{},{}'.format(idzao, titular, cepef, numeroPessoas, tipoQuarto, numeroDias, calculoValor, status))
                else:
                    listaFinal.append(reserva)

            print('>>>Check-in realizado com sucesso!')
            arquivo = open("reservas.txt", "w")
            arquivo.writelines(listaFinal)
            arquivo.close()
    else:
        #Se caiu aqui, significa que só tem 1 única reserva registrada no CPF, então é só fazer alteração automática.
        for reserva in listaBusca:
            idzao, titular, cepef, numeroPessoas, tipoQuarto, numeroDias, calculoValor, status = reserva.split(',')
            status = 'A\n'
            listaFinal.append('{},{},{},{},{},{},{},{}'.format(idzao, titular, cepef, numeroPessoas, tipoQuarto, numeroDias, calculoValor, status))

        print('>>>Check-in realizado com sucesso!')
        arquivo = open("reservas.txt", "w")
        arquivo.writelines(listaFinal)
        arquivo.close()
    return arquivo


#DEF para opção 1 da tabela -> Realizar cadastro de uma reserva
def cadastroReservas():
    print('-'*50)
    print('A seguir, preencha as informações para realizar o cadastro.\n')

    arquivo = open("reservas.txt", "r")
    tamanhoArquivo = arquivo.readlines()
    arquivo.close()

    #Sistema de IDS
    idzao = 0
    #Enquanto o arquivo txt for nulo, seta automaticamente o Idzao para 1. Só serve pra quando for o primeiro de todos
    if len(tamanhoArquivo) <= 0:
        idzao = 1
    else:
        #A partir do segundo registro, vai cair aqui automaticamente.
        #Jogou todo o txt dentro da listaId()
        listaId = list()
        arquivo = open("reservas.txt", "r") 
        listaId = arquivo.readlines()
        arquivo.close()

        minhaLista = list()
        for i in listaId:
            minhaLista.append(int(i.split(',')[0]))
        #criado uma lista percorrendo todos os IDs[0] e usado max para encontrar o maior valor
        idzao = max(minhaLista)+1

    #Solicitando Nome//Para fins de praticidade, coloca tudo maiusculo e remove os Espaços.
    titular = input('Nome da pessoa titular: ')
    if titular.find(' ') == -1:
        titular = titular.upper()
    else:
        titular = titular.replace(' ','')
        titular = titular.upper()
    verifNome = titular.isalpha()

    #Checagem para ver se o nome é valido, utilizando isalpha() para saber se é somente letras.
    while verifNome is False:
        print('Digite um nome válido!')
        titular = input('Nome da pessoa titular: ')
        if titular.find(' ') == -1:
            titular = titular.upper()
        else:
            titular = titular.replace(' ','')
            titular = titular.upper()
        verifNome = titular.isalpha()

    #Solicitando/Validando CPF
    cepef = input('Digite um CPF (somente números): ')
    conferecepef = cepef.isdigit()
    while len(cepef) != 11 or conferecepef == (False):
        print("Digite um CPF válido!")
        cepef = input('Digite um CPF (somente números): ')
        conferecepef = cepef.isdigit()
    else:
        pass

    #Numero de Pessoas//Verificação para não haver aluguel fantasma.
    numeroPessoas = int(input('Quantas pessoas vão ir? (Somente números) '))
    while numeroPessoas <= 0:
        print('Voce não pode alugar para {} pessoa(s).'.format(numeroPessoas))
        numeroPessoas = int(input('Quantas pessoas vão ir? (Somente números) '))
    else:
        pass

    #Tipo do Quarto//Identifica qual tipo de quarto+informa caso não tenha escolhido algúm da tabela
    letters = ['S','D','P']

    tipoQuarto = input('''
    -----SELECIONE O TIPO DE QUARTO-----
    |S- Standard     (R$100 diária por pessoa)
    |D- Deluxe       (R$200 diária por pessoa)
    |P- Premium      (R$300 diária por pessoa)
    Opção Desejada: ''')
    tipoQuarto = tipoQuarto.upper()
    while tipoQuarto not in letters:
        print('Tipo: "{}" não identificado.\nPor favor, siga a tabela.'.format(tipoQuarto))
        tipoQuarto = input('''
    -----SELECIONE O TIPO DE QUARTO-----
    |S- Standard     (R$100 diária por pessoa)
    |D- Deluxe       (R$200 diária por pessoa)
    |P- Premium      (R$300 diária por pessoa)
    Opção Desejada: ''')
        tipoQuarto = tipoQuarto.upper()
    else:
        pass
    
    #Numero de dias, já faz validação para não ter aluguel fantasma.
    numeroDias = int(input('Quantos dias? (Somente números) '))
    while numeroDias <=0:
        print('Você não pode alugar um quarto por "{}" dias.\n'.format(numeroDias))
        numeroDias = int(input('Quantos dias? (Somente números) '))
    else:
        pass
    
    #Calculando o valor R$.
    if tipoQuarto == "S":
        calculoValor = (numeroPessoas*100)*numeroDias
        calculoValor = str(calculoValor)
    elif tipoQuarto == "D":
        calculoValor = (numeroPessoas*200)*numeroDias
        calculoValor = str(calculoValor)
    elif tipoQuarto == "P":
        calculoValor = (numeroPessoas*300)*numeroDias
        calculoValor = str(calculoValor)

    #Status padrão
    status = 'R'
    
    #Transformando em lista
    listaGeral = "{} {} {} {} {} {} {} {}".format(idzao, titular, cepef, numeroPessoas, tipoQuarto, numeroDias, calculoValor, status)
    listaGeral = listaGeral.split(' ')
    
    
    #Aqui é a validação final. Se alguma das variáveis anteriores foram definidas para None, não será adicionado no txt, vai cair no else.

    arquivo = open("reservas.txt", "a")#Abrir arquivo com 'a', para dar append
    arquivo.write(listaGeral[0]+',')
    arquivo.write(listaGeral[1]+',')
    arquivo.write(listaGeral[2]+',')
    arquivo.write(listaGeral[3]+',')
    arquivo.write(listaGeral[4]+',')
    arquivo.write(listaGeral[5]+',')
    arquivo.write(listaGeral[6]+',')
    arquivo.write(listaGeral[7]+'\n')
    arquivo.close()
    print('-'*50)
    print('>>>Cadastro realizado com sucesso!')
    return arquivo



#Menu Principal
menup = ('''
    ------MENU PRINCIPAL------
    |1- Cadastrar uma reserva.
    |2- Entrada do Cliente(Check-in).
    |3- Saída do Cliente(Check-out).
    |4- Alterar reserva.
    |5- Relatório de Reservas.
    |6- Sair.
    ''')

numero = 0 #Auxiliar para funcionamento do while
opcoes = [1,2,3,4,5,6] #Opcoes disponíveis

resposta = input('{}\nQual opção você deseja realizar? '.format(menup))
while numero >=0 and numero <=6:
    while resposta not in str(opcoes):
        print('\n>>>Escolha um número presenta na tabela!')
        resposta = input('{}\nQual opção você deseja realizar? '.format(menup))
    else:
        if int(resposta) == 1:
            cadastroReservas()
            resposta = input('{}\nQual opção você deseja realizar? '.format(menup))

        elif int(resposta) == 2:
            checkin()
            resposta = input('{}\nQual opção você deseja realizar? '.format(menup))

        elif int(resposta) == 3:
            checkout()
            resposta = input('{}\nQual opção você deseja realizar? '.format(menup))

        elif int(resposta) == 4:
            alterarreserva()
            resposta = input('{}\nQual opção você deseja realizar? '.format(menup))

        elif int(resposta) == 5:
            relatorioReservas()
            resposta = input('{}\nQual opção você deseja realizar? '.format(menup))

        elif int(resposta) == 6:
            print('>>>Saindo...')
            break