import copy

# 端午节主题的主色调：绿色和棕色
Canvas = {
    "bg": "#E0F7E9",
    "insertbackground": "#2E7D32",
    "highlightthickness": 0,
}

Frame = {
    "bg": "#C8E6C9",
    "insertbackground": "#2E7D32",
    "highlightthickness": 0,
}

Button = {
    "Information": {
        "normal": {"fill": "#2E7D32"},
        "hover": {"fill": "#2E7D32"},
        "active": {"fill": "#2E7D32"},
    },
    "Rectangle": {
        "normal": {"fill": "#A5D6A7", "outline": "#81C784"},
        "hover": {"fill": "#C8E6C9", "outline": "#388E3C"},
        "active": {"fill": "#81C784", "outline": "#2E7D32"},
    },
    "RoundedRectangle": {
        "normal": {"fill": "#FFFFFF", "outline": "#81C784"},
        "hover": {"fill": "#A5D6A7", "outline": "#388E3C"},
        "active": {"fill": "#C8E6C9", "outline": "#2E7D32"},
    }
}

CheckButton = copy.deepcopy(Button)

ToggleButton = {
    "Information": {
        "normal-off": {"fill": "#2E7D32"},
        "hover-off": {"fill": "#2E7D32"},
        "active-off": {"fill": "#2E7D32"},
        "normal-on": {"fill": "#2E7D32"},
        "hover-on": {"fill": "#2E7D32"},
        "active-on": {"fill": "#2E7D32"},
    },
    "Rectangle": {
        "normal-off": {"fill": "#FFFFFF", "outline": "#81C784"},
        "hover-off": {"fill": "#A5D6A7", "outline": "#81C784"},
        "active-off": {"fill": "#C8E6C9", "outline": "#81C784"},
        "normal-on": {"fill": "#66BB6A", "outline": "#66BB6A"},
        "hover-on": {"fill": "#81C784", "outline": "#81C784"},
        "active-on": {"fill": "#388E3C", "outline": "#66BB6A"},
    },
    "RoundedRectangle": {
        "normal-off": {"fill": "#FFFFFF", "outline": "#81C784"},
        "hover-off": {"fill": "#A5D6A7", "outline": "#81C784"},
        "active-off": {"fill": "#C8E6C9", "outline": "#81C784"},
        "normal-on": {"fill": "#66BB6A", "outline": "#66BB6A"},
        "hover-on": {"fill": "#81C784", "outline": "#81C784"},
        "active-on": {"fill": "#388E3C", "outline": "#66BB6A"},
    }
}

HighlightButton = {
    "Information": {
        "normal": {"fill": "#2E7D32"},
        "hover": {"fill": "#1B5E20"},
        "active": {"fill": "#0C4A1E"},
    }
}

IconButton = copy.deepcopy(Button)

InputBox = {
    "Rectangle": {
        "normal": {"fill": "#F1F8E9", "outline": "#81C784"},
        "hover": {"fill": "#E8F5E9", "outline": "#388E3C"},
        "active": {"fill": "#FFFFFF", "outline": "#2E7D32"},
    },
    "RoundedRectangle.in": {
        "normal": {"fill": "#F1F8E9", "outline": "#B8E786"},
        "hover": {"fill": "#E8F5E9", "outline": "#B8E786"},
        "active": {"fill": "#FFFFFF", "outline": "#B8E786"},
    },
    "RoundedRectangle.out": {
        "normal": {"fill": "#868686", "outline": "#868686"},
        "hover": {"fill": "#868686", "outline": "#868686"},
        "active": {"fill": "#388E3C", "outline": "#388E3C"},
    },
    "SingleLineText": {
        "normal": {"fill": "#2E7D32"},
        "hover": {"fill": "#2E7D32"},
        "active": {"fill": "#2E7D32"},
    }
}

Label = {
    "Information": {
        "normal": {"fill": "#2E7D32"},
        "hover": {"fill": "#2E7D32"},
    },
    "Rectangle": {
        "normal": {"fill": "#F1F8E9", "outline": "#81C784"},
        "hover": {"fill": "#E8F5E9", "outline": "#81C784"},
    },
    "RoundedRectangle": {
        "normal": {"fill": "#F1F8E9", "outline": "#81C784"},
        "hover": {"fill": "#E8F5E9", "outline": "#81C784"},
    }
}

OptionButton = copy.deepcopy(Button)

ProgressBar = {
    "Rectangle.in": {
        "normal": {"fill": "#66BB6A", "outline": "#66BB6A"},
        "hover": {"fill": "#81C784", "outline": "#81C784"},
    },
    "Rectangle.out": {
        "normal": {"fill": "#A5D6A7", "outline": "#81C784"},
        "hover": {"fill": "#C8E6C9", "outline": "#388E3C"},
    },
    "SemicircularRectangle.in": {
        "normal": {"fill": "#66BB6A", "outline": "#66BB6A"},
        "hover": {"fill": "#81C784", "outline": "#81C784"},
    },
    "SemicircularRectangle.out": {
        "normal": {"fill": "#F1F8E9", "outline": "#81C784"},
        "hover": {"fill": "#E8F5E9", "outline": "#81C784"},
    }
}

