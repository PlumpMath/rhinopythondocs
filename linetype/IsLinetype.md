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
  - [IsLinetypeReference](./IsLinetypeReference.html)  

[view code on github](https://github.com/acormier/rhinopythondocs/blob/233504a3f4ddb4233db057d15459948256e6631c/linetype/linetype.py#L13-L18)  
