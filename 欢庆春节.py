import copy

# 春节主题的主色调：柔和的红色和金色
Canvas = {
    "bg": "#FFF5E1",
    "insertbackground": "#8B0000",
    "highlightthickness": 0,
}

Frame = {
    "bg": "#FFE4B5",  
    "insertbackground": "#8B0000",
    "highlightthickness": 0,
}

Button = {
    "Information": {
        "normal": {"fill": "#8B0000"},
        "hover": {"fill": "#8B0000"},
        "active": {"fill": "#8B0000"},
    },
    "Rectangle": {
        "normal": {"fill": "#FF6347", "outline": "#CD5C5C"},
        "hover": {"fill": "#FFA07A", "outline": "#FF6347"},
        "active": {"fill": "#FF7F50", "outline": "#CD5C5C"},
    },
    "RoundedRectangle": {
        "normal": {"fill": "#FFFFFF", "outline": "#CD5C5C"},
        "hover": {"fill": "#FFC1C1", "outline": "#FF6347"},
        "active": {"fill": "#FFE4E1", "outline": "#CD5C5C"},
    }
}

CheckButton = copy.deepcopy(Button)

ToggleButton = {
    "Information": {
        "normal-off": {"fill": "#8B0000"},
        "hover-off": {"fill": "#8B0000"},
        "active-off": {"fill": "#8B0000"},
        "normal-on": {"fill": "#8B0000"},
        "hover-on": {"fill": "#8B0000"},
        "active-on": {"fill": "#8B0000"},
    },
    "Rectangle": {
        "normal-off": {"fill": "#FFFFFF", "outline": "#CD5C5C"},
        "hover-off": {"fill": "#FFC1C1", "outline": "#CD5C5C"},
        "active-off": {"fill": "#FFE4E1", "outline": "#CD5C5C"},
        "normal-on": {"fill": "#FF6347", "outline": "#FF6347"},
        "hover-on": {"fill": "#FF7F50", "outline": "#FF7F50"},
        "active-on": {"fill": "#CD5C5C", "outline": "#FF6347"},
    },
    "RoundedRectangle": {
        "normal-off": {"fill": "#FFFFFF", "outline": "#CD5C5C"},
        "hover-off": {"fill": "#FFC1C1", "outline": "#CD5C5C"},
        "active-off": {"fill": "#FFE4E1", "outline": "#CD5C5C"},
        "normal-on": {"fill": "#FF6347", "outline": "#FF6347"},
        "hover-on": {"fill": "#FF7F50", "outline": "#FF7F50"},
        "active-on": {"fill": "#CD5C5C", "outline": "#FF6347"},
    }
}

HighlightButton = {
    "Information": {
        "normal": {"fill": "#8B0000"},
        "hover": {"fill": "#A52A2A"},
        "active": {"fill": "#5C0000"},
    }
}

IconButton = copy.deepcopy(Button)

InputBox = {
    "Rectangle": {
        "normal": {"fill": "#FFE4B5", "outline": "#CD5C5C"},
        "hover": {"fill": "#FFEFD5", "outline": "#8B0000"},
        "active": {"fill": "#FFFFFF", "outline": "#FF6347"},
    },
    "RoundedRectangle.in": {
        "normal": {"fill": "#FFE4B5", "outline": "#E5E5E5"},
        "hover": {"fill": "#FFEFD5", "outline": "#E5E5E5"},
        "active": {"fill": "#FFFFFF", "outline": "#E5E5E5"},
    },
    "RoundedRectangle.out": {
        "normal": {"fill": "#868686", "outline": "#868686"},
        "hover": {"fill": "#868686", "outline": "#868686"},
        "active": {"fill": "#FF6347", "outline": "#FF6347"},
    },
    "SingleLineText": {
        "normal": {"fill": "#8B0000"},
        "hover": {"fill": "#8B0000"},
        "active": {"fill": "#8B0000"},
    }
}

Label = {
    "Information": {
        "normal": {"fill": "#8B0000"},
        "hover": {"fill": "#8B0000"},
    },
    "Rectangle": {
        "normal": {"fill": "#FFE4B5", "outline": "#CD5C5C"},
        "hover": {"fill": "#FFEFD5", "outline": "#CD5C5C"},
    },
    "RoundedRectangle": {
        "normal": {"fill": "#FFE4B5", "outline": "#CD5C5C"},
        "hover": {"fill": "#FFEFD5", "outline": "#CD5C5C"},
    }
}

OptionButton = copy.deepcopy(Button)

ProgressBar = {
    "Rectangle.in": {
        "normal": {"fill": "#FF6347", "outline": "#FF6347"},
        "hover": {"fill": "#FF7F50", "outline": "#FF7F50"},
    },
    "Rectangle.out": {
        "normal": {"fill": "#FFC1C1", "outline": "#CD5C5C"},
        "hover": {"fill": "#FFE4E1", "outline": "#8B0000"},
    },
    "SemicircularRectangle.in": {
        "normal": {"fill": "#FF6347", "outline": "#FF6347"},
        "hover": {"fill": "#FF7F50", "outline": "#FF7F50"},
    },
    "SemicircularRectangle.out": {
        "normal": {"fill": "#FFE4B5", "outline": "#CD5C5C"},
        "hover": {"fill": "#FFEFD5", "outline": "#CD5C5C"},
    }
}

