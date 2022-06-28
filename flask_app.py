from ctypes.wintypes import POINT
from email.errors import InvalidMultipartContentTransferEncodingDefect
import json
from unittest import result
from urllib import response

from urllib.robotparser import RequestRate
from flask_restful import reqparse, Api, Resource , request
from flaskext.mysql import MySQL
from flask_cors import CORS, cross_origin
from flask import Flask, jsonify, render_template, request, send_file, make_response, abort, session
from numpy import int64, ndarray, result_type, true_divide
# from plots_code import barchart_diseases
import pymysql
from pymysql import Error
import pandas as pd
import logging
import numpy as np

app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'Tandem7'
app.config['MYSQL_DATABASE_PASSWORD'] = 'shani@@@@143'
app.config['MYSQL_DATABASE_DB'] = 'Tandem7$articles_db'
app.config['MYSQL_DATABASE_HOST'] = 'Tandem7.mysql.pythonanywhere-services.com'
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = ''
# app.config['MYSQL_DATABASE_DB'] = 'mydb'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'

cors = CORS(app)
MySql = MySQL()
MySql.init_app(app)
connection = MySql.connect()
Pointer = connection.cursor()


def init_db():
    sql_query = """DROP TABLE IF EXISTS articles;
                    CREATE TABLE articles  (
                    id int NOT NULL AUTO_INCREMENT,
                    pm_id text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
                    pm_link text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
                    date_pub text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
                    journal_id int NULL DEFAULT NULL,
                    title longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
                    abstract longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
                    category_name text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
                    n_participant int NULL DEFAULT NULL,
                    PRIMARY KEY (id) USING BTREE
                    ) ENGINE = InnoDB AUTO_INCREMENT = 196 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;"""
    Pointer.execute(sql_query)
    sql_query = """DROP TABLE IF EXISTS authors;
                    CREATE TABLE authors  (
                    id int NOT NULL AUTO_INCREMENT,
                    author text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
                    author_ranking text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
                    PRIMARY KEY (id) USING BTREE
                    ) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;"""
    Pointer.execute(sql_query)
    sql_query = """DROP TABLE IF EXISTS authors_connect;
                    CREATE TABLE authors_connect  (
                    article_id int NULL DEFAULT NULL,
                    author_id int NULL DEFAULT NULL
                    ) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;"""
    Pointer.execute(sql_query)
    sql_query = """DROP TABLE IF EXISTS data_type;
                    CREATE TABLE data_type  (
                    id int NOT NULL AUTO_INCREMENT,
                    data_type text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
                    PRIMARY KEY (id) USING BTREE
                    ) ENGINE = InnoDB AUTO_INCREMENT = 93 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;"""
    Pointer.execute(sql_query)
    sql_query = """DROP TABLE IF EXISTS geography;
                    CREATE TABLE geography  (
                    id int NOT NULL AUTO_INCREMENT,
                    country text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
                    region text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
                    city text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
                    PRIMARY KEY (id) USING BTREE
                    ) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;"""
    Pointer.execute(sql_query)
    sql_query = """DROP TABLE IF EXISTS journals;
                    CREATE TABLE journals  (
                    id int NOT NULL AUTO_INCREMENT,
                    journal text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
                    journal_country text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
                    ranking text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
                    PRIMARY KEY (id) USING BTREE
                    ) ENGINE = InnoDB AUTO_INCREMENT = 146 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;"""
    Pointer.execute(sql_query)
    sql_query = """DROP TABLE IF EXISTS mesh;
                    CREATE TABLE mesh  (
                    id int NOT NULL AUTO_INCREMENT,
                    mesh text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
                    concept_id text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
                    domain text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
                    PRIMARY KEY (id) USING BTREE
                    ) ENGINE = InnoDB AUTO_INCREMENT = 382 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;"""
    Pointer.execute(sql_query)
    sql_query = """DROP TABLE IF EXISTS meshes_connect;
                    CREATE TABLE meshes_connect  (
                    article_id int NULL DEFAULT NULL,
                    mesh_id int NULL DEFAULT NULL
                    ) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;"""
    Pointer.execute(sql_query)
    sql_query = """DROP TABLE IF EXISTS study_design;
                    CREATE TABLE study_design  (
                    id int NOT NULL AUTO_INCREMENT,
                    study_design text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
                    PRIMARY KEY (id) USING BTREE
                    ) ENGINE = InnoDB AUTO_INCREMENT = 42 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;"""
    Pointer.execute(sql_query)
    sql_query = """DROP TABLE IF EXISTS study_design_connect;
                    CREATE TABLE study_design_connect  (
                    article_id int NULL DEFAULT NULL,
                    study_design_id int NULL DEFAULT NULL
                    ) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;"""
    Pointer.execute(sql_query)
    sql_query = """DROP TABLE IF EXISTS vocabs_connect;
                    CREATE TABLE vocabs_connect  (
                    article_id int NULL DEFAULT NULL,
                    vocab_id int NULL DEFAULT NULL
                    ) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;"""
    Pointer.execute(sql_query)
    sql_query = """DROP TABLE IF EXISTS vocabularies;
                    CREATE TABLE vocabularies  (
                    id int NOT NULL AUTO_INCREMENT,
                    omop_vocab text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
                    PRIMARY KEY (id) USING BTREE
                    ) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;"""
    Pointer.execute(sql_query)
    

