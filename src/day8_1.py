from util import iohandler

inputFile = iohandler.begin(__file__)

# --- solution ---

imgBits = inputFile.readline()

layerSize = 150
layers = [imgBits[i:i+layerSize] for i in range(0, len(imgBits), layerSize)]  # TODO: research this

minCount = layerSize
minLayer = ''
for layer in layers:
    cnt = layer.count('0')
    if cnt < minCount:
        minCount = cnt
        minLayer = layer

validationValue = minLayer.count('1') * minLayer.count('2')

# --- solution ---

iohandler.end(str(validationValue))
