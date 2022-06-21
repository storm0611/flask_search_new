from os import sync
from selectors import SelectSelector
from turtle import tilt
from unittest import result
from wsgiref import headers
import requests
import pandas
from flask import Flask, request, Response
import pymysql
from pymysql import NULL, Error
from datetime import datetime
import re
import json


# SERVER_URL = 'http://localhost:5000' # same this for this one it's API_SERVER URL
SERVER_URL = 'http://tandem7.pythonanywhere.com'
endpoint = '/add'

# It is the function to read your csv data returnd by scraping script that you have.
def read_csv_data():
    
    #first let me show you how much already added data in database. 4195 already present data.
    # can you please show me this .csv file or put this csv file in same path of sccript?
    # yeah let me search for it..
    # you can also set it's path to csv file
    data = pandas.read_csv('final_df_sample_noindex_with_domain1.csv', sep=',')
    return data # and here it's returning all the readed data from csv file , I am using pandas for reading file

def upload_data():
        csv_data = read_csv_data()

        for i in range(len(csv_data)):
    
            data = {}    
        
            data['journal'] = re.split("\'|\"", csv_data['journal'][i])[1]
            data['pm_id'] = str(csv_data['pmid'][i])
            data['pm_link'] = csv_data['pm_link'][i]
            data['date_pub'] = re.split("\'|\"", csv_data['date_pub'][i])[1]
            data['abstract'] = re.split("\'|\"", csv_data['abstract'][i])[1]
            data['title'] = re.split("\'|\"", csv_data['title'][i])[1]
            data['study_design'] = csv_data['study_design'][i]
            data['data_type'] = csv_data['data_type'][i]
            data['mesh'] = csv_data['mesh'][i]
            data['concept_id'] = str(csv_data['concept_id_1'][i])
            data['domain'] = csv_data['domain_id'][i]
            data['category_name'] = csv_data['category_name'][i]
            # and here sending data to server and getting response.
            res = await requests.post(SERVER_URL + endpoint, json={
                'journal': re.split("\'|\"", csv_data['journal'][i])[1],
                'pm_id': str(csv_data['pmid'][i]),
                'pm_link': csv_data['pm_link'][i],
                'date_pub': re.split("\'|\"", csv_data['date_pub'][i])[1],
                'abstract': re.split("\'|\"", csv_data['abstract'][i])[1],
                'title': re.split("\'|\"", csv_data['title'][i])[1],
                'study_design': csv_data['study_design'][i],
                'data_type': csv_data['data_type'][i],
                'mesh': csv_data['mesh'][i],
                'concept_id': str(csv_data['concept_id_1'][i]),
                'domain': csv_data['domain_id'][i],
                'category_name': csv_data['category_name'][i]
            })
            if (res.status_code == 200):
                print(res.text + ": "+str(i) + " out of {}".format(len(csv_data['title'])))
            else:
                print(res.text)
            
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


        #Sure so now let me show you how you can add more columns in easy way but one more thing when you will add more columns you need to add columns in server script too.
        # ok, just show me please)
        # ok


if __name__ == "__main__":
    upload_data()