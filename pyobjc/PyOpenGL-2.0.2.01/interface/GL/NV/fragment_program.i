/*
# AUTOGENERATED DO NOT EDIT

# If you edit this file, delete the AUTOGENERATED line to prevent re-generation
# BUILD api_versions [0x001]
*/

%module fragment_program

#define __version__ "$Revision: 1.1.2.1 $"
#define __date__ "$Date: 2004/11/15 07:38:07 $"
#define __api_version__ API_VERSION
#define __author__ "PyOpenGL Developers <pyopengl-devel@lists.sourceforge.net>"
#define __doc__ ""

%{
/**
 *
 * GL.NV.fragment_program Module for PyOpenGL
 * 
 * Authors: PyOpenGL Developers <pyopengl-devel@lists.sourceforge.net>
 * 
***/
%}

%include util.inc
%include gl_exception_handler.inc

%{
#ifdef CGL_PLATFORM
# include <OpenGL/glext.h>
#else
# include <GL/glext.h>
#endif

#if !EXT_DEFINES_PROTO || !defined(GL_NV_fragment_program)
DECLARE_VOID_EXT(glProgramNamedParameter4fNV, (GLuint id, GLsizei len, const GLubyte *name, GLfloat x, GLfloat y, GLfloat z, GLfloat w), (id, len, name, x, y, z, w))
DECLARE_VOID_EXT(glProgramNamedParameter4dNV, (GLuint id, GLsizei len, const GLubyte *name, GLdouble x, GLdouble y, GLdouble z, GLdouble w), (id, len, name, x, y, z, w))
DECLARE_VOID_EXT(glProgramNamedParameter4fvNV, (GLuint id, GLsizei len, const GLubyte *name, const GLfloat *v), (id, len, name, v))
DECLARE_VOID_EXT(glProgramNamedParameter4dvNV, (GLuint id, GLsizei len, const GLubyte *name, const GLdouble *v), (id, len, name, v))
DECLARE_VOID_EXT(glGetProgramNamedParameterfvNV, (GLuint id, GLsizei len, const GLubyte *name, GLfloat *params), (id, len, name, params))
DECLARE_VOID_EXT(glGetProgramNamedParameterdvNV, (GLuint id, GLsizei len, const GLubyte *name, GLdouble *params), (id, len, name, params))
#endif
%}

/* FUNCTION DECLARATIONS */
void glProgramNamedParameter4fNV(GLuint id, GLsizei len, const GLubyte *name, GLfloat x, GLfloat y, GLfloat z, GLfloat w);
DOC(glProgramNamedParameter4fNV, "glProgramNamedParameter4fNV(id, len, name, x, y, z, w)")
void glProgramNamedParameter4dNV(GLuint id, GLsizei len, const GLubyte *name, GLdouble x, GLdouble y, GLdouble z, GLdouble w);
DOC(glProgramNamedParameter4dNV, "glProgramNamedParameter4dNV(id, len, name, x, y, z, w)")
void glProgramNamedParameter4fvNV(GLuint id, GLsizei len, const GLubyte *name, const GLfloat *v);
DOC(glProgramNamedParameter4fvNV, "glProgramNamedParameter4fvNV(id, len, name, v)")
void glProgramNamedParameter4dvNV(GLuint id, GLsizei len, const GLubyte *name, const GLdouble *v);
DOC(glProgramNamedParameter4dvNV, "glProgramNamedParameter4dvNV(id, len, name, v)")
void glGetProgramNamedParameterfvNV(GLuint id, GLsizei len, const GLubyte *name, GLfloat *params);
DOC(glGetProgramNamedParameterfvNV, "glGetProgramNamedParameterfvNV(id, len, name, params)")
void glGetProgramNamedParameterdvNV(GLuint id, GLsizei len, const GLubyte *name, GLdouble *params);
DOC(glGetProgramNamedParameterdvNV, "glGetProgramNamedParameterdvNV(id, len, name, params)")

/* CONSTANT DECLARATIONS */
#define GL_MAX_FRAGMENT_PROGRAM_LOCAL_PARAMETERS_NV 0x8868
#define         GL_FRAGMENT_PROGRAM_NV 0x8870
#define       GL_MAX_TEXTURE_COORDS_NV 0x8871
#define  GL_MAX_TEXTURE_IMAGE_UNITS_NV 0x8872
#define GL_FRAGMENT_PROGRAM_BINDING_NV 0x8873
#define     GL_PROGRAM_ERROR_STRING_NV 0x8874


%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_NV_fragment_program)
"glProgramNamedParameter4fNV",
"glProgramNamedParameter4dNV",
"glProgramNamedParameter4fvNV",
"glProgramNamedParameter4dvNV",
"glGetProgramNamedParameterfvNV",
"glGetProgramNamedParameterdvNV",
#endif
	NULL
};

#define glInitFragmentProgramNV() InitExtension("GL_NV_fragment_program", proc_names)
%}

int glInitFragmentProgramNV();
DOC(glInitFragmentProgramNV, "glInitFragmentProgramNV() -> bool")

%{
PyObject *__info()
{
	if (glInitFragmentProgramNV())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();
