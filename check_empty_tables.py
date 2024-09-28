#import the modules
import psycopg2

#database function
def check_empty_table(host,dbname,username,password,port,table_name):
    try:
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(
            host= host
            dbname = dbname
            user = username
            password = password
            port = port
            )
        query= "select coalesce(count(1),0) from "+table_name
        cur = conn.cursor()
        cur.execute(query)
        result=cur.fetchone()
        cur.close()
    return result

# main function
def main(host,dbname,username,password,port,input_file,output_file):
    file1 = open(input_file, 'r')
    Lines = file1.readlines()
    for line in Lines:
        result=check_empty_table(host,dbname,username,password,port,line)
        text = "Table name:"+line+" row count:"+result+"\n"
        with open(output_file,'a') as f:
            f.write(text)
        

if __name__ == "__main__":
    # usage example
    main('localhost','test','user','pass12345',5432,'table.txt','result.txt')

    
            
