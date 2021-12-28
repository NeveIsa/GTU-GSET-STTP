import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plotdb(predict, save="", originaldata=[]):
    grid={"reflectance":[], "weight":[], "denomination":[]}
    for x in np.arange(20,30,0.05):
        for y in np.arange(3,8, 0.05):
            grid["reflectance"]+=[x]
            grid["weight"]+=[y]
            grid["denomination"] += [predict(x,y)]


    grid = pd.DataFrame(grid)
    # print(grid)
    sns.scatterplot(data=grid, x="reflectance", y="weight", hue="denomination", palette="dark")
    
    # plot the original data
    if len(originaldata):
        sns.scatterplot(data=originaldata, x="reflectance", y="weight", hue="denomination", palette="tab10")
    
    if save:
        plt.savefig(save,bbox_inches='tight')
        plt.clf()


if __name__ == "__main__":
    plotdb(lambda x,y:1)
