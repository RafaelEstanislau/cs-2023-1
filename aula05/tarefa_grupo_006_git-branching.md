### Tarefa 006: Git Branching - 28/04/2023

1. Qual o nome do branch padrão do Git? 
 R: O Padrão é master

2. O que o comando **<code>git branch nome</code>** realiza?
 R: Muda de branch para a branch desejada

3. Como criar um branch a partir de um commit específico?
 R: git branch [id do commit]

4. Em um repositório, qual o efeito do comando **<code>git checkout -b bugfix/234</code>**?
 R: Cria a branch bugfix/234

5. Qual o comando para se alternar para um branch de nome **experimento2**?
 R: git checkout experimento2

6. Em um repositório com dois branches, **b1** e **b2**, onde b1 é o corrente, qual o efeito do comando **<code>git branch</code>**?
 R: Irá mostrar as branchs disponíveis e a corrente com um * na frente

7. O que o comando **<code>git checkout -b</code>** nome faz?
 R: Cria uma nova branch e muda para ela

8. Qual a função do <code>**comando git branch -d teste</code>**?
 R: Deleta a branch desejada.

9. Durante o desenvolvimento de um software é comum, por exemplo, utilizar um novo recurso por meio de experimentação. Talvez uma nova tecnologia, uma nova biblioteca que pode ser útil ao que está em desenvolvimento, ou até mesmo uma nova versão de um produto já empregado. Para que o uso deste novo recurso não interfira com o que é considerado pronto, um branch pode ser criado para a experimentação. Código que for criado para a experimentação existirá apenas no branch criado. Se eventualmente o experimento demonstrar um resultado satisfatório, as alterações realizadas no branch poderão ser incorporadas no que é considerado pronto, ou seja, no branch principal (master). Esta última ação é conhecida por merge. Neste item, crie uma sequência de comandos que simula um caso simples de criação e uso seguido de merge empregando um branch para ilustrar uma experimentação conforme acima. A sequência deve incluir, obrigatoriamente: (a) criação de um ou mais branches; (b) chaveamento para pelo menos dois branches e (c) merge.

 R: git checkout -b exemplo
    git add .
    git commit -m "mensagem do commit"
    git push origin exemplo
    git checkout master
    git merge exemplo


INSTRUÇÕES:

1. No seu repositório pessoal, na sua branch pessoal, criar a pasta aula05.
2. Commitar este arquivo respondido nesta pasta.
3. A data limite para concluir esta tarefa é dia 01/05/2023, as 23h59min.

</DIV/>
