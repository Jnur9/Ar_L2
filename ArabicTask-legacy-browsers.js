/******************* 
 * Arabictask *
 *******************/


// store info about the experiment session:
let expName = 'ArabicTask';  // from the Builder filename that created this script
let expInfo = {
    'participant': util.randint(10000, 99999),
    'Language Proficiency': ["Professional Native", "Professional L2"],
};
let PILOTING = util.getUrlParameters().has('__pilotToken');

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: false,
  color: new util.Color('#beb0df'),
  units: 'height',
  waitBlanking: true,
  backgroundImage: 'background.jpg',
  backgroundFit: 'contain',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(WelcomeScreenRoutineBegin());
flowScheduler.add(WelcomeScreenRoutineEachFrame());
flowScheduler.add(WelcomeScreenRoutineEnd());
flowScheduler.add(baseline_InstructionsRoutineBegin());
flowScheduler.add(baseline_InstructionsRoutineEachFrame());
flowScheduler.add(baseline_InstructionsRoutineEnd());
flowScheduler.add(ParagraphTypingRoutineBegin());
flowScheduler.add(ParagraphTypingRoutineEachFrame());
flowScheduler.add(ParagraphTypingRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);


flowScheduler.add(GoodbyeScreenRoutineBegin());
flowScheduler.add(GoodbyeScreenRoutineEachFrame());
flowScheduler.add(GoodbyeScreenRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'IntialTask.xlsx', 'path': 'IntialTask.xlsx'},
    {'name': 'background.jpg', 'path': 'background.jpg'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2026.1.3';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var WelcomeScreenClock;
var textWelcome;
var polygonStart;
var text_ButtonStart;
var mouseStart;
var baseline_InstructionsClock;
var baseline_typing;
var polygonBaseline;
var textBaseline_Start;
var mouse_Instruc;
var ParagraphTypingClock;
var baseline_Paragraph;
var textbox_baseline_input;
var textClocktimer;
var TaskClock;
var text_Taskquestion;
var textbox_answer;
var key_respTask;
var TaskCounter;
var GoodbyeScreenClock;
var text_Goodbye;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "WelcomeScreen"
  WelcomeScreenClock = new util.Clock();
  // Grab the whole web page element
  var elem = document.documentElement;
  
  // Ask the browser to enter full screen
  if (elem.requestFullscreen) {
    elem.requestFullscreen();
  } else if (elem.webkitRequestFullscreen) { /* Safari Support */
    elem.webkitRequestFullscreen();
  } else if (elem.msRequestFullscreen) { /* Edge/IE Support */
    elem.msRequestFullscreen();
  }
  // Create a global background image object
  window.global_bg = new visual.ImageStim({
      win: psychoJS.window,
      name: 'global_bg',
      image: 'background.jpg',
      units: 'norm',
      size: [2, 2], // Stretches to cover 100% of the screen
      depth: 100    // Pushes it to the absolute back layer
  });
  
  // Command PsychoJS to automatically draw it on every frame forever
  window.global_bg.setAutoDraw(true);
  textWelcome = new visual.TextStim({
    win: psychoJS.window,
    name: 'textWelcome',
    text: 'Welcome to the Arabic Fluency Task\nمرحبا بك في اختبار إتقان اللغة العربية',
    font: 'Broadway',
    units: 'height', 
    pos: [0, 0.1], draggable: false, height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'Arabic',
    color: new util.Color('#62547c'),  opacity: undefined,
    depth: -2.0 
  });
  
  polygonStart = new visual.ShapeStim({
    win: psychoJS.window, name: 'polygonStart', 
    vertices: [[(- 0.35), 0.15], [0.35, 0.15], [0.365, 0.149], [0.379, 0.147], [0.394, 0.144], [0.407, 0.139], [0.421, 0.132], [0.433, 0.125], [0.445, 0.116], [0.456, 0.106], [0.466, 0.095], [0.475, 0.083], [0.482, 0.071], [0.489, 0.057], [0.494, 0.044], [0.497, 0.029], [0.499, 0.015], [0.5, 0], [0.499, (- 0.015)], [0.497, (- 0.029)], [0.494, (- 0.044)], [0.489, (- 0.057)], [0.482, (- 0.071)], [0.475, (- 0.083)], [0.466, (- 0.095)], [0.456, (- 0.106)], [0.445, (- 0.116)], [0.433, (- 0.125)], [0.421, (- 0.132)], [0.407, (- 0.139)], [0.394, (- 0.144)], [0.379, (- 0.147)], [0.365, (- 0.149)], [0.35, (- 0.15)], [(- 0.35), (- 0.15)], [(- 0.365), (- 0.149)], [(- 0.379), (- 0.147)], [(- 0.394), (- 0.144)], [(- 0.407), (- 0.139)], [(- 0.421), (- 0.132)], [(- 0.433), (- 0.125)], [(- 0.445), (- 0.116)], [(- 0.456), (- 0.106)], [(- 0.466), (- 0.095)], [(- 0.475), (- 0.083)], [(- 0.482), (- 0.071)], [(- 0.489), (- 0.057)], [(- 0.494), (- 0.044)], [(- 0.497), (- 0.029)], [(- 0.499), (- 0.015)], [(- 0.5), 0], [(- 0.499), 0.015], [(- 0.497), 0.029], [(- 0.494), 0.044], [(- 0.489), 0.057], [(- 0.482), 0.071], [(- 0.475), 0.083], [(- 0.466), 0.095], [(- 0.456), 0.106], [(- 0.445), 0.116], [(- 0.433), 0.125], [(- 0.421), 0.132], [(- 0.407), 0.139], [(- 0.394), 0.144], [(- 0.379), 0.147], [(- 0.365), 0.149]], size: [0.35, 0.35],
    ori: 0.0, 
    pos: [0, (- 0.3)], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 2.0, 
    lineColor: new util.Color('#b6a7da'), 
    fillColor: new util.Color('#b6a7da'), 
    colorSpace: 'hex', 
    opacity: undefined, 
    depth: -3, 
    interpolate: false, 
  });
  
  text_ButtonStart = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_ButtonStart',
    text: 'START\nإبدا',
    font: 'Broadway',
    units: 'height', 
    pos: [0, (- 0.3)], draggable: false, height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'Arabic',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  mouseStart = new core.Mouse({
    win: psychoJS.window,
  });
  mouseStart.mouseClock = new util.Clock();
  // Initialize components for Routine "baseline_Instructions"
  baseline_InstructionsClock = new util.Clock();
  baseline_typing = new visual.TextStim({
    win: psychoJS.window,
    name: 'baseline_typing',
    text: 'A paragraph will appear after you hit start! trying to type it as fast and accurately as you can. You will have 60 seconds to finish.\n\nسيظهر مقال بعد الضغط على زر البدء؛ حاول كتابته بأقصى سرعة ودقة ممكنتين. سيكون لديك ستون ثانية لإتمام المهمة',
    font: 'Bahnschrift',
    units: 'height', 
    pos: [0, 0.1], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'Arabic',
    color: new util.Color('#62547c'),  opacity: undefined,
    depth: 0.0 
  });
  
  polygonBaseline = new visual.ShapeStim({
    win: psychoJS.window, name: 'polygonBaseline', 
    vertices: [[(- 0.35), 0.15], [0.35, 0.15], [0.365, 0.149], [0.379, 0.147], [0.394, 0.144], [0.407, 0.139], [0.421, 0.132], [0.433, 0.125], [0.445, 0.116], [0.456, 0.106], [0.466, 0.095], [0.475, 0.083], [0.482, 0.071], [0.489, 0.057], [0.494, 0.044], [0.497, 0.029], [0.499, 0.015], [0.5, 0], [0.499, (- 0.015)], [0.497, (- 0.029)], [0.494, (- 0.044)], [0.489, (- 0.057)], [0.482, (- 0.071)], [0.475, (- 0.083)], [0.466, (- 0.095)], [0.456, (- 0.106)], [0.445, (- 0.116)], [0.433, (- 0.125)], [0.421, (- 0.132)], [0.407, (- 0.139)], [0.394, (- 0.144)], [0.379, (- 0.147)], [0.365, (- 0.149)], [0.35, (- 0.15)], [(- 0.35), (- 0.15)], [(- 0.365), (- 0.149)], [(- 0.379), (- 0.147)], [(- 0.394), (- 0.144)], [(- 0.407), (- 0.139)], [(- 0.421), (- 0.132)], [(- 0.433), (- 0.125)], [(- 0.445), (- 0.116)], [(- 0.456), (- 0.106)], [(- 0.466), (- 0.095)], [(- 0.475), (- 0.083)], [(- 0.482), (- 0.071)], [(- 0.489), (- 0.057)], [(- 0.494), (- 0.044)], [(- 0.497), (- 0.029)], [(- 0.499), (- 0.015)], [(- 0.5), 0], [(- 0.499), 0.015], [(- 0.497), 0.029], [(- 0.494), 0.044], [(- 0.489), 0.057], [(- 0.482), 0.071], [(- 0.475), 0.083], [(- 0.466), 0.095], [(- 0.456), 0.106], [(- 0.445), 0.116], [(- 0.433), 0.125], [(- 0.421), 0.132], [(- 0.407), 0.139], [(- 0.394), 0.144], [(- 0.379), 0.147], [(- 0.365), 0.149]], size: [0.35, 0.35],
    ori: 0.0, 
    pos: [0, (- 0.3)], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 2.0, 
    lineColor: new util.Color('#b6a7da'), 
    fillColor: new util.Color('#b6a7da'), 
    colorSpace: 'hex', 
    opacity: undefined, 
    depth: -1, 
    interpolate: true, 
  });
  
  textBaseline_Start = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBaseline_Start',
    text: 'Begin\nإبدا',
    font: 'Broadway',
    units: 'height', 
    pos: [0, (- 0.3)], draggable: false, height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'Arabic',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  mouse_Instruc = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_Instruc.mouseClock = new util.Clock();
  // Initialize components for Routine "ParagraphTyping"
  ParagraphTypingClock = new util.Clock();
  baseline_Paragraph = new visual.TextStim({
    win: psychoJS.window,
    name: 'baseline_Paragraph',
    text: 'تعد القراءة غذاء للعقل والروح. فهي ليست مجرد هواية نقضي بها اوقات فراغنا بل مفتاح يفتح لنا أبواب المعرفة. من خلال صفحات الكتب نسافر عبر الزمن لنتعرف على حضارات الأمم السابقة ونطوف حول العالم دون أن نتحرك من أماكننا. تتجلى أهمية القراءة في توسيع مدارك الإنسان وتطوير مهارات التفكير لديه كما تزيد من حصيلته اللغوية وتقدم له حلولا مبتكرة للمشكلات.',
    font: 'Bahnschrift',
    units: 'height', 
    pos: [0, 0.2], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'Arabic',
    color: new util.Color('#62547c'),  opacity: undefined,
    depth: 0.0 
  });
  
  textbox_baseline_input = new visual.TextBox({
    win: psychoJS.window,
    name: 'textbox_baseline_input',
    text: '',
    placeholder: 'Type here... اكتب هنا...',
    font: 'Bahnschrift',
    pos: [0, (- 0.3)], 
    draggable: false,
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [1, 0.35],  units: 'height', 
    ori: 0.0,
    color: '#62547c', colorSpace: 'rgb',
    fillColor: 'white', borderColor: undefined,
    languageStyle: 'Arabic',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  textClocktimer = new visual.TextStim({
    win: psychoJS.window,
    name: 'textClocktimer',
    text: '',
    font: 'Broadway',
    units: undefined, 
    pos: [0.6, 0.4], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('darkred'),  opacity: undefined,
    depth: -2.0 
  });
  
  // Initialize components for Routine "Task"
  TaskClock = new util.Clock();
  text_Taskquestion = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_Taskquestion',
    text: '',
    font: 'Broadway',
    units: 'height', 
    pos: [0, 0.2], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'Arabic',
    color: new util.Color('#62547c'),  opacity: undefined,
    depth: 0.0 
  });
  
  textbox_answer = new visual.TextBox({
    win: psychoJS.window,
    name: 'textbox_answer',
    text: '',
    placeholder: '...',
    font: 'Broadway',
    pos: [0, 0], 
    draggable: false,
    letterHeight: 0.05,
    lineSpacing: 1.0,
    size: [0.35, 0.1],  units: 'height', 
    ori: 0.0,
    color: '#62547c', colorSpace: 'rgb',
    fillColor: 'white', borderColor: undefined,
    languageStyle: 'Arabic',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  key_respTask = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  TaskCounter = new visual.TextStim({
    win: psychoJS.window,
    name: 'TaskCounter',
    text: '',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0.4], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('#62547c'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "GoodbyeScreen"
  GoodbyeScreenClock = new util.Clock();
  text_Goodbye = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_Goodbye',
    text: 'Thank you for Participating!\n\nPlease wait while we save your results...',
    font: 'Broadway',
    units: 'height', 
    pos: [0, 0], draggable: false, height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('#62547c'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var routineForceEnded;
var WelcomeScreenMaxDurationReached;
var gotValidClick;
var WelcomeScreenMaxDuration;
var WelcomeScreenComponents;
function WelcomeScreenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'WelcomeScreen' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    WelcomeScreenClock.reset();
    routineTimer.reset();
    WelcomeScreenMaxDurationReached = false;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouseStart
    mouseStart.clicked_name = [];
    gotValidClick = false; // until a click is received
    psychoJS.experiment.addData('WelcomeScreen.started', globalClock.getTime());
    WelcomeScreenMaxDuration = null
    // keep track of which components have finished
    WelcomeScreenComponents = [];
    WelcomeScreenComponents.push(textWelcome);
    WelcomeScreenComponents.push(polygonStart);
    WelcomeScreenComponents.push(text_ButtonStart);
    WelcomeScreenComponents.push(mouseStart);
    
    WelcomeScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var prevButtonState;
var _mouseButtons;
function WelcomeScreenRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'WelcomeScreen' ---
    // get current time
    t = WelcomeScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *textWelcome* updates
    if (t >= 0.0 && textWelcome.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textWelcome.tStart = t;  // (not accounting for frame time here)
      textWelcome.frameNStart = frameN;  // exact frame index
      
      textWelcome.setAutoDraw(true);
    }
    
    
    // if textWelcome is active this frame...
    if (textWelcome.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *polygonStart* updates
    if (t >= 0.0 && polygonStart.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygonStart.tStart = t;  // (not accounting for frame time here)
      polygonStart.frameNStart = frameN;  // exact frame index
      
      polygonStart.setAutoDraw(true);
    }
    
    
    // if polygonStart is active this frame...
    if (polygonStart.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *text_ButtonStart* updates
    if (t >= 0.0 && text_ButtonStart.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_ButtonStart.tStart = t;  // (not accounting for frame time here)
      text_ButtonStart.frameNStart = frameN;  // exact frame index
      
      text_ButtonStart.setAutoDraw(true);
    }
    
    
    // if text_ButtonStart is active this frame...
    if (text_ButtonStart.status === PsychoJS.Status.STARTED) {
    }
    
    // *mouseStart* updates
    if (t >= 0.0 && mouseStart.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouseStart.tStart = t;  // (not accounting for frame time here)
      mouseStart.frameNStart = frameN;  // exact frame index
      
      mouseStart.status = PsychoJS.Status.STARTED;
      mouseStart.mouseClock.reset();
      prevButtonState = mouseStart.getPressed();  // if button is down already this ISN'T a new click
    }
    
    // if mouseStart is active this frame...
    if (mouseStart.status === PsychoJS.Status.STARTED) {
      _mouseButtons = mouseStart.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          mouseStart.clickableObjects = eval(polygonStart)
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(mouseStart.clickableObjects)) {
              mouseStart.clickableObjects = [mouseStart.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of mouseStart.clickableObjects) {
              if (obj.contains(mouseStart)) {
                  gotValidClick = true;
                  mouseStart.clicked_name.push(obj.name);
              }
          }
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          mouseStart.clickableObjects = eval(polygonStart)
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(mouseStart.clickableObjects)) {
              mouseStart.clickableObjects = [mouseStart.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of mouseStart.clickableObjects) {
              if (obj.contains(mouseStart)) {
                  gotValidClick = true;
                  mouseStart.clicked_name.push(obj.name);
              }
          }
          // end routine on response
          continueRoutine = false;
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    WelcomeScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function WelcomeScreenRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'WelcomeScreen' ---
    WelcomeScreenComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('WelcomeScreen.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    // the Routine "WelcomeScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var baseline_InstructionsMaxDurationReached;
var baseline_InstructionsMaxDuration;
var baseline_InstructionsComponents;
function baseline_InstructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'baseline_Instructions' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    baseline_InstructionsClock.reset();
    routineTimer.reset();
    baseline_InstructionsMaxDurationReached = false;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse_Instruc
    // current position of the mouse:
    mouse_Instruc.x = [];
    mouse_Instruc.y = [];
    mouse_Instruc.leftButton = [];
    mouse_Instruc.midButton = [];
    mouse_Instruc.rightButton = [];
    mouse_Instruc.time = [];
    mouse_Instruc.clicked_name = [];
    gotValidClick = false; // until a click is received
    psychoJS.experiment.addData('baseline_Instructions.started', globalClock.getTime());
    baseline_InstructionsMaxDuration = null
    // keep track of which components have finished
    baseline_InstructionsComponents = [];
    baseline_InstructionsComponents.push(baseline_typing);
    baseline_InstructionsComponents.push(polygonBaseline);
    baseline_InstructionsComponents.push(textBaseline_Start);
    baseline_InstructionsComponents.push(mouse_Instruc);
    
    baseline_InstructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var _mouseXYs;
function baseline_InstructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'baseline_Instructions' ---
    // get current time
    t = baseline_InstructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *baseline_typing* updates
    if (t >= 0.0 && baseline_typing.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      baseline_typing.tStart = t;  // (not accounting for frame time here)
      baseline_typing.frameNStart = frameN;  // exact frame index
      
      baseline_typing.setAutoDraw(true);
    }
    
    
    // if baseline_typing is active this frame...
    if (baseline_typing.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *polygonBaseline* updates
    if (t >= 0.0 && polygonBaseline.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygonBaseline.tStart = t;  // (not accounting for frame time here)
      polygonBaseline.frameNStart = frameN;  // exact frame index
      
      polygonBaseline.setAutoDraw(true);
    }
    
    
    // if polygonBaseline is active this frame...
    if (polygonBaseline.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *textBaseline_Start* updates
    if (t >= 0.0 && textBaseline_Start.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textBaseline_Start.tStart = t;  // (not accounting for frame time here)
      textBaseline_Start.frameNStart = frameN;  // exact frame index
      
      textBaseline_Start.setAutoDraw(true);
    }
    
    
    // if textBaseline_Start is active this frame...
    if (textBaseline_Start.status === PsychoJS.Status.STARTED) {
    }
    
    // *mouse_Instruc* updates
    if (t >= 0.0 && mouse_Instruc.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_Instruc.tStart = t;  // (not accounting for frame time here)
      mouse_Instruc.frameNStart = frameN;  // exact frame index
      
      mouse_Instruc.status = PsychoJS.Status.STARTED;
      mouse_Instruc.mouseClock.reset();
      prevButtonState = mouse_Instruc.getPressed();  // if button is down already this ISN'T a new click
    }
    
    // if mouse_Instruc is active this frame...
    if (mouse_Instruc.status === PsychoJS.Status.STARTED) {
      _mouseButtons = mouse_Instruc.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          mouse_Instruc.clickableObjects = eval(polygonBaseline)
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(mouse_Instruc.clickableObjects)) {
              mouse_Instruc.clickableObjects = [mouse_Instruc.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of mouse_Instruc.clickableObjects) {
              if (obj.contains(mouse_Instruc)) {
                  gotValidClick = true;
                  mouse_Instruc.clicked_name.push(obj.name);
              }
          }
          if (!gotValidClick) {
              mouse_Instruc.clicked_name.push(null);
          }
          _mouseXYs = mouse_Instruc.getPos();
          mouse_Instruc.x.push(_mouseXYs[0]);
          mouse_Instruc.y.push(_mouseXYs[1]);
          mouse_Instruc.leftButton.push(_mouseButtons[0]);
          mouse_Instruc.midButton.push(_mouseButtons[1]);
          mouse_Instruc.rightButton.push(_mouseButtons[2]);
          mouse_Instruc.time.push(mouse_Instruc.mouseClock.getTime());
          // end routine on response
          continueRoutine = false;
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    baseline_InstructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function baseline_InstructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'baseline_Instructions' ---
    baseline_InstructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('baseline_Instructions.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('mouse_Instruc.x', mouse_Instruc.x);
    psychoJS.experiment.addData('mouse_Instruc.y', mouse_Instruc.y);
    psychoJS.experiment.addData('mouse_Instruc.leftButton', mouse_Instruc.leftButton);
    psychoJS.experiment.addData('mouse_Instruc.midButton', mouse_Instruc.midButton);
    psychoJS.experiment.addData('mouse_Instruc.rightButton', mouse_Instruc.rightButton);
    psychoJS.experiment.addData('mouse_Instruc.time', mouse_Instruc.time);
    psychoJS.experiment.addData('mouse_Instruc.clicked_name', mouse_Instruc.clicked_name);
    
    // the Routine "baseline_Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var ParagraphTypingMaxDurationReached;
var ParagraphTypingMaxDuration;
var ParagraphTypingComponents;
function ParagraphTypingRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ParagraphTyping' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    ParagraphTypingClock.reset(routineTimer.getTime());
    routineTimer.add(5.000000);
    ParagraphTypingMaxDurationReached = false;
    // update component parameters for each repeat
    textbox_baseline_input.setText('');
    textbox_baseline_input.refresh();
    psychoJS.experiment.addData('ParagraphTyping.started', globalClock.getTime());
    ParagraphTypingMaxDuration = null
    // keep track of which components have finished
    ParagraphTypingComponents = [];
    ParagraphTypingComponents.push(baseline_Paragraph);
    ParagraphTypingComponents.push(textbox_baseline_input);
    ParagraphTypingComponents.push(textClocktimer);
    
    ParagraphTypingComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function ParagraphTypingRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ParagraphTyping' ---
    // get current time
    t = ParagraphTypingClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *baseline_Paragraph* updates
    if (t >= 0.0 && baseline_Paragraph.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      baseline_Paragraph.tStart = t;  // (not accounting for frame time here)
      baseline_Paragraph.frameNStart = frameN;  // exact frame index
      
      baseline_Paragraph.setAutoDraw(true);
    }
    
    
    // if baseline_Paragraph is active this frame...
    if (baseline_Paragraph.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (baseline_Paragraph.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      baseline_Paragraph.tStop = t;  // not accounting for scr refresh
      baseline_Paragraph.frameNStop = frameN;  // exact frame index
      // update status
      baseline_Paragraph.status = PsychoJS.Status.FINISHED;
      baseline_Paragraph.setAutoDraw(false);
    }
    
    
    // *textbox_baseline_input* updates
    if (t >= 0.0 && textbox_baseline_input.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textbox_baseline_input.tStart = t;  // (not accounting for frame time here)
      textbox_baseline_input.frameNStart = frameN;  // exact frame index
      
      textbox_baseline_input.setAutoDraw(true);
    }
    
    
    // if textbox_baseline_input is active this frame...
    if (textbox_baseline_input.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (textbox_baseline_input.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      textbox_baseline_input.tStop = t;  // not accounting for scr refresh
      textbox_baseline_input.frameNStop = frameN;  // exact frame index
      // update status
      textbox_baseline_input.status = PsychoJS.Status.FINISHED;
      textbox_baseline_input.setAutoDraw(false);
    }
    
    
    // *textClocktimer* updates
    if (t >= 0.0 && textClocktimer.status === PsychoJS.Status.NOT_STARTED) {
      // update params
      textClocktimer.setText(util.round((5 - t)).toString(), false);
      // keep track of start time/frame for later
      textClocktimer.tStart = t;  // (not accounting for frame time here)
      textClocktimer.frameNStart = frameN;  // exact frame index
      
      textClocktimer.setAutoDraw(true);
    }
    
    
    // if textClocktimer is active this frame...
    if (textClocktimer.status === PsychoJS.Status.STARTED) {
      // update params
      textClocktimer.setText(util.round((5 - t)).toString(), false);
    }
    
    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (textClocktimer.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      textClocktimer.tStop = t;  // not accounting for scr refresh
      textClocktimer.frameNStop = frameN;  // exact frame index
      // update status
      textClocktimer.status = PsychoJS.Status.FINISHED;
      textClocktimer.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    ParagraphTypingComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ParagraphTypingRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ParagraphTyping' ---
    ParagraphTypingComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('ParagraphTyping.stopped', globalClock.getTime());
    psychoJS.experiment.addData('textbox_baseline_input.text',textbox_baseline_input.text)
    if (routineForceEnded) {
        routineTimer.reset();} else if (ParagraphTypingMaxDurationReached) {
        ParagraphTypingClock.add(ParagraphTypingMaxDuration);
    } else {
        ParagraphTypingClock.add(5.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'IntialTask.xlsx',
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials.forEach(function() {
      snapshot = trials.getSnapshot();
    
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(TaskRoutineBegin(snapshot));
      trialsLoopScheduler.add(TaskRoutineEachFrame());
      trialsLoopScheduler.add(TaskRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var TaskMaxDurationReached;
var _key_respTask_allKeys;
var TaskMaxDuration;
var TaskComponents;
function TaskRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Task' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    TaskClock.reset();
    routineTimer.reset();
    TaskMaxDurationReached = false;
    // update component parameters for each repeat
    text_Taskquestion.setText(Question);
    textbox_answer.setText('');
    textbox_answer.refresh();
    key_respTask.keys = undefined;
    key_respTask.rt = undefined;
    _key_respTask_allKeys = [];
    TaskCounter.setText((((" \u0627\u0644\u0633\u0624\u0627\u0644" + (trials.thisN + 1).toString()) + " :") + "\u0627\u0645\u0644\u0623 \u0627\u0644\u0641\u0631\u0627\u063a \u0628\u062a\u0635\u0631\u064a\u0641 \u0627\u0644\u0641\u0639\u0644 \u0627\u0644\u0635\u062d\u064a\u062d"));
    psychoJS.experiment.addData('Task.started', globalClock.getTime());
    TaskMaxDuration = null
    // keep track of which components have finished
    TaskComponents = [];
    TaskComponents.push(text_Taskquestion);
    TaskComponents.push(textbox_answer);
    TaskComponents.push(key_respTask);
    TaskComponents.push(TaskCounter);
    
    TaskComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function TaskRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Task' ---
    // get current time
    t = TaskClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_Taskquestion* updates
    if (t >= 0.0 && text_Taskquestion.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_Taskquestion.tStart = t;  // (not accounting for frame time here)
      text_Taskquestion.frameNStart = frameN;  // exact frame index
      
      text_Taskquestion.setAutoDraw(true);
    }
    
    
    // if text_Taskquestion is active this frame...
    if (text_Taskquestion.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *textbox_answer* updates
    if (t >= 0.0 && textbox_answer.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textbox_answer.tStart = t;  // (not accounting for frame time here)
      textbox_answer.frameNStart = frameN;  // exact frame index
      
      textbox_answer.setAutoDraw(true);
    }
    
    
    // if textbox_answer is active this frame...
    if (textbox_answer.status === PsychoJS.Status.STARTED) {
    }
    
    
    // *key_respTask* updates
    if (t >= 0.0 && key_respTask.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_respTask.tStart = t;  // (not accounting for frame time here)
      key_respTask.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_respTask.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_respTask.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_respTask.clearEvents(); });
    }
    
    // if key_respTask is active this frame...
    if (key_respTask.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_respTask.getKeys({
        keyList: typeof 'return' === 'string' ? ['return'] : 'return', 
        waitRelease: false
      });
      _key_respTask_allKeys = _key_respTask_allKeys.concat(theseKeys);
      if (_key_respTask_allKeys.length > 0) {
        key_respTask.keys = _key_respTask_allKeys[_key_respTask_allKeys.length - 1].name;  // just the last key pressed
        key_respTask.rt = _key_respTask_allKeys[_key_respTask_allKeys.length - 1].rt;
        key_respTask.duration = _key_respTask_allKeys[_key_respTask_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *TaskCounter* updates
    if (t >= 0.0 && TaskCounter.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TaskCounter.tStart = t;  // (not accounting for frame time here)
      TaskCounter.frameNStart = frameN;  // exact frame index
      
      TaskCounter.setAutoDraw(true);
    }
    
    
    // if TaskCounter is active this frame...
    if (TaskCounter.status === PsychoJS.Status.STARTED) {
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    TaskComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var typed_text;
var expected_text;
var accuracy;
function TaskRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Task' ---
    TaskComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Task.stopped', globalClock.getTime());
    psychoJS.experiment.addData('textbox_answer.text',textbox_answer.text)
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_respTask.corr, level);
    }
    psychoJS.experiment.addData('key_respTask.keys', key_respTask.keys);
    if (typeof key_respTask.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_respTask.rt', key_respTask.rt);
        psychoJS.experiment.addData('key_respTask.duration', key_respTask.duration);
        routineTimer.reset();
        }
    
    key_respTask.stop();
    // Run 'End Routine' code from code_correctanswer
    typed_text = textbox_answer.text.trim();
    expected_text = Correct_Answer.trim();
    if ((typed_text === expected_text)) {
        accuracy = 1;
    } else {
        accuracy = 0;
    }
    psychoJS.experiment.addData("Accuracy_Score", accuracy);
    
    // the Routine "Task" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var GoodbyeScreenMaxDurationReached;
var GoodbyeScreenMaxDuration;
var GoodbyeScreenComponents;
function GoodbyeScreenRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'GoodbyeScreen' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    GoodbyeScreenClock.reset();
    routineTimer.reset();
    GoodbyeScreenMaxDurationReached = false;
    // update component parameters for each repeat
    // Disable downloading results to browser
    psychoJS._saveResults = 0;
    
    // Generate filename for results
    let filename = psychoJS._experiment._experimentName + '_' + psychoJS._experiment._datetime + '.csv';
    
    // Extract data object from experiment
    let dataObj = psychoJS._experiment._trialsData;
    
    // Convert data object to CSV
    let data = [Object.keys(dataObj[0])].concat(dataObj).map(it => {
      return Object.values(it).toString()
    }).join('\n')
    
    // Add the UTF-8 BOM (\uFEFF) to the very beginning of the file
    //let data = '\uFEFF' + csvString;
    
    // Send data to OSF via DataPipe
    console.log('Saving data...');
    fetch('https://pipe.jspsych.org/api/data', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Accept: '*/*',
      },
      body: JSON.stringify({
        experimentID: 'RKpwU2zVcqiA', // * UPDATE WITH YOUR DATAPIPE EXPERIMENT ID *
        filename: filename,
        data: data,
      }),
    }).then(response => response.json()).then(data => {
      // Log response and force experiment end
      console.log(data);
      quitPsychoJS();
    })
    psychoJS.experiment.addData('GoodbyeScreen.started', globalClock.getTime());
    GoodbyeScreenMaxDuration = null
    // keep track of which components have finished
    GoodbyeScreenComponents = [];
    GoodbyeScreenComponents.push(text_Goodbye);
    
    GoodbyeScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function GoodbyeScreenRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'GoodbyeScreen' ---
    // get current time
    t = GoodbyeScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_Goodbye* updates
    if (t >= 0.0 && text_Goodbye.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_Goodbye.tStart = t;  // (not accounting for frame time here)
      text_Goodbye.frameNStart = frameN;  // exact frame index
      
      text_Goodbye.setAutoDraw(true);
    }
    
    
    // if text_Goodbye is active this frame...
    if (text_Goodbye.status === PsychoJS.Status.STARTED) {
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    GoodbyeScreenComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function GoodbyeScreenRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'GoodbyeScreen' ---
    GoodbyeScreenComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('GoodbyeScreen.stopped', globalClock.getTime());
    // the Routine "GoodbyeScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