RadioButton = {
    "Oval.in": {
        "normal": {"fill": "#66BB6A", "outline": "#66BB6A"},
        "hover": {"fill": "#81C784", "outline": "#81C784"},
        "active": {"fill": "#81C784", "outline": "#81C784"},
    },
    "Oval.out": {
        "normal": {"fill": "#FFFFFF", "outline": "#81C784"},
        "hover": {"fill": "#A5D6A7", "outline": "#81C784"},
        "active": {"fill": "#C8E6C9", "outline": "#81C784"},
    },
    "Rectangle.in": {
        "normal": {"fill": "#66BB6A", "outline": "#66BB6A"},
        "hover": {"fill": "#81C784", "outline": "#81C784"},
        "active": {"fill": "#81C784", "outline": "#81C784"},
    },
    "Rectangle.out": {
        "normal": {"fill": "#FFFFFF", "outline": "#81C784"},
        "hover": {"fill": "#A5D6A7", "outline": "#81C784"},
        "active": {"fill": "#C8E6C9", "outline": "#81C784"},
    }
}

SegmentedButton = copy.deepcopy(Label)

Slider = {
    "Oval.in": {
        "normal": {"fill": "#66BB6A", "outline": "#66BB6A"},
    },
    "Oval.out": {
        "normal": {"fill": "#FFFFFF", "outline": "#E8E8E8"},
    },
    "Rectangle.in": {
        "normal": {"fill": "#66BB6A", "outline": "#66BB6A"},
    },
    "Rectangle": {
        "normal": {"fill": "#66BB6A", "outline": "#66BB6A"},
        "hover": {"fill": "#388E3C", "outline": "#388E3C"},
        "active": {"fill": "#2E7D32", "outline": "#2E7D32"},
    },
    "Rectangle.out": {
        "normal": {"fill": "#81C784", "outline": "#81C784"},
    },
    "SemicircularRectangle.in": {
        "normal": {"fill": "#66BB6A", "outline": "#66BB6A"},
    },
    "SemicircularRectangle.out": {
        "normal": {"fill": "#81C784", "outline": "#81C784"},
    }
}

Switch = {
    "Oval": {
        "normal-off": {"fill": "#2E7D32", "outline": "#2E7D32"},
        "hover-off": {"fill": "#1B5E20", "outline": "#1B5E20"},
        "active-off": {"fill": "#0C4A1E", "outline": "#0C4A1E"},
        "normal-on": {"fill": "#FFFFFF", "outline": "#FFFFFF"},
        "hover-on": {"fill": "#FFFFFF", "outline": "#FFFFFF"},
        "active-on": {"fill": "#FFFFFF", "outline": "#FFFFFF"},
    },
    "Rectangle.in": {
        "normal-off": {"fill": "#2E7D32", "outline": "#2E7D32"},
        "hover-off": {"fill": "#1B5E20", "outline": "#1B5E20"},
        "active-off": {"fill": "#0C4A1E", "outline": "#0C4A1E"},
        "normal-on": {"fill": "#FFFFFF", "outline": "#FFFFFF"},
        "hover-on": {"fill": "#FFFFFF", "outline": "#FFFFFF"},
        "active-on": {"fill": "#FFFFFF", "outline": "#FFFFFF"},
    },
    "Rectangle.out": {
        "normal-off": {"fill": "#E0F7E9", "outline": "#B8B8B9"},
        "hover-off": {"fill": "#C8E6C9", "outline": "#858687"},
        "active-off": {"fill": "#A5D6A7", "outline": "#848586"},
        "normal-on": {"fill": "#66BB6A", "outline": "#66BB6A"},
        "hover-on": {"fill": "#81C784", "outline": "#81C784"},
        "active-on": {"fill": "#388E3C", "outline": "#2072B9"},
    },
    "SemicircularRectangle": {
        "normal-off": {"fill": "#E0F7E9", "outline": "#B8B8B9"},
        "hover-off": {"fill": "#C8E6C9", "outline": "#858687"},
        "active-off": {"fill": "#A5D6A7", "outline": "#848586"},
        "normal-on": {"fill": "#66BB6A", "outline": "#66BB6A"},
        "hover-on": {"fill": "#81C784", "outline": "#81C784"},
        "active-on": {"fill": "#388E3C", "outline": "#2072B9"},
    }
}

Text = {
    "Information": {
        "normal": {"fill": "#2E7D32"},
    }
}

UnderlineButton = {
    "Information": {
        "normal": {"fill": "#2E7D32"},
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
