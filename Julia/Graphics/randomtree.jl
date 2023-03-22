using GLMakie
using Colors
using Luxor
window_width = 1000
window_height = 1000
mygrey = parse(Colorant, "#20262e")
mywhite = parse(Colorant, "#d8e9e6")

origin = (window_height/2, window_width/2)
xMax = window_width/2
yMax = window_height/2


#Set Tree Parameteres
branch_dispersion = 60 #Angle for each subbranch
subbranch_range = 2:3
branch_shortening = 0.6:0.01:0.75
sunlight = 1/10
minimum_branch_length = 5
    #trunk
trunk_start = origin .- (0, yMax)
trunk_length = yMax/3
trunk_angle = 90






#Functions
function point_at_angle(init_point, length, angle)
    return (init_point .+ ((cospi(angle/180), sinpi(angle/180)) .* length))
end
trunk_end = point_at_angle(trunk_start, trunk_length, trunk_angle)

function draw_line(point1, point2)
    # lines!(canvas, )
    line(Point(point1...), Point(point2...), :stroke)
end

function intfloat(number)
    if modf(number)[2] == number
        try
            return Int(number) 
        catch
            return BigInt(number)
        end
    else
        return number
    end
end

function define_angles!(angle_list::Vector{Tuple{Real, Real}}, n::Int64, start_angle::Number = 90, angle_range=branch_dispersion)
    if iseven(n)
        for i in 0:(n÷2)-1
            push!(angle_list,
            (start_angle - i*angle_range, start_angle - (i+1)*angle_range),
            (start_angle + i*angle_range, start_angle + (i+1)*angle_range))
        end
    else
        push!(angle_list, (start_angle-intfloat(angle_range/2), start_angle+intfloat(angle_range/2)))
        for i in 0:((n-1)÷2)-1
            push!(angle_list,
            (angle_list[1][1] - i*angle_range, angle_list[1][1] - (i + 1) * angle_range),
            (angle_list[1][2] + i*angle_range, angle_list[1][2] + (i + 1) * angle_range))
        end
    end
    return nothing
end
# angle_list = Vector{Tuple{Real, Real}}(); define_angles(angle_list, 5); println(angle_list)
function branch_further(branch_end, branch_length, branch_angle)
    number_of_subbranches = rand(subbranch_range)
    subbranch_angles = Vector{Tuple{Real, Real}}()
    define_angles(subbranch_angles, number_of_subbranches, branch_angle)
    for subbranch in 1:number_of_subbranches
        subbranch_length = branch_length * rand(branch_shortening)
        if subbranch_length > 5
            subbranch_angle = rand(subbranch_angles[subbranch])
                #Consider Sunlight
            subbranch_angle -= (subbranch_angle - 90) * sunlight

                #Create the branch
            subbranch_end = point_at_angle(branch_end, subbranch_length, subbranch_angle)
            draw_line(branch_end, subbranch_end) #Draw method can be changeds
            branch_further(subbranch_end, subbranch_length, subbranch_angle)
        end
    end
end

function draw_tree()
    draw_line(trunk_start, trunk_end)
    branch_further(trunk_end, trunk_length, trunk_angle)
end



Drawing(window_width, window_height, "hello-world.png")
background(mygrey)
setcolor(mywhite)
draw_tree()
finish()
preview()
        