import MySQLdb
class Database(object):
    def __init__(self):
        self.__db = MySQLdb.connect("localhost","root","","kicrev" )
        self.__cursor=self.__db.cursor()
    def masukan_kicauan(self,topik,kicauan,jenis_kicauan):
        kicauan=kicauan.encode('ascii', 'replace')
        sql= "INSERT INTO KICAUAN(ID,Topik,isi_kicauan,Jenis_kicauan)VALUES (NULL,'%s', '%s', '%d')" % (topik,kicauan,jenis_kicauan)
        try :
            self.__cursor.execute(sql)
            self.__db.commit()
        except:
            self.__db.rollback()
        #self.db.close()


        
