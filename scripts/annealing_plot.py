#!/usr/bin/python3

import os
import styles
import matplotlib.pyplot as plt
from tools import convert60CTo0C, convert60CTom30C, convert60CTo15C, convert60Cto21C

from pointset import pointSetsContainer, pointSet, loadAnnealings

datadir=os.getenv("DATAOUTPATH")


def minat60ToDaysAt0(t):
    return convert60CTo0C(t/(60*24.))

def minat60ToMonthsAtm30(t):
    return convert60CTom30C(t/(60*24.*30.4166)) 

def minat60ToDaysAt15(t):
    return convert60CTo15C(t)/(60*24.)

def minat60ToDaysAt21(t):
    return convert60Cto21C(t)/(60*24.)


for func, altxlabel, addout in zip(
    [minat60ToDaysAt21, minat60ToDaysAt15, minat60ToDaysAt0, minat60ToMonthsAtm30],
    ["time (21˚C) [d]" , "time (15˚C) [d]" , "time (0˚C) [d]", "time (-30˚C) [months]"],
    ["_21C",             "_15C",             "_0C",            "_-30C"]
    ):
    

    def cosmetics(x, ylabel="-$U_{depl}$ [V]", func=func, altxlabel=altxlabel):
        
        plt.legend()
        plt.xscale('log')
        plt.xlabel("time (60˚C) [min]", fontsize=12)
        plt.ylabel(ylabel, fontsize=12)
        
        styles.addModifiedXAxis(x, func, altxlabel)
        plt.xscale('log')
        
        plt.tight_layout()
        
    
    pointsets, kneepointset= loadAnnealings()
    
    
    plt.close()
    pointsets.addToPlot("Udep",["6002_6in"],
                        colors='fluence',
                        #colors=['tab:red','tab:purple'],
                        marker='x')
    kneepointset.addToPlot("Udep",["6002_6in"],[" first kink"],
                           #colors=['tab:red','tab:purple']
                        colors='fluence',
                           )
    pointsets.addToPlot("Udep",["1002_UR", "1003_UR", "1102_UR"],[" UR"," UR"," UR"],
                        #colors=['tab:blue','tab:green','tab:orange'],
                        colors='fluence',
                        marker='x')
    
    
    xs = pointsets.addToPlot("Udep",["1002_UL", "1003_UL", "1102_UL"],
                        #colors=['tab:blue','tab:green','tab:orange']
                        colors='fluence',
                        )
    cosmetics(xs)
    plt.savefig(datadir+"/annealing_plots/300_6inch"+addout+".pdf")
    
    
    plt.close()
    pointsets.addToPlot("Udep",["6002_6in"],[" second kink"],
                        #colors=['tab:red','tab:purple'],
                        colors='fluence',
                        marker='x')
    xs = kneepointset.addToPlot("Udep",["6002_6in"],[" first kink"],
                           #colors=['tab:red','tab:purple']
                        colors='fluence',
                           )
    cosmetics(xs)
    plt.savefig(datadir+"/annealing_plots/6inch"+addout+".pdf")
    
    
    plt.close()
    pointsets.addToPlot("Udep", ["1002_UL","1003_UL","1102_UL"],
                        #colors=['tab:blue','tab:green','tab:orange']
                        colors='fluence',
                        )
    xs = pointsets.addToPlot("Udep", ["1002_UR","1003_UR","1102_UR"],[" UR"," UR"," UR"],
                        #colors=['tab:blue','tab:green','tab:orange'],
                        colors='fluence',
                        marker='x')
    cosmetics(xs)
    plt.savefig(datadir+"/annealing_plots/300"+addout+".pdf")
    
    
    plt.close()
    pointsets.addToPlot("Udep", ["2002_UL","2003_UL","2102_UL"],
                        #colors=['tab:blue','tab:green','tab:orange']
                        colors='fluence',
                        )
    xs = pointsets.addToPlot("Udep", ["2002_UR","2003_UR","2102_UR"],[" UR"," UR"," UR"],
                        #colors=['tab:blue','tab:green','tab:orange'],
                        colors='fluence',
                        marker='x')
    cosmetics(xs)
    plt.savefig(datadir+"/annealing_plots/200"+addout+".pdf")
    
    
    plt.close()
    xs = pointsets.addToPlot("Udep", ["3003_UL","3007_UL","3008_UL"],
                        #colors=['tab:blue','tab:green','tab:orange']
                        colors='fluence',
                        )
    
    cosmetics(xs)
    plt.savefig(datadir+"/annealing_plots/120"+addout+".pdf")
    

#plt.close()
#xs = pointsets.addToPlot("NEff", ["3003_UL","3007_UL","3008_UL"]+["2002_UL","2003_UL","2102_UL"]+["2002_UR","2003_UR","2102_UR"])
#
#cosmetics(xs,"NEff $[1/cm^{3}]$")
#plt.show()



