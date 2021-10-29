from Banco2 import Banco
import pandas as pd
import tkinter.filedialog as fdlg

def writeTofile(self,data, filename):
  # Convert binary data to proper format and write it on Hard Disk
  with open(filename, 'wb') as file:
    file.write(data)

class Usuarios(object):


  def __init__(self, idcont = "", tipo = "", historico = "",
  compet = "", ccusto = "", doc = "", valor = "", vcto = "", pgto= "", fpg = "",status="",saldo="",cclistados="",tlistados=""):
    self.info = {}
    #self.idusuario = idusuario

    self.idcont = idcont
    self.tipo = tipo
    self.historico = historico
    self.compet = compet
    self.ccusto = ccusto
    self.doc = doc
    self.valor = valor
    self.vcto = vcto
    self.pgto = pgto
    self.fpg = fpg
    self.status = status
    self.saldo = saldo
    self.cclistados = cclistados
    self.tlistados = tlistados


  def insertUser(self):

    banco = Banco()
    try:
      c = banco.conexao.cursor()

      minha_query = """INSERT INTO controles (tipo, historico, compet, ccusto, doc, valor, vcto, pgto, fpg, status, saldo) VALUES (?,?,?,?,?,?,?,?,?,?,?)"""
      
      # Convert data into tuple format
      data_tuple = (self.tipo, self.historico, self.compet, self.ccusto, self.doc, self.valor, self.vcto, self.pgto, self.fpg, self.status, self.saldo)

      c.execute(minha_query, data_tuple)



      banco.conexao.commit()
      c.close()


      return " Registrado com sucesso!"
    except:
      return " Atenção: Ocorreu um erro na inserção"

  def updateUser(self):

    banco = Banco()
    try:

        c = banco.conexao.cursor()

        c.execute("UPDATE controles SET tipo = '" + self.tipo + "',  historico = '" + self.historico + "', compet = '" + self.compet +
        "', ccusto = '" + self.ccusto + "', doc = '" + self.doc +
        "' , valor = '" + self.valor + "', vcto = '" + self.vcto +
         "' , pgto = '" + self.pgto + "' , fpg = '" + self.fpg + "', status = '" +
          self.status + "', saldo = '" + self.saldo + "' WHERE idcont = '" + self.idcont + "' ")

      
        banco.conexao.commit()
        c.close()

        return " Atualizado com sucesso!"
    except:
        return " Ocorreu um erro na alteração"

 
  def deleteUser(self,idcont):

    banco = Banco()
    try:

        c = banco.conexao.cursor()

        c.execute("delete from controles where idcont = '" + self.idcont + "' ")

        banco.conexao.commit()
        c.close()

        return " Excluído com sucesso!"
    except:
        return " Ocorreu um erro na exclusão do usuário"



  def selecfiltros(self, tipo,status,ccusto,fpg,competencia,
    datapago,ValDtini,ValDtfim,tb_movimento):
    banco = Banco()
    valorTotal=0
    compTotal=0
    saldTotal=0
    pagoTotal=0
    valCompet='0'
    #valores para grafic1
    valorf = 0
    valoru = 0
    valorc = 0
    valorp = 0
    todoscc = 0
    #valores para grafic2
    tvalorf = 0
    tvalorv = 0
    tvalorc = 0
    tvalori = 0
    todostip = 0
    
    try:
        if tipo != "" and status != "" and ccusto != "" and fpg != "" and datapago == 2 and competencia == 2:
          c = banco.conexao.cursor()
          #c.execute("SELECT * FROM controles ORDER BY vcto DESC")
          c.execute("SELECT * FROM controles WHERE tipo = '" + tipo + "'" + " and status ='" + status + "'" +
           " and ccusto ='" + ccusto + "'" + " and fpg ='" + fpg + "'" + " and vcto >='" + ValDtini + "'" +
            " and vcto <='" + ValDtfim + "' ORDER BY vcto DESC")
        
        elif tipo != "" and status != "" and ccusto != "" and fpg != "" and datapago == 1 and competencia == 2:
          c = banco.conexao.cursor()
          #c.execute("SELECT * FROM controles ORDER BY vcto DESC")
          c.execute("SELECT * FROM controles WHERE tipo = '" + tipo + "'" + " and status ='" + status + "'" +
           " and ccusto ='" + ccusto + "'" + " and fpg ='" + fpg + "'" + " and pgto >='" + ValDtini + "'" +
            " and pgto <='" + ValDtfim + "' ORDER BY vcto DESC")

        elif tipo != "" and status != "" and ccusto != "" and fpg != "" and datapago == 2 and competencia == 1:
          c = banco.conexao.cursor()
          #c.execute("SELECT * FROM controles ORDER BY vcto DESC")
          c.execute("SELECT * FROM controles WHERE tipo = '" + tipo + "'" + " and status ='" + status + "'" +
           " and ccusto ='" + ccusto + "'" + " and fpg ='" + fpg + "'" + " and vcto >='" + ValDtini + "'" +
            " and vcto <='" + ValDtfim + "' and compet <> '0' ORDER BY vcto DESC")

        elif tipo != "" and status != "" and ccusto != "" and fpg != "" and datapago == 1 and competencia == 1:
          c = banco.conexao.cursor()
          #c.execute("SELECT * FROM controles ORDER BY vcto DESC")
          c.execute("SELECT * FROM controles WHERE tipo = '" + tipo + "'" + " and status ='" + status + "'" +
           " and ccusto ='" + ccusto + "'" + " and fpg ='" + fpg + "'" + " and pgto >='" + ValDtini + "'" +
            " and pgto <='" + ValDtfim + "' and compet <> '0' ORDER BY vcto DESC")

        elif tipo != "" and status != "" and ccusto != "" and fpg == "" and datapago == 2 and competencia == 2:
          c = banco.conexao.cursor()
          #c.execute("SELECT * FROM controles ORDER BY vcto DESC")
          c.execute("SELECT * FROM controles WHERE tipo = '" + tipo + "'" + " and status ='" + status + "'" +
           " and ccusto ='" + ccusto + "'" + " and vcto >='" + ValDtini + "'" +
            " and vcto <='" + ValDtfim + "' ORDER BY vcto DESC")
        
        elif tipo != "" and status != "" and ccusto != "" and fpg == "" and datapago == 1 and competencia == 2:
          c = banco.conexao.cursor()
          #c.execute("SELECT * FROM controles ORDER BY vcto DESC")
          c.execute("SELECT * FROM controles WHERE tipo = '" + tipo + "'" + " and status ='" + status + "'" +
           " and ccusto ='" + ccusto + "'" + " and pgto >='" + ValDtini + "'" +
            " and pgto <='" + ValDtfim + "' ORDER BY vcto DESC")

        elif tipo != "" and status != "" and ccusto != "" and fpg == "" and datapago == 2 and competencia == 1:
          c = banco.conexao.cursor()
          #c.execute("SELECT * FROM controles ORDER BY vcto DESC")
          c.execute("SELECT * FROM controles WHERE tipo = '" + tipo + "'" + " and status ='" + status + "'" +
           " and ccusto ='" + ccusto + "'" + " and vcto >='" + ValDtini + "'" +
            " and vcto <='" + ValDtfim + "' and compet <> '0' ORDER BY vcto DESC")

        elif tipo != "" and status != "" and ccusto != "" and fpg == "" and datapago == 1 and competencia == 1:
          c = banco.conexao.cursor()
          #c.execute("SELECT * FROM controles ORDER BY vcto DESC")
          c.execute("SELECT * FROM controles WHERE tipo = '" + tipo + "'" + " and status ='" + status + "'" +
           " and ccusto ='" + ccusto + "'" + " and pgto >='" + ValDtini + "'" +
            " and pgto <='" + ValDtfim + "' and compet <> '0' ORDER BY vcto DESC")

        elif tipo != "" and status != "" and ccusto == "" and fpg == "" and datapago == 2 and competencia == 2:
          c = banco.conexao.cursor()
          #c.execute("SELECT * FROM controles ORDER BY vcto DESC")
          c.execute("SELECT * FROM controles WHERE tipo = '" + tipo + "'" + " and status ='" + status +
           "'" + " and vcto >='" + ValDtini + "'" +
            " and vcto <='" + ValDtfim + "' ORDER BY vcto DESC")
        
        elif tipo != "" and status != "" and ccusto == "" and fpg == "" and datapago == 1 and competencia == 2:
          c = banco.conexao.cursor()
          #c.execute("SELECT * FROM controles ORDER BY vcto DESC")
          c.execute("SELECT * FROM controles WHERE tipo = '" + tipo + "'" + " and status ='" + status +
           "'" + " and pgto >='" + ValDtini + "'" +
            " and pgto <='" + ValDtfim + "' ORDER BY vcto DESC")

        elif tipo != "" and status != "" and ccusto == "" and fpg == "" and datapago == 2 and competencia == 1:
          c = banco.conexao.cursor()
          #c.execute("SELECT * FROM controles ORDER BY vcto DESC")
          c.execute("SELECT * FROM controles WHERE tipo = '" + tipo + "'" + " and status ='" + status +
           "'" + " and vcto >='" + ValDtini + "'" +
            " and vcto <='" + ValDtfim + "' and compet <> '0' ORDER BY vcto DESC")

        elif tipo != "" and status != "" and ccusto == "" and fpg == "" and datapago == 1 and competencia == 1:
          c = banco.conexao.cursor()
          #c.execute("SELECT * FROM controles ORDER BY vcto DESC")
          c.execute("SELECT * FROM controles WHERE tipo = '" + tipo + "'" + " and status ='" + status +
           "'" + " and pgto >='" + ValDtini + "'" +
            " and pgto <='" + ValDtfim + "' and compet <> '0' ORDER BY vcto DESC")

        elif tipo != "" and status == "" and ccusto == "" and fpg == "" and datapago == 2 and competencia == 2:
          c = banco.conexao.cursor()
          #c.execute("SELECT * FROM controles ORDER BY vcto DESC")
          c.execute("SELECT * FROM controles WHERE tipo = '" + tipo + "'" + " and vcto >='" + ValDtini + "'" +
            " and vcto <='" + ValDtfim + "' ORDER BY vcto DESC")
        
        elif tipo != "" and status == "" and ccusto == "" and fpg == "" and datapago == 1 and competencia == 2:
          c = banco.conexao.cursor()
          #c.execute("SELECT * FROM controles ORDER BY vcto DESC")
          c.execute("SELECT * FROM controles WHERE tipo = '" + tipo + "'" + " and pgto >='" + ValDtini + "'" +
            " and pgto <='" + ValDtfim + "' ORDER BY vcto DESC")

        elif tipo != "" and status == "" and ccusto == "" and fpg == "" and datapago == 2 and competencia == 1:
          c = banco.conexao.cursor()
          #c.execute("SELECT * FROM controles ORDER BY vcto DESC")
          c.execute("SELECT * FROM controles WHERE tipo = '" + tipo + "'" + " and vcto >='" + ValDtini + "'" +
            " and vcto <='" + ValDtfim + "' and compet <> '0' ORDER BY vcto DESC")

        elif tipo != "" and status == "" and ccusto == "" and fpg == "" and datapago == 1 and competencia == 1:
          c = banco.conexao.cursor()
          #c.execute("SELECT * FROM controles ORDER BY vcto DESC")
          c.execute("SELECT * FROM controles WHERE tipo = '" + tipo + "'" + " and pgto >='" + ValDtini + "'" +
            " and pgto <='" + ValDtfim + "' and compet <> '0' ORDER BY vcto DESC")

        elif tipo == "" and status != "" and ccusto != "" and fpg != "" and datapago == 2 and competencia == 2:
          c = banco.conexao.cursor()
          #c.execute("SELECT * FROM controles ORDER BY vcto DESC")
          c.execute("SELECT * FROM controles WHERE status ='" + status + "'" +
           " and ccusto ='" + ccusto + "'" + " and fpg ='" + fpg + "'" + " and vcto >='" + ValDtini + "'" +
            " and vcto <='" + ValDtfim + "' ORDER BY vcto DESC")
        
        elif tipo == "" and status != "" and ccusto != "" and fpg != "" and datapago == 1 and competencia == 2:
          c = banco.conexao.cursor()
          #c.execute("SELECT * FROM controles ORDER BY vcto DESC")
          c.execute("SELECT * FROM controles WHERE status ='" + status + "'" +
           " and ccusto ='" + ccusto + "'" + " and fpg ='" + fpg + "'" + " and pgto >='" + ValDtini + "'" +
            " and pgto <='" + ValDtfim + "' ORDER BY vcto DESC")

        elif tipo == "" and status != "" and ccusto != "" and fpg != "" and datapago == 2 and competencia == 1:
          c = banco.conexao.cursor()
          #c.execute("SELECT * FROM controles ORDER BY vcto DESC")
          c.execute("SELECT * FROM controles WHERE status ='" + status + "'" +
           " and ccusto ='" + ccusto + "'" + " and fpg ='" + fpg + "'" + " and vcto >='" + ValDtini + "'" +
            " and vcto <='" + ValDtfim + "' and compet <> '0' ORDER BY vcto DESC")

        elif tipo == "" and status != "" and ccusto != "" and fpg != "" and datapago == 1 and competencia == 1:
          c = banco.conexao.cursor()
          #c.execute("SELECT * FROM controles ORDER BY vcto DESC")
          c.execute("SELECT * FROM controles WHERE status ='" + status + "'" +
           " and ccusto ='" + ccusto + "'" + " and fpg ='" + fpg + "'" + " and pgto >='" + ValDtini + "'" +
            " and pgto <='" + ValDtfim + "' and compet <> '0' ORDER BY vcto DESC")

        elif tipo == "" and status != "" and ccusto != "" and fpg == "" and datapago == 2 and competencia == 2:
          c = banco.conexao.cursor()
          #c.execute("SELECT * FROM controles ORDER BY vcto DESC")
          c.execute("SELECT * FROM controles WHERE status ='" + status + "'" +
           " and ccusto ='" + ccusto + "'" + " and vcto >='" + ValDtini + "'" +
            " and vcto <='" + ValDtfim + "' ORDER BY vcto DESC")
        
        elif tipo == "" and status != "" and ccusto != "" and fpg == "" and datapago == 1 and competencia == 2:
          c = banco.conexao.cursor()
          #c.execute("SELECT * FROM controles ORDER BY vcto DESC")
          c.execute("SELECT * FROM controles WHERE status ='" + status + "'" +
           " and ccusto ='" + ccusto + "'" + " and pgto >='" + ValDtini + "'" +
            " and pgto <='" + ValDtfim + "' ORDER BY vcto DESC")

        elif tipo == "" and status != "" and ccusto != "" and fpg == "" and datapago == 2 and competencia == 1:
          c = banco.conexao.cursor()
          #c.execute("SELECT * FROM controles ORDER BY vcto DESC")
          c.execute("SELECT * FROM controles WHERE status ='" + status + "'" +
           " and ccusto ='" + ccusto + "'" + " and vcto >='" + ValDtini + "'" +
            " and vcto <='" + ValDtfim + "' and compet <> '0' ORDER BY vcto DESC")

        elif tipo == "" and status != "" and ccusto != "" and fpg == "" and datapago == 1 and competencia == 1:
          c = banco.conexao.cursor()
          #c.execute("SELECT * FROM controles ORDER BY vcto DESC")
          c.execute("SELECT * FROM controles WHERE status ='" + status + "'" +
           " and ccusto ='" + ccusto + "'" + " and pgto >='" + ValDtini + "'" +
            " and pgto <='" + ValDtfim + "' and compet <> '0' ORDER BY vcto DESC")

        elif tipo == "" and status != "" and ccusto == "" and fpg == "" and datapago == 2 and competencia == 2:
          c = banco.conexao.cursor()
          #c.execute("SELECT * FROM controles ORDER BY vcto DESC")
          c.execute("SELECT * FROM controles WHERE status ='" + status + "'" + " and vcto >='" + ValDtini + "'" +
            " and vcto <='" + ValDtfim + "' ORDER BY vcto DESC")
        
        elif tipo == "" and status != "" and ccusto == "" and fpg == "" and datapago == 1 and competencia == 2:
          c = banco.conexao.cursor()
          #c.execute("SELECT * FROM controles ORDER BY vcto DESC")
          c.execute("SELECT * FROM controles WHERE status ='" + status + "'" + " and pgto >='" + ValDtini + "'" +
            " and pgto <='" + ValDtfim + "' ORDER BY vcto DESC")

        elif tipo == "" and status != "" and ccusto == "" and fpg == "" and datapago == 2 and competencia == 1:
          c = banco.conexao.cursor()
          #c.execute("SELECT * FROM controles ORDER BY vcto DESC")
          c.execute("SELECT * FROM controles WHERE status ='" + status + "'" + " and vcto >='" + ValDtini + "'" +
            " and vcto <='" + ValDtfim + "' and compet <> '0' ORDER BY vcto DESC")

        elif tipo == "" and status != "" and ccusto == "" and fpg == "" and datapago == 1 and competencia == 1:
          c = banco.conexao.cursor()
          #c.execute("SELECT * FROM controles ORDER BY vcto DESC")
          c.execute("SELECT * FROM controles WHERE status ='" + status + "'" + " and pgto >='" + ValDtini + "'" +
            " and pgto <='" + ValDtfim + "' and compet <> '0' ORDER BY vcto DESC")

        elif tipo == "" and status == "" and ccusto != "" and fpg != "" and datapago == 2 and competencia == 2:
          c = banco.conexao.cursor()
          #c.execute("SELECT * FROM controles ORDER BY vcto DESC")
          c.execute("SELECT * FROM controles WHERE ccusto ='" + ccusto + "'" + " and fpg ='" + fpg + "'" + " and vcto >='" + ValDtini + "'" +
            " and vcto <='" + ValDtfim + "' ORDER BY vcto DESC")
        
        elif tipo == "" and status == "" and ccusto != "" and fpg != "" and datapago == 1 and competencia == 2:
          c = banco.conexao.cursor()
          #c.execute("SELECT * FROM controles ORDER BY vcto DESC")
          c.execute("SELECT * FROM controles WHERE ccusto ='" + ccusto + "'" + " and fpg ='" + fpg + "'" + " and pgto >='" + ValDtini + "'" +
            " and pgto <='" + ValDtfim + "' ORDER BY vcto DESC")

        elif tipo == "" and status == "" and ccusto != "" and fpg != "" and datapago == 2 and competencia == 1:
          c = banco.conexao.cursor()
          #c.execute("SELECT * FROM controles ORDER BY vcto DESC")
          c.execute("SELECT * FROM controles WHERE ccusto ='" + ccusto + "'" + " and fpg ='" + fpg + "'" + " and vcto >='" + ValDtini + "'" +
            " and vcto <='" + ValDtfim + "' and compet <> '0' ORDER BY vcto DESC")

        elif tipo == "" and status == "" and ccusto != "" and fpg != "" and datapago == 1 and competencia == 1:
          c = banco.conexao.cursor()
          #c.execute("SELECT * FROM controles ORDER BY vcto DESC")
          c.execute("SELECT * FROM controles WHERE ccusto ='" + ccusto + "'" + " and fpg ='" + fpg + "'" + " and pgto >='" + ValDtini + "'" +
            " and pgto <='" + ValDtfim + "' and compet <> '0' ORDER BY vcto DESC")

        elif tipo == "" and status == "" and ccusto != "" and fpg == "" and datapago == 2 and competencia == 2:
          c = banco.conexao.cursor()
          #c.execute("SELECT * FROM controles ORDER BY vcto DESC")
          c.execute("SELECT * FROM controles WHERE ccusto ='" + ccusto + "'" + " and vcto >='" + ValDtini + "'" +
            " and vcto <='" + ValDtfim + "' ORDER BY vcto DESC")
        
        elif tipo == "" and status == "" and ccusto != "" and fpg == "" and datapago == 1 and competencia == 2:
          c = banco.conexao.cursor()
          #c.execute("SELECT * FROM controles ORDER BY vcto DESC")
          c.execute("SELECT * FROM controles WHERE ccusto ='" + ccusto + "'" + " and pgto >='" + ValDtini + "'" +
            " and pgto <='" + ValDtfim + "' ORDER BY vcto DESC")

        elif tipo == "" and status == "" and ccusto != "" and fpg == "" and datapago == 2 and competencia == 1:
          c = banco.conexao.cursor()
          #c.execute("SELECT * FROM controles ORDER BY vcto DESC")
          c.execute("SELECT * FROM controles WHERE ccusto ='" + ccusto + "'" + " and vcto >='" + ValDtini + "'" +
            " and vcto <='" + ValDtfim + "' and compet <> '0' ORDER BY vcto DESC")

        elif tipo == "" and status == "" and ccusto != "" and fpg == "" and datapago == 1 and competencia == 1:
          c = banco.conexao.cursor()
          c.execute("SELECT * FROM controles WHERE ccusto ='" + ccusto + "'" + " and pgto >='" + ValDtini + "'" +
            " and pgto <='" + ValDtfim + "' and compet <> '0' ORDER BY vcto DESC")

        elif tipo == "" and status == "" and ccusto == "" and fpg != "" and datapago == 2 and competencia == 2:
          c = banco.conexao.cursor()
          c.execute("SELECT * FROM controles WHERE fpg ='" + fpg + "'" + " and vcto >='" + ValDtini + "'" +
            " and vcto <='" + ValDtfim + "' ORDER BY vcto DESC")
        
        elif tipo == "" and status == "" and ccusto == "" and fpg != "" and datapago == 1 and competencia == 2:
          c = banco.conexao.cursor()
          c.execute("SELECT * FROM controles WHERE fpg ='" + fpg + "'" + " and pgto >='" + ValDtini + "'" +
            " and pgto <='" + ValDtfim + "' ORDER BY vcto DESC")

        elif tipo == "" and status == "" and ccusto == "" and fpg != "" and datapago == 2 and competencia == 1:
          c = banco.conexao.cursor()
          c.execute("SELECT * FROM controles WHERE fpg ='" + fpg + "'" + " and vcto >='" + ValDtini + "'" +
            " and vcto <='" + ValDtfim + "' and compet <> '0' ORDER BY vcto DESC")

        elif tipo == "" and status == "" and ccusto == "" and fpg != "" and datapago == 1 and competencia == 1:
          c = banco.conexao.cursor()
          c.execute("SELECT * FROM controles WHERE fpg ='" + fpg + "'" + " and pgto >='" + ValDtini + "'" +
            " and pgto <='" + ValDtfim + "' and compet <> '0' ORDER BY vcto DESC")

        elif tipo == "" and status == "" and ccusto == "" and fpg == "" and datapago == 2 and competencia == 2:
          c = banco.conexao.cursor()
          c.execute("SELECT * FROM controles WHERE vcto >='" + ValDtini + "'" +
            " and vcto <='" + ValDtfim + "' ORDER BY vcto DESC")
                  
        elif tipo == "" and status == "" and ccusto == "" and fpg == "" and datapago == 1 and competencia == 2:
          c = banco.conexao.cursor()
          c.execute("SELECT * FROM controles WHERE pgto >='" + ValDtini + "'" +
            " and pgto <='" + ValDtfim + "' ORDER BY vcto DESC")

        elif tipo == "" and status == "" and ccusto == "" and fpg == "" and datapago == 2 and competencia == 1:
          c = banco.conexao.cursor()
          c.execute("SELECT * FROM controles WHERE vcto >='" + ValDtini + "'" +
            " and vcto <='" + ValDtfim + "' and compet <> '0' ORDER BY vcto DESC")

        elif tipo == "" and status == "" and ccusto == "" and fpg == "" and datapago == 1 and competencia == 1:
          c = banco.conexao.cursor()
          c.execute("SELECT * FROM controles WHERE pgto >='" + ValDtini + "'" +
            " and pgto <='" + ValDtfim + "' and compet <> '0' ORDER BY vcto DESC")


        tb_movimento.delete(*tb_movimento.get_children())

    

        for linha in c:
            self.id = linha[0]
            self.tipo = linha[1]
            self.historico = linha[2]
            self.compet = linha[3]
            self.ccusto = linha[4]
            self.doc = linha[5]
            self.valor=linha[6]
            self.vcto=linha[7]
            self.pgto=linha[8]
            self.fpg=linha[9]
            self.status=linha[10]
            self.saldo=linha[11]
            
            valorTotal= valorTotal + float(self.valor)
            compTotal= compTotal + float(self.compet)
            saldTotal= saldTotal + float(self.saldo)
            pagoTotal= float(valorTotal) - float(saldTotal)

            if self.ccusto == 'F':
              valorf = valorf + self.valor
            if self.ccusto == 'U':
              valoru = valoru + self.valor
            if self.ccusto == 'C':
              valorc = valorc + self.valor
            if self.ccusto == 'P':
              valorp = valorp + self.valor

            if self.tipo == 'F':
              tvalorf = tvalorf + self.valor
            if self.tipo == 'V':
              tvalorv = tvalorv + self.valor
            if self.tipo == 'I':
              tvalori = tvalori + self.valor
            if self.tipo == 'C':
              tvalorc = tvalorc + self.valor

            tb_movimento.insert("","end",values=(self.id,self.tipo,self.historico,self.compet,self.ccusto,self.doc,self.valor,
              self.vcto,self.pgto,self.fpg,self.status,self.saldo))
            #print(valorTotal)

        compTotal = "R$ " + str("%.2f" %compTotal).replace('.',',')
        valorTotal = "R$ " + str("%.2f" %valorTotal).replace('.',',')
        pagoTotal = "R$ " + str("%.2f" %pagoTotal).replace('.',',')
        saldTotal = "R$ " + str("%.2f" %saldTotal).replace('.',',')

        tb_movimento.insert("","end",values=("","",""))
        tb_movimento.insert("","end",values=("","","SubTotal",compTotal,"","",valorTotal,"",pagoTotal,"","",saldTotal))
        
        todoscc = valorf + valorc + valoru + valorp
        self.cclistados=[valorf,valoru,valorc,valorp]

        todostip = tvalorf + tvalorc + tvalori + tvalorv
        self.tlistados=[tvalori,tvalorc,tvalorf,tvalorv]
        
        c.close()
        return "Atualizado com sucesso!"
    except banco.conexao.Error as error:
        return "Ocorreu um erro na atualização"

  

  def selecttodos(self, tb_movimento):
    banco = Banco()
    valorTotal=0
    compTotal=0
    saldTotal=0
    pagoTotal=0
    #valores para grafic1
    valorf = 0
    valoru = 0
    valorc = 0
    valorp = 0
    todoscc = 0
    #valores para grafic2
    tvalorf = 0
    tvalorv = 0
    tvalorc = 0
    tvalori = 0
    todostip = 0

    try:

        c = banco.conexao.cursor()

        c.execute("SELECT * FROM controles ORDER BY vcto DESC")

        
        tb_movimento.delete(*tb_movimento.get_children())
        for linha in c:
            self.id = linha[0]
            self.tipo = linha[1]
            self.historico = linha[2]
            self.compet = linha[3]
            self.ccusto = linha[4]
            self.doc = linha[5]
            self.valor=linha[6]
            self.vcto=linha[7]
            self.pgto=linha[8]
            self.fpg=linha[9]
            self.status=linha[10]
            self.saldo=linha[11]
            print(valor)
            #valorTotal= valorTotal + float(self.valor)
            compTotal= compTotal + float(self.compet)
            saldTotal= saldTotal + float(self.saldo)
            pagoTotal= float(valorTotal) - float(saldTotal)

            if self.ccusto == 'F':
              valorf = valorf + self.valor
            if self.ccusto == 'U':
              valoru = valoru + self.valor
            if self.ccusto == 'C':
              valorc = valorc + self.valor
            if self.ccusto == 'P':
              valorp = valorp + self.valor

            if self.tipo == 'F':
              tvalorf = tvalorf + self.valor
            if self.tipo == 'V':
              tvalorv = tvalorv + self.valor
            if self.tipo == 'I':
              tvalori = tvalori + self.valor
            if self.tipo == 'C':
              tvalorc = tvalorc + self.valor

            self.compet = "R$ " + str("%.2f" %self.compet).replace('.',',')
            self.valor = "R$ " + str("%.2f" %self.valor).replace('.',',')
            self.saldo = "R$ " + str("%.2f" %self.saldo).replace('.',',')

            

            tb_movimento.insert("","end",values=(self.id,self.tipo,self.historico,self.compet,self.ccusto,self.doc,self.valor,
              self.vcto,self.pgto,self.fpg,self.status,self.saldo))
            #print(valorTotal)
        compTotal = "R$ " + str("%.2f" %compTotal).replace('.',',')
        valorTotal = "R$ " + str("%.2f" %valorTotal).replace('.',',')
        pagoTotal = "R$ " + str("%.2f" %pagoTotal).replace('.',',')
        saldTotal = "R$ " + str("%.2f" %saldTotal).replace('.',',')

        tb_movimento.insert("","end",values=("","",""))
        tb_movimento.insert("","end",values=("","","Total",compTotal,"","",valorTotal,"",pagoTotal,"","",saldTotal))

        todoscc = valorf + valorc + valoru + valorp
        self.cclistados=[valorf,valoru,valorc,valorp]

        todostip = tvalorf + tvalorc + tvalori + tvalorv
        self.tlistados=[tvalori,tvalorc,tvalorf,tvalorv]

        c.close()
        return "Atualizado com sucesso!"
    except banco.conexao.Error as error:
        return "Ocorreu um erro na atualização"


  def selectidic(self):
    banco = Banco()
    valorTotal=0
    compTotal=0
    saldTotal=0
    pagoTotal=0
    valorf = 0
    valoru = 0
    valorc = 0
    valorp = 0
    todoscc = 0
    tvalorf = 0
    tvalorv = 0
    tvalorc = 0
    tvalori = 0
    todostip = 0

    try:

        c = banco.conexao.cursor()

        c.execute("SELECT * FROM controles ORDER BY vcto DESC")

        
        #tb_movimento.delete(*tb_movimento.get_children())
        for linha in c:
            self.id = linha[0]
            self.tipo = linha[1]
            self.historico = linha[2]
            self.compet = linha[3]
            self.ccusto = linha[4]
            self.doc = linha[5]
            self.valor=linha[6]
            self.vcto=linha[7]
            self.pgto=linha[8]
            self.fpg=linha[9]
            self.status=linha[10]
            self.saldo=linha[11]
            
            valorTotal= valorTotal + float(self.valor)
            compTotal= compTotal + float(self.compet)
            saldTotal= saldTotal + float(self.saldo)
            pagoTotal= float(valorTotal) - float(saldTotal)

            self.compet = "R$ " + str("%.2f" %self.compet).replace('.',',')
            if self.ccusto == 'F':
              valorf = valorf + self.valor
            if self.ccusto == 'U':
              valoru = valoru + self.valor
            if self.ccusto == 'C':
              valorc = valorc + self.valor
            if self.ccusto == 'P':
              valorp = valorp + self.valor

            if self.tipo == 'F':
              tvalorf = tvalorf + self.valor
            if self.tipo == 'V':
              tvalorv = tvalorv + self.valor
            if self.tipo == 'I':
              tvalori = tvalori + self.valor
            if self.tipo == 'C':
              tvalorc = tvalorc + self.valor
            

            self.saldo = "R$ " + str("%.2f" %self.saldo).replace('.',',')
        todoscc = valorf + valorc + valoru + valorp
        
        
        self.listados=[valorf,valoru,valorc,valorp]

            
        c.close()
        return "Atualizado com sucesso!"
    except banco.conexao.Error as error:
        return "Ocorreu um erro na atualização"
 