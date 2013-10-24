# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline

x = np.genfromtxt('/Users/hmiller/Dropbox/git-shared/private-progfun-data/dat/huff-scores-fall2012.csv')
y = np.genfromtxt('/Users/hmiller/Dropbox/git-shared/private-progfun-data/dat/huff-numsubs-fall2012.csv')
xmin = x.min()
xmax = x.max()
ymin = y.min()
ymax = y.max()

plt.subplot(121)
plt.hexbin(x,y,bins='log', cmap=plt.cm.gnuplot2)
plt.axis([xmin, xmax, ymin, 24])
plt.title("Fall 2012", fontsize=16)
cb = plt.colorbar()
cb.set_label('log10(N)')
plt.xlabel('Score', fontsize=16)
plt.ylabel('# Submissions', fontsize=16)


x2 = np.genfromtxt('/Users/hmiller/Dropbox/git-shared/private-progfun-data/dat/huff-scores-spring2013.csv')
y2 = np.genfromtxt('/Users/hmiller/Dropbox/git-shared/private-progfun-data/dat/huff-numsubs-spring2013.csv')
xmin2 = x2.min()
xmax2 = x2.max()
ymin2 = y2.min()
ymax2 = y2.max()

plt.subplot(122)
plt.hexbin(x2,y2,bins='log', cmap=plt.cm.gnuplot2)
plt.axis([xmin2, xmax2, ymin2, ymax2])
plt.title("Spring 2013", fontsize=16)
cb = plt.colorbar()
cb.set_label('log10(N)')
plt.xlabel('Score', fontsize=16)
plt.ylabel('# Submissions', fontsize=16)

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(16,4)
plt.savefig('/Users/hmiller/Dropbox/git-shared/private-progfun-data/plots/score-2d-histogram-fall2012-spring2013.pdf')

# <codecell>

import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline

x = np.genfromtxt('/Users/hmiller/Dropbox/git-shared/private-progfun-data/dat/huff-scores-spring2013.csv')
y = np.genfromtxt('/Users/hmiller/Dropbox/git-shared/private-progfun-data/dat/huff-numsubs-spring2013.csv')
xmin = x.min()
xmax = x.max()
ymin = y.min()
ymax = y.max()

# plt.subplot(122)
plt.hexbin(x,y,bins='log', cmap=plt.cm.gnuplot2)
plt.axis([xmin, xmax, ymin, ymax])
# plt.title("With a log color scale")
cb = plt.colorbar()
cb.set_label('log10(N)')
plt.xlabel('Score', fontsize=16)
plt.ylabel('# Submissions', fontsize=16)

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(8,4)
plt.savefig('/Users/hmiller/Dropbox/git-shared/private-progfun-data/plots/score-2d-histogram-spring2013.pdf')

# <codecell>

import math
math.log10(3.2)

# <codecell>

import numpy as np
import pylab as P
from matplotlib.ticker import FuncFormatter
from matplotlib import rc, font_manager

plt.rc('font', family='serif') 
plt.rc('font', serif='Times New Roman') 

bns = range(1,21)

def to_percent(y, position):
    # Ignore the passed in position. This has the effect of scaling the default
    # tick locations.
    s = str(100 * y)

    # The percent symbol needs escaping in latex
    if matplotlib.rcParams['text.usetex'] == True:
        return s + r'$\%$'
    else:
        return s + '%'

formatter = FuncFormatter(to_percent)    
P.gca().yaxis.set_major_formatter(formatter)

# overall_font = font_manager.FontProperties(family='Helvetica', style='normal', weight='normal', stretch='normal')
# rc('font',**{'family':'sans-serif','sans-serif':['Helvetica'],'weight':'normal'})

unfiltered1 = np.genfromtxt('/Users/hmiller/Desktop/top-scores.csv')
x1 = filter(lambda x: x <= 20, unfiltered1)

n1, bins1, patches1 = P.hist(x1, bns, normed=1, histtype='stepfilled')
P.setp(patches1, 'facecolor', '#85004B', 'alpha', 1, edgecolor='black', hatch="//")

unfiltered2 = np.genfromtxt('/Users/hmiller/Desktop/top-scores2.csv')
x2 = filter(lambda x: x <= 20, unfiltered2)
n2, bins2, patches2 = P.hist(x2, bns, normed=1, histtype='stepfilled')
P.setp(patches2, 'facecolor', '#FF9640', 'alpha', 0.6, edgecolor='black', hatch="||")

