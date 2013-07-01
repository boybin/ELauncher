'''
Created on Jul 1, 2013

@author: xiaobinc
'''
import shutil;
import os

class WorkspacesHandler():
    
    def __init__(self, src, dest):
        self.fSrc = src;
        self.fDest = dest;

    '''
        The destination directory must not exist, otherwise you need to see if there is already have created the workspace
    '''
    def copyMetaWorkspace(self) :
        shutil.copytree(self.fSrc, self.fDest);
    
    def deleteDestWorkspace(self) :
        if os.path.isdir(self.fDest) :
            shutil.rmtree(self.fDest); 