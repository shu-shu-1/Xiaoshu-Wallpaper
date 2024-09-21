import copy

# 樱花粉色系的主色调：浅粉色、深粉色和白色
Canvas = {
    "bg": "#FFF5F7",  # 樱花粉
    "insertbackground": "#D81B60",  # 深粉色
    "highlightthickness": 0,
}

Frame = {
    "bg": "#FFD1D9",  # 更淡的粉色
    "insertbackground": "#D81B60",
    "highlightthickness": 0,
}

Button = {
    "Information": {
        "normal": {"fill": "#D81B60"},  # 深粉色
        "hover": {"fill": "#C2185B"},  # 更深的粉色
        "active": {"fill": "#AD1457"},  # 最深的粉色
    },
    "Rectangle": {
        "normal": {"fill": "#FFCDD2", "outline": "#F8BBD0"},  # 浅粉色
        "hover": {"fill": "#F8BBD0", "outline": "#F48FB1"},  # 更浅的粉色
        "active": {"fill": "#F48FB1", "outline": "#EC407A"},  # 粉色
    },
    "RoundedRectangle": {
        "normal": {"fill": "#FFF5F7", "outline": "#FFD1D9"},  # 浅粉色
        "hover": {"fill": "#FFD1D9", "outline": "#FFCDD2"},  # 更浅的粉色
        "active": {"fill": "#FFCDD2", "outline": "#EF9A9A"},  # 粉色
    }
}

CheckButton = copy.deepcopy(Button)

ToggleButton = {
    "Information": {
        "normal-off": {"fill": "#D81B60"},
        "hover-off": {"fill": "#C2185B"},
        "active-off": {"fill": "#AD1457"},
        "normal-on": {"fill": "#D81B60"},
        "hover-on": {"fill": "#C2185B"},
        "active-on": {"fill": "#AD1457"},
    },
    "Rectangle": {
        "normal-off": {"fill": "#FFF5F7", "outline": "#FFD1D9"},
        "hover-off": {"fill": "#FFD1D9", "outline": "#FFCDD2"},
        "active-off": {"fill": "#FFCDD2", "outline": "#EF9A9A"},
        "normal-on": {"fill": "#FFCDD2", "outline": "#F8BBD0"},
        "hover-on": {"fill": "#F8BBD0", "outline": "#F48FB1"},
        "active-on": {"fill": "#F48FB1", "outline": "#EC407A"},
    },
    "RoundedRectangle": {
        "normal-off": {"fill": "#FFF5F7", "outline": "#FFD1D9"},
        "hover-off": {"fill": "#FFD1D9", "outline": "#FFCDD2"},
        "active-off": {"fill": "#FFCDD2", "outline": "#EF9A9A"},
        "normal-on": {"fill": "#FFCDD2", "outline": "#F8BBD0"},
        "hover-on": {"fill": "#F8BBD0", "outline": "#F48FB1"},
        "active-on": {"fill": "#F48FB1", "outline": "#EC407A"},
    }
}

HighlightButton = {
    "Information": {
        "normal": {"fill": "#D81B60"},
        "hover": {"fill": "#C2185B"},
        "active": {"fill": "#AD1457"},
    }
}

IconButton = copy.deepcopy(Button)

InputBox = {
    "Rectangle": {
        "normal": {"fill": "#FFD1D9", "outline": "#F8BBD0"},
        "hover": {"fill": "#F8BBD0", "outline": "#F48FB1"},
        "active": {"fill": "#FFFFFF", "outline": "#EC407A"},
    },
    "RoundedRectangle.in": {
        "normal": {"fill": "#FFD1D9", "outline": "#E5E5E5"},
        "hover": {"fill": "#F8BBD0", "outline": "#E5E5E5"},
        "active": {"fill": "#FFFFFF", "outline": "#E5E5E5"},
    },
    "RoundedRectangle.out": {
        "normal": {"fill": "#D81B60", "outline": "#D81B60"},
        "hover": {"fill": "#D81B60", "outline": "#D81B60"},
        "active": {"fill": "#AD1457", "outline": "#AD1457"},
    },
    "SingleLineText": {
        "normal": {"fill": "#D81B60"},
        "hover": {"fill": "#D81B60"},
        "active": {"fill": "#D81B60"},
    }
}

Label = {
    "Information": {
        "normal": {"fill": "#D81B60"},
        "hover": {"fill": "#D81B60"},
    },
    "Rectangle": {
        "normal": {"fill": "#FFD1D9", "outline": "#F8BBD0"},
        "hover": {"fill": "#F8BBD0", "outline": "#F48FB1"},
    },
    "RoundedRectangle": {
        "normal": {"fill": "#FFD1D9", "outline": "#F8BBD0"},
        "hover": {"fill": "#F8BBD0", "outline": "#F48FB1"},
    }
}

OptionButton = copy.deepcopy(Button)

