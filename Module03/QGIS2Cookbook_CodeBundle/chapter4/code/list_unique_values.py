import processing 
layer = iface.activeLayer()
classes = {}
features = processing.features(layer)
for f in features:
    attrs = f.attributes()
    class_value = f['class']
    if class_value in classes:
        classes[class_value] += 1
    else:
        classes[class_value] = 1
print classes
