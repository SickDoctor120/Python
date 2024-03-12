import pandas as pd
import mysql.connector
from mysql.connector import Error
import datetime

# MySQL数据库连接配置
db_config = {
    'host': '**.**.**.**',
    'port': 3306,
    'database': 'test',
    'user': 'root',
    'password': 'password'
}

# 查询条件日期
query_date = '2023-06-30'

try:
    # 建立数据库连接
    connection = mysql.connector.connect(**db_config)

    if connection.is_connected():
        cursor = connection.cursor()

        # 执行查询，使用LIKE进行模糊匹配
        query = f"SELECT * FROM clients WHERE update_time LIKE '%{query_date}%'"
        cursor.execute(query)

        # 获取查询结果
        result = cursor.fetchall()

        if result:
            # 将查询结果转换为DataFrame
            df = pd.DataFrame(result, columns=[i[0] for i in cursor.description])

            # 获取当前日期作为文件名后缀
            current_date = datetime.datetime.now().strftime("%Y%m%d%H")

            # 生成Excel文件
            excel_file_name = f"Mysql-scan_{current_date}.xlsx"
            excel_path = f"d:\\Users\\******\\桌面\\{excel_file_name}"

            # 保存DataFrame为Excel文件
            df.to_excel(excel_path, index=False)

            print(f"查询结果已保存至 {excel_path}")
        else:
            print("未找到匹配的记录")

except Error as e:
    print(f"数据库连接错误: {e}")
finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
