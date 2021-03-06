import scriptcontext
import utility as rhutil
import Rhino


def __getlinetype(name_or_id):
    id = rhutil.coerceguid(name_or_id)
    if id: name_or_id = id
    linetype = scriptcontext.doc.Linetypes.Find(name_or_id, True)
    if linetype>=0: return scriptcontext.doc.Linetypes[linetype]


def IsLinetype(name_or_id):
    """
    ### IsLinetype

    Verifies the existence of a linetype in the document.  

    ***Syntax***
    ```python
    rhinoscriptsyntax.IsLinetype (name_or_id)
    rhinoscript.linetype.IsLinetype (name_or_id)
    ```

    ***Parameters***
    *name_or_id* Required.  String or Guid.  The name or identifier of an existing linetype.  

    ***Returns***
    Boolean True or False indicating success or failure.

    ***Example***
    ```python
    import rhinoscriptsyntax as rs
    name = rs.GetString("Linetype name")
    if rs.IsLinetype(name): print "The linetype exists."
    else: print "The linetype does not exist"
    ```

    ***Also See***
      - IsLinetypeReference
    """
    lt = __getlinetype(name_or_id)
    return lt is not None


def IsLinetypeReference(name_or_id):
    """Verifies that an existing linetype is from a reference file
    Returns: True or False
    """
    lt = __getlinetype(name_or_id)
    if lt is None: raise ValueError("unable to coerce %s into linetype"%name_or_id)
    return lt.IsReference


def LinetypeCount():
    "Returns number of linetypes in the document"
    return scriptcontext.doc.Linetypes.Count


def LinetypeNames(sort=False):
    """Returns names of all linetypes in the document
    Parameters:
      sort[opt] = return a sorted list of the linetype names
    Returns
      list of strings if successful
    """
    count = scriptcontext.doc.Linetypes.Count
    rc = []
    for i in xrange(count):
        linetype = scriptcontext.doc.Linetypes[i]
        if not linetype.IsDeleted: rc.append(linetype.Name)
    if sort: rc.sort()
    return rc
