input.onButtonPressed(Button.A, function () {
    strip2.shift(1)
    strip2.setPixelColor(0, neopixel.rgb(0, 255, 0))
    strip2.show()
})
// 植物身高测量
input.onPinPressed(TouchPin.P2, function () {
    basic.showString("ok！")
})
input.onButtonPressed(Button.AB, function () {
    strip2.clear()
    strip2.show()
})
input.onButtonPressed(Button.B, function () {
    strip2.shift(1)
    strip2.setPixelColor(0, neopixel.rgb(255, 0, 0))
    strip2.show()
})
let 角度 = 0
let strip2: neopixel.Strip = null
// 彩灯的变量
strip2 = neopixel.create(DigitalPin.P0, 15, NeoPixelMode.RGB_RGB)
// 电机的变量
let 增量 = 1
// 显示温度
basic.forever(function () {
    basic.showNumber(input.temperature())
    basic.pause(1000)
    serial.writeLine("温度：")
    serial.writeNumber(input.temperature())
    basic.pause(100)
})
// 电机转动
basic.forever(function () {
    pins.servoWritePin(AnalogPin.P2, 角度)
    角度 = 角度 + 增量
    if (角度 == 0) {
        增量 = 5
    } else if (角度 == 180) {
        增量 = -1
    }
    basic.pause(10)
})
