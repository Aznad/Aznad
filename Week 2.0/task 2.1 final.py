#z = (x+6)^2 + (y+2)^2

l_min = 0.00001
#lambdaa = 0.5  #'''learning rate'''

def fn(x1, x2, lamdaa, maxiterations = 1000):

    if not max_iterations:
        return print(x, y, count)

    pre_x1_val = x1
    pre_x2_val = x2

    curr_x1_val -= lambdaa * 2*(pre_x1_val+6)
    curr_x2_val -= lambdaa * 2*(pre_x2_val+2)
    max_iterations -= 1
    fn(x1, x2, max_iterations)

fn(1,5, 0.5)