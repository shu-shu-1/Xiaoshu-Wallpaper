import copy

# 黑白主题的主色调：黑色和白色
Canvas = {
    "bg": "#FFFFFF",
    "insertbackground": "#000000",
    "highlightthickness": 0,
}

Frame = {
    "bg": "#F0F0F0",
    "insertbackground": "#000000",
    "highlightthickness": 0,
}

Button = {
    "Information": {
        "normal": {"fill": "#000000"},
        "hover": {"fill": "#000000"},
        "active": {"fill": "#000000"},
    },
    "Rectangle": {
        "normal": {"fill": "#E0E0E0", "outline": "#B0B0B0"},
        "hover": {"fill": "#D0D0D0", "outline": "#A0A0A0"},
        "active": {"fill": "#C0C0C0", "outline": "#909090"},
    },
    "RoundedRectangle": {
        "normal": {"fill": "#FFFFFF", "outline": "#B0B0B0"},
        "hover": {"fill": "#F0F0F0", "outline": "#A0A0A0"},
        "active": {"fill": "#E0E0E0", "outline": "#909090"},
    }
}

CheckButton = copy.deepcopy(Button)

ToggleButton = {
    "Information": {
        "normal-off": {"fill": "#000000"},
        "hover-off": {"fill": "#000000"},
        "active-off": {"fill": "#000000"},
        "normal-on": {"fill": "#000000"},
        "hover-on": {"fill": "#000000"},
        "active-on": {"fill": "#000000"},
    },
    "Rectangle": {
        "normal-off": {"fill": "#FFFFFF", "outline": "#B0B0B0"},
        "hover-off": {"fill": "#F0F0F0", "outline": "#B0B0B0"},
        "active-off": {"fill": "#E0E0E0", "outline": "#B0B0B0"},
        "normal-on": {"fill": "#707070", "outline": "#808080"},
        "hover-on": {"fill": "#808080", "outline": "#808080"},
        "active-on": {"fill": "#505050", "outline": "#808080"},
    },
    "RoundedRectangle": {
        "normal-off": {"fill": "#FFFFFF", "outline": "#B0B0B0"},
        "hover-off": {"fill": "#F0F0F0", "outline": "#B0B0B0"},
        "active-off": {"fill": "#E0E0E0", "outline": "#B0B0B0"},
        "normal-on": {"fill": "#707070", "outline": "#808080"},
        "hover-on": {"fill": "#808080", "outline": "#808080"},
        "active-on": {"fill": "#505050", "outline": "#808080"},
    }
}

HighlightButton = {
    "Information": {
        "normal": {"fill": "#000000"},
        "hover": {"fill": "#333333"},
        "active": {"fill": "#111111"},
    }
}

IconButton = copy.deepcopy(Button)

InputBox = {
    "Rectangle": {
        "normal": {"fill": "#F5F5F5", "outline": "#B0B0B0"},
        "hover": {"fill": "#E0E0E0", "outline": "#000000"},
        "active": {"fill": "#FFFFFF", "outline": "#707070"},
    },
    "RoundedRectangle.in": {
        "normal": {"fill": "#F5F5F5", "outline": "#E5E5E5"},
        "hover": {"fill": "#E0E0E0", "outline": "#E5E5E5"},
        "active": {"fill": "#FFFFFF", "outline": "#E5E5E5"},
    },
    "RoundedRectangle.out": {
        "normal": {"fill": "#868686", "outline": "#868686"},
        "hover": {"fill": "#868686", "outline": "#868686"},
        "active": {"fill": "#505050", "outline": "#505050"},
    },
    "SingleLineText": {
        "normal": {"fill": "#000000"},
        "hover": {"fill": "#000000"},
        "active": {"fill": "#000000"},
    }
}

Label = {
    "Information": {
        "normal": {"fill": "#000000"},
        "hover": {"fill": "#000000"},
    },
    "Rectangle": {
        "normal": {"fill": "#F5F5F5", "outline": "#B0B0B0"},
        "hover": {"fill": "#E0E0E0", "outline": "#B0B0B0"},
    },
    "RoundedRectangle": {
        "normal": {"fill": "#F5F5F5", "outline": "#B0B0B0"},
        "hover": {"fill": "#E0E0E0", "outline": "#B0B0B0"},
    }
}

OptionButton = copy.deepcopy(Button)

ProgressBar = {
    "Rectangle.in": {
        "normal": {"fill": "#707070", "outline": "#707070"},
        "hover": {"fill": "#808080", "outline": "#808080"},
    },
    "Rectangle.out": {
        "normal": {"fill": "#E0E0E0", "outline": "#B0B0B0"},
        "hover": {"fill": "#D0D0D0", "outline": "#A0A0A0"},
    },
    "SemicircularRectangle.in": {
        "normal": {"fill": "#707070", "outline": "#707070"},
        "hover": {"fill": "#808080", "outline": "#808080"},
    },
    "SemicircularRectangle.out": {
        "normal": {"fill": "#F5F5F5", "outline": "#B0B0B0"},
        "hover": {"fill": "#E0E0E0", "outline": "#A0A0A0"},
    }
}

