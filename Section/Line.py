from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT)
    glLineWidth(6)                     
    glBegin(GL_LINES)
    # First line 
    glColor3f(1.0, 0.0, 0.0)
    glVertex2i(-10, -2)
    glVertex2i(10, 10)
    # Second line 
    glColor3f(0.0, 0.0, 1.0)
    glVertex2i(10, -14)
    glVertex2i(-10, -5)
    glEnd()
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_RGB)
glutInitWindowSize(600, 400)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"Graphics OpenGL Labs")   
glutDisplayFunc(plotpoints)
gluOrtho2D(-15.0, 15.0, -15.0, 15.0)
glutMainLoop()