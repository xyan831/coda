# interpolate yi for xi
def interpolation(xi, x, y):
    # x = [x1, x2], y = [y1, y2]
    # get yi for xi btw [x1, x2]
    p = (y[1]-y[0]) / (x[1]-x[0])
    yi = y[0] + (xi-x[0])*p
    return yi

if __name__ == "__main__":
    x = [3,5]
    y = [350,480]
    xi = 4
    yi = interpolation(xi,x,y)
    print(yi)

