using REPL.Terminals
"""
    clear_line()

Clears the current line in Julia REPL

# Examples
```jldoctest
julia> begin
        println("The Following line is going to be cleared")
        print("Hello World")
        clear_line()
        print("The Line has been replaced by this text")
       end
The Following line is going to be cleared
The Line has been replaced by this text
```
"""
function clear_line()
    terminal = Terminals.TTYTerminal("", stdin, stdout, stderr)
    Terminals.clear_line(terminal)
end

