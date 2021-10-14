import os,json,gzip,toml
rootDir = "./libs"
print("rootDir",rootDir)
libs ={}
keys = ["name","version","url","git","hash","authors","description"]
def addLib(lib):
    global libs
    name = lib['name']
    lib= {k:v for k,v in lib.items() if k in keys}
    libs[name] = lib

def loadFiles():
    global libs
    for root,dirs,files in os.walk(rootDir):
        for name in files:
            if name[-4:] !='toml':
                print(name[-4:])
                continue
            path = os.path.join(root,name)
            try:
                lib = toml.load(path)['package']
                addLib(lib)
            except e as err:
                print(name)
                print(err)
def main():
    loadFiles()
    with gzip.open('./libs.json.gz', 'wb') as f:
        f.write(json.dumps(libs).encode("unicode_escape"))
    #print(libs)
main()
