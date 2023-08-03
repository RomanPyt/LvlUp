from kivy.metrics import dp
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout

from datetime import datetime
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.behaviors import CommonElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel

from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.pickers import MDDatePicker

from kivymd.uix.selectioncontrol.selectioncontrol import MDCheckbox
from kivymd.uix.snackbar import MDSnackbar

from KV import KV
import json
Builder.load_string(KV)

from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import NoTransition

from kivy.core.window import Window
Window.size = (510, 840)




def write(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def read(filename):
    with open(filename, 'r') as file:
        return json.load(file)







class TaskScreen(MDScreen):
    pass

class NewTaskScreen(MDScreen):
    pass
class NewQuestScreen(MDScreen):
    pass
class NewProfileScreen(MDScreen):
    pass


class Task(MDFloatLayout):
    def __init__(self, name, exp):
        self.name = name
        self.exp = exp

class Quest(MDFloatLayout):
    def __init__(self, name, exp, data):
        self.name = name
        self.exp = exp
        self.data = data

class TaskLayout(ScrollView):
    pass


class QuestScreen(MDScreen):
    pass

class PassiveScreen(MDScreen):
    pass

class CalendarScreen(MDScreen):
    pass

class ProfileScreen(MDScreen):
    b = read('progressbar.json')
    lvl_text = b['lvl_text']
    max = int(b['max'])
    value = int(b['value'])

class NavigationBar(CommonElevationBehavior, MDBoxLayout):
    pass



class DemoApp(MDApp):
    # Текст кнопки которая вызывает DropDownMenu
    date = datetime.now()
    current_task_day = date.strftime("%A")
    text_day = date.strftime("%A").lower()
    a = read('profile.json')
    profile_name = f"Name: {a['name']}"
    profile_title = f"Title: {a['title']}"
    profile_job = f"Job: {a['job']}"
    profile_grl = f"Girlfriend: {a['grl']}"
    profile_goal = f"Goal: {a['goal']}"
    profile_law1 = f"1: {a['law1']}"
    profile_law2 = f"2: {a['law2']}"
    profile_law3 = f"3: {a['law3']}"
    profile_law4 = f"4: {a['law4']}"
    profile_law5 = f"5: {a['law5']}"
    profile_law6 = f"6: {a['law6']}"
    profile_law7 = f"7: {a['law7']}"



    def build(self):
        self.theme_cls.theme_style = 'Dark'

        date = datetime.now()





        self.text_day = date.strftime("%A").lower()

        self.sm = ScreenManager(transition=NoTransition())
        self.sm.add_widget(TaskScreen(name='taskscreen'))
        self.sm.add_widget(QuestScreen(name='questscreen'))
        self.sm.add_widget(PassiveScreen(name='passivescreen'))
        self.sm.add_widget(CalendarScreen(name='calendarscreen'))
        self.sm.add_widget(ProfileScreen(name='profilescreen'))
        self.sm.add_widget(NewProfileScreen(name='newprofile'))
        self.sm.add_widget(NewTaskScreen(name='newtask'))
        self.sm.add_widget(NewQuestScreen(name='newquest'))


        self.current_task_day = date.strftime("%A").lower()
        self.build_task(self.text_day)
        self.build_quest()

        return self.sm
    # Task Screen
    def new_task_name(self):
        print(self.sm.get_screen('newtask').ids.task_name.text)
        print(self.sm.get_screen('newtask').ids.task_exp.text)
        task = Task(name=self.sm.get_screen('newtask').ids.task_name.text, exp=self.sm.get_screen('newtask').ids.task_exp.text)
        if task.name != '' and task.exp != '' and task.exp.isnumeric():
            if int(task.exp) <= 500:
                if self.sm.get_screen('newtask').ids.monday_switch.active:
                    a = read('tasks.json')
                    a['monday'][task.name] = {'value': task.exp,
                                              'button': False}
                    write(a, 'tasks.json')
                if self.sm.get_screen('newtask').ids.tuesday_switch.active:
                    a = read('tasks.json')
                    a['tuesday'][task.name] = {'value': task.exp,
                                               'button': False}
                    write(a, 'tasks.json')
                if self.sm.get_screen('newtask').ids.wednesday_switch.active:
                    a = read('tasks.json')
                    a['wednesday'][task.name] = {'value': task.exp,
                                                 'button': False}
                    write(a, 'tasks.json')
                if self.sm.get_screen('newtask').ids.thursday_switch.active:
                    a = read('tasks.json')
                    a['thursday'][task.name] = {'value': task.exp,
                                                'button': False}
                    write(a, 'tasks.json')
                if self.sm.get_screen('newtask').ids.friday_switch.active:
                    a = read('tasks.json')
                    a['friday'][task.name] = {'value': task.exp,
                                              'button': False}
                    write(a, 'tasks.json')
                if self.sm.get_screen('newtask').ids.saturday_switch.active:
                    a = read('tasks.json')
                    a['saturday'][task.name] = {'value': task.exp,
                                                'button': False}
                    write(a, 'tasks.json')
                if self.sm.get_screen('newtask').ids.sunday_switch.active:
                    a = read('tasks.json')
                    a['sunday'][task.name] = {'value': task.exp,
                                              'button': False}
                    write(a, 'tasks.json')
        self.sm.get_screen('newtask').ids.task_name.text = ''
        self.sm.get_screen('newtask').ids.task_exp.text = ''
        self.sm.get_screen('newtask').ids.monday_switch.active = False
        self.sm.get_screen('newtask').ids.tuesday_switch.active = False
        self.sm.get_screen('newtask').ids.wednesday_switch.active = False
        self.sm.get_screen('newtask').ids.thursday_switch.active = False
        self.sm.get_screen('newtask').ids.friday_switch.active = False
        self.sm.get_screen('newtask').ids.saturday_switch.active = False
        self.sm.get_screen('newtask').ids.sunday_switch.active = False
    def build_task(self, day):
        self.texting = ''
        self.scroll = ScrollView(do_scroll_y=True, pos_hint={'center_y': .55}, size_hint=(1, .75))
        anchor_lay = MDAnchorLayout(size_hint_y=None, anchor_y='top', height=dp(1500))
        stack_lay = StackLayout(padding=dp(10), spacing=dp(10), size_hint_y=None)
        anchor_lay.add_widget(stack_lay)
        self.scroll.add_widget(anchor_lay)

        a = read('tasks.json')
        date = datetime.now()

        if int(date.day) != int(a['date']):
            if date.strftime("%A").lower() == 'monday':
                for key in a['sunday']:
                    if a['sunday'][key]['button'] == False:
                        self.anti_task_press('sunday', key)

            elif date.strftime("%A").lower() == 'tuesday':
                for key in a['monday']:
                    if a['monday'][key]['button'] == False:
                        self.anti_task_press('monday', key)

            elif date.strftime("%A").lower() == 'wednesday':
                for key in a['tuesday']:
                    if a['tuesday'][key]['button'] == False:
                        self.anti_task_press('tuesday', key)

            elif date.strftime("%A").lower() == 'thursday':
                for key in a['wednesday']:
                    if a['wednesday'][key]['button'] == False:
                        self.anti_task_press('wednesday', key)

            elif date.strftime("%A").lower() == 'friday':
                for key in a['thursday']:
                    if a['thursday'][key]['button'] == False:
                        self.anti_task_press('thursday', key)

            elif date.strftime("%A").lower() == 'saturday':
                for key in a['friday']:
                    if a['friday'][key]['button'] == False:
                        self.anti_task_press('friday', key)

            elif date.strftime("%A").lower() == 'sunday':
                for key in a['saturday']:
                    if a['saturday'][key]['button'] == False:
                        self.anti_task_press('saturday', key)

            b = read('progressbar.json')

            if b['anti_value'] != 0:
                MDSnackbar(
                    MDLabel(
                        text="Congratulations",
                        size_hint_min_x=.6,
                        theme_text_color="Custom",
                        text_color="#393231",
                    ),
                    MDLabel(
                        text=f'- {b["anti_value"]} exp.',
                        theme_text_color="Custom",
                        text_color="#393231",
                    ),
                    y=dp(24),
                    pos_hint={"center_x": 0.5, 'center_y': .2},
                    size_hint_x=0.7,
                    md_bg_color="#E8D8D7",
                ).open()
                b["anti_value"] = 0
                write(b, 'progressbar.json')

        a = read('tasks.json')
        for key in a[day]:

            if int(date.day) != int(a['date']):
                a[day][key]['button'] = False
                write(a, 'tasks.json')

            float_lay = MDFloatLayout()
            self.check = MDCheckbox(pos_hint={'center_x': .065, 'center_y': .5}, size_hint=(None, None), group=key, size=(dp(64), dp(64)), id=a[day][key]['value'],
                               on_press=self.task_press, disabled_color='lightgrey', active=a[day][key]['button'])
            card = MDCard(radius=[16], pos_hint={'center_x': .5, 'center_y': .5}, elevation=2, shadow_softness=4, shadow_offset=(2, -2))
            label_name = Label(text=key, strikethrough=a[day][key]['button'], text_size=(dp(300), None), font_size=dp(25), bold=True, pos_hint={'center_x': .45, 'center_y': .53})
            label_exp = Label(text=a[day][key]['value'], text_size=(dp(300), None), font_size=dp(10), bold=True,pos_hint={'center_x': .455, 'center_y': .3})
            del_button = MDIconButton(icon='trash-can-outline', pos_hint={'center_x': .9, 'center_y': .5}, id=key, on_press=self.del_task)
            float_lay.add_widget(card)
            self.check.color_active = 'grey'
            float_lay.add_widget(self.check)
            float_lay.add_widget(label_name)
            float_lay.add_widget(label_exp)
            float_lay.add_widget(del_button)
            stack_lay.add_widget(float_lay)
            date = datetime.now()
            a = read('tasks.json')
            if date.strftime("%A").lower() != self.text_day:
                a[day][key]['button'] = True
                write(a, 'tasks.json')
                self.check.active = True

        date = datetime.now()
        a = read('tasks.json')
        a['date'] = date.day
        write(a, 'tasks.json')

        self.sm.get_screen('taskscreen').add_widget(self.scroll)




    def delete_task_lay(self):
        self.sm.get_screen('taskscreen').remove_widget(self.scroll)

    def del_task(self, instance):
        print(instance.id)
        d = False
        a = read('tasks.json')
        for key in a[self.text_day]:
            if instance.id == key:
                d = True
        if d:
            a[self.text_day].pop(instance.id)
            #a.pop('button' + str(instance.id)+ str(self.text_day))
            #a.pop('line' + str(instance.id) + str(self.text_day))
            write(a, 'tasks.json')

        self.delete_task_lay()
        self.build_task(self.text_day)

    def disabled_me(self, instance):
        pass


    #def task_press_button(self, day, key):
        #a = read('tasks.json')
        #a[day][key]['button'] = True
        #write(a, 'tasks.json')

    def task_press(self, instance):
        print(str(instance.group))
        print(instance.id)
        key = str(instance.group)
        a = read('tasks.json')
        if a[self.text_day][key]['button'] == True:
            instance.active = True
        b = read('progressbar.json')
        self.lvl_text = b['lvl_text']
        self.my_max = int(b['max'])
        self.my_value = int(b['value'])
        self.my_value += int(instance.id)
        a = read('tasks.json')
        key = str(instance.group)
        if a[self.text_day][key]['button'] == False:
            while self.my_value >= self.my_max:
                self.my_value = self.my_value - self.my_max
                self.lvl_text = str(int(self.lvl_text) + 1)
                if int(self.lvl_text) >= 5:
                    self.my_max = 1000
                elif int(self.lvl_text) >= 10:
                    self.my_max = 2000
                elif int(self.lvl_text) >= 15:
                    self.my_max = 2500
                elif int(self.lvl_text) >= 20:
                    self.my_max = 3500
                elif int(self.lvl_text) >= 25:
                    self.my_max = 4000
                elif int(self.lvl_text) >= 30:
                    self.my_max = 5000
                elif int(self.lvl_text) >= 35:
                    self.my_max = 5500
                elif int(self.lvl_text) >= 40:
                    self.my_max = 6500
                elif int(self.lvl_text) >= 45:
                    self.my_max = 7000
                elif int(self.lvl_text) >= 50:
                    self.my_max = 8000
            b['lvl_text'] = self.lvl_text
            b['max'] = self.my_max
            b['value'] = self.my_value
            a = read('tasks.json')
            key = str(instance.group)
            a[self.text_day][key]['button'] = True
            #a[str('line' + key + self.text_day)] = True
            write(a, 'tasks.json')
            write(b, 'progressbar.json')
            self.sm.get_screen('profilescreen').ids.progressbar.max = self.my_max
            self.sm.get_screen('profilescreen').ids.progressbar.value = self.my_value
            self.sm.get_screen('profilescreen').ids.lvl_text.text = self.lvl_text
            self.delete_task_lay()
            self.build_task(self.text_day)

            MDSnackbar(
                MDLabel(
                    text="Congratulations",
                    size_hint_min_x=.6,
                    theme_text_color="Custom",
                    text_color="#393231",
                ),
                MDLabel(
                    text=f'+ {instance.id} exp.',
                    theme_text_color="Custom",
                    text_color="#393231",
                ),
                y=dp(24),
                pos_hint={"center_x": 0.5, 'center_y': .2},
                size_hint_x=0.7,
                md_bg_color="#E8D8D7",
            ).open()


    def anti_task_press(self, day, key):
        b = read('progressbar.json')
        a = read('tasks.json')
        self.lvl_text = b['lvl_text']
        self.my_max = int(b['max'])
        self.my_value = int(b['value'])
        self.my_value -= int(a[day][key]['value']) * 3
        self.anti_value = int(a[day][key]['value']) * 3
        if a[day][key]['button'] == False:
            # b['lvl_text'] = self.lvl_text
            # b['max'] = self.my_max
            # b['value'] = self.my_value
            a = read('tasks.json')
            key = str(key)
            a[day][key]['button'] = True
            # a[str('line' + key + self.text_day)] = True
            write(a, 'tasks.json')
            b = read('progressbar.json')
            b_val = b['anti_value']
            b = {
                "lvl_text": self.lvl_text,
                "max": self.my_max,
                "value": self.my_value,
                "anti_value": b_val + self.anti_value
            }
            write(b, 'progressbar.json')
            self.sm.get_screen('profilescreen').ids.progressbar.max = self.my_max
            self.sm.get_screen('profilescreen').ids.progressbar.value = self.my_value
            self.sm.get_screen('profilescreen').ids.lvl_text.text = self.lvl_text
            #self.delete_task_lay()
            #self.build_task(self.text_day)





    # QuestScreen
    # Data Picker
    def on_save(self, instance, value, date_range):
        '''
        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;
        :param value: selected date;
        :type value: <class 'datetime.date'>;
        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        '''
        self.sm.get_screen('newquest').ids.date_button.text = str(value)
        print(value)

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''


    def show_date_picker(self):
        date_dialog = MDDatePicker(
            primary_color='#444444',
            selector_color='#444444',
            text_button_color=(1, 1, 1, 1),
            text_current_color="white",
        )
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()
        #print("'_anim_alpha', '_anim_duration', '_background_origin', '_background_x', '_background_y', '_calendar_layout', '_date_label_text', '_input_date_dialog_open', '_is_open', '_md_bg_color', '_origin_line_color', '_origin_md_bg_color', '_scale_calendar_layout', '_scale_x', '_scale_y', '_scale_year_layout', '_shift_dialog_height', '_window', 'accent_color', 'anchor_x', 'anchor_y', 'angle', 'attach_to', 'auto_dismiss', 'background', 'background_color', 'background_hue', 'background_origin', 'background_palette', 'border', 'center', 'center_x', 'center_y', 'children', 'cls', 'date_range_text_error', 'day', 'device_ios', 'disabled', 'elevation', 'font_name', 'height', 'helper_text', 'hide_duration', 'hide_transition', 'ids', 'input_field_background_color', 'input_field_background_color_focus', 'input_field_background_color_normal', 'input_field_cls', 'input_field_text_color', 'input_field_text_color_focus', 'input_field_text_color_normal', 'line_color', 'line_width', 'max_date', 'max_year', 'md_bg_color', 'min_date', 'min_year', 'mode', 'month', 'motion_filter', 'opacity', 'opposite_colors', 'overlay_color', 'padding', 'parent', 'pos', 'pos_hint', 'primary_color', 'radius', 'right', 'rotate_value_angle', 'rotate_value_axis', 'scale_value_center', 'scale_value_x', 'scale_value_y', 'scale_value_z', 'scale_x', 'scale_y', 'sel_day', 'sel_month', 'sel_year', 'selector_color', 'shadow_color', 'shadow_offset', 'shadow_radius', 'shadow_softness', 'shadow_softness_size', 'show_duration', 'show_transition', 'size', 'size_hint', 'size_hint_max', 'size_hint_max_x', 'size_hint_max_y', 'size_hint_min', 'size_hint_min_x', 'size_hint_min_y', 'size_hint_x', 'size_hint_y', 'specific_secondary_text_color', 'specific_text_color', 'text_button_color', 'text_color', 'text_current_color', 'text_toolbar_color', 'text_weekday_color', 'theme_cls', 'title', 'title_input', 'top', 'widget_style', 'width', 'x', 'y', 'year'")

    def new_quest_name(self):
        #value = '0'
        #but_1 = True
        #but_2 = False
        #but_3 = False
        print(self.sm.get_screen('newquest').ids.quest_name.text)
        print(self.sm.get_screen('newquest').ids.quest_exp.text)

        print(self.sm.get_screen('newquest').ids.date_button.text)
        quest = Quest(name=self.sm.get_screen('newquest').ids.quest_name.text,
                      exp=self.sm.get_screen('newquest').ids.quest_exp.text,
                      data=str(self.sm.get_screen('newquest').ids.date_button.text),
                      )
        if quest.name != '' and quest.exp.isnumeric() and quest.data != '':
            a = read('quest.json')
            a[quest.name] = {'value': quest.exp,
                             'data': quest.data}
            write(a, 'quest.json')
        self.sm.get_screen('newquest').ids.quest_name.text = ''
        self.sm.get_screen('newquest').ids.quest_exp.text = ''
        self.sm.get_screen('newquest').ids.date_button.text = 'Data'

    def build_quest(self):
        self.scroll2 = ScrollView(do_scroll_y=True, pos_hint={'center_y': .55}, size_hint=(1, .75))
        anchor_lay = MDAnchorLayout(size_hint_y=None, anchor_y='top', height=dp(1500))
        stack_lay = StackLayout(padding=dp(10), spacing=dp(10), size_hint_y=.1)
        anchor_lay.add_widget(stack_lay)
        self.scroll2.add_widget(anchor_lay)
        a = read('quest.json')
        for key in a:
            float_lay = MDFloatLayout()
            check = MDIconButton(pos_hint={'center_x': .92, 'center_y': .285}, icon='check-bold', size_hint=(None, None),
                               size=(dp(64), dp(64)), id=a[key]['value'], text=key, on_press=self.quest_press)
            card = MDCard(radius=[16], pos_hint={'center_x': .5, 'center_y': .5}, elevation=2, shadow_softness=4,
                          shadow_offset=(2, -2))
            label_name = Label(text=key, text_size=(dp(300), None), font_size=dp(30), bold=True,
                               pos_hint={'center_x': .33, 'center_y': .5})
            label_exp = Label(text=a[key]['value'], text_size=(dp(300), None), font_size=dp(12), bold=True,
                              pos_hint={'center_x': .335, 'center_y': .292}, color='darkgrey')
            label_data = Label(text=a[key]['data'], text_size=(dp(300), None), font_size=dp(25), bold=True,
                              pos_hint={'center_x': .331, 'center_y': .77}, color='grey')
            del_button = MDIconButton(icon='trash-can-outline', pos_hint={'center_x': .92, 'center_y': .77}, id=key,
                                      on_press=self.del_quest)
            float_lay.add_widget(card)
            float_lay.add_widget(check)
            float_lay.add_widget(label_name)
            float_lay.add_widget(label_exp)
            float_lay.add_widget(label_data)
            float_lay.add_widget(del_button)
            stack_lay.add_widget(float_lay)
        self.sm.get_screen('questscreen').add_widget(self.scroll2)


    def quest_press(self, instance):
        print(instance.id)
        print(instance.id)
        b = read('progressbar.json')
        self.lvl_text = b['lvl_text']
        self.my_max = int(b['max'])
        self.my_value = int(b['value'])
        self.my_value += int(instance.id)
        while self.my_value >= self.my_max:
            self.my_value = self.my_value - self.my_max
            self.lvl_text = str(int(self.lvl_text) + 1)
            if int(self.lvl_text) == 5:
                self.my_max += 500
            elif int(self.lvl_text) == 10:
                self.my_max += 1000
            elif int(self.lvl_text) == 15:
                self.my_max += 500
            elif int(self.lvl_text) == 20:
                self.my_max += 1000
            elif int(self.lvl_text) == 25:
                self.my_max += 500
            elif int(self.lvl_text) == 30:
                self.my_max += 1000
            elif int(self.lvl_text) == 35:
                self.my_max += 500
            elif int(self.lvl_text) == 40:
                self.my_max += 1000
            elif int(self.lvl_text) == 45:
                self.my_max += 500
            elif int(self.lvl_text) == 50:
                self.my_max += 1000
        b['lvl_text'] = self.lvl_text
        b['max'] = self.my_max
        b['value'] = self.my_value
        write(b, 'progressbar.json')
        self.sm.get_screen('profilescreen').ids.progressbar.max = self.my_max
        self.sm.get_screen('profilescreen').ids.progressbar.value = self.my_value
        self.sm.get_screen('profilescreen').ids.lvl_text.text = self.lvl_text

        a = read('quest.json')
        a.pop(instance.text)
        write(a, 'quest.json')
        self.delete_quest_lay()
        self.build_quest()
        MDSnackbar(
            MDLabel(
                text="Congratulations",
                size_hint_min_x=.6,
                theme_text_color="Custom",
                text_color="#393231",
            ),
            MDLabel(
                text=f'+ {instance.id} exp.',
                theme_text_color="Custom",
                text_color="#393231",
            ),
            y=dp(24),
            pos_hint={"center_x": 0.5, 'center_y': .2},
            size_hint_x=0.7,
            md_bg_color="#E8D8D7",
        ).open()




    def delete_quest_lay(self):
        self.sm.get_screen('questscreen').remove_widget(self.scroll2)

    def del_quest(self, instance):
        print(instance.id)
        d = False
        a = read('quest.json')
        for key in a:
            d = True
        if d:
            a.pop(instance.id)
            write(a, 'quest.json')
        self.delete_quest_lay()
        self.build_quest()


    def menu_open(self):
        self.menu_items = [
            {
                "text": f"Monday",
                "on_release": lambda x=f"monday": self.menu_callback(x),
            },
            {
                "text": f"Tuesday",
                "on_release": lambda x=f"tuesday": self.menu_callback(x),
            },
            {
                "text": f"Wednesday",
                "on_release": lambda x=f"wednesday": self.menu_callback(x),
            },
            {
                "text": f"Thursday",
                "on_release": lambda x=f"thursday": self.menu_callback(x),
            },
            {
                "text": f"Friday",
                "on_release": lambda x=f"friday": self.menu_callback(x),
            },
            {
                "text": f"Saturday",
                "on_release": lambda x=f"saturday": self.menu_callback(x),
            },
            {
                "text": f"Sunday",
                "on_release": lambda x=f"sunday": self.menu_callback(x),
            }
        ]
        self.drop_menu = MDDropdownMenu(
                caller=self.sm.get_screen('taskscreen').ids.button, items=self.menu_items
            )
        self.drop_menu.open()



    def menu_callback(self, text_item):
        print(text_item)
        self.drop_menu.dismiss()
        self.text_day = text_item
        if self.text_day == 'monday':
            self.sm.get_screen('taskscreen').remove_widget(self.scroll)
            self.build_task('monday')
            self.current_task_day = 'monday'
            self.sm.get_screen('taskscreen').ids.button.text = 'Monday'
        elif self.text_day == 'tuesday':
            self.sm.get_screen('taskscreen').remove_widget(self.scroll)
            self.build_task('tuesday')
            self.current_task_day = 'tuesday'
            self.sm.get_screen('taskscreen').ids.button.text = 'Tuesday'
        elif self.text_day == 'wednesday':
            self.sm.get_screen('taskscreen').remove_widget(self.scroll)
            self.build_task('wednesday')
            self.current_task_day = 'wednesday'
            self.sm.get_screen('taskscreen').ids.button.text = 'Wednesday'
        elif self.text_day == 'thursday':
            self.sm.get_screen('taskscreen').remove_widget(self.scroll)
            self.build_task('thursday')
            self.current_task_day = 'thursday'
            self.sm.get_screen('taskscreen').ids.button.text = 'Thursday'
        elif self.text_day == 'friday':
            self.sm.get_screen('taskscreen').remove_widget(self.scroll)
            self.build_task('friday')
            self.current_task_day = 'friday'
            self.sm.get_screen('taskscreen').ids.button.text = 'Friday'
        elif self.text_day == 'saturday':
            self.sm.get_screen('taskscreen').remove_widget(self.scroll)
            self.build_task('saturday')
            self.current_task_day = 'saturday'
            self.sm.get_screen('taskscreen').ids.button.text = 'Saturday'
        elif self.text_day == 'sunday':
            self.sm.get_screen('taskscreen').remove_widget(self.scroll)
            self.build_task('sunday')
            self.current_task_day = 'sunday'
            self.sm.get_screen('taskscreen').ids.button.text = 'Sunday'

    def new_profile(self):
        a = read('profile.json')
        a['name'] = self.sm.get_screen('newprofile').ids.profile_name.text
        a['title'] = self.sm.get_screen('newprofile').ids.profile_title.text
        a['job'] = self.sm.get_screen('newprofile').ids.profile_job.text
        a['grl'] = self.sm.get_screen('newprofile').ids.profile_grl.text
        a['goal'] = self.sm.get_screen('newprofile').ids.profile_goal.text
        a['law1'] = self.sm.get_screen('newprofile').ids.profile_law1.text
        a['law2'] = self.sm.get_screen('newprofile').ids.profile_law2.text
        a['law3'] = self.sm.get_screen('newprofile').ids.profile_law3.text
        a['law4'] = self.sm.get_screen('newprofile').ids.profile_law4.text
        a['law5'] = self.sm.get_screen('newprofile').ids.profile_law5.text
        a['law6'] = self.sm.get_screen('newprofile').ids.profile_law6.text
        a['law7'] = self.sm.get_screen('newprofile').ids.profile_law7.text
        write(a, 'profile.json')

    def build_profile(self):
        a = read('profile.json')
        self.sm.get_screen('newprofile').ids.profile_name.text = a['name']
        self.sm.get_screen('newprofile').ids.profile_title.text = a['title']
        self.sm.get_screen('newprofile').ids.profile_job.text = a['job']
        self.sm.get_screen('newprofile').ids.profile_grl.text = a['grl']
        self.sm.get_screen('newprofile').ids.profile_goal.text = a['goal']
        self.sm.get_screen('newprofile').ids.profile_law1.text = a['law1']
        self.sm.get_screen('newprofile').ids.profile_law2.text = a['law2']
        self.sm.get_screen('newprofile').ids.profile_law3.text = a['law3']
        self.sm.get_screen('newprofile').ids.profile_law4.text = a['law4']
        self.sm.get_screen('newprofile').ids.profile_law5.text = a['law5']
        self.sm.get_screen('newprofile').ids.profile_law6.text = a['law6']
        self.sm.get_screen('newprofile').ids.profile_law7.text = a['law7']



DemoApp().run()
