### IsLinetypeReference

Verifies that an existing linetype is from a reference file.  

***Syntax***
```python
rhinoscriptsyntax.IsLinetypeReference (name_or_id)
rhinoscript.linetype.IsLinetypeReference (name_or_id)
```

***Parameters***
*name_or_id* Required.  String or Guid.  The name or identifier of an existing linetype.  

***Returns***
*Boolean* True or False indicating success or failure.  
*None* On error.  

***Example***
```python
import rhinoscriptsyntax as rs
name = rs.GetString("Linetype name")
if rs.IsLinetype(name):
    if rs.IsLinetypeReference(name):
        print "The linetype is a reference linetype."
    else:
        print "The linetype is not a reference linetype."
else:
    print "The linetype does not exist."
```

***Also See***
  - [IsLinetype](./IsLinetype.md)  

[view code on github](https://github.com/acormier/rhinopythondocs/blob/233504a3f4ddb4233db057d15459948256e6631c/linetype/linetype.py#L21-L27)  
