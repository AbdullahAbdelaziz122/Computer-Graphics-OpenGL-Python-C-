from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import * 


def plotpoint():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(20)
    glBegin(GL_POINTS)
    glColor3f(1.0, 0.0, 0.5)
    glVertex(0, 0)
    glEnd()
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_RGB)

glutInitWindowSize(600, 400)
glutInitWindowPosition(0, 0)

glutCreateWindow(b"Graphics OpenGLLabs")
glutDisplayFunc(plotpoint)          

gluOrtho2D(-15.0, 15.0, -15.0, 15.0)
glutMainLoop()                      