RadioButton = {
    "Oval.in": {
        "normal": {"fill": "#707070", "outline": "#707070"},
        "hover": {"fill": "#808080", "outline": "#808080"},
        "active": {"fill": "#808080", "outline": "#808080"},
    },
    "Oval.out": {
        "normal": {"fill": "#FFFFFF", "outline": "#B0B0B0"},
        "hover": {"fill": "#F0F0F0", "outline": "#B0B0B0"},
        "active": {"fill": "#E0E0E0", "outline": "#B0B0B0"},
    },
    "Rectangle.in": {
        "normal": {"fill": "#707070", "outline": "#707070"},
        "hover": {"fill": "#808080", "outline": "#808080"},
        "active": {"fill": "#808080", "outline": "#808080"},
    },
    "Rectangle.out": {
        "normal": {"fill": "#FFFFFF", "outline": "#B0B0B0"},
        "hover": {"fill": "#F0F0F0", "outline": "#B0B0B0"},
        "active": {"fill": "#E0E0E0", "outline": "#B0B0B0"},
    }
}

SegmentedButton = copy.deepcopy(Label)

Slider = {
    "Oval.in": {
        "normal": {"fill": "#707070", "outline": "#707070"},
    },
    "Oval.out": {
        "normal": {"fill": "#FFFFFF", "outline": "#E8E8E8"},
    },
    "Rectangle.in": {
        "normal": {"fill": "#707070", "outline": "#707070"},
    },
    "Rectangle": {
        "normal": {"fill": "#707070", "outline": "#707070"},
        "hover": {"fill": "#808080", "outline": "#808080"},
        "active": {"fill": "#505050", "outline": "#505050"},
    },
    "Rectangle.out": {
        "normal": {"fill": "#B0B0B0", "outline": "#B0B0B0"},
    },
    "SemicircularRectangle.in": {
        "normal": {"fill": "#707070", "outline": "#707070"},
    },
    "SemicircularRectangle.out": {
        "normal": {"fill": "#B0B0B0", "outline": "#B0B0B0"},
    }
}

Switch = {
    "Oval": {
        "normal-off": {"fill": "#000000", "outline": "#000000"},
        "hover-off": {"fill": "#333333", "outline": "#333333"},
        "active-off": {"fill": "#111111", "outline": "#111111"},
        "normal-on": {"fill": "#FFFFFF", "outline": "#FFFFFF"},
        "hover-on": {"fill": "#FFFFFF", "outline": "#FFFFFF"},
        "active-on": {"fill": "#FFFFFF", "outline": "#FFFFFF"},
    },
    "Rectangle.in": {
        "normal-off": {"fill": "#000000", "outline": "#000000"},
        "hover-off": {"fill": "#333333", "outline": "#333333"},
        "active-off": {"fill": "#111111", "outline": "#111111"},
        "normal-on": {"fill": "#FFFFFF", "outline": "#FFFFFF"},
        "hover-on": {"fill": "#FFFFFF", "outline": "#FFFFFF"},
        "active-on": {"fill": "#FFFFFF", "outline": "#FFFFFF"},
    },
    "Rectangle.out": {
        "normal-off": {"fill": "#F5F5F5", "outline": "#B0B0B9"},
        "hover-off": {"fill": "#E7E7E8", "outline": "#858585"},
        "active-off": {"fill": "#DEDEDE", "outline": "#848584"},
        "normal-on": {"fill": "#707070", "outline": "#707070"},
        "hover-on": {"fill": "#808080", "outline": "#808080"},
        "active-on": {"fill": "#505050", "outline": "#505050"},
    },
    "SemicircularRectangle": {
        "normal-off": {"fill": "#F5F5F5", "outline": "#B0B0B9"},
        "hover-off": {"fill": "#E7E7E8", "outline": "#858585"},
        "active-off": {"fill": "#DEDEDE", "outline": "#848584"},
        "normal-on": {"fill": "#707070", "outline": "#707070"},
        "hover-on": {"fill": "#808080", "outline": "#808080"},
        "active-on": {"fill": "#505050", "outline": "#505050"},
    }
}

Text = {
    "Information": {
        "normal": {"fill": "#000000"},
    }
}

UnderlineButton = {
    "Information": {
        "normal": {"fill": "#000000"},
        "hover": {"fill": "#333333"},
        "active": {"fill": "#111111"},
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
