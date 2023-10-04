import os , sys
from os.path import join, dirname, abspath

sys.path.insert(0, abspath(join(dirname(__file__), '..')))


from Course import course_details

def payment():
    print("This is my payment details")

course_details.course()