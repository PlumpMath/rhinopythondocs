### LinetypeCount

Returns the number of linetypes in the document.  

***Syntax***
```python
rhinoscriptsyntax.LinetypeCount()
rhinoscript.linetype.LinetypCount()
```

***Parameters***
None.  

***Returns***
*Number* The number of linetypes in the document.  

***Example***
```python
import rhinoscriptsyntax as rs
count = rs.LinetypeCount()
print "There are", count, "linetypes."
```

***Also See***
  - [LinetypeNames](./LinetypeNames.html)  

[view code on github](https://github.com/acormier/rhinopythondocs/blob/233504a3f4ddb4233db057d15459948256e6631c/linetype/linetype.py#L30-L32)  
