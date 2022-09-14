def on_button_pressed_a():
    strip2.shift(1)
    strip2.set_pixel_color(0, neopixel.rgb(0, 255, 0))
    strip2.show()
input.on_button_pressed(Button.A, on_button_pressed_a)

# 植物身高测量

def on_pin_pressed_p2():
    basic.show_string("ok！")
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_button_pressed_ab():
    strip2.clear()
    strip2.show()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    strip2.shift(1)
    strip2.set_pixel_color(0, neopixel.rgb(255, 0, 0))
    strip2.show()
input.on_button_pressed(Button.B, on_button_pressed_b)

角度 = 0
strip2: neopixel.Strip = None
# 彩灯的变量
strip2 = neopixel.create(DigitalPin.P0, 15, NeoPixelMode.RGB_RGB)
# 电机的变量
增量 = 1
# 显示温度

def on_forever():
    basic.show_number(input.temperature())
    basic.pause(1000)
    serial.write_line("温度：")
    serial.write_number(input.temperature())
    basic.pause(100)
basic.forever(on_forever)

# 电机转动

def on_forever2():
    global 角度, 增量
    pins.servo_write_pin(AnalogPin.P2, 角度)
    角度 = 角度 + 增量
    if 角度 == 0:
        增量 = 5
    else:
        if 角度 == 180:
            增量 = -1
    basic.pause(10)
basic.forever(on_forever2)