ProgressBar = {
    "Rectangle.in": {
        "normal": {"fill": "#F48FB1", "outline": "#F48FB1"},
        "hover": {"fill": "#EC407A", "outline": "#EC407A"},
    },
    "Rectangle.out": {
        "normal": {"fill": "#FFCDD2", "outline": "#F8BBD0"},
        "hover": {"fill": "#F8BBD0", "outline": "#F48FB1"},
    },
    "SemicircularRectangle.in": {
        "normal": {"fill": "#F48FB1", "outline": "#F48FB1"},
        "hover": {"fill": "#EC407A", "outline": "#EC407A"},
    },
    "SemicircularRectangle.out": {
        "normal": {"fill": "#FFD1D9", "outline": "#F8BBD0"},
        "hover": {"fill": "#F8BBD0", "outline": "#F48FB1"},
    }
}

RadioButton = {
    "Oval.in": {
        "normal": {"fill": "#F48FB1", "outline": "#F48FB1"},
        "hover": {"fill": "#EC407A", "outline": "#EC407A"},
        "active": {"fill": "#EC407A", "outline": "#EC407A"},
    },
    "Oval.out": {
        "normal": {"fill": "#FFFFFF", "outline": "#F8BBD0"},
        "hover": {"fill": "#F8BBD0", "outline": "#F8BBD0"},
        "active": {"fill": "#FFD1D9", "outline": "#F8BBD0"},
    },
    "Rectangle.in": {
        "normal": {"fill": "#F48FB1", "outline": "#F48FB1"},
        "hover": {"fill": "#EC407A", "outline": "#EC407A"},
        "active": {"fill": "#EC407A", "outline": "#EC407A"},
    },
    "Rectangle.out": {
        "normal": {"fill": "#FFFFFF", "outline": "#F8BBD0"},
        "hover": {"fill": "#F8BBD0", "outline": "#F8BBD0"},
        "active": {"fill": "#FFD1D9", "outline": "#F8BBD0"},
    }
}

SegmentedButton = copy.deepcopy(Label)

Slider = {
    "Oval.in": {
        "normal": {"fill": "#F48FB1", "outline": "#F48FB1"},
    },
    "Oval.out": {
        "normal": {"fill": "#FFFFFF", "outline": "#E8E8E8"},
    },
    "Rectangle.in": {
        "normal": {"fill": "#F48FB1", "outline": "#F48FB1"},
    },
    "Rectangle": {
        "normal": {"fill": "#F48FB1", "outline": "#F48FB1"},
        "hover": {"fill": "#EC407A", "outline": "#EC407A"},
        "active": {"fill": "#D81B60", "outline": "#D81B60"},
    },
    "Rectangle.out": {
        "normal": {"fill": "#F8BBD0", "outline": "#F8BBD0"},
    },
    "SemicircularRectangle.in": {
        "normal": {"fill": "#F48FB1", "outline": "#F48FB1"},
    },
    "SemicircularRectangle.out": {
        "normal": {"fill": "#F8BBD0", "outline": "#F8BBD0"},
    }
}

Switch = {
    "Oval": {
        "normal-off": {"fill": "#D81B60", "outline": "#D81B60"},
        "hover-off": {"fill": "#C2185B", "outline": "#C2185B"},
        "active-off": {"fill": "#AD1457", "outline": "#AD1457"},
        "normal-on": {"fill": "#FFFFFF", "outline": "#FFFFFF"},
        "hover-on": {"fill": "#FFFFFF", "outline": "#FFFFFF"},
        "active-on": {"fill": "#FFFFFF", "outline": "#FFFFFF"},
    },
    "Rectangle.in": {
        "normal-off": {"fill": "#D81B60", "outline": "#D81B60"},
        "hover-off": {"fill": "#C2185B", "outline": "#C2185B"},
        "active-off": {"fill": "#AD1457", "outline": "#AD1457"},
        "normal-on": {"fill": "#FFFFFF", "outline": "#FFFFFF"},
        "hover-on": {"fill": "#FFFFFF", "outline": "#FFFFFF"},
        "active-on": {"fill": "#FFFFFF", "outline": "#FFFFFF"},
    },
    "Rectangle.out": {
        "normal-off": {"fill": "#FFD1D9", "outline": "#E8E8E8"},
        "hover-off": {"fill": "#FFCDD2", "outline": "#C8C8C8"},
        "active-off": {"fill": "#F8BBD0", "outline": "#B8B8B8"},
        "normal-on": {"fill": "#F48FB1", "outline": "#F48FB1"},
        "hover-on": {"fill": "#EC407A", "outline": "#EC407A"},
        "active-on": {"fill": "#D81B60", "outline": "#D81B60"},
    },
    "SemicircularRectangle": {
        "normal-off": {"fill": "#FFD1D9", "outline": "#E8E8E8"},
        "hover-off": {"fill": "#FFCDD2", "outline": "#C8C8C8"},
        "active-off": {"fill": "#F8BBD0", "outline": "#B8B8B8"},
        "normal-on": {"fill": "#F48FB1", "outline": "#F48FB1"},
        "hover-on": {"fill": "#EC407A", "outline": "#EC407A"},
        "active-on": {"fill": "#D81B60", "outline": "#D81B60"},
    }
}

Text = {
    "Information": {
        "normal": {"fill": "#D81B60"},
    }
}

UnderlineButton = {
    "Information": {
        "normal": {"fill": "#D81B60"},
        "hover": {"fill": "#C2185B"},
        "active": {"fill": "#AD1457"},
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
