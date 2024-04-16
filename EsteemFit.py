from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivy.uix.behaviors import ButtonBehavior

from kivymd.app import MDApp
from kivymd.uix.behaviors import RotateBehavior
from kivymd.uix.expansionpanel import MDExpansionPanel
from kivymd.uix.list import MDListItemTrailingIcon
from kivymd.uix.navigationbar import MDNavigationBar, MDNavigationItem
from kivymd.uix.screen import MDScreen


class BaseMDNavigationItem(MDNavigationItem):
    icon = StringProperty()
    text = StringProperty()


class BaseScreen(MDScreen):
    image_size = StringProperty()
    list_items = ListProperty([])  # List to hold items for the list view


KV = '''
<BaseMDNavigationItem>
    MDNavigationItemIcon:
        icon: root.icon
    MDNavigationItemLabel:
        text: root.text


<BaseScreen>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1  # White color (RGB values: 1, 1, 1), fully opaque (alpha value: 1)
        Rectangle:
            size: self.size
            pos: self.pos

    FitImage:
        size_hint: .9, .9
        pos_hint: {"center_x": .5, "center_y": .5}
        radius: dp(24)

    ScrollView:
        size_hint_y: None
        height: "400dp" if root.name == "Exercises" else 0  # Only show the ScrollView when on "Exercises" screen
        GridLayout:
            cols: 1
            size_hint_y: None
            height: self.minimum_height
            spacing: dp(10)
            padding: dp(10)
            MDListItem:
                MDListItemLeadingIcon:
                    icon: "human-handsup"
                MDListItemHeadlineText:
                    text: "Jumping Jacks"
                MDListItemSupportingText:
                    text: "Home Exercise"
                MDListItemTrailingCheckbox:      
            MDListItem:
                on_release: app.handle_item_click("Push-ups")  # Specify the action when clicked
                MDListItemLeadingIcon:
                    icon: "arm-flex"
                MDListItemHeadlineText:
                    text: "Push-ups"
                MDListItemSupportingText:
                    text: "Strength Training"
                MDListItemTrailingCheckbox:   
            MDListItem:
                MDListItemLeadingIcon:
                    icon: "arm-flex-outline"
                MDListItemHeadlineText:
                    text: "Plank"
                MDListItemSupportingText:
                    text: "Core Strength"
                MDListItemTrailingCheckbox:   
            MDListItem:
                MDListItemLeadingIcon:
                    icon: "yoga"
                MDListItemHeadlineText:
                    text: "Burpees"
                MDListItemSupportingText:
                    text: "Stamina"
                MDListItemTrailingCheckbox:   
            MDListItem:
                MDListItemLeadingIcon:
                    icon: "run-fast"
                MDListItemHeadlineText:
                    text: "Jog"
                MDListItemSupportingText:
                    text: "Stamina"
                MDListItemTrailingCheckbox:   

    ScrollView:
        size_hint_y: None
        height: "450dp" if root.name == "Tips" else 0  # Only show the ScrollView when on "Exercises" screen
        GridLayout:
            cols: 1
            size_hint_y: None
            height: self.minimum_height
            spacing: dp(10)
            padding: dp(10)
            MDListItem:
                MDListItemLeadingIcon:
                    icon: "cards-heart"
                MDListItemHeadlineText:
                    text: "Self-Help"
                MDListItemSupportingText:
                    text: "You are enough"    
            MDListItem:
                MDListItemLeadingIcon:
                    icon: "cards-heart"
                MDListItemHeadlineText:
                    text: "Love Thyself"
                MDListItemSupportingText:
                    text: "You deserve love my friend"
  

MDBoxLayout:
    orientation: "vertical"
    md_bg_color: 1, 1, 1, 1

    MDScreenManager:
        id: screen_manager

        BaseScreen:
            name: "Exercises"
            image_size: "1024"
            list_items: ["Exercise 1", "Exercise 2", "Exercise 3"]  # Example list items

        BaseScreen:
            name: "Goals"
            image_size: "800"

        BaseScreen:
            name: "Tips"
            image_size: "600"
            list_items: []  # Empty list for Save screen

        BaseScreen:
            name: "Settings" 
            image_size: "400"
            list_items: ["Setting 1", "Setting 2", "Setting 3"]  # Example list items

    MDNavigationBar:
        md_bg_color: self.theme_cls.backgroundColor
    
        on_switch_tabs: app.on_switch_tabs(*args)

        BaseMDNavigationItem
            icon: "dumbbell"
            text: "Exercises"
            active: True

        BaseMDNavigationItem
            icon: "flag-variant"
            text: "Goals"

        BaseMDNavigationItem
            icon: "cog-box"
            text: "Settings"

        BaseMDNavigationItem
            icon: "bookmark-plus"
            text: "Tips"
'''
class TrailingPressedIconButton(
    ButtonBehavior, RotateBehavior, MDListItemTrailingIcon
):
    ...

class EsteemFit(MDApp):
    def on_switch_tabs(
        self,
        bar: MDNavigationBar,
        item: MDNavigationItem,
        item_icon: str,
        item_text: str,
    ):
        self.root.ids.screen_manager.current = item_text

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Mediumslateblue"  # "Purple", "Red"

        return Builder.load_string(KV)
    
    def handle_item_click(self, item_name):
        # Define the action to be performed when an item is clicked
        print(f"You clicked on: {item_name}")

    def tap_expansion_chevron(
        self, panel: MDExpansionPanel, chevron: TrailingPressedIconButton
    ):
        panel.open() if not panel.is_open else panel.close()
        panel.set_chevron_down(
            chevron
        ) if not panel.is_open else panel.set_chevron_up(chevron)


EsteemFit().run()
