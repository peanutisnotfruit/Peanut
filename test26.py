class Phone():

    def __init__(link, brand, model, battery=100):
        link.brand = brand
        link.model = model
        link.battery = battery

    def camera(link):
        print(link.brand + " is filming. Cha luck!")

    def call(link):
        print(link.brand + " is calling. Tu tu tu")