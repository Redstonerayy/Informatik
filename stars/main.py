from stardiff import *
from stardiff import checklighting

# diff = imagediff(bild1, bild2)
# printimg(diff)
# img1data = makeimg(bild1, "bild1.png")
# img2data = makeimg(bild2, "bild2.png")
# diffdata = makeimg(diff, "diff.png")
# joined = [*img1data, *img2data, *diffdata]
# imgfromdata(joined, 10, 30)
printimg(bild1)
light = checklighting(bild1)
gradient(light, "light.png")