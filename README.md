# diral - The Directory Aliaser
I use aliases a lot when I use command line. alias a='a very long command', and then use `a` to repeat the command as much times as I want. 

This tool saves your aliases by directory. I'll have specific alias for each of my repositories/ directories, and this command will load those aliases for me. 

```


diral.py a go run main.go # This saves go run main.go in the alias a
diral.py -d a # Deletes the alias
diral.py # Lists the aliases specific to that directory
```
