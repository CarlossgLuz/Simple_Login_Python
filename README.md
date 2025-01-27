# 🔒 Sistema de Login em Python com Dicionários

Este projeto é um sistema de autenticação simples e funcional desenvolvido em Python, utilizando **dicionários** para gerenciar os dados de usuários. Ele permite aos usuários realizar diversas ações, como login, cadastro, redefinição de senha e exclusão de cadastro, tudo em um ambiente de terminal interativo.

---

## 🛠️ Funcionalidades

- **Fazer Login**: Autenticação de usuário com email e senha.
- **Cadastrar Usuário**: Criação de novas contas com validação de email e senha.
- **Redefinir Senha**: Alteração da senha mediante autenticação.
- **Excluir Cadastro**: Remoção permanente de contas após confirmação.
- **Sistema de Menu**: Interface de texto para fácil navegação entre as opções.

---

## 💻 Tecnologias Utilizadas

- **Python**
- Uso de dicionários para armazenar e gerenciar credenciais de usuários.
- Estrutura de repetição e validação de entrada do usuário para maior segurança e funcionalidade.

---

## 📝 Regras de Validação
**Email**:
- Deve conter "@" e "." com a posição correta.
- Não pode ser duplicado no sistema.
**Senha**:  
- Deve conter no mínimo 5 caracteres.
- Não pode conter espaços em branco.

---

## ⚙️ Estrutura do Código
- **Menu Principal:** Apresenta as opções disponíveis para o usuário.
- **Login:** Valida o email e a senha. Após 3 tentativas incorretas, bloqueia temporariamente.
- **Cadastro:** Verifica a unicidade do email e valida a senha antes de salvar.
- **Redefinir Senha:** Exige autenticação antes de permitir a alteração.
- **Excluir Cadastro:** Solicita confirmação antes de remover o usuário do sistema.

---

## 📂 Exemplo de Uso
O usuário seleciona a opção desejada no menu.
Caso escolha a opção de cadastro, um email e uma senha válidos devem ser fornecidos.
Após o cadastro, o login pode ser realizado com as credenciais criadas.
Para alterar a senha ou excluir a conta, o usuário precisa confirmar sua identidade.

---

## 🔒 Segurança e Limitações
Os dados dos usuários são armazenados em um dicionário em tempo de execução, o que significa que todas as informações serão perdidas ao encerrar o programa.
Este sistema não é adequado para produção, pois não utiliza métodos seguros de armazenamento de dados, como hashing de senhas.

---

## 📌 Melhorias Futuras
- Integração com banco de dados para persistência de dados.
- Implementação de hashing para maior segurança de senhas.
- Interface gráfica ou integração com um framework web como **Flask** ou **Django**.

---

## 📧 Contato
> Se tiver dúvidas ou sugestões, sinta-se à vontade para abrir uma issue ou enviar um pull request.
