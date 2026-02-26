from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

"""
Question 5: Draw a Triangle Using Minimal Lines 
once by normal line, once by Strip Lines and once by 
Loop Lines using gradient colors.
"""


def draw_normal():
    glClear(GL_COLOR_BUFFER_BIT)
    glLineWidth(5)
    glBegin(GL_LINES)
    
    # First-Line 
    glColor(1.0, 0.0, 0.0)
    glVertex2i(0,5)
    glVertex2i(-5,-5)
    
    # Second-Line
    glColor(0.0, 1.0, 0.0)
    glVertex2i(0,5)
    glVertex2i(5,-5)
    
    # Third-Line
    glColor(0.0, 0.0, 1.0)
    glVertex2i(-5,-5)
    glVertex2i(5,-5)
    
    glEnd()
    glFlush()
    

def draw_strip():
    glClear(GL_COLOR_BUFFER_BIT)
    glLineWidth(5)
    glBegin(GL_LINE_LOOP)

    glColor(1.0, 1.0, 1.0)
    glVertex2i(0, 5)
    glVertex2i(-5, 0)
    glVertex2i(5, 0)
    
    
    glEnd()
    glFlush()
    
    
    


glutInit()
glutInitWindowSize(600, 400)
glutCreateWindow(b"Q5 - Triangle")
glutDisplayFunc(draw_strip)   
gluOrtho2D(-10, 10, -10, 10)
glutMainLoop()