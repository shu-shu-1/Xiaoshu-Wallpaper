import copy

Canvas = {
    "bg": "#FDE8D0",
    "insertbackground": "#663300",
    "highlightthickness": 0,
}

Frame = {
    "bg": "#FCD5B5",
    "insertbackground": "#663300",
    "highlightthickness": 0,
}

Button = {
    "Information": {
        "normal": {"fill": "#663300"},
        "hover": {"fill": "#663300"},
        "active": {"fill": "#663300"},
    },
    "Rectangle": {
        "normal": {"fill": "#FAD7A0", "outline": "#E59866"},
        "hover": {"fill": "#FFF2CC", "outline": "#D68910"},
        "active": {"fill": "#F7DC6F", "outline": "#B9770E"},
    },
    "RoundedRectangle": {
        "normal": {"fill": "#FFFFFF", "outline": "#E59866"},
        "hover": {"fill": "#FAE5D3", "outline": "#D68910"},
        "active": {"fill": "#FDEBD0", "outline": "#B9770E"},
    }
}

CheckButton = copy.deepcopy(Button)

ToggleButton = {
    "Information": {
        "normal-off": {"fill": "#663300"},
        "hover-off": {"fill": "#663300"},
        "active-off": {"fill": "#663300"},
        "normal-on": {"fill": "#663300"},
        "hover-on": {"fill": "#663300"},
        "active-on": {"fill": "#663300"},
    },
    "Rectangle": {
        "normal-off": {"fill": "#FFFFFF", "outline": "#E59866"},
        "hover-off": {"fill": "#FAE5D3", "outline": "#E59866"},
        "active-off": {"fill": "#FDEBD0", "outline": "#E59866"},
        "normal-on": {"fill": "#FFA726", "outline": "#FFB74D"},
        "hover-on": {"fill": "#FFB74D", "outline": "#FFB74D"},
        "active-on": {"fill": "#FF8A65", "outline": "#FFB74D"},
    },
    "RoundedRectangle": {
        "normal-off": {"fill": "#FFFFFF", "outline": "#E59866"},
        "hover-off": {"fill": "#FAE5D3", "outline": "#E59866"},
        "active-off": {"fill": "#FDEBD0", "outline": "#E59866"},
        "normal-on": {"fill": "#FFA726", "outline": "#FFB74D"},
        "hover-on": {"fill": "#FFB74D", "outline": "#FFB74D"},
        "active-on": {"fill": "#FF8A65", "outline": "#FFB74D"},
    }
}

HighlightButton = {
    "Information": {
        "normal": {"fill": "#663300"},
        "hover": {"fill": "#804000"},
        "active": {"fill": "#4D2600"},
    }
}

IconButton = copy.deepcopy(Button)

InputBox = {
    "Rectangle": {
        "normal": {"fill": "#FFF7E1", "outline": "#E59866"},
        "hover": {"fill": "#FFF2CC", "outline": "#B9770E"},
        "active": {"fill": "#FFFFFF", "outline": "#FF8A65"},  # 修改后的颜色
    },
    "RoundedRectangle.in": {
        "normal": {"fill": "#FFF7E1", "outline": "#E5E5E5"},
        "hover": {"fill": "#FFF2CC", "outline": "#E5E5E5"},
        "active": {"fill": "#FFFFFF", "outline": "#FF8A65"},  # 修改后的颜色
    },
    "RoundedRectangle.out": {
        "normal": {"fill": "#868686", "outline": "#868686"},
        "hover": {"fill": "#868686", "outline": "#868686"},
        "active": {"fill": "#FF8A65", "outline": "#FF8A65"},  # 修改后的颜色
    },
    "SingleLineText": {
        "normal": {"fill": "#663300"},
        "hover": {"fill": "#663300"},
        "active": {"fill": "#663300"},
    }
}

Label = {
    "Information": {
        "normal": {"fill": "#663300"},
        "hover": {"fill": "#663300"},
    },
    "Rectangle": {
        "normal": {"fill": "#FFF7E1", "outline": "#E59866"},
        "hover": {"fill": "#FFF2CC", "outline": "#E59866"},
    },
    "RoundedRectangle": {
        "normal": {"fill": "#FFF7E1", "outline": "#E59866"},
        "hover": {"fill": "#FFF2CC", "outline": "#E59866"},
    }
}

OptionButton = copy.deepcopy(Button)

ProgressBar = {
    "Rectangle.in": {
        "normal": {"fill": "#FFA726", "outline": "#FFA726"},
        "hover": {"fill": "#FFB74D", "outline": "#FFB74D"},
    },
    "Rectangle.out": {
        "normal": {"fill": "#FAD7A0", "outline": "#E59866"},
        "hover": {"fill": "#FFF2CC", "outline": "#D68910"},
    },
    "SemicircularRectangle.in": {
        "normal": {"fill": "#FFA726", "outline": "#FFA726"},
        "hover": {"fill": "#FFB74D", "outline": "#FFB74D"},
    },
    "SemicircularRectangle.out": {
        "normal": {"fill": "#FFF7E1", "outline": "#E59866"},
        "hover": {"fill": "#FFF2CC", "outline": "#E59866"},
    }
}

