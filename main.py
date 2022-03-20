import os,sys,shutil
def contract_leaf_folder(targdir):
    targdir = os.path.realpath(targdir)
    it = os.walk(targdir)
    for parent_folder,folders,files in it:
        print(parent_folder,len(folders),len(files))
        # print()
        if len(files)==1:
            if len(folders)== 0 or folders==['img']:
                fn = files[0]
                # ppf = os.path.dirname(parent_folder)
                tfn = parent_folder+'.'+fn
                # tfn = ppf+'.'+fn
                fn = (os.path.join(parent_folder,fn))
                tfn = (os.path.join(parent_folder,tfn))
                # print(fn,tfn)
                for x in folders:
                    x = os.path.join(parent_folder,x)
                    fns = os.listdir(x)
                    _targ = (parent_folder+'.'+os.path.basename(x))
                    os.makedirs(_targ) if not os.path.exists(_targ) else None
                    for _f in fns:
                        src,targ = os.path.join(x,_f),_targ
                        print(src,targ)
                        shutil.copy2(src,targ);os.unlink(src)
                    os.rmdir(x)

                src,targ = fn,tfn
                print(src,targ)
                shutil.copy2(src,targ);os.unlink(src)

                os.rmdir(parent_folder)
                # shutil.rmtree(parent_folder)
    return



def main():
    contract_leaf_folder('NLPinterview')
if __name__=='__main__':
    main()
