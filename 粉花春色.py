import copy

# 春天主题的主色调：柔和的绿色和粉色
Canvas = {
    "bg": "#E8F5E9",  # 非常淡的绿色
    "insertbackground": "#4CAF50",  # 绿色
    "highlightthickness": 0,
}

Frame = {
    "bg": "#F1F8E9",  # 更淡的绿色
    "insertbackground": "#4CAF50",
    "highlightthickness": 0,
}

Button = {
    "Information": {
        "normal": {"fill": "#388E3C"},  # 深绿色
        "hover": {"fill": "#2E7D32"},  # 更深的绿色
        "active": {"fill": "#1B5E20"},  # 最深的绿色
    },
    "Rectangle": {
        "normal": {"fill": "#A5D6A7", "outline": "#81C784"},  # 浅绿色
        "hover": {"fill": "#C8E6C9", "outline": "#66BB6A"},  # 更浅的绿色
        "active": {"fill": "#4CAF50", "outline": "#388E3C"},  # 绿色
    },
    "RoundedRectangle": {
        "normal": {"fill": "#FFE0E0", "outline": "#FFCDD2"},  # 非常浅的粉色
        "hover": {"fill": "#FFCDD2", "outline": "#EF9A9A"},  # 更浅的粉色
        "active": {"fill": "#EF9A9A", "outline": "#E57373"},  # 粉色
    }
}

CheckButton = copy.deepcopy(Button)

ToggleButton = {
    "Information": {
        "normal-off": {"fill": "#388E3C"},
        "hover-off": {"fill": "#2E7D32"},
        "active-off": {"fill": "#1B5E20"},
        "normal-on": {"fill": "#388E3C"},
        "hover-on": {"fill": "#2E7D32"},
        "active-on": {"fill": "#1B5E20"},
    },
    "Rectangle": {
        "normal-off": {"fill": "#FFE0E0", "outline": "#FFCDD2"},
        "hover-off": {"fill": "#FFCDD2", "outline": "#EF9A9A"},
        "active-off": {"fill": "#EF9A9A", "outline": "#E57373"},
        "normal-on": {"fill": "#A5D6A7", "outline": "#81C784"},
        "hover-on": {"fill": "#C8E6C9", "outline": "#66BB6A"},
        "active-on": {"fill": "#4CAF50", "outline": "#388E3C"},
    },
    "RoundedRectangle": {
        "normal-off": {"fill": "#FFE0E0", "outline": "#FFCDD2"},
        "hover-off": {"fill": "#FFCDD2", "outline": "#EF9A9A"},
        "active-off": {"fill": "#EF9A9A", "outline": "#E57373"},
        "normal-on": {"fill": "#A5D6A7", "outline": "#81C784"},
        "hover-on": {"fill": "#C8E6C9", "outline": "#66BB6A"},
        "active-on": {"fill": "#4CAF50", "outline": "#388E3C"},
    }
}

HighlightButton = {
    "Information": {
        "normal": {"fill": "#388E3C"},
        "hover": {"fill": "#2E7D32"},
        "active": {"fill": "#1B5E20"},
    }
}

IconButton = copy.deepcopy(Button)

InputBox = {
    "Rectangle": {
        "normal": {"fill": "#F1F8E9", "outline": "#81C784"},
        "hover": {"fill": "#E8F5E9", "outline": "#66BB6A"},
        "active": {"fill": "#FFFFFF", "outline": "#4CAF50"},
    },
    "RoundedRectangle.in": {
        "normal": {"fill": "#F1F8E9", "outline": "#E5E5E5"},
        "hover": {"fill": "#E8F5E9", "outline": "#E5E5E5"},
        "active": {"fill": "#FFFFFF", "outline": "#E5E5E5"},
    },
    "RoundedRectangle.out": {
        "normal": {"fill": "#388E3C", "outline": "#388E3C"},
        "hover": {"fill": "#388E3C", "outline": "#388E3C"},
        "active": {"fill": "#1B5E20", "outline": "#1B5E20"},
    },
    "SingleLineText": {
        "normal": {"fill": "#388E3C"},
        "hover": {"fill": "#388E3C"},
        "active": {"fill": "#388E3C"},
    }
}

Label = {
    "Information": {
        "normal": {"fill": "#388E3C"},
        "hover": {"fill": "#388E3C"},
    },
    "Rectangle": {
        "normal": {"fill": "#F1F8E9", "outline": "#81C784"},
        "hover": {"fill": "#E8F5E9", "outline": "#66BB6A"},
    },
    "RoundedRectangle": {
        "normal": {"fill": "#F1F8E9", "outline": "#81C784"},
        "hover": {"fill": "#E8F5E9", "outline": "#66BB6A"},
    }
}

OptionButton = copy.deepcopy(Button)

