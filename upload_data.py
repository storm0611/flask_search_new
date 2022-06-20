from selectors import SelectSelector
from turtle import tilt
from unittest import result
import requests
import pandas
from flask import Flask, request, Response
import pymysql
from pymysql import Error
from datetime import datetime
import re

SERVER_URL = 'http://tandem7.pythonanywhere.com' # same this for this one it's API_SERVER URL
endpoint = '/add'

# It is the function to read your csv data returnd by scraping script that you have.
def read_csv_data():

    #first let me show you how much already added data in database. 4195 already present data.
    # can you please show me this .csv file or put this csv file in same path of sccript?
    # yeah let me search for it..
    # you can also set it's path to csv file
    data = pandas.read_csv('final_df_sample_noindex_with_domain.csv', sep=',')
    return data # and here it's returning all the readed data from csv file , I am using pandas for reading file

def insert_data(_table, _what, _where, _wval, _where1='', _wval1='', _where2='', _wval2='', _where3='', _wval3='', _where4='', _wval4=''):
    select_query = "SELECT " + _what + " FROM " + _table + " WHERE " + _where + "=" + _wval + ";";
    print(select_query)
    cursor.execute(select_query)
    result = cursor.fetchall()
    if len(result):
        id = result[0][0]
    else:
        insert_query = "INSERT INTO " + _table + " (" + _where + _where1 + _where2 + _where3 + _where4 + ") VALUES (" + _wval + _wval1 + _wval2 + _wval3 + _wval4 + ");";
        print(insert_query)
        cursor.execute(insert_query)
        connection.commit()
        select_query = "SELECT " + _what + " FROM " + _table + ";"
        print(select_query)
        cursor.execute(select_query)
        result = cursor.fetchall()
        id = len(result)
    return id

def insert_data_connect(_table, _val1, _val2):
    insert_query = insert_query = "INSERT INTO " + _table + " VALUES (" + _val1 + ', ' + _val2 + ");";
    print(insert_query)
    cursor.execute(insert_query)
    connection.commit()
        

def upload_data():
    global cursor
    with connection.cursor() as cursor:
        csv_data = read_csv_data()

        for i in range(len(csv_data)):

            journal = re.split("\'|\"", csv_data['journal'][i])[1]
            pm_id = csv_data['pmid'][i]
            pm_link = csv_data['pm_link'][i]
            date_pub = re.split("\'|\"", csv_data['date_pub'][i])[1]
            abstract = re.split("\'|\"", csv_data['abstract'][i])[1]
            title = re.split("\'|\"", csv_data['title'][i])[1]
            study_design = csv_data['study_design'][i]
            data_type = csv_data['data_type'][i]
            mesh = csv_data['mesh'][i]
            concept_id = csv_data['concept_id_1'][i]
            domain = csv_data['domain_id'][i]
            
            journal_id = insert_data('journals', 'id', 'journal', "'" + str(journal) + "'")
            print(journal_id)
            
            insert_query = "INSERT INTO articles (pm_id, pm_link, date_pub, abstract, title, journal_id) VALUES (" + \
                                                    str(pm_id) + ", '" + str(pm_link) + "', '" + date_pub + "', '" + abstract + "', '" + title + "', " + str(journal_id) + ");"
            print(insert_query)
            cursor.execute(insert_query)
            connection.commit()
            select_query = "SELECT id FROM articles;"
            cursor.execute(select_query)
            result = cursor.fetchall()
            article_id = len(result)
            print(article_id)
            
            study_design_id = insert_data('study_design', 'id', 'study_design', "'" + study_design + "'")
            print(study_design_id)
            
            insert_data_connect('study_design_connect', str(article_id), str(study_design_id))
            
            data_type_id = insert_data('data_type', 'id', 'data_type', "'" + data_type + "'")
            print(data_type_id)
            
            insert_data_connect('data_type_connect', str(article_id), str(data_type_id))
            
            mesh_id = insert_data('mesh', 'id', 'mesh', "'" + mesh + "'", ', concept_id', ", " + str(concept_id), ', domain', ", '" + domain + "'",)
            insert_data_connect('meshes_connect', str(article_id), str(mesh_id))
            
            
            # category_name = csv_data['category_name'][i]
            # print(category_name)

            # So now here is i am putting data to payload to send data to server via API
            # data = {}
            # data['pmid'] = str(pm_id)
            # data['pm_link'] = str(pm_link)
            # data['date_pub'] = str(date_pub)
            # data['journal'] = str(journal)
            # data['abstract'] = str(abstract)
            # data['title'] = str(title)
            # data['mesh'] = str(mesh)
            # data['concept_id_1'] = str(concept_id_1)
            # data['concept_name'] = str(concept_name)
            # data['study_design'] = str(study_design)
            # data['data_type'] = str(data_type)
            # data['domain_id'] = str(domain_id)
            # data['category_name'] = str(category_name)
            # print(data)

            # res = requests.post(url=SERVER_URL + endpoint ,json=data) # and here sending data to server and getting response.
            # if (res.status_code == 200):
            #     print(res.text + ": "+str(i) + " out of {}".format(len(csv_data['title'])))
            # else:
            #     print(res.text)


        #Sure so now let me show you how you can add more columns in easy way but one more thing when you will add more columns you need to add columns in server script too.
        # ok, just show me please)
        # ok


if __name__ == "__main__":
    try:
        # Connect table in db

        global connection

        with pymysql.connect(
            host="localhost",
            user='root',
            password='',
            database='mydb'
        ) as connection:
            print(connection)

            upload_data()
    
            # Create new threads
            # check_file_thread = myThread(0, "Thread-1", 0.5)

            # Start new Threads
            # check_file_thread.start()

            # while check_file_thread.is_alive():
            #     if keyboard.is_pressed("esc"):
            #         exitFlag = 1

            # print("Exiting Main Thread")

    except Error as e:
        print(e)
