import matplotlib.pyplot as plt
import numpy as np

# f_label = '$x**3 - 18*x - 83$'
f_label = '$sin(x) + cos(x) * x$'

def drawPlot(a, b, f, roots, exes, infp, points=[]):

    x = np.arange(a, b, 0.001)
    fx = [ f(i) for i in x ]
    plt.plot(x, fx, 'k', label=f_label)


    if 'roots' in points:
        froots = [ f(i) for i in roots ]
        plt.plot(roots, froots, 'ro', label='Roots')

    if 'exes' in points:
        fexes = [ f(i) for i in exes ]
        plt.plot(exes, fexes, 'go', label='Extremas')

    if 'infp' in points:
        finfp = [ f(i) for i in infp ]
        plt.plot(infp, finfp, 'bo', label='Inflection points')


    if exes:
        fexes = [ f(i) for i in exes ]

        minY = min(fexes)
        maxY = max(fexes)

        for i in range(len(exes)):
            if f(exes[i]) == minY:
                minX = exes[i]
            if f(exes[i]) == maxY:
                maxX = exes[i]

        plt.plot(minX, minY, 'co')
        plt.plot(maxX, maxY, 'co')

        plt.annotate('max', xy=(maxX, maxY), xytext=(maxX + 1.5, maxY),
            arrowprops=dict(facecolor='cyan', shrink=0.05),
            )

        plt.annotate('min', xy=(minX, minY), xytext=(minX + 1.5, minY),
            arrowprops=dict(facecolor='cyan', shrink=0.05),
            )


    legend = plt.legend(loc='upper left', shadow=True)

    frame = legend.get_frame()
    frame.set_facecolor('0.90')

    for label in legend.get_texts():
        label.set_fontsize('large')

    for label in legend.get_lines():
        label.set_linewidth(1.5)

    #plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

    plt.subplot().spines['bottom'].set_position('zero')
    #plt.ylim(-3,3)
    #plt.axis([-10, 10, -5, 5])
    plt.grid(True)
    plt.show()
    
    return True
