#### AddAlias

Adds a new command alias to Rhino. Command aliases can be added manually by using Rhino's Options command and modifying the contents of the Aliases tab. See "Options Aliases" in the Rhino help file for more details.  

***Syntax***
```python
rhinoscriptsyntax.AddAlias ( alias, macro )
rhinoscript.application.AddAlias ( alias, macro )
```

***Parameters***
alias Required.  String.  The name of the new command alias. The name cannot match command names or existing aliases.
macro Required.  String.  The macro to run when the alias is executed.

***Returns***
Boolean True or False indicating success or failure.

***Example***
```python
import rhinoscriptsyntax as rs
rs.AddAlias("OriginLine", "!_Line 0,0,0")
```
 
***Also See***
  - AliasCount
  - AliasMacro
  - AliasNames
  - DeleteAlias
  - IsAlias
