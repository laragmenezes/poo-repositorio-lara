
# Projeto Final - Sistema de Gestão Escolar
# Classe base: Pessoa

class Pessoa:
    def __init__(self, nome, cpf, mensalidade_base):
        self.__nome = ""
        self.__cpf = ""
        self.__mensalidade_base = 0.0

        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_mensalidade_base(mensalidade_base)

    # Getter e Setter do nome
    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        if isinstance(nome, str) and len(nome.strip()) >= 3:
            self.__nome = nome
        else:
            print("Erro: o nome deve ter pelo menos 3 caracteres.")

    # Getter e Setter do CPF
    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        if isinstance(cpf, str) and len(cpf.strip()) == 11 and cpf.isdigit():
            self.__cpf = cpf
        else:
            print("Erro: o CPF deve conter 11 números.")

    # Getter e Setter da mensalidade base
    def get_mensalidade_base(self):
        return self.__mensalidade_base

    def set_mensalidade_base(self, valor):
        if isinstance(valor, (int, float)) and not isinstance(valor, bool) and valor >= 0:
            self.__mensalidade_base = float(valor)
        else:
            print("Erro: o valor não pode ser negativo.")

    # Método para calcular o pagamento
    def calcular_pagamento(self):
        return self.__mensalidade_base


# ==========================================================
# TESTE DE VALIDAÇÃO DO PROJETO FINAL
# ==========================================================
if __name__ == "__main__":
    print("=== TESTANDO A CLASSE BASE DO PROJETO FINAL ===")

    # 1. Teste com dados válidos
    pessoa_valida = Pessoa("Maria Oliveira", "12345678901", 850.00)

    print(
        f"Pessoa criada: {pessoa_valida.get_nome()} - "
        f"CPF: {pessoa_valida.get_cpf()}"
    )
    print(
        f"Pagamento base: R$ "
        f"{pessoa_valida.get_mensalidade_base():.2f}"
    )

    # 2. Teste de mensalidade negativa
    print("\n--- Teste 1: Mensalidade negativa ---")
    pessoa_valida.set_mensalidade_base(-150.00)

    print(
        f"Valor mantido com segurança: "
        f"R$ {pessoa_valida.get_mensalidade_base():.2f}"
    )

    # 3. Teste de nome muito curto
    print("\n--- Teste 2: Nome muito curto ---")
    pessoa_valida.set_nome("AB")

    print(f"Nome protegido: {pessoa_valida.get_nome()}")

    # 4. Teste de CPF inválido
    print("\n--- Teste 3: CPF inválido ---")
    pessoa_valida.set_cpf("123")

    print(f"CPF protegido: {pessoa_valida.get_cpf()}")
