'''
Offscreen rendering using GLUT hidden window
Standalone code - not using LibGL from this repository
'''

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.osmesa import *

from PIL import Image
from PIL import ImageOps

import os

width, height = 300, 300

def init():
    glClearColor(0.5, 0.5, 0.5, 1.0)
    glColor(0.0, 1.0, 0.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
    glViewport(0, 0, width, height)

def render():

    glClear(GL_COLOR_BUFFER_BIT)

    # draw xy axis with arrows
    glBegin(GL_LINES)

    # x
    glVertex2d(-1, 0)
    glVertex2d(1, 0)
    glVertex2d(1, 0)
    glVertex2d(0.95, 0.05)
    glVertex2d(1, 0)
    glVertex2d(0.95, -0.05)

    # y
    glVertex2d(0, -1)
    glVertex2d(0, 1)
    glVertex2d(0, 1)
    glVertex2d(0.05, 0.95)
    glVertex2d(0, 1)
    glVertex2d(-0.05, 0.95)

    glEnd()

    glFlush()


def draw():
    render()
    glutSwapBuffers()

def main():


    if not os.environ.get('PYOPENGL_PLATFORM') == 'osmesa':
        print 'Use with: PYOPENGL_PLATFORM=osmesa'
        return 0



    ctx = OSMesaCreateContext(OSMESA_RGBA, None)
    #ctx = OSMesaCreateContextExt(OSMESA_RGBA, 32, 0, 0, None)

    buf = arrays.GLubyteArray.zeros((height, width, 4))
    assert(OSMesaMakeCurrent(ctx, buf, GL_UNSIGNED_BYTE, width, height))
    assert(OSMesaGetCurrentContext())


    z = glGetIntegerv(GL_DEPTH_BITS)
    s = glGetIntegerv(GL_STENCIL_BITS)
    a = glGetIntegerv(GL_ACCUM_RED_BITS)
    print "Depth=%d Stencil=%d Accum=%d" % (z, s, a)

    print "Width=%d Height=%d" % (OSMesaGetIntegerv(OSMESA_WIDTH), OSMesaGetIntegerv(OSMESA_HEIGHT))
    #OSMesaPixelStore(OSMESA_Y_UP, 0)

    print "Rendering..."
    init()
    render()

    print "Saving osmesa.png..."

    glPixelStorei(GL_PACK_ALIGNMENT, 1)
    data = glReadPixels(0, 0, width, height, GL_RGBA, GL_UNSIGNED_BYTE)
    image = Image.frombytes("RGBA", (width, height), data)
    image = ImageOps.flip(image) # in my case image is flipped top-bottom for some reason
    image.save('osmesa.png', 'PNG')


    OSMesaDestroyContext(ctx)

    print "Done!"

main()