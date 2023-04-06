#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector

dataBase = mysql.connector.connect(
host ="localhost",
user ="root"
)

#preparing a cursor object
cursorObject = dataBase.cursor()

#creating database
cursorObject.execute("CREATE DATABASE D3_TI_2023")


# In[2]:


import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    database="D3_TI_2023"
)

# preparing a cursor object
cursorObject = dataBase.cursor()

# create table Mata_Kuliah
courseRecord = """CREATE TABLE Mata_Kuliah (
                    Kode_MK VARCHAR(10) PRIMARY KEY,
                    Nama_MK VARCHAR(50) NOT NULL,
                    Waktu DATE,
                    Ruangan VARCHAR(10)
                   )"""
cursorObject.execute(courseRecord)

# creating table Mahasiswa
studentRecord = """CREATE TABLE Mahasiswa (
                    NIM VARCHAR(10) PRIMARY KEY,
                    Nama VARCHAR(30) NOT NULL,
                    Jurusan VARCHAR(30),
                    Alamat VARCHAR(255),
                    Mata_kuliah_yang_diikuti VARCHAR(10),
                    FOREIGN KEY (Mata_kuliah_yang_diikuti) REFERENCES Mata_Kuliah(Kode_MK)
                   )"""
cursorObject.execute(studentRecord)

# creating table Dosen
teacherRecord = """CREATE TABLE Dosen (
                    NIP VARCHAR(20) PRIMARY KEY,
                    Nama_Dosen VARCHAR(50) NOT NULL,
                    Alamat VARCHAR(255),
                    Mata_kuliah_yang_diajar VARCHAR(10),
                    FOREIGN KEY ( Mata_kuliah_yang_diajar) REFERENCES Mata_Kuliah(Kode_MK)
                   )"""
cursorObject.execute(teacherRecord)

# disconnecting from server
dataBase.close()


# In[6]:


import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    database="D3_TI_2023"
)

# preparing a cursor object
cursorObject = dataBase.cursor()

# inserting data into the Mata_Kuliah table
sql3 = "INSERT INTO Mata_Kuliah (Kode_MK, Nama_MK, Waktu, Ruangan) VALUES (%s, %s, %s, %s)"
val3 = [('MK001', 'Pemrograman Berorientasi Objek', '2023-03-10', 'A101'),
       ('MK002', 'Pemrograman Web', '2023-03-12', 'B201'),
       ('MK003', 'Python', '2023-03-14', 'C301'),
       ('MK004', 'Algoritma dan Pemrograman', '2023-04-16', 'D401'),
       ('MK005', 'Basis Data', '2023-03-18', 'E501')]
cursorObject.executemany(sql3, val3)

# inserting data into the Mahasiswa table
sql1 = "INSERT INTO Mahasiswa (NIM, Nama, jurusan, Alamat, Mata_kuliah_yang_diikuti) VALUES (%s, %s, %s, %s, %s)"
val1 = [('1234567890', 'Rony', 'Teknik Informatika', 'Jakarta', 'MK001'),
       ('2345678901', 'Salma', 'Teknik Informatika', 'Bandung', 'MK002'),
       ('3456789012', 'Keshya', 'Teknik Informatika', 'Surabaya', 'MK003'),
       ('4567890123', 'Paul', 'Teknik Informatika', 'Bali', 'MK004'),
       ('5678901234', 'Nabila', 'Teknik Informatika', 'Kalimantan', 'MK005')]
cursorObject.executemany(sql1, val1)

# inserting data into the Dosen table
sql2 = "INSERT INTO Dosen (NIP, Nama_Dosen, Alamat, Mata_kuliah_yang_diajar) VALUES (%s, %s, %s, %s)"
val2 = [('123456789012', 'Budi', 'Madiun', 'MK001'),
       ('234567890123', 'Dika', 'Blitar', 'MK002'),
       ('345678901234', 'Bella', 'Jombang', 'MK003'),
       ('456789012345', 'Elena', 'Jakarta', 'MK004'),
       ('567890123456', 'Leo', 'Medan', 'MK005')]
cursorObject.executemany(sql2, val2)



dataBase.commit()

# disconnecting from server
dataBase.close()


# In[23]:


import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    database="D3_TI_2023"
)

# preparing a cursor object
cursorObject = dataBase.cursor()

# query 1: ambil data NIM dan nama mahasiswa yang diikuti oleh setiap mata kuliah beserta nama dosen pengajar
query1 = "SELECT Mahasiswa.NIM, Mahasiswa.Nama, Mata_kuliah.Nama_MK, Dosen.Nama_Dosen FROM Mahasiswa JOIN Mata_kuliah ON Mahasiswa.Mata_kuliah_yang_diikuti = Mata_kuliah.Kode_MK JOIN Dosen ON Mata_Kuliah.Kode_MK = Dosen.Mata_kuliah_yang_diajar"

cursorObject.execute(query1)
result1 = cursorObject.fetchall()

# tampilkan hasil
for row in result1:
    print(row[0], row[1], row[2], row[3])

# disconnecting from server
dataBase.close()


# In[ ]:




