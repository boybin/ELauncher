'''
Created on Jul 1, 2013

@author: xiaobinc
'''
from com.elauncher.modules.WorkspacesHandler import WorkspacesHandler
import os
import win32api

class ELauncher(object):
    
    def __init__(self, eclipseCmdPath, src, dest):
        self.fEclipseCmdPath = eclipseCmdPath;
        self.fSrc = src;
        self.fDest = dest;
        
    def launch(self):
        if not os.path.exists(self.fDest):
            wsHandler = WorkspacesHandler(self.fSrc, self.fDest);
            wsHandler.copyMetaWorkspace();
            
        if os.path.isdir(self.fDest):
            win32api.ShellExecute(0, 'open', self.fEclipseCmdPath, ' -data '+self.fDest, '', 0)