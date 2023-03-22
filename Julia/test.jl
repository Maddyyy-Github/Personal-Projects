# include("MathsCustom/expr2func.jl")



# my_function = expr2func(:(a*x + b), :(a, b, x))

# a = 10
# b = 100
# for i in 1:10
#     x = i
#     println(my_function(a, b, x))
# end

include("MathsCustom/summation.jl")

# @time Σ(1, 100_000, :(i*i))
#   0.022506 seconds (308.36 k allocations: 5.071 MiB, 13.06% compilation time)
# 333338333350000