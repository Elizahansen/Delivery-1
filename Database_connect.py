
############################## Import #####################
from inspect import ClassFoundException
import mysql.connector

###################### MySQL connection ####################
def dbconnect():
        conn = mysql.connector.connect(host='emh-mysql-server.mysql.database.azure.com',
                                       user='emh',
                                       password='Elizamhansen10.',
                                       database='Delivery1')
        return conn