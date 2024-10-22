import mysql.connector

def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="ticket"
    )

def listar_manifestacoes():
    db = conectar_banco()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM manifestacoes")
    resultados = cursor.fetchall()
    
    if not resultados:
        print("Não existem manifestações cadastradas.")
    else:
        print("\nListagem de Manifestações:")
        print(f"{'Código':<10} {'Tipo':<20} {'Descrição'}")
        print("-" * 50)
        for row in resultados:
            print(f"{row[0]:<10} {row[1]:<20} {row[2]}")
    
    cursor.close()
    db.close()

def listar_manifestacoes_por_tipo(tipo):
    db = conectar_banco()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM manifestacoes WHERE tipo = %s", (tipo,))
    resultados = cursor.fetchall()

    if not resultados:
        print(f"Não existem manifestações do tipo '{tipo}' cadastradas.")
    else:
        print(f"\nListagem de Manifestações do Tipo '{tipo}':")
        print(f"{'Código':<10} {'Descrição'}")
        print("-" * 50)
        for row in resultados:
            print(f"{row[0]:<10} {row[2]}")

    cursor.close()
    db.close()

def criar_manifestacao(tipo, descricao):
    db = conectar_banco()
    cursor = db.cursor()
    cursor.execute("INSERT INTO manifestacoes (tipo, descricao) VALUES (%s, %s)", (tipo, descricao))
    db.commit()
    print("Nova manifestação criada com sucesso!")
    cursor.close()
    db.close()

def exibir_quantidade_manifestacoes():
    db = conectar_banco()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM manifestacoes")
    quantidade = cursor.fetchone()[0]
    print(f"Total de manifestações: {quantidade}")
    
    cursor.close()
    db.close()

def pesquisar_manifestacao_por_codigo(codigo):
    db = conectar_banco()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM manifestacoes WHERE codigo = %s", (codigo,))
    resultado = cursor.fetchone()

    if resultado:
        print(f"Código: {resultado[0]}, Tipo: {resultado[1]}, Descrição: {resultado[2]}")
    else:
        print("Manifestação não encontrada.")
    
    cursor.close()
    db.close()

def excluir_manifestacao_por_codigo(codigo):
    db = conectar_banco()
    cursor = db.cursor()
    cursor.execute("DELETE FROM manifestacoes WHERE codigo = %s", (codigo,))
    db.commit()
    if cursor.rowcount > 0:
        print("Manifestação excluída com sucesso!")
    else:
        print("Código não encontrado. Nenhuma manifestação excluída.")
    
    cursor.close()
    db.close()

def menu():
    while True:
        print("\nMenu do Sistema de Ouvidoria")
        print("1) Listagem das Manifestações")
        print("2) Listagem de Manifestações por Tipo")
        print("3) Criar uma nova Manifestação")
        print("4) Exibir quantidade de manifestações")
        print("5) Pesquisar uma manifestação por código")
        print("6) Excluir uma Manifestação pelo Código")
        print("7) Sair do Sistema")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            listar_manifestacoes()
        elif opcao == '2':
            tipo = input("Digite o tipo (reclamação, elogio ou sugestão): ")
            listar_manifestacoes_por_tipo(tipo)
        elif opcao == '3':
            tipo = input("Digite o tipo (reclamação, elogio ou sugestão): ")
            descricao = input("Digite a descrição da manifestação: ")
            criar_manifestacao(tipo, descricao)
        elif opcao == '4':
            exibir_quantidade_manifestacoes()
        elif opcao == '5':
            codigo = input("Digite o código da manifestação: ")
            pesquisar_manifestacao_por_codigo(codigo)
        elif opcao == '6':
            codigo = input("Digite o código da manifestação a ser excluída: ")
            excluir_manifestacao_por_codigo(codigo)
        elif opcao == '7':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
