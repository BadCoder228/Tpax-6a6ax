from car_hood.main_of_da_funcs import starting
from time import sleep
from flet import *
import asyncio

def main(page:Page):

    ''' кастомизация страницы '''
    page.window.center()
    page.title = 'Трах-бабах'
    page.window.always_on_top = True
    page.bgcolor = colors.TRANSPARENT
    page.decoration= BoxDecoration(image=DecorationImage(src='https://i.pinimg.com/236x/cb/d4/02/cbd402797ba396f561e96774c62c14a4.jpg', fit=ImageFit.COVER, opacity=0.1))
    page.window.width = 500
    page.window.height = 500
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.scroll = 'adaptive'
    page.auto_scroll = False
    page.theme_mode ='#000000'
    page.window.maximizable = False
    page.window.resizable = False

    ''' смена разрешения '''
    def change_resolution(e):
        res = str(resolution.value).split('x', -1)
        page.window.width = res[1] 
        page.window.height = res[0]
        for i in ([number, 120], [laps, 120], [start_button, 190], [resolution, 262]):
            i[0].width = (int(res[1])/2-(0.15*i[1])) if i[0] == number or i[0] == laps else (int(res[1])-(0.15*i[1]))
        topSeparation.size = (30 * 0.86) if res[0] == '800' else 30*0.05
        bottomSeparation.size = (50 * 0.86) if res[0] == '800' else (50*0.05) 
        page.update()

    ''' проверка на валидность номера '''
    def check(e):
        if number.value.startswith('9') and number.value.isdigit() and len(number.value) == 10:
            if laps.value.isdigit() and (int(laps.value) > 0 or int(laps.value) <= 100):
                    attack_window = AlertDialog(modal=True, title=Text('ЗАПУЩЕНО', color=col, size=30,weight=FontWeight.BOLD, text_align=TextAlign.CENTER), content=Row([Text("Прогресс:", size=10,weight=FontWeight.BOLD, text_align=TextAlign.CENTER), progress]), actions_alignment='end', open=True,bgcolor="#000000")
                    page.dialog = attack_window
                    page.update()
                    for _ in range(int(laps.value)):
                        progress.value = ((_+0.05)/int(laps.value))
                        page.update()
                        asyncio.run(starting(str("7"+number.value), telegramspam.value))
                    else:
                        progress.value = 1;page.update();sleep(2)
                        attack_window.open = False
                        page.update()
                        error("Атака завершена.")
            else:
                error('Неправильное количество повторений!')
        else:
            error('Некорректный номер телефона!')
    
    ''' объявление ошибок (и не только) '''
    def error(error_itself):
        def button_cancel(e):
            error_message.open = False
            page.update()
        error_message = AlertDialog(title=Text(error_itself, size=20, text_align='center', font_family='Open Sans', color=col, weight=FontWeight.BOLD),actions=[TextButton('Понятно', on_click=button_cancel, icon_color=col_border, style=ButtonStyle(color=col))], actions_alignment='end', bgcolor="#000000")
        page.dialog = error_message
        error_message.open = True
        page.update()
    
        
    ''' переменные '''
    col, col_border, col_label = "#8D4205", "#CC5E03", '#00FF7F'
    progress = ProgressBar(width=150, color=col_label)
    number = TextField(label='Номер\n(без "+7")', width=250-(0.15*120), text_align='center', border_radius=40, border_color=col_border, cursor_color=col, focused_border_color=col_border, autofocus=True, selection_color=col, label_style=TextStyle(color=col))
    laps = TextField(label='Повторений\n(до 100)', width=250-(0.15*120), text_align='center', border_radius=40, border_color=col_border, cursor_color=col, focused_border_color=col_border, selection_color=col, label_style=TextStyle(color=col))
    start_button = ElevatedButton(content=Text('ЗАПУСК', size=25), on_click=check, width=500-(0.15*190), height=60, color=col, bgcolor="#00000000", style=ButtonStyle("#00000000", "#00000000", "#00000000", "#00000000"))
    resolution = Dropdown(label='Разрешение экрана', hint_text='Выберите разрешение экрана', options=[dropdown.Option('800x360'), dropdown.Option('500x500')], width=500-(0.15*262), border_radius=40, alignment=alignment.bottom_center, border_color=col_border, value='500x500', label_style=TextStyle(color=col), on_change=change_resolution)
    bottomSeparation, topSeparation, banner, afterbanner = Text('\n\n', size=50* 0.05), Text('\n\n', size=30* 0.05), Text('ТРАХ-БАБАХ', size=50, color=col, font_family="Open Sans",weight=FontWeight.BOLD,italic=True), Text('* необходимо стабильное подключение', size=9)
    telegramspam = Switch(label_position=LabelPosition.RIGHT, label="+ Спам телеграма (могут увидеть ваш ip)", label_style=TextStyle(size=13), track_color= "#00000000", thumb_color='#FFFFFF', track_outline_color=col)

    ''' добавление всего на страницу '''
    page.add(
    Text('\n', size=7),
    banner,
    afterbanner,
    topSeparation,
    Row([number, laps], "CENTER"),
    Text('\n', size=7),
    start_button,
    bottomSeparation,
    telegramspam,
    resolution)

''' запуск '''
app(target=main)

