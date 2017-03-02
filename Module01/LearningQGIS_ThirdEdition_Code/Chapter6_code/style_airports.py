from PyQt4.QtGui import QColor
rules = [['Civil','USE LIKE \'%Civil%\'','green'], ['Other','USE NOT LIKE \'%Civil%\'','red']]
symbol = QgsSymbolV2.defaultSymbol(v_layer.geometryType())
renderer = QgsRuleBasedRendererV2(symbol)
root_rule = renderer.rootRule()
for label, expression, color_name in rules:
    rule = root_rule.children()[0].clone()
    rule.setLabel(label)
    rule.setFilterExpression(expression)
    rule.symbol().setColor(QColor(color_name))
    root_rule.appendChild(rule)
root_rule.removeChildAt(0)
v_layer.setRendererV2(renderer)
v_layer.triggerRepaint()
