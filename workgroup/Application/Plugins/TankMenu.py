# TankMenu
# Initial code generated by Softimage SDK Wizard
# Executed Wed Oct 3 18:19:33 EDT 2012 by bgabe
# 
# Tip: To add a command to this plug-in, right-click in the 
# script editor and choose Tools > Add Command.
import win32com.client
from win32com.client import constants

import tank

null = None
false = 0
true = 1

def XSILoadPlugin( in_reg ):
    in_reg.Author = "bgabe"
    in_reg.Name = "TankMenu"
    in_reg.Major = 1
    in_reg.Minor = 0
    
    engine = tank.platform.current_engine()
    if not engine:
        return
    in_reg.RegisterMenu(constants.siMenuMainTopLevelID,"Tank",false,false)
    #RegistrationInsertionPoint - do not remove this line

    return true

def XSIUnloadPlugin( in_reg ):
    strPluginName = in_reg.Name
    Application.LogMessage(str(strPluginName) + str(" has been unloaded."),constants.siVerbose)
    return true

def UpdateTankMenu_Init( in_ctxt ):
    oCmd = in_ctxt.Source
    oCmd.Description = ""
    oCmd.ReturnValue = true

    return true

def UpdateTankMenu_Execute(  ):

    Application.LogMessage("TankMenu_Execute called",constants.siVerbose)
    # 
    # TODO: Put your command implementation here.
    # 
    return true

#########################################################################################################################

def Tank_Init( in_ctxt ):
    
    engine = tank.platform.current_engine()
    if engine:
        print "TankMenu_Init: ", engine
    else:
        Application.LogMessage("TankMenu_Init() -- No Tank engine currently running!", 8)
        return            

    mg = engine.get_menu_generator(in_ctxt.Source, globals())
    mg.create_menu()
    return true   
   
        