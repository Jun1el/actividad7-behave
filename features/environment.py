from src.belly import Belly

def before_scenario(context, scenario):
    print("before_scenario ejecutado")
    context.belly = Belly()