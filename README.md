# Message Passing Interface - MPI

## Montagem do Cluster - Fazendo as conexões entre as máquinas

* Abra o **Oracle VM VirtualBox**
* Clique [aqui](https://drive.google.com/file/d/1Ls0aK9VIoZbdWka1UbynlR1Z9GjzfwRQ/view?usp=sharing) para fazer o download das máquinas virtuais já configuradas.
* Faça a instalação das máquinas virtuais Linux.
* Selecione a máquina linux OK, vá em configurações > Pastas Compartilhadas > Acrescenta uma nova pasta compartilhada ,que é a pasta deste repositório ,com o nome cloud, marque as opções montar automaticamente e tornar permanente, desmarque a opção somente leitura.
* Salve todas essas configurações
* Abra cada máquina virtual
* **Login**: aluno **Senha**: 123456 

* No terminal das máquinas Linux OK2, Linux OK3 e Linux OK4, faça:
```shell
sudo su - 
mount -t nfs maq1:/home/mpiuser/cloud /home/mpiuser/cloud
```
Esse comando acima, vai compartilhar a pasta cloud da máquina 1 com as outras máquinas 

* Na máquina Linux OK, faça:
```shell
sudo mount -t vboxsf cloud /home/mpiuser/cloud 
```
Esse comando vai associar a pasta cloud que foi criada no Windows com a pasta cloud do Linux

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