RadioButton = {
    "Oval.in": {
        "normal": {"fill": "#FFA726", "outline": "#FFA726"},
        "hover": {"fill": "#FFB74D", "outline": "#FFB74D"},
        "active": {"fill": "#FFB74D", "outline": "#FFB74D"},
    },
    "Oval.out": {
        "normal": {"fill": "#FFFFFF", "outline": "#E59866"},
        "hover": {"fill": "#FAE5D3", "outline": "#E59866"},
        "active": {"fill": "#FDEBD0", "outline": "#E59866"},
    },
    "Rectangle.in": {
        "normal": {"fill": "#FFA726", "outline": "#FFA726"},
        "hover": {"fill": "#FFB74D", "outline": "#FFB74D"},
        "active": {"fill": "#FFB74D", "outline": "#FFB74D"},
    },
    "Rectangle.out": {
        "normal": {"fill": "#FFFFFF", "outline": "#E59866"},
        "hover": {"fill": "#FAE5D3", "outline": "#E59866"},
        "active": {"fill": "#FDEBD0", "outline": "#E59866"},
    }
}

SegmentedButton = copy.deepcopy(Label)

Slider = {
    "Oval.in": {
        "normal": {"fill": "#FFA726", "outline": "#FFA726"},
    },
    "Oval.out": {
        "normal": {"fill": "#FFFFFF", "outline": "#E8E8E8"},
    },
    "Rectangle.in": {
        "normal": {"fill": "#FFA726", "outline": "#FFA726"},
    },
    "Rectangle": {
        "normal": {"fill": "#FFA726", "outline": "#FFA726"},
        "hover": {"fill": "#FFB74D", "outline": "#FFB74D"},
        "active": {"fill": "#FF8A65", "outline": "#FF8A65"},
    },
    "Rectangle.out": {
        "normal": {"fill": "#E59866", "outline": "#E59866"},
    },
    "SemicircularRectangle.in": {
        "normal": {"fill": "#FFA726", "outline": "#FFA726"},
    },
    "SemicircularRectangle.out": {
        "normal": {"fill": "#E59866", "outline": "#E59866"},
    }
}

Switch = {
    "Oval": {
        "normal-off": {"fill": "#663300", "outline": "#663300"},
        "hover-off": {"fill": "#804000", "outline": "#804000"},
        "active-off": {"fill": "#4D2600", "outline": "#4D2600"},
        "normal-on": {"fill": "#FFFFFF", "outline": "#FFFFFF"},
        "hover-on": {"fill": "#FFFFFF", "outline": "#FFFFFF"},
        "active-on": {"fill": "#FFFFFF", "outline": "#FFFFFF"},
    },
    "Rectangle.in": {
        "normal-off": {"fill": "#663300", "outline": "#663300"},
        "hover-off": {"fill": "#804000", "outline": "#804000"},
        "active-off": {"fill": "#4D2600", "outline": "#4D2600"},
        "normal-on": {"fill": "#FFFFFF", "outline": "#FFFFFF"},
        "hover-on": {"fill": "#FFFFFF", "outline": "#FFFFFF"},
        "active-on": {"fill": "#FFFFFF", "outline": "#FFFFFF"},
    },
    "Rectangle.out": {
        "normal-off": {"fill": "#FDE8D0", "outline": "#B8B8B9"},
        "hover-off": {"fill": "#FCD5B5", "outline": "#858687"},
        "active-off": {"fill": "#FAD7A0", "outline": "#848586"},
        "normal-on": {"fill": "#FFA726", "outline": "#FFA726"},
        "hover-on": {"fill": "#FFB74D", "outline": "#FFB74D"},
        "active-on": {"fill": "#FF8A65", "outline": "#2072B9"},
    },
    "SemicircularRectangle": {
        "normal-off": {"fill": "#FDE8D0", "outline": "#B8B8B9"},
        "hover-off": {"fill": "#FCD5B5", "outline": "#858687"},
        "active-off": {"fill": "#FAD7A0", "outline": "#848586"},
        "normal-on": {"fill": "#FFA726", "outline": "#FFA726"},
        "hover-on": {"fill": "#FFB74D", "outline": "#FFB74D"},
        "active-on": {"fill": "#FF8A65", "outline": "#2072B9"},
    }
}

Text = {
    "Information": {
        "normal": {"fill": "#663300"},
    }
}

UnderlineButton = {
    "Information": {
        "normal": {"fill": "#663300"},
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
