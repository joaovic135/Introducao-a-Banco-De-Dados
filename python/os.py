import mysql.connector 
import psycopg2 
from faker import Faker 

fake = Faker()



mysql = mysql.connector.connect(
    user='root' , password='password',host='172.19.0.1' , port = '3302',database='IBDteste'
)

postgree = psycopg2.connect(
    user='postgres', password = 'password',host = '172.19.0.1',port = '3303', database = 'postgres'
)

postexec = postgree.cursor()
mysqlexec = mysql.cursor()
id = 1
for i in range(10000):
    #PREENCHENDO A TABELA ALUNO

    
    variavelAluno = {} 
    variavelAluno = [id,fake.first_name(),fake.last_name(),fake.last_name(),fake.city(),fake.date()]

    Aluno = "INSERT INTO Aluno(codigo, primeiroNome, nomeMeio, ultimoNome, naturalidade, dataNascimento) VALUES(%s, %s,%s,%s,%s,%s)"
    valoresAluno = (variavelAluno[0],variavelAluno[1],variavelAluno[2],variavelAluno[3],variavelAluno[4],variavelAluno[5])

    postexec.execute(Aluno,valoresAluno)
    postgree.commit()
    mysqlexec.execute(Aluno,valoresAluno)
    mysql.commit()



    #PREENCHENDO A TABELA TELEFONE ALUNO

    variavelTelefone = {}
    variavelTelefone = [variavelAluno[0] , fake.phone_number()]

    TelefoneAluno = "INSERT INTO TelefoneAluno(cod_aluno, telefone) VALUES(%s,%s)"
    valoresTelefoneAluno = (variavelTelefone[0],variavelTelefone[1])


    postexec.execute(TelefoneAluno,valoresTelefoneAluno)
    postgree.commit()
    mysqlexec.execute(TelefoneAluno,valoresTelefoneAluno)
    mysql.commit()



    #PREENCHENDO A TABELA INSTITUTO 

    variavelInstituto = {}
    variavelInstituto = [id ,fake.company_suffix(), fake.address(), fake.phone_number() ]

    Instituto = "INSERT INTO Instituto(codigo, nome, endereco, telefone) VALUES(%s, %s, %s, %s)"
    valoresInstituto = (variavelInstituto[0],variavelInstituto[1],variavelInstituto[2],variavelInstituto[3])


    postexec.execute(Instituto,valoresInstituto)
    postgree.commit()
    mysqlexec.execute(Instituto,valoresInstituto)
    mysql.commit()



    #PREENCHENDO A TABELA CURSO

    variavelCurso =  {}
    variavelCurso = [ id, variavelInstituto[0], fake.job(), fake.phone_number()]

    Curso = "INSERT INTO Curso(codigo, cod_instituto, nome, telefone) VALUES(%s,%s,%s,%s)"
    valoresCurso = (variavelCurso[0],variavelCurso[1],variavelCurso[2],variavelCurso[3])


    postexec.execute(Curso,valoresCurso)
    postgree.commit()
    mysqlexec.execute(Curso,valoresCurso)
    mysql.commit()



    #PREENCHENDO A TABELA DISCIPLINA 

    variavelDisciplina = {}
    variavelDisciplina = [id,variavelCurso[0],fake.job()]


    Disciplina = "INSERT INTO Disciplina(codigo, cod_curso, nome ) VALUES(%s,%s,%s)"
    valoresDisciplina = (variavelDisciplina[0],variavelDisciplina[1],variavelDisciplina[2])


    postexec.execute(Disciplina,valoresDisciplina)
    postgree.commit()
    mysqlexec.execute(Disciplina,valoresDisciplina)
    mysql.commit()



    #PREENCHENDO A TABELA SEMESTRE 

    variavelSemestre = {}

    variavelSemestre = [id ,fake.date() , fake.date()]

    Semestre = "INSERT INTO Semestre(codigo, dataInicio, dataFim) VALUES(%s,%s,%s)"
    valoresSemestre = (variavelSemestre[0], variavelSemestre[1] , variavelSemestre[2])

    postexec.execute(Semestre,valoresSemestre)
    postgree.commit()
    mysqlexec.execute(Semestre,valoresSemestre)
    mysql.commit()



    #PREENCHENDO A TABELA DISCIPLINASEMESTRE 

    variavelDisciplinaSemestre = {}
    variavelDisciplinaSemestre = [variavelSemestre[0],variavelDisciplina[0]]

    DisciplinaSemestre = "INSERT INTO DisciplinaSemestre(cod_semestre, cod_disciplina) VALUES(%s,%s)"
    valoresDisciplinaSemestre = (variavelDisciplinaSemestre[0],variavelDisciplinaSemestre[1])

    postexec.execute(DisciplinaSemestre,valoresDisciplinaSemestre)
    postgree.commit()
    mysqlexec.execute(DisciplinaSemestre , valoresDisciplinaSemestre)
    mysql.commit()



    #PREENCHENDO A TABELA INSCRICAO 

    variavelInscricao = {}
    variavelInscricao = [variavelAluno[0], variavelDisciplinaSemestre[1] , variavelDisciplinaSemestre[0], 'A' , fake.random_digit(),fake.random_number(digits=2)]

    Inscricao = "INSERT INTO Inscricao(cod_aluno, cod_disciplina, cod_semestre , situacao , notaFinal, qtFaltas) VALUES(%s,%s,%s,%s,%s,%s)"
    valoresInscricao = (variavelInscricao[0],variavelInscricao[1],variavelInscricao[2],variavelInscricao[3],variavelInscricao[4],variavelInscricao[5])

    postexec.execute(Inscricao,valoresInscricao)
    postgree.commit()
    mysqlexec.execute(Inscricao,valoresInscricao)
    mysql.commit()

    id +=1

#PREENCHENDO A TABELA 
print("DB CONNECTED")