from util import iohandler

inputFile = iohandler.begin(__file__)

# --- solution ---

imgBits = inputFile.readline()

layerSize = 150  # 25x6
layers = [imgBits[i:i+layerSize] for i in range(0, len(imgBits), layerSize)]

print(layers)

visibleLayer = ''
bitNum = 0
while bitNum < layerSize:
    pxColor = 2

    for layer in layers:
        if int(layer[bitNum]) < 2:
            pxColor = layer[bitNum]
            break

    visibleLayer += pxColor
    bitNum += 1

# visibleLayer = visibleLayer.replace('0', ' ')
# print(visibleLayer[:25])
# print(visibleLayer[25:50])
# print(visibleLayer[50:75])
# print(visibleLayer[75:100])
# print(visibleLayer[100:125])
# print(visibleLayer[125:150])

# --- solution ---

iohandler.end(str(visibleLayer))
