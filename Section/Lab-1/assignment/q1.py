from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

"""
Question 1: Draw 5 points at different coordinates on 
the screen. Each point should have a different color.
"""

def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(15)
    glBegin(GL_POINTS)
    # Point 1
    glColor3f(1, 0, 0)
    glVertex2f(-5, 5)
    # Point 2 
    glColor3f(0, 1, 0)
    glVertex2f(5, 5)
    # Point 3 
    glColor3f(0, 0, 1)
    glVertex2f(-5, -5)
    # Point 4 
    glColor3f(1, 1, 0)
    glVertex2f(5, -5)
    # Point 5 
    glColor3f(0, 1, 1)
    glVertex2f(0, 0)
    glEnd()
    glFlush()

glutInit()
glutInitWindowSize(600, 400)
glutCreateWindow(b"Question 1")
glutDisplayFunc(plotpoints)
gluOrtho2D(-10, 10, -10, 10)   
glutMainLoop()