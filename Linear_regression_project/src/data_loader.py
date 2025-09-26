from sqlalchemy import create_engine
conn_str= 'postgresql://neondb_owner:npg_Xd3WsCbL8wiE@ep-lucky-wildflower-adgmjudg-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'
engine = create_engine(conn_str)
print("Connection to NeonDB successful!")