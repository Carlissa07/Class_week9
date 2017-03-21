#-------------------------------------------------------------------------------
# Name: SQL function       module1
# Purpose:
#
# Author:      cacole
#
# Created:     07/02/2017
# Copyright:   (c) cacole 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

##def formatSQLIN(dataList, sqlTemplate):
##    'a function to generate a SQL statement'
##    sql = sqlTemplate #"OBJECTID IN "
##    step = "("
##    for data in dataList:
##        step += str(data)
##    sql += step + ")"
##    return sql
##
##def formatSQL(dataList, sqlTemplate):
##    'a function to generate a SQL statement'
##    sql = ''
##    for count, data in enumerate(dataList):
##        if count != len(dataList) -1:
##            sql += sqlTemplate.format(data) + ' OR '
##        else:
##            sql += sqlTemplate.format(data)
##    return sql
##
##dataVals = [1,2,3,4]
##sqlOID = "OBJECTID = {0}"
##sql = formatSQL(dataVals, sqlOID)
##print sql
##
##
##
##def formatSQL2(dataList, sqlTemplate, operator=" OR "):
##    'a function to generate a SQL statement'
##    sql = ''
##    for count, data in enumerate(dataList):
##        if count != len(dataList) -1:
##            sql += sqlTemplate.format(data) +operator
##        else:
##            sql += sqlTemplate.format(data)
##    return sql
##
##sql = formatSQL2(dataVals, sqlOID, " AND ")
##print sql
##
##
##
##sqlTemplate = "NAME = '{0}'"
##lineNames = ['71 IB', '71 OB']
##sql = formatSQL2(lineNames, sqlTemplate)
##print sql



def formatSQLMultiple(dataList, sqlTemplate, operator=' OR '):
    'a function to generate a SQL statement'
    sql = ''
    for count, data in enumerate(dataList):
        if count != len(dataList)-1:
            sql += sqlTemplate.format(*data) + operator
        else:
            sql += sqlTemplate.format(*data)
    return sql

sqlTemplate = "(NAME = '{0}' AND BUS_SIGNAG = '{1}')"
lineNames = [('71 IB', 'Ferry Plaza'),('71 OB', '48th Avenue')]
sql = formatSQLMultiple(lineNames, sqlTemplate)
print sql


##arcpy.Select_analysis(Bus_Stops, Inbound71, sql)

