import marshal as ms
import zlib
import base64 as bs

fo=open('main.py','r')
data=fo.read()
fo.close()


val=ms.dumps(data)
val=bs.b64encode(val)
val2=zlib.compress(val,9)

print(val2)

fw=open('bit.py','bw')
fw.write(val2)
fw.close()

print('done')