Python 3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:38:22) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def print_lyrics():
	print"Im a lumber jack and Im okay"
	
SyntaxError: invalid syntax
>>> def print_lyrics():
	print"Im a lumber jack and Im okay".....
	
SyntaxError: invalid syntax
>>>  def print_lyrics():
	 
SyntaxError: unexpected indent
>>> def print_lyrics():
	...print"Im a lumberjack and im okay"
	
SyntaxError: invalid syntax
>>> print (print_lyrics)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print (print_lyrics)
NameError: name 'print_lyrics' is not defined
>>> print_lyrics()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print_lyrics()
NameError: name 'print_lyrics' is not defined
>>> def print_lyrics():
	print "Im okay."
	
SyntaxError: invalid syntax
>>> def print_lyrics():
	print "Im okay."
	
SyntaxError: invalid syntax
>>> def print_lyrics():
	    print"im a lumberjack and im okay"
	    
SyntaxError: invalid syntax
>>> def print_lyrics():
	print("im a lumberjack and im okay")
	print("i sleep all night and i work all day")

	
>>> print (print_lyrics)
<function print_lyrics at 0x02DABDB0>
>>> type(print_lyrics)
<class 'function'>
>>> 
