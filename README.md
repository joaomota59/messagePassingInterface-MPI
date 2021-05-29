# Message Passing Interface - MPI

## Montagem do Cluster - Fazendo as conexões entre as máquinas

* Abra o **Oracle VM VirtualBox**
* Clique [aqui](https://drive.google.com/file/d/1Ls0aK9VIoZbdWka1UbynlR1Z9GjzfwRQ/view?usp=sharing) para fazer o download das máquinas virtuais já configuradas.
* Faça a instalação das máquinas virtuais Linux.
* Selecione a máquina linux OK, vá em configurações > Pastas Compartilhadas > Acrescenta uma nova pasta compartilhada ,que é a pasta deste repositório ,com o nome cloud, marque as opções montar automaticamente e tornar permanente, desmarque a opção somente leitura.
* Ponto de montagem: **/home/mpiuser/cloud**
![Configuração para cada máquina](https://imgur.com/LsxTEsO.png)
* Salve todas essas configurações
* Repita esse processo acima para as máquinas Linux OK2, Linux OK3 e Linux OK4.
* Abra cada máquina virtual
* **Login**: aluno **Senha**: 123456 


* No terminal das máquinas Linux OK2, Linux OK3 e Linux OK4, faça:
```shell
sudo su - 
mount -t nfs maq1:/home/mpiuser/cloud /home/mpiuser/cloud
```
Esse comando acima, vai compartilhar a pasta cloud da máquina 1 com as outras máquinas 

* Na máquina Linux OK,Linux OK2, Linux OK3, Linux OK4 faça:
```shell
sudo mount -t vboxsf cloud /home/mpiuser/cloud 
```
Esse comando vai associar a pasta cloud que foi criada no Windows com a pasta cloud do Linux, em cada máquina virtual.

Agora para fazer qualquer edição no algoritmo basta abrir a pasta pelo windows.
Para executar o script execute somente pela máquina Linux OK e deixe as outras ligadas.


## Execução do Script
* Antes de executar, extraia todo arquivo deste repositório na sua pasta cloud do windows
* Em seguida, no linux OK, entre com o comando:

```shell
su - mpiuser
cd cloud
mpiexec -np 5 --hostfile maqs.txt python3 MPI.py
```
* Obs o numero após np significa a quantidade de processos que serão distribuídos entre as máquinas.
* O arquivo maqs.txt contém o hostname das máquinas em que a máquina Linux OK se conectará para distribuir os processos.

## Erro de hostfile
* Se ocorrer algum erro de hostfile vá na LINUX OK e faça os seguintes comandos:
```shell
su - mpiuser
cd cloud
rm maqs.txt
echo maq1 >> maqs.txt
echo maq2 >> maqs.txt
echo maq4 >> maqs.txt
```
* Em seguida tente executar o programa novamente.

## Versões do Algoritmo
> Depois de entrar na pasta cloud dentro de mpiuser, na máquina LINUX OK, digite os comandos seguintes comandos:
### Primeira Versão - MPI.py
```shell
mpiexec -np 3 --hostfile maqs.txt python3 MPI.py
```
* Cada nó do cluster calcula de maneira independente o valor de π.
### Segunda Versão - MPI2.py
```shell
mpiexec -np 2 --hostfile maqs.txt python3 MPI2.py
```
* Diferentes processos no cluster calculem o valor do somatório para diferentes intervalos de i. Exemplo: Considere ter 2 processos, o processo de rank 0 calcula o somatório para i de 1 a N/2 e o processo de rank 1 calcula o somatório para i de N/2+1 a N.

### Terceira Versão - MPI3-1.py
```shell
mpiexec -np 5 --hostfile maqs.txt python3 MPI3.py
```
* Os recursos da biblioteca MPI são utilizados para dividir a operação de somatório entre vários processos (observe que o número de processos deve ser múltiplo de N=840) e cada processo realize o seu cálculo, o envio do resultado deve ser enviado para o processo mestre que recebe esses valores a utilição do send e recv é feita nessa versão.
* Obs: Como dito no item anterior, o número após -np deve ser multiplo de 840!
* Esta versão foi criada para observar o tempo de execução de **processamento** do algoritmo, observando o tempo de execução do processo que durou mais.

### Terceira Versão - MPI3-2.py
```shell
mpiexec -np 5 --hostfile maqs.txt python3 MPI3.py
```
* Os recursos da biblioteca MPI são utilizados para dividir a operação de somatório entre vários processos (observe que o número de processos deve ser múltiplo de N=840) e cada processo realize o seu cálculo, o envio do resultado deve ser enviado para o processo mestre que recebe esses valores a utilição do send e recv é feita nessa versão.
* Obs: Como dito no item anterior, o número após -np deve ser multiplo de 840!
* Esta versão foi criada para observar o tempo de execução de **processamento** do algoritmo, observando o tempo de execução do processo que durou mais e incluindo com o **tempo de troca de mensagens**.

### Quarta Versão - MPI4-1.py
```shell
mpiexec -np 5 --hostfile maqs.txt python3 MPI4.py
```
* Mesma ideia da **Terceira Versão** porém, utiliza-se o método **reduce**.
* Obs: O número após -np deve ser multiplo de 840!
* Esta versão foi criada para observar o tempo de execução de **processamento** do algoritmo, observando o tempo de execução do processo que durou mais.


### Quarta Versão - MPI4-2.py
```shell
mpiexec -np 5 --hostfile maqs.txt python3 MPI4.py
```
* Mesma ideia da **Terceira Versão** porém, utiliza-se o método reduce.
* Obs: O número após -np deve ser multiplo de 840!
* Esta versão foi criada para observar o tempo de execução de **processamento** do algoritmo, observando o tempo de execução do processo que durou mais e incluindo com o **tempo de troca de mensagens**.

### Comando para executar 100 vezes cada script

```bash
for i in {1..100}; do mpiexec -np 3 --hostfile maqs.txt python3 /home/mpiuser/cloud/MPI.py; done
```
* OBS:
> * O número após -np é o número de processos correspondente a cada versão!
> * O arquivo correspondente após /cloud/ deve ser passado neste exemplo foi MPI.py


## Testes

### Testes com algoritmos rodando somente uma vez, mostrando o resultado calculado por cada processo e o tempo de execução
* Primeira Versão - MPI.py
![Primeira Versão](https://imgur.com/AwVuU1f.png)

* Segunda Versão - MPI2.py
![Segunda Versão](https://imgur.com/OIbtn8V.png)

* Terceira Versão - MPI3-1.py - Tempo de execução para 2 processos e para 10 processos / tempo da execução dos cálculos
![Terceira Versão](https://imgur.com/59xWSRt.png)

* Terceira Versão - MPI3-2.py - Tempo de execução para 2 processos e para 10 processos / tempo da execução dos cálculos incluindo o tempo com troca de mensagens.
![Terceira Versão](https://imgur.com/xGLDTZN.png)

* Terceira Versão - MPI3-2.py - Resultado para 5 processos - Resultado individual de cada processo
![Terceira Versão](https://imgur.com/P0bOyhg.png)

* Quarta Versão - MPI4-1.py - Tempo de execução para 2 processos e para 10 processos / tempo da execução dos cálculos
![Quarta Versão](https://imgur.com/PEvZa1K.png)

* Quarta Versão - MPI4-2.py - Tempo de execução para 2 processos e para 10 processos / tempo da execução dos cálculos incluindo o tempo com troca de mensagens.
![Quarta Versão](https://imgur.com/6IHrBeQ.png)

* Quarta Versão - MPI4-2.py - Resultado para 5 processos - Resultado individual de cada processo
![Quarta Versão](https://imgur.com/4QhVNaI.png)

### Testes 

### Testes com algoritmos rodando com N = 300. Ou seja 
* Primeira Versão - MPI.py
![Primeira Versão](https://imgur.com/0M3w5qx.png)

* Segunda Versão - MPI2.py
![Segunda Versão](https://imgur.com/QhS9dvV.png)

* Terceira Versão - MPI3-1.py - Tempo de execução para 10 processos executado N vezes/ tempo da execução dos cálculos
![Terceira Versão](https://imgur.com/ort7xp7.png)

* Terceira Versão - MPI3-2.py - Tempo de sendv e recv para 10 processos executado N vezes/ tempo da comunicação entre processos
![Terceira Versão](https://imgur.com/Y6SkIA2.png)



* Quarta Versão - MPI4-1.py - Tempo de execução para 10 processos executado N vezes/ tempo da execução dos cálculos
![Quarta Versão](https://imgur.com/y5ocA5O.png)

* Quarta Versão - MPI4-2.py - Tempo de sendv e recv para 10 processos executado N vezes/ tempo da comunicação entre processos
![Quarta Versão](https://imgur.com/UhEZbOv.png)


