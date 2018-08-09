# coanlib
A library for python code analysis.

### Overview
Coanlib gives the user tools to list all the functions and function calls of a
source code file. Coanlib also finds all comment-lines and trailing comments
from source code file. It can be used to find unused functions, temporary
comments, code statistics etc.

### Usage
Example:
```
import coanlib
coanlib.code_statistics("coanlib.py")
```