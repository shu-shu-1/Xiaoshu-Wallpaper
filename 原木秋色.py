import copy

# 定义颜色
PRIMARY_COLOR = "#D95D39"  # 主色调，秋天的橙红色
SECONDARY_COLOR = "#F6C4A2"  # 次级色调，柔和的米黄色
ACCENT_COLOR = "#FBB03B"  # 强调色，金黄色
HIGHLIGHT_COLOR = "#6F4E37"  # 高亮色，深棕色
DARKER_ACCENT_COLOR = "#A0522D"  # 较深的棕色
TEXT_COLOR = "#4B3D3A"  # 深灰色，确保文本可读性


Canvas = {
    "bg": SECONDARY_COLOR,  # 使用柔和的米黄色作为背景
    "insertbackground": PRIMARY_COLOR,  # 使用主色调作为插入背景
    "highlightthickness": 0,
}

Frame = {
    "bg": ACCENT_COLOR,  # 使用金黄色作为背景
    "insertbackground": PRIMARY_COLOR,
    "highlightthickness": 0,
}

Button = {
    "Information": {
        "normal": {"fill": PRIMARY_COLOR, "text": TEXT_COLOR},
        "hover": {"fill": HIGHLIGHT_COLOR, "text": TEXT_COLOR},
        "active": {"fill": DARKER_ACCENT_COLOR, "text": TEXT_COLOR},
    },
    "Rectangle": {
        "normal": {"fill": SECONDARY_COLOR, "outline": HIGHLIGHT_COLOR, "text": TEXT_COLOR},
        "hover": {"fill": ACCENT_COLOR, "outline": DARKER_ACCENT_COLOR, "text": TEXT_COLOR},
        "active": {"fill": HIGHLIGHT_COLOR, "outline": DARKER_ACCENT_COLOR, "text": TEXT_COLOR},
    },
    "RoundedRectangle": {
        "normal": {"fill": ACCENT_COLOR, "outline": HIGHLIGHT_COLOR, "text": TEXT_COLOR},
        "hover": {"fill": SECONDARY_COLOR, "outline": DARKER_ACCENT_COLOR, "text": TEXT_COLOR},
        "active": {"fill": HIGHLIGHT_COLOR, "outline": DARKER_ACCENT_COLOR, "text": TEXT_COLOR},
    }
}

CheckButton = copy.deepcopy(Button)

ToggleButton = {
    "Information": {
        "normal-off": {"fill": PRIMARY_COLOR, "text": TEXT_COLOR},
        "hover-off": {"fill": HIGHLIGHT_COLOR, "text": TEXT_COLOR},
        "active-off": {"fill": DARKER_ACCENT_COLOR, "text": TEXT_COLOR},
        "normal-on": {"fill": PRIMARY_COLOR, "text": TEXT_COLOR},
        "hover-on": {"fill": HIGHLIGHT_COLOR, "text": TEXT_COLOR},
        "active-on": {"fill": DARKER_ACCENT_COLOR, "text": TEXT_COLOR},
    },
    "Rectangle": {
        "normal-off": {"fill": ACCENT_COLOR, "outline": HIGHLIGHT_COLOR, "text": TEXT_COLOR},
        "hover-off": {"fill": SECONDARY_COLOR, "outline": DARKER_ACCENT_COLOR, "text": TEXT_COLOR},
        "active-off": {"fill": HIGHLIGHT_COLOR, "outline": DARKER_ACCENT_COLOR, "text": TEXT_COLOR},
        "normal-on": {"fill": SECONDARY_COLOR, "outline": HIGHLIGHT_COLOR, "text": TEXT_COLOR},
        "hover-on": {"fill": ACCENT_COLOR, "outline": DARKER_ACCENT_COLOR, "text": TEXT_COLOR},
        "active-on": {"fill": HIGHLIGHT_COLOR, "outline": DARKER_ACCENT_COLOR, "text": TEXT_COLOR},
    },
    "RoundedRectangle": {
        "normal-off": {"fill": ACCENT_COLOR, "outline": HIGHLIGHT_COLOR, "text": TEXT_COLOR},
        "hover-off": {"fill": SECONDARY_COLOR, "outline": DARKER_ACCENT_COLOR, "text": TEXT_COLOR},
        "active-off": {"fill": HIGHLIGHT_COLOR, "outline": DARKER_ACCENT_COLOR, "text": TEXT_COLOR},
        "normal-on": {"fill": SECONDARY_COLOR, "outline": HIGHLIGHT_COLOR, "text": TEXT_COLOR},
        "hover-on": {"fill": ACCENT_COLOR, "outline": DARKER_ACCENT_COLOR, "text": TEXT_COLOR},
        "active-on": {"fill": HIGHLIGHT_COLOR, "outline": DARKER_ACCENT_COLOR, "text": TEXT_COLOR},
    }
}