def insert_data(_table, _what, _where, _wval, _where1='', _wval1='', _where2='', _wval2='', _where3='', _wval3='', _where4='', _wval4=''):
    select_query = "SELECT " + _what + " FROM " + \
        _table + " WHERE " + _where + "=" + _wval + ";"
    print(select_query)    
    Pointer.execute(select_query)
    result = Pointer.fetchall()
    if len(result):
        id = result[0][0]
    else:
        insert_query = "INSERT INTO " + _table + \
            " (" + _where + _where1 + _where2 + _where3 + _where4 + \
            ") VALUES (" + _wval + _wval1 + _wval2 + _wval3 + _wval4 + ");"
        print(insert_query)
        Pointer.execute(insert_query)
        connection.commit()
        select_query = "SELECT " + _what + " FROM " + _table + ";"
        print(select_query)
        Pointer.execute(select_query)
        result = Pointer.fetchall()
        id = len(result)
    return id

def insert_data_connect(_table, _val1, _val2):
    insert_query = insert_query = "INSERT INTO " + \
        _table + " VALUES (" + _val1 + ', ' + _val2 + ");"
    print(insert_query)
    Pointer.execute(insert_query)
    connection.commit()

# Sevrer script with two API endpoints (Upload and Fetch) that only accept http or https POST requests
@app.route('/add', methods=['POST']) #/add end point that can only be call via POST request
def add_article():
    init_db()
    #get data from the Client side through API and put data to the database
    json_data = request.get_json(force=True)
    print(json_data)
#     json_data = request.get_json()
    pm_id = int64(json_data['pm_id'])
    pm_link = json_data['pm_link']
    date_pub = json_data['date_pub']
    journal = json_data['journal']
    abstract = json_data['abstract']
    title = json_data['title']
    mesh = json_data['mesh']
    concept_id = int64(json_data['concept_id'])
    study_design = json_data['study_design']
    data_type = json_data['data_type']
    domain_id = json_data['domain']
    category_name = json_data['category_name']
    
    if pm_id and pm_link and date_pub and journal and abstract and title and mesh and concept_id and study_design and data_type and domain_id and category_name and request.method == 'POST':
        journal_id = insert_data(
            'journals', 'id', 'journal', "'" + str(journal) + "'")
        print(journal_id)

        select_query = "SELECT id FROM articles WHERE pm_id=" + str(pm_id)
        Pointer.execute(select_query)
        res = Pointer.fetchall()
        if len(res):
            article_id = res[0][0]
        else:
            insert_query = "INSERT INTO articles (pm_id, pm_link, date_pub, abstract, title, journal_id, category_name) VALUES (" + \
                str(pm_id) + ", '" + str(pm_link) + "', '" + date_pub + "', '" + \
                abstract + "', '" + title + "', " + str(journal_id) + ", '" + category_name + "');"
            # print(insert_query)
            Pointer.execute(insert_query)
            connection.commit()
            select_query = "SELECT id FROM articles;"
            Pointer.execute(select_query)
            result = Pointer.fetchall()
            article_id = len(result)
        print(article_id)

        study_design_id = insert_data(
            'study_design', 'id', 'study_design', "'" + study_design + "'")
        print(study_design_id)

        insert_data_connect('study_design_connect', str(
            article_id), str(study_design_id))

        data_type_id = insert_data(
            'data_type', 'id', 'data_type', "'" + data_type + "'")
        print(data_type_id)

        insert_data_connect('data_type_connect', str(
            article_id), str(data_type_id))

        mesh_id = insert_data('mesh', 'id', 'mesh', "'" + mesh + "'", ', concept_id',
                              ", " + str(concept_id), ', domain', ", '" + domain_id + "'",)
        insert_data_connect(
            'meshes_connect', str(article_id), str(mesh_id))
        response = jsonify('Article Added!')
        response.status_code = 200 #if data addedd successfully: response 200
        return response
    else:
        # if error: response 500
        response = jsonify('err')
        return response


