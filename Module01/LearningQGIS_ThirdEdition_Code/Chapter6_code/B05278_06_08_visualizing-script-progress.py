i = 0
n = my_layer.featureCount()
for input_feature in my_layer.getFeatures():
    progress.setPercentage(int(100*i/n))
    i+=1