HighlightButton = {
    "Information": {
        "normal": {"fill": PRIMARY_COLOR, "text": TEXT_COLOR},
        "hover": {"fill": HIGHLIGHT_COLOR, "text": TEXT_COLOR},
        "active": {"fill": DARKER_ACCENT_COLOR, "text": TEXT_COLOR},
    }
}

IconButton = copy.deepcopy(Button)

InputBox = {
    "Rectangle": {
        "normal": {"fill": SECONDARY_COLOR, "outline": HIGHLIGHT_COLOR, "text": TEXT_COLOR},
        "hover": {"fill": ACCENT_COLOR, "outline": DARKER_ACCENT_COLOR, "text": TEXT_COLOR},
        "active": {"fill": "#FFFFFF", "outline": PRIMARY_COLOR, "text": TEXT_COLOR},
    },
    "RoundedRectangle.in": {
        "normal": {"fill": SECONDARY_COLOR, "outline": "#E5E5E5", "text": TEXT_COLOR},
        "hover": {"fill": ACCENT_COLOR, "outline": "#E5E5E5", "text": TEXT_COLOR},
        "active": {"fill": "#FFFFFF", "outline": "#E5E5E5", "text": TEXT_COLOR},
    },
    "RoundedRectangle.out": {
        "normal": {"fill": PRIMARY_COLOR, "outline": PRIMARY_COLOR, "text": TEXT_COLOR},
        "hover": {"fill": PRIMARY_COLOR, "outline": PRIMARY_COLOR, "text": TEXT_COLOR},
        "active": {"fill": DARKER_ACCENT_COLOR, "outline": DARKER_ACCENT_COLOR, "text": TEXT_COLOR},
    },
    "SingleLineText": {
        "normal": {"fill": TEXT_COLOR},
        "hover": {"fill": TEXT_COLOR},
        "active": {"fill": TEXT_COLOR},
    }
}

Label = {
    "Information": {
        "normal": {"fill": TEXT_COLOR},
        "hover": {"fill": TEXT_COLOR},
    },
    "Rectangle": {
        "normal": {"fill": SECONDARY_COLOR, "outline": HIGHLIGHT_COLOR, "text": TEXT_COLOR},
        "hover": {"fill": ACCENT_COLOR, "outline": DARKER_ACCENT_COLOR, "text": TEXT_COLOR},
    },
    "RoundedRectangle": {
        "normal": {"fill": SECONDARY_COLOR, "outline": HIGHLIGHT_COLOR, "text": TEXT_COLOR},
        "hover": {"fill": ACCENT_COLOR, "outline": DARKER_ACCENT_COLOR, "text": TEXT_COLOR},
    }
}

OptionButton = copy.deepcopy(Button)