@app.route('/fetch',methods=['POST'])  #Method to fetch / search data from the database
def fetch_article():
    json = request.json
    start = json['start']
    end = json['end']

    if (start and end and request.method == 'POST'):
        connection =MySql.connect()
        Pointer = connection.cursor(pymysql.cursors.DictCursor)
        Pointer.execute("select * from articles limit "+str(start)+" , "+str(end)+";")
        records = Pointer.fetchall()

        response = jsonify(records)
        response.status_code = 200
        return response #return all the rows from (start , end)
    else:
        return "err"


@app.route('/get_study_design',methods=['POST'])
def get_study_design():
    if (request.method == 'POST'):
        connection =MySql.connect()
        Pointer = connection.cursor()
        Pointer.execute("SELECT study_design FROM study_design")
        records = Pointer.fetchall()

        response = jsonify(records)
        response.status_code = 200
        return response #return all the rows (start , end)
    else:
        return "err"


@app.route('/get_drug_categories',methods=['POST'])
def get_drug_categories():
    if (request.method == 'POST'):
        connection =MySql.connect()
        Pointer = connection.cursor()
        Pointer.execute("SELECT category_name FROM articles")
        records = Pointer.fetchall()

        response = jsonify(records)
        response.status_code = 200
        return response #return all the rows (start , end)
    else:
        return "err"

@app.route('/get_condition_categories',methods=['POST'])
def get_condition_categories():
    if (request.method == 'POST'):
        connection =MySql.connect()
        Pointer = connection.cursor()
        Pointer.execute("SELECT category_name FROM articles")
        records = Pointer.fetchall()

        response = jsonify(records)
        response.status_code = 200
        return response #return all the rows (start , end)
    else:
        return "err"



@app.route('/get_data_type',methods=['POST'])
def get_data_type():
    if (request.method == 'POST'):

        connection =MySql.connect()
        Pointer = connection.cursor()
        Pointer.execute("SELECT data_type FROM data_type")
        records = Pointer.fetchall()

        response = jsonify(records)
        response.status_code = 200
        return response #return all the rows (start , end)
    else:
        return "err"


@app.route('/get_date_pub', methods=['POST'])
def get_date_pub():
    if (request.method == 'POST'):

        connection =MySql.connect()
        Pointer = connection.cursor()
        Pointer.execute("SELECT distinct date_pub FROM articles ORDER BY date_pub ASC")
        records = Pointer.fetchall()

        response = jsonify(records)
        response.status_code = 200
        return response #return all the rows (start , end)
    else:
        return "err"
    

@app.route('/get_geography', methods=['POST'])
def get_geography():
    if (request.method == 'POST'):

        connection = MySql.connect()
        Pointer = connection.cursor()
        Pointer.execute("SELECT distinct country FROM geography")
        records = Pointer.fetchall()

        response = jsonify(records)
        response.status_code = 200
        return response  # return all the rows (start , end)
    else:
        return "err"


@app.route('/get_vocabulary', methods=['POST'])
def get_vocabulary():
    if (request.method == 'POST'):

        connection = MySql.connect()
        Pointer = connection.cursor()
        Pointer.execute("SELECT distinct omop_vocab FROM vocabularies")
        records = Pointer.fetchall()

        response = jsonify(records)
        response.status_code = 200
        return response  # return all the rows (start , end)
    else:
        return "err"


@app.route('/get_journal', methods=['POST'])
def get_journal():
    if (request.method == 'POST'):

        connection = MySql.connect()
        Pointer = connection.cursor()
        Pointer.execute("SELECT distinct journal FROM journals")
        records = Pointer.fetchall()

        response = jsonify(records)
        response.status_code = 200
        return response  # return all the rows (start , end)
    else:
        return "err"