P.xlim([1,20])
P.legend([patches1[0], patches2[0]], ['Fall 2012', 'Spring 2013'], fontsize=14)
P.xlabel('# Submissions', fontsize=16)
P.ylabel('Percentage of Students', fontsize=16)
P.tick_params(axis='both', labelsize=12)
P.gcf().subplots_adjust(left=0.15)

P.savefig('/Users/hmiller/Dropbox/git-shared/private-progfun-data/plots/top-scores-submissions-histogram.pdf',transparent=True)


# <codecell>

import numpy as np
import matplotlib.pyplot as plt
from itertools import islice

def downsample_to_proportion(rows, proportion=1):
    return list(islice(rows, 0, len(rows), int(1/proportion)))

plt.rc('font', family='serif') 
plt.rc('font', serif='Times New Roman') 

n = 80
width = 0.4

final_scores_fall2012 = np.genfromtxt('/Users/hmiller/Dropbox/git-shared/private-progfun-data/dat/final-score-histogram-fall2012.csv')
final_scores_spring2013 = np.genfromtxt('/Users/hmiller/Dropbox/git-shared/private-progfun-data/dat/final-score-histogram-spring2013.csv')

ind = np.arange(n)
fig, ax = plt.subplots()

rects1 = ax.bar(ind, final_scores_fall2012, width, 
                alpha=1,
                hatch="//",
                color='#85004B')
rects2 = ax.bar(ind+width, final_scores_spring2013, width, 
                alpha=1,
                hatch="||",
                color='#FD7422')

ax.legend((rects1[0], rects2[0]), ('Fall 2012', 'Spring 2013'), fontsize=18,loc='upper left')
plt.xlabel('Score', fontsize=20)
plt.ylabel('Number of Students', fontsize=20)
plt.tick_params(axis='both', labelsize=20)
downsampled = downsample_to_proportion(ind+width, 0.1)
place_ticks = [10-(1.5*width), 20-(1.5*width), 30-(1.5*width), 40-(1.5*width), 50-(1.5*width), 60-(1.5*width), 70-(1.5*width), 80-(1.5*width)]
ax.set_xticks(place_ticks)
ax.set_xticklabels( ('10', '20', '30', '40', '50', '60', '70', '80') )
plt.grid()

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(20,3)
P.gcf().subplots_adjust(bottom=0.25)
plt.savefig('/Users/hmiller/Dropbox/git-shared/private-progfun-data/plots/final-scores.pdf',transparent=True,dpi=150)

# <codecell>

import numpy
import matplotlib.pyplot as plt

x1 = np.genfromtxt('/Users/hmiller/Dropbox/git-shared/private-progfun-data/dat/huff-fvf-final-fall2012.csv')
y1 = np.genfromtxt('/Users/hmiller/Dropbox/git-shared/private-progfun-data/dat/huff-fvf-first-fall2012.csv')
plt.scatter(x1, y1, c="#85004B", s=2, edgecolors='None', alpha=1)

x2 = np.genfromtxt('/Users/hmiller/Dropbox/git-shared/private-progfun-data/dat/huff-fvf-final-spring2013.csv')
y2 = np.genfromtxt('/Users/hmiller/Dropbox/git-shared/private-progfun-data/dat/huff-fvf-first-spring2013.csv')
plt.scatter(x2, y2, c="#FF9640", s=2, edgecolors='None', alpha=0.6)

plt.savefig('/Users/hmiller/Dropbox/git-shared/private-progfun-data/plots/huffman-final-vs-final-scores.pdf',transparent=True,dpi=150)

# <codecell>

import matplotlib.pyplot as plt
import numpy as np

data = [29.0, 20.0, 20.0, 8.0, 3.0, 2.0, 4.0]
labels = ["6 - Strongly Agree", "5", "4", "3", "2", "1 - Strongly Disagree", "No Opinion"]
total = sum(data)
perc = data/total*100

fig = plt.figure(figsize=(12, 0.8))
ax = fig.add_subplot(211)

def colorer(imp):
    if imp == "6 - Strongly Agree":
        out = "#85004B" #dark purple
    elif imp == "5":
        out = "#CD0074" #purple
    elif imp == "4":
        out = "#FF0000" #red
    elif imp == "3":
        out = "#FF7400" #orange
    elif imp == "2":
        out = "#FFB273" #light orange
    elif imp == "1 - Strongly Disagree":
        out = "#00CC00" #green
    else:
        out = "#d0d0d0" #gray

    return out