ProgressBar = {
    "Rectangle.in": {
        "normal": {"fill": HIGHLIGHT_COLOR, "outline": HIGHLIGHT_COLOR},
        "hover": {"fill": DARKER_ACCENT_COLOR, "outline": DARKER_ACCENT_COLOR},
    },
    "Rectangle.out": {
        "normal": {"fill": ACCENT_COLOR, "outline": HIGHLIGHT_COLOR},
        "hover": {"fill": SECONDARY_COLOR, "outline": DARKER_ACCENT_COLOR},
    },
    "SemicircularRectangle.in": {
        "normal": {"fill": HIGHLIGHT_COLOR, "outline": HIGHLIGHT_COLOR},
        "hover": {"fill": DARKER_ACCENT_COLOR, "outline": DARKER_ACCENT_COLOR},
    },
    "SemicircularRectangle.out": {
        "normal": {"fill": ACCENT_COLOR, "outline": HIGHLIGHT_COLOR},
        "hover": {"fill": SECONDARY_COLOR, "outline": DARKER_ACCENT_COLOR},
    }
}

RadioButton = {
    "Oval.in": {
        "normal": {"fill": HIGHLIGHT_COLOR, "outline": HIGHLIGHT_COLOR, "text": TEXT_COLOR},
        "hover": {"fill": DARKER_ACCENT_COLOR, "outline": DARKER_ACCENT_COLOR, "text": TEXT_COLOR},
        "active": {"fill": DARKER_ACCENT_COLOR, "outline": DARKER_ACCENT_COLOR, "text": TEXT_COLOR},
    },
    "Oval.out": {
        "normal": {"fill": "#FFFFFF", "outline": HIGHLIGHT_COLOR, "text": TEXT_COLOR},
        "hover": {"fill": ACCENT_COLOR, "outline": HIGHLIGHT_COLOR, "text": TEXT_COLOR},
        "active": {"fill": SECONDARY_COLOR, "outline": HIGHLIGHT_COLOR, "text": TEXT_COLOR},
    },
    "Rectangle.in": {
        "normal": {"fill": HIGHLIGHT_COLOR, "outline": HIGHLIGHT_COLOR, "text": TEXT_COLOR},
        "hover": {"fill": DARKER_ACCENT_COLOR, "outline": DARKER_ACCENT_COLOR, "text": TEXT_COLOR},
        "active": {"fill": DARKER_ACCENT_COLOR, "outline": DARKER_ACCENT_COLOR, "text": TEXT_COLOR},
    },
    "Rectangle.out": {
        "normal": {"fill": "#FFFFFF", "outline": HIGHLIGHT_COLOR, "text": TEXT_COLOR},
        "hover": {"fill": ACCENT_COLOR, "outline": HIGHLIGHT_COLOR, "text": TEXT_COLOR},
        "active": {"fill": SECONDARY_COLOR, "outline": HIGHLIGHT_COLOR, "text": TEXT_COLOR},
    }
}

SegmentedButton = copy.deepcopy(Label)

Slider = {
    "Oval.in": {
        "normal": {"fill": HIGHLIGHT_COLOR, "outline": HIGHLIGHT_COLOR},
    },
    "Oval.out": {
        "normal": {"fill": "#FFFFFF", "outline": "#E8E8E8"},
    },
    "Rectangle.in": {
        "normal": {"fill": HIGHLIGHT_COLOR, "outline": HIGHLIGHT_COLOR},
    },
    "Rectangle": {
        "normal": {"fill": HIGHLIGHT_COLOR, "outline": HIGHLIGHT_COLOR},
        "hover": {"fill": DARKER_ACCENT_COLOR, "outline": DARKER_ACCENT_COLOR},
        "active": {"fill": PRIMARY_COLOR, "outline": PRIMARY_COLOR},
    },
    "Rectangle.out": {
        "normal": {"fill": HIGHLIGHT_COLOR, "outline": HIGHLIGHT_COLOR},
    },
    "SemicircularRectangle.in": {
        "normal": {"fill": HIGHLIGHT_COLOR, "outline": HIGHLIGHT_COLOR},
    },
    "SemicircularRectangle.out": {
        "normal": {"fill": HIGHLIGHT_COLOR, "outline": HIGHLIGHT_COLOR},
    }
}