RadioButton = {
    "Oval.in": {
        "normal": {"fill": "#FF6347", "outline": "#FF6347"},
        "hover": {"fill": "#FF7F50", "outline": "#FF7F50"},
        "active": {"fill": "#FF7F50", "outline": "#FF7F50"},
    },
    "Oval.out": {
        "normal": {"fill": "#FFFFFF", "outline": "#CD5C5C"},
        "hover": {"fill": "#FFC1C1", "outline": "#CD5C5C"},
        "active": {"fill": "#FFE4E1", "outline": "#CD5C5C"},
    },
    "Rectangle.in": {
        "normal": {"fill": "#FF6347", "outline": "#FF6347"},
        "hover": {"fill": "#FF7F50", "outline": "#FF7F50"},
        "active": {"fill": "#FF7F50", "outline": "#FF7F50"},
    },
    "Rectangle.out": {
        "normal": {"fill": "#FFFFFF", "outline": "#CD5C5C"},
        "hover": {"fill": "#FFC1C1", "outline": "#CD5C5C"},
        "active": {"fill": "#FFE4E1", "outline": "#CD5C5C"},
    }
}

SegmentedButton = copy.deepcopy(Label)

Slider = {
    "Oval.in": {
        "normal": {"fill": "#FF6347", "outline": "#FF6347"},
    },
    "Oval.out": {
        "normal": {"fill": "#FFFFFF", "outline": "#E8E8E8"},
    },
    "Rectangle.in": {
        "normal": {"fill": "#FF6347", "outline": "#FF6347"},
    },
    "Rectangle": {
        "normal": {"fill": "#FF6347", "outline": "#FF6347"},
        "hover": {"fill": "#CD5C5C", "outline": "#CD5C5C"},
        "active": {"fill": "#8B0000", "outline": "#8B0000"},
    },
    "Rectangle.out": {
        "normal": {"fill": "#FF7F50", "outline": "#FF7F50"},
    },
    "SemicircularRectangle.in": {
        "normal": {"fill": "#FF6347", "outline": "#FF6347"},
    },
    "SemicircularRectangle.out": {
        "normal": {"fill": "#FF7F50", "outline": "#FF7F50"},
    }
}

Switch = {
    "Oval": {
        "normal-off": {"fill": "#8B0000", "outline": "#8B0000"},
        "hover-off": {"fill": "#A52A2A", "outline": "#A52A2A"},
        "active-off": {"fill": "#5C0000", "outline": "#5C0000"},
        "normal-on": {"fill": "#FFFFFF", "outline": "#FFFFFF"},
        "hover-on": {"fill": "#FFFFFF", "outline": "#FFFFFF"},
        "active-on": {"fill": "#FFFFFF", "outline": "#FFFFFF"},
    },
    "Rectangle.in": {
        "normal-off": {"fill": "#8B0000", "outline": "#8B0000"},
        "hover-off": {"fill": "#A52A2A", "outline": "#A52A2A"},
        "active-off": {"fill": "#5C0000", "outline": "#5C0000"},
        "normal-on": {"fill": "#FFFFFF", "outline": "#FFFFFF"},
        "hover-on": {"fill": "#FFFFFF", "outline": "#FFFFFF"},
        "active-on": {"fill": "#FFFFFF", "outline": "#FFFFFF"},
    },
    "Rectangle.out": {
        "normal-off": {"fill": "#FFF5E1", "outline": "#B8B8B9"},
        "hover-off": {"fill": "#FFE4B5", "outline": "#858687"},
        "active-off": {"fill": "#FFE4E1", "outline": "#848586"},
        "normal-on": {"fill": "#FF6347", "outline": "#FF6347"},
        "hover-on": {"fill": "#FF7F50", "outline": "#FF7F50"},
        "active-on": {"fill": "#CD5C5C", "outline": "#2072B9"},
    },
    "SemicircularRectangle": {
        "normal-off": {"fill": "#FFF5E1", "outline": "#B8B8B9"},
        "hover-off": {"fill": "#FFE4B5", "outline": "#858687"},
        "active-off": {"fill": "#FFE4E1", "outline": "#848586"},
        "normal-on": {"fill": "#FF6347", "outline": "#FF6347"},
        "hover-on": {"fill": "#FF7F50", "outline": "#FF7F50"},
        "active-on": {"fill": "#CD5C5C", "outline": "#2072B9"},
    }
}

Text = {
    "Information": {
        "normal": {"fill": "#8B0000"},
    }
}

UnderlineButton = {
    "Information": {
        "normal": {"fill": "#8B0000"},
        "hover": {"fill": "blue"},
        "active": {"fill": "purple"},
    }
}

_AuxiliaryLabel = copy.deepcopy(Label)
del _AuxiliaryLabel["RoundedRectangle"]
_AuxiliaryLabel["HalfRoundedRectangle"] = Label["RoundedRectangle"]

_AuxiliaryButton = copy.deepcopy(Button)
del _AuxiliaryButton["RoundedRectangle"]
_AuxiliaryButton["HalfRoundedRectangle"] = Button["RoundedRectangle"]

_AuxiliaryInputBox = copy.deepcopy(InputBox)
del _AuxiliaryInputBox["RoundedRectangle.in"]
del _AuxiliaryInputBox["RoundedRectangle.out"]
_AuxiliaryInputBox["HalfRoundedRectangle.in"] = InputBox["RoundedRectangle.in"]
_AuxiliaryInputBox["HalfRoundedRectangle.out"] = InputBox["RoundedRectangle.out"]