lefter = 0

for i in np.arange(0, len(perc)):
    ax.barh([0], perc[i], height=10, left=lefter, color=colorer(labels[i]), label="%s" % ([i]))
    ax.text(lefter+(perc[i]/2), 1.5, "%s%s" % (round(perc[i], 2), "%"), size=10)

    lefter += data[i]

print perc

#hide x ticks    
ax.set_xticks([])

#asjust y axis
ax.set_ylim(0.4,10)

#set y tick location
ax.set_yticks([1.5])

#replace y tick with text string
# ax.set_yticklabels(["nutrients"])

ax.set_title("Horizontal bar plot")

#generate legend and move  it off the plot, labels are defined in ax1.barh argument "label="
# ax.legend(bbox_to_anchor = (1.37, 0.8))

# <codecell>

import numpy as np
import matplotlib.pyplot as plt

plt.rc('font', family='serif') 
plt.rc('font', serif='Times New Roman') 

n = 5
width = 0.45

wi_fall2012 = np.genfromtxt('/Users/hmiller/Dropbox/git-shared/private-progfun-data/dat/worth-it-fall2012.csv')
wiai_fall2012 = np.genfromtxt('/Users/hmiller/Dropbox/git-shared/private-progfun-data/dat/worth-it-apply-it-fall2012.csv')
wi_spring2013 = np.genfromtxt('/Users/hmiller/Dropbox/git-shared/private-progfun-data/dat/worth-it-spring2013.csv')
wiai_spring2013 = np.genfromtxt('/Users/hmiller/Dropbox/git-shared/private-progfun-data/dat/worth-it-apply-it-spring2013.csv')

ind = np.arange(n)
ax1 = plt.subplot(121)

rects1 = ax1.bar(ind, wi_fall2012, width, 
                alpha=1,
                hatch="//",
                color='#85004B')
rects2 = ax1.bar(ind+width, wiai_fall2012, width, 
                alpha=1,
                hatch="||",
                color='#FD7422')

# ax1.legend((rects1[0], rects2[0]), ('Fall 2012', 'Spring 2013'), fontsize=18,loc='upper left')
plt.axis([0, 5, 0, 100])
plt.title('Fall 2012', fontsize=18)
plt.ylabel('Percentage of Students', fontsize=18)
plt.tick_params(axis='both', labelsize=18)
ax1.set_xticks(ind+width)
ax1.set_xticklabels( ('1\n(Disagree)', '2', '3', '4', '5\n(Agree)') )
plt.grid()

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax1.text(rect.get_x()+rect.get_width()/2., 1.0*height, '%d%%'%int(height),
                ha='center', va='bottom', fontsize=14)

autolabel(rects1)
autolabel(rects2)


ax2 = plt.subplot(122)

rects3 = ax2.bar(ind, wi_spring2013, width, 
                alpha=1,
                hatch="//",
                color='#85004B')
rects4 = ax2.bar(ind+width, wiai_spring2013, width, 
                alpha=1,
                hatch="||",
                color='#FD7422')

plt.axis([0, 5, 0, 100])
# plt.ylabel('Percentage of Students', fontsize=20)
plt.tick_params(axis='both', labelsize=18)
plt.title('Spring 2013', fontsize=18)
ax2.set_xticks(ind+width)
ax2.set_xticklabels( ('1\n(Disagree)', '2', '3', '4', '5\n(Agree)') )
plt.grid()

def autolabel2(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax2.text(rect.get_x()+rect.get_width()/2., 1.0*height, '%d%%'%int(height),
                ha='center', va='bottom', fontsize=14)

autolabel2(rects3)
autolabel2(rects4)

fig = matplotlib.pyplot.gcf()
fig.legend((rects1[0], rects2[0]), ('All Respondents', 'Respondents Using Scala at Work'), fontsize=14, loc='lower center', ncol=2)
fig.set_size_inches(12,4)
plt.gcf().subplots_adjust(bottom=0.26)

plt.savefig('/Users/hmiller/Dropbox/git-shared/private-progfun-data/plots/worth-it-apply-it.pdf',transparent=True,dpi=150)

# <codecell>

# 

# <codecell>


