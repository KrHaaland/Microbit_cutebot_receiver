def on_received_string(receivedString):
    if receivedString == "A":
        cuteBot.motors(20, 50)
    if receivedString == "B":
        cuteBot.motors(50, 20)
    if receivedString == "AB":
        cuteBot.motors(40, 40)
    if receivedString == "0":
        cuteBot.motors(0, 0)
radio.on_received_string(on_received_string)

radio.set_group(23)