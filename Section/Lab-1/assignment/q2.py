from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

"""
Question 2: Draw 3 separate lines between arbitrary 
vertices. Each line should have a different color.  
"""

def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT)
    glLineWidth(6)

    # first line
    glBegin(GL_LINES)
    # point-1
    glColor3f(1.0, 0.0, 0.0)
    glVertex2i(-10, -2)
    # point-2
    glColor3f(0.0, 1.0, 0.0)
    glVertex2i(10, 10)
    
    # Secound Line
    # point-3
    glColor3f(0.0, 0.0, 1.0)
    glVertex2i(10, -14)
    # point-4
    glColor3f(0.5, 0.5, 0.5)
    glVertex2i(-10, -5)
    
    # Third Line
    # point-5
    glColor3f(0.3, 0.3, 1.0)
    glVertex2i(7, -7)
    # point-6
    glColor3f(0.6, 0.6, 0.0)
    glVertex2i(3, -3)
    glEnd()
    glFlush()
    

glutInit()
glutInitWindowSize(600, 400)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"Question 2")
glutDisplayFunc(plotpoints)
gluOrtho2D(-15.0, 15.0, -15.0, 15.0)
glutMainLoop()
    