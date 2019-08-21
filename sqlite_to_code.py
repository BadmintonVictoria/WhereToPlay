# Reference: https://www.datacamp.com/community/tutorials/sqlite-in-python
import sqlite3
from datetime import datetime

YYYYMMDD = datetime.today().strftime('%Y-%m-%d')

def output_mdb_tables(cursor):
    for table_info in cursor.tables(tableType='TABLE'):
        print(table_info.table_name)
    print("="*100)

def output_query_fields(cursor):
    for field in cursor.description:
        print(field[0])

def get_row_json(row,fields):
    i = 0
    json = ""
    for field in fields:
        if i>0:
            json = json + ", "
        json_field = field[0]
        if row[i] is None:
            json_value = '"null"'
        else:
            json_string = str(row[i])
            json_value = '"{}"'.format(json_string.rstrip())
        json = json + '"{}":{}'.format(json_field,json_value)
        i=i+1
    return "{" + json + "}"

def main():

    # Open a file
    fo = open("json_data.js", "w")
    fo.write("var json_update = '{}';\n\n".format(YYYYMMDD))

    conn = sqlite3.connect('Badminton.sqlite')
    cursor = conn.cursor()

    sql = '''
    select DOW_Order, WTP.* from WhereToPlay WTP
    left join DOW_Order DOW on DOW.DayofWeek=WTP.DayofWeek
    order by DOW_Order, GroupDescription
    '''


    cursor.execute(sql)
    rows = cursor.fetchall() 
    total_rows = len(rows)-1
    print("[")
    fo.write("var json_data = [\n")
    for index, row in enumerate(rows):
        row_json = get_row_json(row,cursor.description)
        if index==total_rows:
            print(row_json)
            fo.write("{}\n".format(row_json))
        else:
            print("{},".format(row_json))
            fo.write("{},\n".format(row_json))
    print("]")
    fo.write("];\n")

    # Close opend file
    fo.close()

if __name__ == "__main__": main()