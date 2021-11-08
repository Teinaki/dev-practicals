from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///practical22.db',
    future=True)

Base = declarative_base()
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    grad_year = Column(String)
    programme_id = Column(ForeignKey('programs.id'))
    programme = relationship('Programme', back_populates='student') 

class Programme(Base):
    __tablename__ = 'programs'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    student = relationship('Student', back_populates='programme')



      
# we can create the table in the database
Base.metadata.create_all(engine)


guy = Student(name='Guy', email='guy@gmail.com', grad_year='2022')
bob = Student(name='Bob', email='bob@gmail.com', grad_year='2024')
dave = Student(name='Dave', email='dave@gmail.com', grad_year='2021')
doober = Student(name='Doober', email='doober@gmail.com', grad_year='2022')
cup = Student(name='Cup', email='cup@gmail.com', grad_year='2022')

programming = Programme(name = 'Programming')

# to work with the ORM features we need a Session
session = Session(engine)
session.add(guy)
session.add(bob)
session.add(dave)
session.add(doober)
session.add(cup)
session.add(programming)
      
# a commit() is necessary to finally save the cats
session.commit()

query = select(Student).where(Student.name == 'Guy')
student = session.execute(query).scalars().first()
print(student.name)

query1 = select(Programme).where(Programme.name == 'Programming')
programme = session.execute(query1).scalars().first()

query2 = select(Student)
students = session.execute(query2).scalars()
for student in students:
    student.programme = programme
session.commit()

query = select(Student).where(Student.name == 'Guy')
student = session.execute(query).scalars().first()
print(student.name)
print(student.programme_id)

#4. Write code for a second  mapped class, `Programme` with a primary 
#key, name (e.g., BIT), and a many-to-one relationship with `Student`s.
#Add the `ForeignKey` field to the `Student` table. Create the table and
#add a sample record to the programme table.

#5. Write a query that return your `Programme` record. Add your five 
#student to the programme and save it. Then use query to get one 
#`Student` and show that it is now linked to the programme.