ProgressBar = {
    "Rectangle.in": {
        "normal": {"fill": "#4CAF50", "outline": "#4CAF50"},
        "hover": {"fill": "#66BB6A", "outline": "#66BB6A"},
    },
    "Rectangle.out": {
        "normal": {"fill": "#A5D6A7", "outline": "#81C784"},
        "hover": {"fill": "#C8E6C9", "outline": "#66BB6A"},
    },
    "SemicircularRectangle.in": {
        "normal": {"fill": "#4CAF50", "outline": "#4CAF50"},
        "hover": {"fill": "#66BB6A", "outline": "#66BB6A"},
    },
    "SemicircularRectangle.out": {
        "normal": {"fill": "#F1F8E9", "outline": "#81C784"},
        "hover": {"fill": "#E8F5E9", "outline": "#66BB6A"},
    }
}

RadioButton = {
    "Oval.in": {
        "normal": {"fill": "#4CAF50", "outline": "#4CAF50"},
        "hover": {"fill": "#66BB6A", "outline": "#66BB6A"},
        "active": {"fill": "#66BB6A", "outline": "#66BB6A"},
    },
    "Oval.out": {
        "normal": {"fill": "#FFFFFF", "outline": "#81C784"},
        "hover": {"fill": "#E8F5E9", "outline": "#81C784"},
        "active": {"fill": "#F1F8E9", "outline": "#81C784"},
    },
    "Rectangle.in": {
        "normal": {"fill": "#4CAF50", "outline": "#4CAF50"},
        "hover": {"fill": "#66BB6A", "outline": "#66BB6A"},
        "active": {"fill": "#66BB6A", "outline": "#66BB6A"},
    },
    "Rectangle.out": {
        "normal": {"fill": "#FFFFFF", "outline": "#81C784"},
        "hover": {"fill": "#E8F5E9", "outline": "#81C784"},
        "active": {"fill": "#F1F8E9", "outline": "#81C784"},
    }
}

SegmentedButton = copy.deepcopy(Label)

Slider = {
    "Oval.in": {
        "normal": {"fill": "#4CAF50", "outline": "#4CAF50"},
    },
    "Oval.out": {
        "normal": {"fill": "#FFFFFF", "outline": "#E8E8E8"},
    },
    "Rectangle.in": {
        "normal": {"fill": "#4CAF50", "outline": "#4CAF50"},
    },
    "Rectangle": {
        "normal": {"fill": "#4CAF50", "outline": "#4CAF50"},
        "hover": {"fill": "#66BB6A", "outline": "#66BB6A"},
        "active": {"fill": "#388E3C", "outline": "#388E3C"},
    },
    "Rectangle.out": {
        "normal": {"fill": "#81C784", "outline": "#81C784"},
    },
    "SemicircularRectangle.in": {
        "normal": {"fill": "#4CAF50", "outline": "#4CAF50"},
    },
    "SemicircularRectangle.out": {
        "normal": {"fill": "#81C784", "outline": "#81C784"},
    }
}

Switch = {
    "Oval": {
        "normal-off": {"fill": "#388E3C", "outline": "#388E3C"},
        "hover-off": {"fill": "#2E7D32", "outline": "#2E7D32"},
        "active-off": {"fill": "#1B5E20", "outline": "#1B5E20"},
        "normal-on": {"fill": "#FFFFFF", "outline": "#FFFFFF"},
        "hover-on": {"fill": "#FFFFFF", "outline": "#FFFFFF"},
        "active-on": {"fill": "#FFFFFF", "outline": "#FFFFFF"},
    },
    "Rectangle.in": {
        "normal-off": {"fill": "#388E3C", "outline": "#388E3C"},
        "hover-off": {"fill": "#2E7D32", "outline": "#2E7D32"},
        "active-off": {"fill": "#1B5E20", "outline": "#1B5E20"},
        "normal-on": {"fill": "#FFFFFF", "outline": "#FFFFFF"},
        "hover-on": {"fill": "#FFFFFF", "outline": "#FFFFFF"},
        "active-on": {"fill": "#FFFFFF", "outline": "#FFFFFF"},
    },
    "Rectangle.out": {
        "normal-off": {"fill": "#E8F5E9", "outline": "#B8B8B9"},
        "hover-off": {"fill": "#C8E6C9", "outline": "#858585"},
        "active-off": {"fill": "#A5D6A7", "outline": "#848584"},
        "normal-on": {"fill": "#4CAF50", "outline": "#4CAF50"},
        "hover-on": {"fill": "#66BB6A", "outline": "#66BB6A"},
        "active-on": {"fill": "#388E3C", "outline": "#388E3C"},
    },
    "SemicircularRectangle": {
        "normal-off": {"fill": "#E8F5E9", "outline": "#B8B8B9"},
        "hover-off": {"fill": "#C8E6C9", "outline": "#858585"},
        "active-off": {"fill": "#A5D6A7", "outline": "#848584"},
        "normal-on": {"fill": "#4CAF50", "outline": "#4CAF50"},
        "hover-on": {"fill": "#66BB6A", "outline": "#66BB6A"},
        "active-on": {"fill": "#388E3C", "outline": "#388E3C"},
    }
}

Text = {
    "Information": {
        "normal": {"fill": "#388E3C"},
    }
}

UnderlineButton = {
    "Information": {
        "normal": {"fill": "#388E3C"},
        "hover": {"fill": "#2E7D32"},
        "active": {"fill": "#1B5E20"},
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
