import numpy as np
from recorder import Recorder

r = Recorder()
r.record(5, output='Out.wav')

Recorder.play("Out.wav")
r.close()