@app.route('/get_domain', methods=['POST'])
def get_domain():
    if (request.method == 'POST'):

        connection = MySql.connect()
        Pointer = connection.cursor()
        Pointer.execute("SELECT distinct domain FROM mesh")
        records = Pointer.fetchall()

        response = jsonify(records)
        response.status_code = 200
        return response  # return all the rows (start , end)
    else:
        return "err"


@app.route('/get_mesh_sug', methods=['POST'])
def get_mesh_sug():
    if (request.method == 'POST'):

        connection = MySql.connect()
        Pointer = connection.cursor()
        Pointer.execute("SELECT distinct mesh FROM mesh")
        records = Pointer.fetchall()

        response = jsonify(records)
        response.status_code = 200
        return response  # return all the rows (start , end)
    else:
        return "err"


@app.route('/get_con_sug', methods=['POST'])
def get_con_sug():
    if (request.method == 'POST'):

        connection = MySql.connect()
        Pointer = connection.cursor()
        Pointer.execute("SELECT distinct concept_id FROM mesh")
        records = Pointer.fetchall()

        response = jsonify(records)
        response.status_code = 200
        return response  # return all the rows (start , end)
    else:
        return "err"


@app.route('/fetch_by_tags',methods=['POST'])  #method to fetch / search data from database
def fetch_by_tags_article():
    json = request.json
    start = json['start']
    end = json['end']
    tags = json['tags']


    tags = tags.split(',')
    if (start and end and tags  and request.method == 'POST'):
        connection =MySql.connect()
        Pointer = connection.cursor(pymysql.cursors.DictCursor)
        query_statement = ''
        if (len(tags) == 1):
            mesh_1 = tags[0]
            one_query = ''
            if (str(mesh_1).isnumeric()):
                one_query = 'concept_id = "'+mesh_1+'"'
            else:
                one_query = 'mesh = "'+mesh_1+'"'
            print("mesh: "+str(mesh_1))
            Pointer.execute("select * from articles where "+one_query+" limit "+str(start)+" , "+str(end)+";")
            records = Pointer.fetchall()
            print(records)
            response = jsonify(records)
            response.status_code = 200
            return response #return all the rows (start , end)
        elif (len(tags) > 1):
            mesh_1 = tags[0]
            one_query = ''
            if (str(mesh_1).isnumeric()):
                one_query = 'concept_id = "'+mesh_1+'"'
            else:
                one_query = 'mesh = "'+mesh_1+'"'
            print("mesh: "+str(mesh_1))
            Pointer.execute("select DISTINCT pm_id from articles where "+one_query+" limit "+str(start)+" , "+str(end)+";")
            records = Pointer.fetchall()
            #print(records)

            meshes = []
            concept_ids = []
            pm_ids = []
            i = 0
            for tag in tags:
                if (i > 0):
                    if (str(tag).isnumeric()):
                        concept_ids.append(tag)
                    else:
                        meshes.append(tag)
                i += 1
            results = []

            for pm_id in records:
                found_res = 0
                pm_id = pm_id['pm_id'] #[a,'b,c]

                    #print(mesh)
                if (len(meshes) > 0 and len(concept_ids) > 0):
                    for mesh in meshes:
                        q = "select * from articles where pm_id = '"+pm_id + "' and mesh like '%"+str(mesh) + "%' limit "+str(start)+" , "+str(end)+";"
                        Pointer.execute(q)
                        records = Pointer.fetchall()
                        if (len(records) > 0):
                            found_res += 1
                            for concept_id in concept_ids:
                                q = "select * from articles where pm_id = '"+pm_id + "' and concept_id like '%"+concept_id + "%' limit "+str(start)+" , "+str(end)+";"
                                #print(q)
                                Pointer.execute(q)
                                records = Pointer.fetchall()
                                if (len(records) > 0):
                                    found_res += 1
                                else:
                                    found_res = 0
                        else:
                            found_res = 0
                elif (len(meshes) > 0 and len(concept_ids) == 0):
                    print("Only MESHES ...............")
                    for mesh in meshes:
                        q = "select * from articles where pm_id = '"+pm_id + "' and mesh like '%"+str(mesh) + "%' limit "+str(start)+" , "+str(end)+";"
                        Pointer.execute(q)
                        records = Pointer.fetchall()
                        if (len(records) > 0):
                            found_res += 1
                        else:
                            found_res = 0
                elif (len(meshes) == 0 and len(concept_ids) > 0):

                    for concept_id in concept_ids:
                        q = "select * from articles where pm_id = '"+pm_id + "' and concept_id like '%"+concept_id + "%' limit "+str(start)+" , "+str(end)+";"
                        #print(q)
                        Pointer.execute(q)
                        records = Pointer.fetchall()
                        if (len(records) > 0):
                            found_res += 1
                        else:
                            found_res = 0

                if (found_res == len(meshes) + len(concept_ids)):
                    results.append(pm_id)

            print(results)

            if (len(results) > 0):
                query = ' where ( '
                i = 0
                for result in results:
                    if (i == len(results) - 1):
                        query += " pm_id = '"+result +"' ) "
                    else:
                        query += " pm_id = '"+result +"' or "
                    i += 1


                q = "select * from articles "+query + "limit "+str(start)+" , "+str(end)+";"
                print(q)
                Pointer.execute(q)
                records = Pointer.fetchall()
                print('res')
                print(result)
                return jsonify(records)

            return jsonify(results)


    else:
        return "err"


