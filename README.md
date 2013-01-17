site-compiler
=============

A (very) simple solution to creating an html static site from markdown.
Generates html from markdown and an index which links to the generated files.

No other site-builder I looked at allowed for automatic indexing, so I wrote this simple solution.
Initially, this project was created because I needed a way to keep track and access of all my markdown notes 
without having to manually build to html.

usage
======
site-compiler accepts a single directory as an argument from the command line.
This directory can be either a relative or absolute path (it's all converted to an abspath in the backend)


You can run site-compiler.py as a unix-script, i.e.
> ./path/to/site-compiler.py ~/Documents/Notes/Example

or as a python program
> python3 /path/to/site-compiler ~/Documents/Notes/Example

watch-dir
=========
watch-dir is a bash script written using inotify-tools that calls site-compiler every time a change is made to a file
in a given directory. 

EX:
> ./watch-dir ~/Documents/Notes/COMP410 

will watch the directory '~/Documents/Notes/COMP410'
