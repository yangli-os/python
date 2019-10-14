Python 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from turtle import*
color('red','red')
begin_fill()
for i in range(5):
    fd(200)
    rt(144)
end_fill()
done()
SyntaxError: multiple statements found while compiling a single statement
>>> 
from turtle import*
color('red','red')
begin_fill()
for i in range(5):
    fd(200)
    rt(144)
end_fill()
done()