@app.route('/fetch_drugs',methods=['POST'])  #method to fetch / search data from database
def fetch_drugs():
    json = request.json
    pm_id = json['pm_id']
    concept_id = json['concept_id']
    if (pm_id and concept_id and request.method == 'POST'):

        connection =MySql.connect()
        Pointer = connection.cursor(pymysql.cursors.DictCursor)
        Pointer.execute("select * from articles where (pm_id = '" +
                        str(pm_id)+"')  and (concept_id = " + str(concept_id) + ");")
        records = Pointer.fetchall()

        response = jsonify(records)
        response.status_code = 200
        return response #return all the rows (start , end)
    else:
        return "err"


@app.route('/fetch_condition',methods=['POST'])  #method to fetch / search data from database
def fetch_condition():
    json = request.json
    pm_id = json['pm_id']
    concept_id = json['concept_id']
    if (pm_id and concept_id and request.method == 'POST'):

        connection =MySql.connect()
        Pointer = connection.cursor(pymysql.cursors.DictCursor)
        Pointer.execute("select * from articles where (pm_id = '" +
                        str(pm_id)+"')  and (concept_id = " + str(concept_id) + ");")
        records = Pointer.fetchall()

        response = jsonify(records)
        response.status_code = 200
        return response #return all the rows (start , end)
    else:
        return "err"


@app.route('/fetch_procedures',methods=['POST'])  #method to fetch / search data from database
def fetch_procedures():
    json = request.json
    pm_id = json['pm_id']
    concept_id = json['concept_id']
    if (pm_id and concept_id and request.method == 'POST'):

        connection =MySql.connect()
        Pointer = connection.cursor(pymysql.cursors.DictCursor)
        Pointer.execute("SELECT * from articles where (pm_id = "+str(pm_id)+") and (concept_id = " + str(concept_id) + ");")
        records = Pointer.fetchall()

        response = jsonify(records)
        response.status_code = 200
        return response #return all the rows (start , end)
    else:
        return "err"


@app.route('/get_database_table_as_dataframe',methods=['POST'])  #method to fetch / search data from database
def get_database_table_as_dataframe():
    """Connect to a table named 'articles'. Returns pandas dataframe."""
    try:
        connection =MySql.connect()
        articles_df = pd.read_sql(sql="""select * FROM articles""",
                               con=connection)
        logging.info(articles_df.head())
        return articles_df
    except:
        logging.exception('Failed to fetch dataframe from DB.')
        return "Oops!"


@app.route('/plots/articles_df/barchart_plot_diseases', methods=['GET'])
def barchart_plot_diseases():
    bytes_obj = barchart_diseases(get_database_table_as_dataframe)

    return send_file(bytes_obj,
                     attachment_filename='barchart_diseases.png',
                     mimetype='image/png')


@app.route('/plots/articles_df/barchart_plot_drugs', methods=['GET'])
def barchart_plot_drugs():
    bytes_obj = barchart_drugs(get_database_table_as_dataframe)

    return send_file(bytes_obj,
                     attachment_filename='barchart_drugs.png',
                     mimetype='image/png')


@app.route('/',methods=['POST','GET']) # '/' (only with slash), accepts POST and GET methods; Output - in the browser
def display():
    # return render_template('index.html')
    return "P is for Panther"

