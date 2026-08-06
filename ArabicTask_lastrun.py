#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2026.1.3),
    on August 06, 2026, at 11:26
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2026.1.3'
expName = 'ArabicTask'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': randint(10000, 99999),
    'Language Proficiency': ['Professional Native','Professional L2'],
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = False
_winSize = (1280, 720)
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\HP\\Downloads\\MASTER RESEARCH\\Ar_L2\\ArabicTask_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    # store pilot mode in data file
    thisExp.addData('piloting', PILOTING, priority=priority.LOW)
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=True, allowStencil=True,
            monitor='testMonitor', color='#beb0df', colorSpace='hex',
            backgroundImage='background.jpg', backgroundFit='contain',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = '#beb0df'
        win.colorSpace = 'hex'
        win.backgroundImage = 'background.jpg'
        win.backgroundFit = 'contain'
        win.units = 'height'
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # update experiment info
    expInfo['date'] = data.getDateStr()
    expInfo['expName'] = expName
    expInfo['expVersion'] = expVersion
    expInfo['psychopyVersion'] = psychopyVersion
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "WelcomeScreen" ---
    textWelcome = visual.TextStim(win=win, name='textWelcome',
        text='Welcome to the Arabic Fluency Task\nمرحبا بك في اختبار إتقان اللغة العربية',
        font='Broadway',
        units='height', pos=(0, 0.1), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='#62547c', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=-2.0);
    polygonStart = visual.ShapeStim(
        win=win, name='polygonStart', vertices=[(-0.35, 0.15), (0.35, 0.15), (0.365, 0.149), (0.379, 0.147), (0.394, 0.144), (0.407, 0.139), (0.421, 0.132), (0.433, 0.125), (0.445, 0.116), (0.456, 0.106), (0.466, 0.095), (0.475, 0.083), (0.482, 0.071), (0.489, 0.057), (0.494, 0.044), (0.497, 0.029), (0.499, 0.015), (0.5, 0), (0.499, -0.015), (0.497, -0.029), (0.494, -0.044), (0.489, -0.057), (0.482, -0.071), (0.475, -0.083), (0.466, -0.095), (0.456, -0.106), (0.445, -0.116), (0.433, -0.125), (0.421, -0.132), (0.407, -0.139), (0.394, -0.144), (0.379, -0.147), (0.365, -0.149), (0.35, -0.15), (-0.35, -0.15), (-0.365, -0.149), (-0.379, -0.147), (-0.394, -0.144), (-0.407, -0.139), (-0.421, -0.132), (-0.433, -0.125), (-0.445, -0.116), (-0.456, -0.106), (-0.466, -0.095), (-0.475, -0.083), (-0.482, -0.071), (-0.489, -0.057), (-0.494, -0.044), (-0.497, -0.029), (-0.499, -0.015), (-0.5, 0), (-0.499, 0.015), (-0.497, 0.029), (-0.494, 0.044), (-0.489, 0.057), (-0.482, 0.071), (-0.475, 0.083), (-0.466, 0.095), (-0.456, 0.106), (-0.445, 0.116), (-0.433, 0.125), (-0.421, 0.132), (-0.407, 0.139), (-0.394, 0.144), (-0.379, 0.147), (-0.365, 0.149)],
        size=(0.35, 0.35),
        ori=0.0, pos=(0, -0.3), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='hex', lineColor='#b6a7da', fillColor='#b6a7da',
        opacity=None, depth=-3.0, interpolate=False)
    text_ButtonStart = visual.TextStim(win=win, name='text_ButtonStart',
        text='START\nإبدا',
        font='Broadway',
        units='height', pos=(0, -0.3), draggable=False, height=0.045, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=-4.0);
    mouseStart = event.Mouse(win=win)
    x, y = [None, None]
    mouseStart.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "baseline_Instructions" ---
    baseline_typing = visual.TextStim(win=win, name='baseline_typing',
        text='A paragraph will appear after you hit start! trying to type it as fast and accurately as you can. You will have 60 seconds to finish.\n\nسيظهر مقال بعد الضغط على زر البدء؛ حاول كتابته بأقصى سرعة ودقة ممكنتين. سيكون لديك ستون ثانية لإتمام المهمة',
        font='Bahnschrift',
        units='height', pos=(0, 0.1), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='#62547c', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=0.0);
    polygonBaseline = visual.ShapeStim(
        win=win, name='polygonBaseline', vertices=[(-0.35, 0.15), (0.35, 0.15), (0.365, 0.149), (0.379, 0.147), (0.394, 0.144), (0.407, 0.139), (0.421, 0.132), (0.433, 0.125), (0.445, 0.116), (0.456, 0.106), (0.466, 0.095), (0.475, 0.083), (0.482, 0.071), (0.489, 0.057), (0.494, 0.044), (0.497, 0.029), (0.499, 0.015), (0.5, 0), (0.499, -0.015), (0.497, -0.029), (0.494, -0.044), (0.489, -0.057), (0.482, -0.071), (0.475, -0.083), (0.466, -0.095), (0.456, -0.106), (0.445, -0.116), (0.433, -0.125), (0.421, -0.132), (0.407, -0.139), (0.394, -0.144), (0.379, -0.147), (0.365, -0.149), (0.35, -0.15), (-0.35, -0.15), (-0.365, -0.149), (-0.379, -0.147), (-0.394, -0.144), (-0.407, -0.139), (-0.421, -0.132), (-0.433, -0.125), (-0.445, -0.116), (-0.456, -0.106), (-0.466, -0.095), (-0.475, -0.083), (-0.482, -0.071), (-0.489, -0.057), (-0.494, -0.044), (-0.497, -0.029), (-0.499, -0.015), (-0.5, 0), (-0.499, 0.015), (-0.497, 0.029), (-0.494, 0.044), (-0.489, 0.057), (-0.482, 0.071), (-0.475, 0.083), (-0.466, 0.095), (-0.456, 0.106), (-0.445, 0.116), (-0.433, 0.125), (-0.421, 0.132), (-0.407, 0.139), (-0.394, 0.144), (-0.379, 0.147), (-0.365, 0.149)],
        size=(0.35, 0.35),
        ori=0.0, pos=(0, -0.3), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='hex', lineColor='#b6a7da', fillColor='#b6a7da',
        opacity=None, depth=-1.0, interpolate=True)
    textBaseline_Start = visual.TextStim(win=win, name='textBaseline_Start',
        text='Begin\nإبدا',
        font='Broadway',
        units='height', pos=(0, -0.3), draggable=False, height=0.045, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=-2.0);
    mouse_Instruc = event.Mouse(win=win)
    x, y = [None, None]
    mouse_Instruc.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "ParagraphTyping" ---
    baseline_Paragraph = visual.TextStim(win=win, name='baseline_Paragraph',
        text='تعد القراءة غذاء للعقل والروح. فهي ليست مجرد هواية نقضي بها اوقات فراغنا بل مفتاح يفتح لنا أبواب المعرفة. من خلال صفحات الكتب نسافر عبر الزمن لنتعرف على حضارات الأمم السابقة ونطوف حول العالم دون أن نتحرك من أماكننا. تتجلى أهمية القراءة في توسيع مدارك الإنسان وتطوير مهارات التفكير لديه كما تزيد من حصيلته اللغوية وتقدم له حلولا مبتكرة للمشكلات.',
        font='Bahnschrift',
        units='height', pos=(0, 0.2), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='#62547c', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=0.0);
    textbox_baseline_input = visual.TextBox2(
         win, text=None, placeholder='Type here... اكتب هنا...', font='Bahnschrift',
         ori=0.0, pos=(0, -0.3), draggable=False, units='height',     letterHeight=0.05,
         size=(1, 0.35), borderWidth=2.0,
         color='#62547c', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor='white', borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='Arabic',
         editable=True,
         name='textbox_baseline_input',
         depth=-1, autoLog=True,
    )
    textClocktimer = visual.TextStim(win=win, name='textClocktimer',
        text='',
        font='Broadway',
        pos=(0.6, 0.4), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='darkred', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "Task" ---
    text_Taskquestion = visual.TextStim(win=win, name='text_Taskquestion',
        text='',
        font='Broadway',
        units='height', pos=(0, 0.2), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='#62547c', colorSpace='rgb', opacity=None, 
        languageStyle='Arabic',
        depth=0.0);
    textbox_answer = visual.TextBox2(
         win, text=None, placeholder='...', font='Broadway',
         ori=0.0, pos=(0, 0), draggable=False, units='height',     letterHeight=0.05,
         size=(0.35, 0.10), borderWidth=2.0,
         color='#62547c', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor='white', borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='Arabic',
         editable=True,
         name='textbox_answer',
         depth=-1, autoLog=True,
    )
    key_respTask = keyboard.Keyboard(deviceName='defaultKeyboard')
    TaskCounter = visual.TextStim(win=win, name='TaskCounter',
        text='',
        font='Arial',
        units='height', pos=(0, 0.4), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='#62547c', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "GoodbyeScreen" ---
    text_Goodbye = visual.TextStim(win=win, name='text_Goodbye',
        text='Thank you for Participating!\n\nPlease wait while we save your results...',
        font='Broadway',
        units='height', pos=(0, 0), draggable=False, height=0.1, wrapWidth=None, ori=0.0, 
        color='#62547c', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    if eyetracker is not None:
        eyetracker.enableEventReporting()
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "WelcomeScreen" ---
    # create an object to store info about Routine WelcomeScreen
    WelcomeScreen = data.Routine(
        name='WelcomeScreen',
        components=[textWelcome, polygonStart, text_ButtonStart, mouseStart],
    )
    WelcomeScreen.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouseStart
    mouseStart.clicked_name = []
    gotValidClick = False  # until a click is received
    # store start times for WelcomeScreen
    WelcomeScreen.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    WelcomeScreen.tStart = globalClock.getTime(format='float')
    WelcomeScreen.status = STARTED
    thisExp.addData('WelcomeScreen.started', WelcomeScreen.tStart)
    WelcomeScreen.maxDuration = None
    # keep track of which components have finished
    WelcomeScreenComponents = WelcomeScreen.components
    for thisComponent in WelcomeScreen.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "WelcomeScreen" ---
    thisExp.currentRoutine = WelcomeScreen
    WelcomeScreen.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textWelcome* updates
        
        # if textWelcome is starting this frame...
        if textWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textWelcome.frameNStart = frameN  # exact frame index
            textWelcome.tStart = t  # local t and not account for scr refresh
            textWelcome.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textWelcome, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textWelcome.started')
            # update status
            textWelcome.status = STARTED
            textWelcome.setAutoDraw(True)
        
        # if textWelcome is active this frame...
        if textWelcome.status == STARTED:
            # update params
            pass
        
        # *polygonStart* updates
        
        # if polygonStart is starting this frame...
        if polygonStart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygonStart.frameNStart = frameN  # exact frame index
            polygonStart.tStart = t  # local t and not account for scr refresh
            polygonStart.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygonStart, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygonStart.started')
            # update status
            polygonStart.status = STARTED
            polygonStart.setAutoDraw(True)
        
        # if polygonStart is active this frame...
        if polygonStart.status == STARTED:
            # update params
            pass
        
        # *text_ButtonStart* updates
        
        # if text_ButtonStart is starting this frame...
        if text_ButtonStart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_ButtonStart.frameNStart = frameN  # exact frame index
            text_ButtonStart.tStart = t  # local t and not account for scr refresh
            text_ButtonStart.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_ButtonStart, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_ButtonStart.started')
            # update status
            text_ButtonStart.status = STARTED
            text_ButtonStart.setAutoDraw(True)
        
        # if text_ButtonStart is active this frame...
        if text_ButtonStart.status == STARTED:
            # update params
            pass
        # *mouseStart* updates
        
        # if mouseStart is starting this frame...
        if mouseStart.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouseStart.frameNStart = frameN  # exact frame index
            mouseStart.tStart = t  # local t and not account for scr refresh
            mouseStart.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouseStart, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouseStart.started', t)
            # update status
            mouseStart.status = STARTED
            mouseStart.mouseClock.reset()
            prevButtonState = mouseStart.getPressed()  # if button is down already this ISN'T a new click
        if mouseStart.status == STARTED:  # only update if started and not finished!
            buttons = mouseStart.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(polygonStart, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouseStart):
                            gotValidClick = True
                            mouseStart.clicked_name.append(obj.name)
                            mouseStart.clicked_name.append(obj.name)
                    continueRoutine = False  # end routine on response        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=WelcomeScreen,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            WelcomeScreen.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if WelcomeScreen.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in WelcomeScreen.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "WelcomeScreen" ---
    for thisComponent in WelcomeScreen.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for WelcomeScreen
    WelcomeScreen.tStop = globalClock.getTime(format='float')
    WelcomeScreen.tStopRefresh = tThisFlipGlobal
    thisExp.addData('WelcomeScreen.stopped', WelcomeScreen.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.nextEntry()
    # the Routine "WelcomeScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "baseline_Instructions" ---
    # create an object to store info about Routine baseline_Instructions
    baseline_Instructions = data.Routine(
        name='baseline_Instructions',
        components=[baseline_typing, polygonBaseline, textBaseline_Start, mouse_Instruc],
    )
    baseline_Instructions.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_Instruc
    mouse_Instruc.x = []
    mouse_Instruc.y = []
    mouse_Instruc.leftButton = []
    mouse_Instruc.midButton = []
    mouse_Instruc.rightButton = []
    mouse_Instruc.time = []
    mouse_Instruc.clicked_name = []
    gotValidClick = False  # until a click is received
    # store start times for baseline_Instructions
    baseline_Instructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    baseline_Instructions.tStart = globalClock.getTime(format='float')
    baseline_Instructions.status = STARTED
    thisExp.addData('baseline_Instructions.started', baseline_Instructions.tStart)
    baseline_Instructions.maxDuration = None
    # keep track of which components have finished
    baseline_InstructionsComponents = baseline_Instructions.components
    for thisComponent in baseline_Instructions.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "baseline_Instructions" ---
    thisExp.currentRoutine = baseline_Instructions
    baseline_Instructions.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *baseline_typing* updates
        
        # if baseline_typing is starting this frame...
        if baseline_typing.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            baseline_typing.frameNStart = frameN  # exact frame index
            baseline_typing.tStart = t  # local t and not account for scr refresh
            baseline_typing.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(baseline_typing, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'baseline_typing.started')
            # update status
            baseline_typing.status = STARTED
            baseline_typing.setAutoDraw(True)
        
        # if baseline_typing is active this frame...
        if baseline_typing.status == STARTED:
            # update params
            pass
        
        # *polygonBaseline* updates
        
        # if polygonBaseline is starting this frame...
        if polygonBaseline.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygonBaseline.frameNStart = frameN  # exact frame index
            polygonBaseline.tStart = t  # local t and not account for scr refresh
            polygonBaseline.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygonBaseline, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'polygonBaseline.started')
            # update status
            polygonBaseline.status = STARTED
            polygonBaseline.setAutoDraw(True)
        
        # if polygonBaseline is active this frame...
        if polygonBaseline.status == STARTED:
            # update params
            pass
        
        # *textBaseline_Start* updates
        
        # if textBaseline_Start is starting this frame...
        if textBaseline_Start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textBaseline_Start.frameNStart = frameN  # exact frame index
            textBaseline_Start.tStart = t  # local t and not account for scr refresh
            textBaseline_Start.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textBaseline_Start, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textBaseline_Start.started')
            # update status
            textBaseline_Start.status = STARTED
            textBaseline_Start.setAutoDraw(True)
        
        # if textBaseline_Start is active this frame...
        if textBaseline_Start.status == STARTED:
            # update params
            pass
        # *mouse_Instruc* updates
        
        # if mouse_Instruc is starting this frame...
        if mouse_Instruc.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_Instruc.frameNStart = frameN  # exact frame index
            mouse_Instruc.tStart = t  # local t and not account for scr refresh
            mouse_Instruc.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_Instruc, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_Instruc.started', t)
            # update status
            mouse_Instruc.status = STARTED
            mouse_Instruc.mouseClock.reset()
            prevButtonState = mouse_Instruc.getPressed()  # if button is down already this ISN'T a new click
        if mouse_Instruc.status == STARTED:  # only update if started and not finished!
            buttons = mouse_Instruc.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(polygonBaseline, namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_Instruc):
                            gotValidClick = True
                            mouse_Instruc.clicked_name.append(obj.name)
                    if not gotValidClick:
                        mouse_Instruc.clicked_name.append(None)
                    x, y = mouse_Instruc.getPos()
                    mouse_Instruc.x.append(float(x))
                    mouse_Instruc.y.append(float(y))
                    buttons = mouse_Instruc.getPressed()
                    mouse_Instruc.leftButton.append(buttons[0])
                    mouse_Instruc.midButton.append(buttons[1])
                    mouse_Instruc.rightButton.append(buttons[2])
                    mouse_Instruc.time.append(mouse_Instruc.mouseClock.getTime())
                    
                    continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=baseline_Instructions,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            baseline_Instructions.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if baseline_Instructions.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in baseline_Instructions.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "baseline_Instructions" ---
    for thisComponent in baseline_Instructions.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for baseline_Instructions
    baseline_Instructions.tStop = globalClock.getTime(format='float')
    baseline_Instructions.tStopRefresh = tThisFlipGlobal
    thisExp.addData('baseline_Instructions.stopped', baseline_Instructions.tStop)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_Instruc.x', mouse_Instruc.x)
    thisExp.addData('mouse_Instruc.y', mouse_Instruc.y)
    thisExp.addData('mouse_Instruc.leftButton', mouse_Instruc.leftButton)
    thisExp.addData('mouse_Instruc.midButton', mouse_Instruc.midButton)
    thisExp.addData('mouse_Instruc.rightButton', mouse_Instruc.rightButton)
    thisExp.addData('mouse_Instruc.time', mouse_Instruc.time)
    thisExp.addData('mouse_Instruc.clicked_name', mouse_Instruc.clicked_name)
    thisExp.nextEntry()
    # the Routine "baseline_Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ParagraphTyping" ---
    # create an object to store info about Routine ParagraphTyping
    ParagraphTyping = data.Routine(
        name='ParagraphTyping',
        components=[baseline_Paragraph, textbox_baseline_input, textClocktimer],
    )
    ParagraphTyping.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    textbox_baseline_input.reset()
    # store start times for ParagraphTyping
    ParagraphTyping.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    ParagraphTyping.tStart = globalClock.getTime(format='float')
    ParagraphTyping.status = STARTED
    thisExp.addData('ParagraphTyping.started', ParagraphTyping.tStart)
    ParagraphTyping.maxDuration = None
    # keep track of which components have finished
    ParagraphTypingComponents = ParagraphTyping.components
    for thisComponent in ParagraphTyping.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ParagraphTyping" ---
    thisExp.currentRoutine = ParagraphTyping
    ParagraphTyping.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *baseline_Paragraph* updates
        
        # if baseline_Paragraph is starting this frame...
        if baseline_Paragraph.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            baseline_Paragraph.frameNStart = frameN  # exact frame index
            baseline_Paragraph.tStart = t  # local t and not account for scr refresh
            baseline_Paragraph.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(baseline_Paragraph, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'baseline_Paragraph.started')
            # update status
            baseline_Paragraph.status = STARTED
            baseline_Paragraph.setAutoDraw(True)
        
        # if baseline_Paragraph is active this frame...
        if baseline_Paragraph.status == STARTED:
            # update params
            pass
        
        # if baseline_Paragraph is stopping this frame...
        if baseline_Paragraph.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > baseline_Paragraph.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                baseline_Paragraph.tStop = t  # not accounting for scr refresh
                baseline_Paragraph.tStopRefresh = tThisFlipGlobal  # on global time
                baseline_Paragraph.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'baseline_Paragraph.stopped')
                # update status
                baseline_Paragraph.status = FINISHED
                baseline_Paragraph.setAutoDraw(False)
        
        # *textbox_baseline_input* updates
        
        # if textbox_baseline_input is starting this frame...
        if textbox_baseline_input.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textbox_baseline_input.frameNStart = frameN  # exact frame index
            textbox_baseline_input.tStart = t  # local t and not account for scr refresh
            textbox_baseline_input.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textbox_baseline_input, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textbox_baseline_input.started')
            # update status
            textbox_baseline_input.status = STARTED
            textbox_baseline_input.setAutoDraw(True)
        
        # if textbox_baseline_input is active this frame...
        if textbox_baseline_input.status == STARTED:
            # update params
            pass
        
        # if textbox_baseline_input is stopping this frame...
        if textbox_baseline_input.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textbox_baseline_input.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                textbox_baseline_input.tStop = t  # not accounting for scr refresh
                textbox_baseline_input.tStopRefresh = tThisFlipGlobal  # on global time
                textbox_baseline_input.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox_baseline_input.stopped')
                # update status
                textbox_baseline_input.status = FINISHED
                textbox_baseline_input.setAutoDraw(False)
        
        # *textClocktimer* updates
        
        # if textClocktimer is starting this frame...
        if textClocktimer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textClocktimer.frameNStart = frameN  # exact frame index
            textClocktimer.tStart = t  # local t and not account for scr refresh
            textClocktimer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textClocktimer, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textClocktimer.started')
            # update status
            textClocktimer.status = STARTED
            textClocktimer.setAutoDraw(True)
        
        # if textClocktimer is active this frame...
        if textClocktimer.status == STARTED:
            # update params
            textClocktimer.setText(str(round(5-t)), log=False)
        
        # if textClocktimer is stopping this frame...
        if textClocktimer.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textClocktimer.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                textClocktimer.tStop = t  # not accounting for scr refresh
                textClocktimer.tStopRefresh = tThisFlipGlobal  # on global time
                textClocktimer.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textClocktimer.stopped')
                # update status
                textClocktimer.status = FINISHED
                textClocktimer.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=ParagraphTyping,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            ParagraphTyping.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if ParagraphTyping.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in ParagraphTyping.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ParagraphTyping" ---
    for thisComponent in ParagraphTyping.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for ParagraphTyping
    ParagraphTyping.tStop = globalClock.getTime(format='float')
    ParagraphTyping.tStopRefresh = tThisFlipGlobal
    thisExp.addData('ParagraphTyping.stopped', ParagraphTyping.tStop)
    thisExp.addData('textbox_baseline_input.text',textbox_baseline_input.text)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if ParagraphTyping.maxDurationReached:
        routineTimer.addTime(-ParagraphTyping.maxDuration)
    elif ParagraphTyping.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler2(
        name='trials',
        nReps=1, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('IntialTask.xlsx'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial in trials:
        trials.status = STARTED
        if hasattr(thisTrial, 'status'):
            thisTrial.status = STARTED
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "Task" ---
        # create an object to store info about Routine Task
        Task = data.Routine(
            name='Task',
            components=[text_Taskquestion, textbox_answer, key_respTask, TaskCounter],
        )
        Task.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        text_Taskquestion.setText(Question)
        textbox_answer.reset()
        # create starting attributes for key_respTask
        key_respTask.keys = []
        key_respTask.rt = []
        _key_respTask_allKeys = []
        TaskCounter.setText(" السؤال" + str(trials.thisN + 1) + " " ":" + "املأ الفراغ بتصريف الفعل الصحيح")
        # store start times for Task
        Task.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        Task.tStart = globalClock.getTime(format='float')
        Task.status = STARTED
        thisExp.addData('Task.started', Task.tStart)
        Task.maxDuration = None
        # keep track of which components have finished
        TaskComponents = Task.components
        for thisComponent in Task.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Task" ---
        thisExp.currentRoutine = Task
        Task.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrial, 'status') and thisTrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_Taskquestion* updates
            
            # if text_Taskquestion is starting this frame...
            if text_Taskquestion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_Taskquestion.frameNStart = frameN  # exact frame index
                text_Taskquestion.tStart = t  # local t and not account for scr refresh
                text_Taskquestion.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_Taskquestion, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_Taskquestion.started')
                # update status
                text_Taskquestion.status = STARTED
                text_Taskquestion.setAutoDraw(True)
            
            # if text_Taskquestion is active this frame...
            if text_Taskquestion.status == STARTED:
                # update params
                pass
            
            # *textbox_answer* updates
            
            # if textbox_answer is starting this frame...
            if textbox_answer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textbox_answer.frameNStart = frameN  # exact frame index
                textbox_answer.tStart = t  # local t and not account for scr refresh
                textbox_answer.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox_answer, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox_answer.started')
                # update status
                textbox_answer.status = STARTED
                textbox_answer.setAutoDraw(True)
            
            # if textbox_answer is active this frame...
            if textbox_answer.status == STARTED:
                # update params
                pass
            
            # *key_respTask* updates
            waitOnFlip = False
            
            # if key_respTask is starting this frame...
            if key_respTask.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_respTask.frameNStart = frameN  # exact frame index
                key_respTask.tStart = t  # local t and not account for scr refresh
                key_respTask.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_respTask, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_respTask.started')
                # update status
                key_respTask.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_respTask.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_respTask.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_respTask.status == STARTED and not waitOnFlip:
                theseKeys = key_respTask.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                _key_respTask_allKeys.extend(theseKeys)
                if len(_key_respTask_allKeys):
                    key_respTask.keys = _key_respTask_allKeys[-1].name  # just the last key pressed
                    key_respTask.rt = _key_respTask_allKeys[-1].rt
                    key_respTask.duration = _key_respTask_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *TaskCounter* updates
            
            # if TaskCounter is starting this frame...
            if TaskCounter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TaskCounter.frameNStart = frameN  # exact frame index
                TaskCounter.tStart = t  # local t and not account for scr refresh
                TaskCounter.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TaskCounter, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TaskCounter.started')
                # update status
                TaskCounter.status = STARTED
                TaskCounter.setAutoDraw(True)
            
            # if TaskCounter is active this frame...
            if TaskCounter.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=Task,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                Task.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if Task.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in Task.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Task" ---
        for thisComponent in Task.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for Task
        Task.tStop = globalClock.getTime(format='float')
        Task.tStopRefresh = tThisFlipGlobal
        thisExp.addData('Task.stopped', Task.tStop)
        trials.addData('textbox_answer.text',textbox_answer.text)
        # check responses
        if key_respTask.keys in ['', [], None]:  # No response was made
            key_respTask.keys = None
        trials.addData('key_respTask.keys',key_respTask.keys)
        if key_respTask.keys != None:  # we had a response
            trials.addData('key_respTask.rt', key_respTask.rt)
            trials.addData('key_respTask.duration', key_respTask.duration)
        # Run 'End Routine' code from code_correctanswer
        # 1. Grab the typed text and the correct answer
        # The .strip() function removes any accidental spaces the user typed before or after the word
        typed_text = textbox_answer.text.strip()
        expected_text = Correct_Answer.strip()
        
        # 2. Compare the two words
        if typed_text == expected_text:
            accuracy = 1  # 1 means Correct
        else:
            accuracy = 0  # 0 means Wrong
        
        # 3. Tell PsychoPy to save this score into the final data file
        thisExp.addData('Accuracy_Score', accuracy)
        # the Routine "Task" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisTrial as finished
        if hasattr(thisTrial, 'status'):
            thisTrial.status = FINISHED
        # if awaiting a pause, pause now
        if trials.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            trials.status = STARTED
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    trials.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "GoodbyeScreen" ---
    # create an object to store info about Routine GoodbyeScreen
    GoodbyeScreen = data.Routine(
        name='GoodbyeScreen',
        components=[text_Goodbye],
    )
    GoodbyeScreen.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for GoodbyeScreen
    GoodbyeScreen.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    GoodbyeScreen.tStart = globalClock.getTime(format='float')
    GoodbyeScreen.status = STARTED
    thisExp.addData('GoodbyeScreen.started', GoodbyeScreen.tStart)
    GoodbyeScreen.maxDuration = None
    # keep track of which components have finished
    GoodbyeScreenComponents = GoodbyeScreen.components
    for thisComponent in GoodbyeScreen.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "GoodbyeScreen" ---
    thisExp.currentRoutine = GoodbyeScreen
    GoodbyeScreen.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_Goodbye* updates
        
        # if text_Goodbye is starting this frame...
        if text_Goodbye.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_Goodbye.frameNStart = frameN  # exact frame index
            text_Goodbye.tStart = t  # local t and not account for scr refresh
            text_Goodbye.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_Goodbye, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_Goodbye.started')
            # update status
            text_Goodbye.status = STARTED
            text_Goodbye.setAutoDraw(True)
        
        # if text_Goodbye is active this frame...
        if text_Goodbye.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=GoodbyeScreen,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            GoodbyeScreen.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if GoodbyeScreen.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in GoodbyeScreen.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "GoodbyeScreen" ---
    for thisComponent in GoodbyeScreen.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for GoodbyeScreen
    GoodbyeScreen.tStop = globalClock.getTime(format='float')
    GoodbyeScreen.tStopRefresh = tThisFlipGlobal
    thisExp.addData('GoodbyeScreen.stopped', GoodbyeScreen.tStop)
    thisExp.nextEntry()
    # the Routine "GoodbyeScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    # stop any playback components
    if thisExp.currentRoutine is not None:
        for comp in thisExp.currentRoutine.getPlaybackComponents():
            comp.stop()
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
