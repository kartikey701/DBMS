SUPABASE_URL = "https://lrdsqtytaroudqsxcbxb.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxyZHNxdHl0YXJvdWRxc3hjYnhiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzU2MzYyMzQsImV4cCI6MjA5MTIxMjIzNH0.RCvhQhkiTV64ilBY1aJxtNbe5MpwfJzB9Mi2wlOjjRY"

from supabase import create_client
import streamlit as st

db = create_client('https://lrdsqtytaroudqsxcbxb.supabase.co','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxyZHNxdHl0YXJvdWRxc3hjYnhiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzU2MzYyMzQsImV4cCI6MjA5MTIxMjIzNH0.RCvhQhkiTV64ilBY1aJxtNbe5MpwfJzB9Mi2wlOjjRY')

st.title('P1 - Student Records')

#INSERT run once, then comment out

'''students = [

    {"name":"Ali Hassan", "email":"ali@uni.edu","age":20, "gpa":3.8},

    {"name":"Siti Aishah", "email":"siti@uni.edu", "age":21, "gpa":3.2},

    {"name": "Raj Kumar", "email":"rajäuni.edu", "age":15, "gpa":2.91},

    {"name": "Lin wel","email": "lin@uni.edu", "age":22, "gpa":3.5},
]

db.table('students').insert(students).execute()

ids = {r['name']:r['id'] for r in db.table('students').select('id,name').execute().data}

enrollments = [

    {"student_id":ids["Ali Hassan"], "course": "RDBMS", "grade":"A"},
    {"student_id":ids["Ali Hassan"], "course":"Networks", "grade" : "B"},
    {"student_id":ids["Siti Aishah"], "course": "RDBMS", "grade": "B"}, 
    {"student_id":ids["Raj Kumar"], "course": "RDBMS","grade":"C"},
    {"student_id":ids["Lin wel"], "course": "Networks", "grade":"A"}, 
]

db.table('enrollments').insert(enrollments).execute()'''

#SELECT all

st.subheader('All Students')

st.dataframe (db.table('students').select('*').execute().data)

#WHERE high GPA

st. subheader('GPA >= 3.5')

st.dataframe(db.table('students').select('name,gpa').gte('gpa',3.5).execute().data)


#JOIN via FK

st.subheader('RDBMS Enrollments (JOIN)')

st.dataframe (db.table('enrollments').select('grade, students (name)').eq('course', 'RDBMS').execute().data)

#UPDATE

db.table('students').update({'gpa':3.9}).eq('name', 'Ali Hassan').execute() 
st.write('Ali updated:', db.table('students').select('name,gpa').eq("name", 'Ali Hassan').execute().data)