@app.route('/about',methods=['POST','GET']) 
def display_about():
    # return render_template('index.html')
    return "This is a About us page"


@app.route('/get_plots_data', methods=['POST', 'GET'])
def display_plots_get():
    if request.method == "POST":
        # print(request.get_json())
        a_id = request.get_json()['articles_id']
        # print(a_id)
        sql_query = "select mesh, domain from mesh inner join (select * from meshes_connect where article_id in (" + a_id + ")) as mh on mh.mesh_id=mesh.id;"
        Pointer.execute(sql_query)
        res = Pointer.fetchall()
        # print(res)
        n_drug = {}
        n_condition = {}
        results = []
        if len(res):
            for i in res:
                if i[1] == 'Drug':
                    try:
                        n_drug[i[0]] += 1
                    except:
                        n_drug[i[0]] = 1
                else:
                    if i[1] == 'Condition':
                        try:
                            n_condition[i[0]] += 1
                        except:
                            n_condition[i[0]] = 1
            
            results = {
                'n_drug' : n_drug,
                'n_condition' : n_condition
            }
        # print(results)
        response = jsonify(results)
        # print(response)
        return response
    if request.method == "GET":
        results = {'processed': 'GET is not supported'}
        return jsonify(results)
    
@app.route('/get_data',methods=['POST','GET']) 
def display_get():
    if request.method == "POST":
        # print(request.get_json())
        flt_mesh = request.get_json()['flt_mesh'].split(',')
        flt_co = []
        flt_sd = request.get_json()['flt_sd']
        flt_dt = request.get_json()['flt_dt']
        flt_date = request.get_json()['flt_date']
        flt_geo = request.get_json()['flt_geo']
        flt_vb = request.get_json()['flt_vb']
        flt_jo = request.get_json()['flt_jo']
        flt_dm = request.get_json()['flt_dm']
        flt_so = request.get_json()['flt_so']
        # print(flt_mesh)
        # print(flt_sd)
        # print(flt_dt)
        # print(flt_dc)
        # print(flt_cc)
        
        sql_query = "select count(*) from articles"
        Pointer.execute(sql_query)
        cnt = Pointer.fetchall()[0][0]       
        sign = np.zeros(cnt + 1)
        
        i = 0   
        sql_query = ""
        for i in range(len(flt_mesh)):
            try:
                # print(flt_mesh[i])
                flt_co.append(int(flt_mesh[i]))
                # print(flt_co)
                whe = 'concept_id'
                val = flt_mesh[i]
            except:
                whe = 'mesh'
                val = "'" + flt_mesh[i] + "'"
            if i > 0:
                sql_query += ", "
            else:
                sql_query += "select distinct article_id from meshes_connect inner join (select id as mh_id from mesh where " + whe + " in ("
            sql_query += (val)
        if sql_query != "":
            sql_query += ")) as mh on mh.mh_id=meshes_connect.mesh_id"
            Pointer.execute(sql_query)
            res_mh = Pointer.fetchall()
            for j in res_mh:
                sign[j[0]] += 1 
                
        i = 0   
        sql_query = ""
        for i in range(len(flt_dm)):
            if i > 0:
                sql_query += ", "
            else:
                sql_query += "select distinct article_id from meshes_connect inner join (select id as mh_id from mesh where domain in ("
            sql_query += ("'" + flt_dm[i] + "'")
        if sql_query != "":
            sql_query += ")) as mh on mh.mh_id=meshes_connect.mesh_id"
            Pointer.execute(sql_query)
            res_dm = Pointer.fetchall()
            for j in res_dm:
                sign[j[0]] += 1 
                
        
        # i = 0
        # sql_query = ""
        # for i in range(len(flt_co)):
        #     if i > 0:
        #         sql_query += ", "
        #     else:
        #         sql_query += "select article_id from meshes_connect inner join (select id as mh_id from mesh where concept_id in ("
        #     sql_query += (str(flt_co[i]))
        # if sql_query != "":
        #     sql_query += ")) as mh on mh.mh_id=meshes_connect.mesh_id"
        #     Pointer.execute(sql_query)
        #     res_co = Pointer.fetchall()
        #     for j in res_co:
        #         sign[j[0]] += 1
        
        i = 0
        sql_query = ""
        for i in range(len(flt_sd)):
            if i > 0:
                sql_query += ", "
            else:
                sql_query += "select distinct article_id from study_design_connect inner join (select id as sd_id from study_design where study_design in ("
            sql_query += ("'" + flt_sd[i] + "'")
        if sql_query != "":
            sql_query += ")) as sd on sd.sd_id=study_design_connect.study_design_id;"
            Pointer.execute(sql_query)
            res_sd = Pointer.fetchall()
            for j in res_sd:
                # if sign[j[0]] == 1:
                    sign[j[0]] += 1
                # else:
                #     sign[j[0]] = 0
        i = 0
        sql_query = ""
        for i in range(len(flt_dt)):
            if i > 0:
                sql_query += ", "
            else:
                sql_query += "select distinct article_id from data_type_connect inner join (select id as dt_id from data_type where data_type in ("
            sql_query += ("'" + flt_dt[i] + "'")
        if sql_query != "":
            sql_query += ")) as dt on dt.dt_id=data_type_connect.data_type_id"
            Pointer.execute(sql_query)
            res_dt = Pointer.fetchall()
            for j in res_dt:
            #     if sign[j[0]] == 2:
                    sign[j[0]] += 1
                # else:
                #     sign[j[0]] = 0
                
        i = 0
        sql_query = ""
        for i in range(len(flt_date)):
            if i > 0:
                sql_query += ", "
            else:
                sql_query += "select distinct id from articles where date_pub in ("
            sql_query += ("'" + flt_date[i] + "'")
        if sql_query != "":
            sql_query += ")"
            Pointer.execute(sql_query)
            res_date = Pointer.fetchall()
            for j in res_date:
                sign[j[0]] += 1

        i = 0
        sql_query = ""
        for i in range(len(flt_geo)):
            if i > 0:
                sql_query += ", "
            else:
                sql_query += "select distinct article_id from geography_connect inner join (select id as dt_id from geography where country in ("
            sql_query += ("'" + flt_geo[i] + "'")
        if sql_query != "":
            sql_query += ")) as dt on dt.dt_id=geography_connect.region_id"
            Pointer.execute(sql_query)
            res_geo = Pointer.fetchall()
            for j in res_geo:
                #     if sign[j[0]] == 2:
                sign[j[0]] += 1
                # else:
                #     sign[j[0]] = 0
        
        i = 0
        sql_query = ""
        for i in range(len(flt_vb)):
            if i > 0:
                sql_query += ", "
            else:
                sql_query += "select distinct article_id from vocabs_connect inner join (select id as dt_id from vocabularies where omop_vocab in ("
            sql_query += ("'" + flt_vb[i] + "'")
        if sql_query != "":
            sql_query += ")) as dt on dt.dt_id=vocabs_connect.vocab_id"
            Pointer.execute(sql_query)
            res_vb = Pointer.fetchall()
            for j in res_vb:
                #     if sign[j[0]] == 2:
                sign[j[0]] += 1
                # else:
                #     sign[j[0]] = 0
        
        i = 0
        sql_query = ""
        for i in range(len(flt_jo)):
            if i > 0:
                sql_query += ", "
            else:
                sql_query += "select distinct id from articles inner join (select id as dt_id from journals where journal in ("
            sql_query += ("'" + flt_jo[i] + "'")
        if sql_query != "":
            sql_query += ")) as dt on dt.dt_id=articles.journal_id"
            Pointer.execute(sql_query)
            # print(sql_query)
            res_jo = Pointer.fetchall()
            for j in res_jo:
                #     if sign[j[0]] == 2:
                sign[j[0]] += 1
                # else:
                #     sign[j[0]] = 0

        if max(sign):
            results = []
            res_id = ", ".join([str(i) for i in np.where(sign == max(sign))[0]])
            print('max(sign):', max(sign))
            # print(np.where(sign == max(sign))[0])
            try:
                sort = flt_so[0].split(' ')
                if sort[0] == 'date_pub':
                    sql_query = "select journal, articles.id from articles inner join journals on articles.journal_id = journals.id where articles.id in (" + res_id + ") ORDER BY " + sort
                else:
                    sql_query = "select journal, a_id from journals inner join (select id as a_id, journal_id from articles where id in (" + \
                            res_id + ")) as jo on jo.journal_id=journals.id order by ranking " + sort[1]
            except:
                sql_query = "select journal, a_id from journals inner join (select id as a_id, journal_id from articles where id in (" + \
                            res_id + ")) as jo on jo.journal_id=journals.id order by ranking asc"
            Pointer.execute(sql_query)
            res_journal_a_id = Pointer.fetchall()
            # print(res_journal_a_id)
            for j in res_journal_a_id:
                # print(j)
                res_journal = j[0]
                
                sql_query = "select pm_link from articles where id in (" + str(j[1]) + ")"
                Pointer.execute(sql_query)
                res_pm_link = Pointer.fetchall()[0][0]
                
                sql_query = "select title from articles where id in (" + str(j[1]) + ")"
                Pointer.execute(sql_query)
                res_title = Pointer.fetchall()[0][0]
                
                sql_query = "select date_pub from articles where id in (" + str(j[1]) + ")"
                Pointer.execute(sql_query)
                res_date_pub = Pointer.fetchall()[0][0]
                
                sql_query = "select abstract from articles where id in (" + str(j[1]) + ")"
                Pointer.execute(sql_query)
                res_abstract = Pointer.fetchall()[0][0]
                
                sql_query = "select study_design from (select * from study_design_connect where article_id in (" + \
                    str(j[1]) + ")) as sd_id inner join study_design on sd_id.study_design_id=study_design.id"
                Pointer.execute(sql_query)
                res_study_design = Pointer.fetchall()[0][0]
                
                sql_query = "select data_type from (select * from data_type_connect where article_id in (" + \
                    str(j[1]) + ")) as dt_id inner join data_type on dt_id.data_type_id=data_type.id"
                Pointer.execute(sql_query)
                try:
                    res_data_type = Pointer.fetchall()[0][0]
                except:
                    # print(sql_query)
                    # print(Pointer.fetchall())
                    res_data_type = ''
                
                sql_query = "select distinct mesh, concept_id, domain from mesh inner join (select * from meshes_connect where article_id in (" + \
                    str(j[1]) + ")) as mh on mh.mesh_id=mesh.id"
                Pointer.execute(sql_query)
                res_mesh_m_c_d = Pointer.fetchall()
                # print(res_mesh_m_c_d)
                res_mesh = []
                res_concept_id = []
                res_Condition = []
                res_Drug = []
                res_Procedure = []
                res_Measurement = []
                for k in res_mesh_m_c_d:
                    # print(k)
                    res_mesh.append(k[0])
                    res_concept_id.append(k[1])
                    if k[2] == "Condition":
                        res_Condition.append({
                            'mesh': k[0],
                            'concept_id': k[1]
                        })
                    else:
                        if k[2] == "Drug":
                            res_Drug.append({
                                'mesh': k[0],
                                'concept_id': k[1]
                            })
                        else:
                            if k[2] == "Procedure":
                                res_Procedure.append({
                                    'mesh': k[0],
                                    'concept_id': k[1]
                                })
                            else:
                                if k[2] == "Measurement":
                                    res_Measurement.append({
                                        'mesh': k[0],
                                        'concept_id': k[1]
                                    })
                                    
                    # instr = eval("res_{0}".format(k[2]))
                    # print(instr)
                    # instr.append(k[0])

                # print("condition: ", res_Condition)
                # print("drug: ", res_Drug)
                # print("procedure: ", res_Procedure)
                # print("measurement: ", res_Measurement)
                # print("mesh: ", res_mesh)
                results.append({
                    'pm_link': res_pm_link,
                    'title': res_title,
                    'date_pub': res_date_pub,
                    'abstract': res_abstract,
                    'study_design': res_study_design,
                    'data_type': res_data_type,
                    'mesh': res_mesh,
                    'concept_id': res_concept_id,
                    'condition': res_Condition,
                    'drug': res_Drug,
                    'procedure': res_Procedure,
                    'measurement': res_Measurement,
                    'journal': res_journal
                })
            for k in flt_mesh:
                try:
                    ss = int(k)
                    flt_mesh.remove(k)
                except:
                    ss = ''
            results.append({
                'flt_mesh': flt_mesh,
                'flt_co': flt_co,
                'articles_id': res_id    
            })
        else:
            results = []   
            
        response = jsonify(results)
        return response
    if request.method == "GET":
        results = {'processed': 'GET is not supported'}
        return jsonify(results)
        


if __name__ == "__main__":
    app.run(debug=True)