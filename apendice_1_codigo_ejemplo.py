import rx
from rx import operators as ops

source = rx.of("Alpha", "Beta", "Gamma", "Delta", "Epsilon")
disp = source.subscribe(lambda value: print(f"Received {value}"), lambda ex: print(ex), lambda: print('completed'))