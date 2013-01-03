import os
import sys
from PIL import Image
from PIL import ImageFilter


def process(source, des=None):
    if not os.path.exists(source):
        raise IOError("{0} does not exists".format(source))

    source_name = os.path.basename(source)
    name, ext = os.path.splitext(source_name)
    if not des:
        des = '/tmp/{0}_shadowed{1}'.format(name, ext)
    sm = Image.open(source)
    sw, sh = sm.size
    dw, dh = sw + 100, sh + 100

    dm = Image.new(sm.mode, (dw, dh), (255, 255, 255))
    limit = 45
    for h in range(limit, dh-limit):
        for w in range(limit, dw-limit):
            dm.putpixel((w, h), (150, 150, 150))

    for i in range(15):
        dm = dm.filter(ImageFilter.BLUR)

    dm.paste(sm, (50, 50))
    dm.save(des, quality=100)
    
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'bad arguments'
        sys.exit(1)

    source = sys.argv[1]
    des = None if len(sys.argv) < 3 else sys.argv[2]
    process(source, des)
