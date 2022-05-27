def manual():
    print(f"\33[1;31;43m Sistema de ajuda PyHelp")
    print(f"\33[1;31;42m Acessando o comando Input ")
    func = str(input("\33[m Função ou Biblioteca > "))
    if func == "fim":
        return
    print(f"\33[1;31;47m Acessando o comando ou manual {func}")
    print(f"\33[1;31;40m")
    help(func)
    manual()


manual()
print("Terminou")
