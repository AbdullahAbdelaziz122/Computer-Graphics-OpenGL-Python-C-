from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import * 

def plotpoint():
    glClear(GL_COLOR_BUFFER_BIT)   
    glPointSize(20)                
    glBegin(GL_POINTS)              
    glVertex2f(0, 0)                
    glEnd()                          
    glFlush()                       

glutInit()
glutCreateWindow(b"Graphics OpenGLLabs")
glutDisplayFunc(plotpoint)          
glutMainLoop()                      