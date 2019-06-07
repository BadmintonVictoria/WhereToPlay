import pyodbc

#print(pyodbc.drivers())

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
        json = json + '"{}":"{}"'.format(field[0],row[i])
        i=i+1;
    return "{" + json + "}"

def main():

    # Open a file
    fo = open("list.json", "w")

    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ=E:\OneDrive\Project\WhereToPlay\Badminton.mdb;')
    cursor = conn.cursor()

    sql = '''
    select DayOfWeek, GroupDescription, GeneralArea, Location, PlayerLevel, PlayerAge, Shuttle, TimeRange, Season
    from WhereToPlay
    order by DayOfWeek, GroupDescription
    '''
    cursor.execute(sql)
    rows = cursor.fetchall() 
    total_rows = len(rows)-1
    print("[")
    fo.write("[\n")
    for index, row in enumerate(rows):
        row_json = get_row_json(row,cursor.description)
        if index==total_rows:
            print(row_json)
            fo.write("{}\n".format(row_json))
        else:
            print("{},".format(row_json))
            fo.write("{},\n".format(row_json))
    print("]")
    fo.write("]\n")

    # Close opend file
    fo.close()

if __name__ == "__main__": main()