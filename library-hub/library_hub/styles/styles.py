from library_hub.styles.fonts import Font, FontWeight

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap", #FONT
    "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css", #Animate CSS
]

BASE_STYLES = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
}

### COMPONENTS STYLES ###

class Logo_Card_Styles():

    IMAGE = {
        "width":"50%"
    }

    TITLE = {
        "font_size":"2em",
        "background":"linear-gradient(#8800FF, #CF00FF)",
        "background_clip":"text",
        "text_fill_color":"transparent" 
    }

    PARENT_BOX = {
        "background":"linear-gradient(to left, #8800FF, #CF00FF)",
        "padding":"3px",
        "width":"25%",
        "height":"300px",
        "border_radius":"15px",
        "box_shadow":"rgba(132, 59, 206, 0.35) 0px 4px 24px"
    }

    CHILDREN_BOX = {
        "display":"flex",
        "justify_content":"center",
        "align_items":"center",
        "gap":"0",
        "padding":"1em",
        "width":"100%",
        "height":"100%",
        "background_color":"#13111C",
        "border_radius":"12px"
    }

class Big_Card_Styles():

    TITLE = {
        "font_size":"1.6em",
        "background":"linear-gradient(#8800FF, #CF00FF)",
        "background_clip":"text",
        "text_fill_color":"transparent",
        "margin_bottom":".6em"
    }

    DESCRIPTION = {
        "color":"#ccccdd",
        "font_weight":"400",
        "position":"relative",
        "z_index":"2",
        "margin_bottom":".4em"
    }

    LIST = {
        "color":"#ccccdd",
    }

    IMAGE = {
        "width":"40%",
        "position":"absolute",
        "left":"423px",
        "top":"77px",
        "z_index":"1",
    }

    BUTTON_BOX = {

    }

    BIG_BUTTON = {
        "font_size":"1em",
        "background":"linear-gradient(to right, #8800FF, #CF00FF)",
        "padding":"1.1em",
        "color":"white",
        "box_sizing":"border-box",
        "_hover":{
            "background_image":"linear-gradient(76.35deg,#660ac2 15.89%,#850ac2 89.75%)",
            "border":"1px solid #e286f9"
        }
    }

    BIG_BUTTON_ICON = {
        "padding":"3px",
        "border_radius":"2px",
        "background_color":"rgba(255,255,255,.35)"
    }

    SMALL_BUTTON = {
        "font_size":"1em",
        "background_color":"#13111C",
        "padding":"1.1em",
        "color":"#7709C2",
        "box_sizing":"border-box",
        "_hover":{
            "color":"#CD00FE",
        }
    }

    PARENT_BOX = {
        "background":"linear-gradient(to right, #8800FF, #CF00FF)",
        "padding":"3px",
        "width":"75%",
        "height":"300px",
        "border_radius":"15px",
        "box_shadow":"rgba(132, 59, 206, 0.35) 0px 4px 24px"
    }

    CHILDREN_BOX = {
        "position":"relative",
        "top":"0",
        "right":"0",
        "padding":"1em",
        "width":"100%",
        "height":"100%",
        "background_color":"#13111C",
        "border_radius":"12px",
        "overflow":"hidden",
        "justify_content":"space-between"
    }

class Medium_Card_Styles():

    TITLE = {
        "font_size":"1.6em",
        "background":"linear-gradient(#8800FF, #CF00FF)",
        "background_clip":"text",
        "text_fill_color":"transparent",
        "margin_bottom":".6em"
    }

    DESCRIPTION = {
        "color":"#ccccdd",
        "font_weight":"400",
        "position":"relative",
        "z_index":"2",
        "margin_bottom":".4em"
    }

    LIST = {
        "color":"#ccccdd",
    }

    IMAGE = {
        "width":"40%",
        "position":"absolute",
        "left":"273px",
        "top":"148px",
        "rotate":"12deg",
        "z_index":"1",
    }
    
    BUTTON_BOX = {
        
    }

    BIG_BUTTON = {
        "font_size":"1em",
        "background":"linear-gradient(to right, #8800FF, #CF00FF)",
        "padding":"1.1em",
        "color":"white",
        "box_sizing":"border-box",
        "_hover":{
            "background_image":"linear-gradient(76.35deg,#660ac2 15.89%,#850ac2 89.75%)",
            "border":"1px solid #e286f9"
        }
    }
    BIG_BUTTON_ICON = {
        "padding":"3px",
        "border_radius":"2px",
        "background_color":"rgba(255,255,255,.35)",

    }

    SMALL_BUTTON = {
        "font_size":"1em",
        "background_color":"rgba(0,0,0,.05)",
        "padding":"1.1em",
        "color":"#7709C2",
        "position":"relative",
        "z_index":"2",
        "box_sizing":"border-box",
        "_hover":{
            "color":"#CD00FE",
        }
    }

    PARENT_BOX = {
        "background":"linear-gradient(to right, #8800FF, #CF00FF)",
        "padding":"3px",
        "width":"50%",
        "height":"300px",
        "border_radius":"15px",
        "box_shadow":"rgba(132, 59, 206, 0.35) 0px 4px 24px"
    }
    
    CHILDREN_BOX = {
        "position":"relative",
        "top":"0",
        "right":"0",
        "padding":"1em",
        "width":"100%",
        "height":"100%",
        "background_color":"#13111C",
        "border_radius":"12px",
        "overflow":"hidden",
        "justify_content":"space-between"
    }



class Small_Card_Styles():

    TITLE = {
        "font_size":"1.6em",
        "background":"linear-gradient(#8800FF, #CF00FF)",
        "background_clip":"text",
        "text_fill_color":"transparent",
        "margin_bottom":".6em"
    }

    DESCRIPTION = {
        "color":"#ccccdd",
        "font_weight":"400",
        "position":"relative",
        "z_index":"2",
    }

    IMAGE = {
        "width":"80%",
        "position":"absolute",
        "left":"75px",
        "top":"124px",
        "rotate":"12deg",
        "z_index":"1",
    }

    BIG_BUTTON = {
        "font_size":"1em",
        "background":"linear-gradient(to right, #8800FF, #CF00FF)",
        "padding":"1.1em",
        "color":"white",
        "box_sizing":"border-box",
        "_hover":{
            "background_image":"linear-gradient(76.35deg,#660ac2 15.89%,#850ac2 89.75%)",
            "border":"1px solid #e286f9"
        },
        "position":"relative",
        "z_index":"2"
    }
    BIG_BUTTON_ICON = {
        "padding":"3px",
        "border_radius":"2px",
        "background_color":"rgba(255,255,255,.35)",
    }

    PARENT_BOX = {
        "background":"linear-gradient(to right, #8800FF, #CF00FF)",
        "padding":"3px",
        "width":"25%",
        "height":"300px",
        "border_radius":"15px",
        "box_shadow":"rgba(132, 59, 206, 0.35) 0px 4px 24px"
    }

    CHILDREN_BOX = {
        "display":"flex",
        "justify_content":"space-between",
        "position":"relative",
        "top":"0",
        "right":"0",
        "padding":"1em",
        "width":"100%",
        "height":"100%",
        "background_color":"#13111C",
        "border_radius":"12px",
        "overflow":"hidden"
    }
