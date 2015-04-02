### LinetypeNames

Returns the names of all linetypes in the document.  

***Syntax***
```python
rhinoscriptsyntax.LinetypeNames(sort=False)
```

***Parameters***
*sort* Optional.  Boolean.  Return a sorted list of linetype names. The default is not to return a sorted list (False).  

***Returns***
*List* A list of linetype names if successful.  
*None* If not successful, or on error.  

***Example***
```python
import rhinoscriptsyntax as rs
names = rs.LinetypeNames()
if names:
    for name in names: print name
```

***Also See***
  - [LinetypeCount](./LinetypeCount.html)  

[view code on github](https://github.com/acormier/rhinopythondocs/blob/233504a3f4ddb4233db057d15459948256e6631c/linetype/linetype.py#L35-L48)  