Switch = {
    "Oval": {
        "normal-off": {"fill": PRIMARY_COLOR, "outline": PRIMARY_COLOR, "text": TEXT_COLOR},
        "hover-off": {"fill": HIGHLIGHT_COLOR, "outline": HIGHLIGHT_COLOR, "text": TEXT_COLOR},
        "active-off": {"fill": DARKER_ACCENT_COLOR, "outline": DARKER_ACCENT_COLOR, "text": TEXT_COLOR},
        "normal-on": {"fill": "#FFFFFF", "outline": "#FFFFFF", "text": TEXT_COLOR},
        "hover-on": {"fill": "#FFFFFF", "outline": "#FFFFFF", "text": TEXT_COLOR},
        "active-on": {"fill": "#FFFFFF", "outline": "#FFFFFF", "text": TEXT_COLOR},
    },
    "Rectangle.in": {
        "normal-off": {"fill": PRIMARY_COLOR, "outline": PRIMARY_COLOR, "text": TEXT_COLOR},
        "hover-off": {"fill": HIGHLIGHT_COLOR, "outline": HIGHLIGHT_COLOR, "text": TEXT_COLOR},
        "active-off": {"fill": DARKER_ACCENT_COLOR, "outline": DARKER_ACCENT_COLOR, "text": TEXT_COLOR},
        "normal-on": {"fill": "#FFFFFF", "outline": "#FFFFFF", "text": TEXT_COLOR},
        "hover-on": {"fill": "#FFFFFF", "outline": "#FFFFFF", "text": TEXT_COLOR},
        "active-on": {"fill": "#FFFFFF", "outline": "#FFFFFF", "text": TEXT_COLOR},
    },
    "Rectangle.out": {
        "normal-off": {"fill": ACCENT_COLOR, "outline": "#B8B8B9", "text": TEXT_COLOR},
        "hover-off": {"fill": SECONDARY_COLOR, "outline": "#858585", "text": TEXT_COLOR},
        "active-off": {"fill": HIGHLIGHT_COLOR, "outline": "#848584", "text": TEXT_COLOR},
        "normal-on": {"fill": HIGHLIGHT_COLOR, "outline": HIGHLIGHT_COLOR, "text": TEXT_COLOR},
        "hover-on": {"fill": DARKER_ACCENT_COLOR, "outline": DARKER_ACCENT_COLOR, "text": TEXT_COLOR},
        "active-on": {"fill": PRIMARY_COLOR, "outline": PRIMARY_COLOR, "text": TEXT_COLOR},
    },
    "SemicircularRectangle": {
        "normal-off": {"fill": ACCENT_COLOR, "outline": "#B8B8B9", "text": TEXT_COLOR},
        "hover-off": {"fill": SECONDARY_COLOR, "outline": "#858585", "text": TEXT_COLOR},
        "active-off": {"fill": HIGHLIGHT_COLOR, "outline": "#848584", "text": TEXT_COLOR},
        "normal-on": {"fill": HIGHLIGHT_COLOR, "outline": HIGHLIGHT_COLOR, "text": TEXT_COLOR},
        "hover-on": {"fill": DARKER_ACCENT_COLOR, "outline": DARKER_ACCENT_COLOR, "text": TEXT_COLOR},
        "active-on": {"fill": PRIMARY_COLOR, "outline": PRIMARY_COLOR, "text": TEXT_COLOR},
    }
}

Text = {
    "Information": {
        "normal": {"fill": TEXT_COLOR},
    }
}

UnderlineButton = {
    "Information": {
        "normal": {"fill": PRIMARY_COLOR, "text": TEXT_COLOR},
        "hover": {"fill": HIGHLIGHT_COLOR, "text": TEXT_COLOR},
        "active": {"fill": DARKER_ACCENT_COLOR, "text": TEXT_COLOR},
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
